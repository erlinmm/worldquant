import re
import javalang
import anthropic
from pathlib import Path

client  = anthropic.Anthropic()
MODEL   = "claude-sonnet-4-5"
MAX_TOK = 2048

SYSTEM_PROMPT = """... (paste system prompt here) ..."""

MANDATORY_CLASS_TAGS = [
    "@pigeon.role",
    "@pigeon.intent",
    "@pigeon.tags",
    "@pigeon.lifecycle",
]

# ── javalang extraction ───────────────────────────────────────────────

def extract_ast_record(java_file: Path) -> dict | None:
    """
    Parse a .java file with javalang and return a structured record
    containing everything process_file needs. Returns None if the file
    cannot be parsed (e.g. unsupported Java syntax).
    """
    source = java_file.read_text(encoding="utf-8")

    try:
        tree = javalang.parse.parse(source)
    except javalang.parser.JavaSyntaxError as e:
        print(f"  PARSE ERROR ({java_file.name}): {e}")
        return None

    # Find the primary top-level type declaration
    # javalang exposes: tree.types → list of type declarations
    if not tree.types:
        return None

    node = tree.types[0]  # primary public type

    # ── identity ──────────────────────────────────────────────────────
    package  = tree.package.name if tree.package else ""
    fqn      = f"{package}.{node.name}" if package else node.name

    # ── existing Javadoc ──────────────────────────────────────────────
    # javalang stores the raw /** ... */ string in .documentation
    # It is None when no Javadoc is present on the declaration
    existing_doc = getattr(node, "documentation", None)

    # ── kind ──────────────────────────────────────────────────────────
    if isinstance(node, javalang.tree.InterfaceDeclaration):
        kind = "interface"
    elif isinstance(node, javalang.tree.AnnotationDeclaration):
        kind = "annotation"
    elif isinstance(node, javalang.tree.EnumDeclaration):
        kind = "enum"
    else:
        kind = "class"

    # ── role hint ─────────────────────────────────────────────────────
    role_hint = derive_role_hint(node, kind)

    # ── public method names + per-method existing doc ─────────────────
    methods = []
    raw_methods = getattr(node, "methods", []) or []
    for m in raw_methods:
        if "public" not in (m.modifiers or set()):
            continue
        methods.append({
            "name":         m.name,
            "signature":    build_signature(m),
            "existing_doc": getattr(m, "documentation", None),
            "body_source":  extract_body(source, m),
        })

    # ── public fields (for config/event classes) ──────────────────────
    fields = []
    raw_fields = getattr(node, "fields", []) or []
    for f in raw_fields:
        if "public" not in (f.modifiers or set()):
            continue
        for decl in f.declarators:
            fields.append(decl.name)

    return {
        "fqn":          fqn,
        "simple_name":  node.name,
        "package":      package,
        "kind":         kind,
        "role_hint":    role_hint,
        "existing_doc": existing_doc,
        "methods":      methods,
        "fields":       fields,
        "source":       source,
    }


def derive_role_hint(node, kind: str) -> str:
    """Derive @pigeon.role from the AST — avoids Claude having to guess."""
    if kind == "annotation":
        return "This is an annotation declaration — use role: annotation"

    extends_name = ""
    if hasattr(node, "extends") and node.extends:
        # ClassDeclaration: extends is a single ReferenceType
        # InterfaceDeclaration: extends is a list
        ext = node.extends
        if isinstance(ext, list):
            extends_name = " ".join(e.name for e in ext)
        else:
            extends_name = ext.name if ext else ""

    implements_names = []
    if hasattr(node, "implements") and node.implements:
        implements_names = [i.name for i in node.implements]

    all_supers = f"{extends_name} {' '.join(implements_names)}".strip()

    if any(k in extends_name for k in ("BaseNode", "SignalNode", "Node")):
        return "This class extends a Node base class — use role: node_base"
    if any("Event" in n or "pigeonEvent" in n for n in implements_names):
        return "This class implements a pigeonEvent interface — use role: event"
    if node.name.endswith(("Config", "Params", "Settings", "Properties")):
        return "This class is a config/parameter POJO — use role: config"
    if "Builder" in node.name or any("Builder" in n for n in implements_names):
        return "This class builds a graph — use role: graph_builder"
    if kind == "interface" and "Event" in node.name:
        return "This interface represents a market event — use role: event"

    return (
        f"Role unclear for {node.name} (extends: '{extends_name}', "
        f"implements: {implements_names}). "
        f"Infer from class body. Options: node_base, event, config, "
        f"annotation, graph_builder, util"
    )


def build_signature(method) -> str:
    """Reconstruct a readable method signature string from javalang AST."""
    modifiers  = " ".join(sorted(method.modifiers or []))
    return_type = method.return_type.name if method.return_type else "void"

    params = []
    for p in (method.parameters or []):
        ptype = p.type.name if p.type else "?"
        params.append(f"{ptype} {p.name}")

    throws = ""
    if method.throws:
        throws = " throws " + ", ".join(method.throws)

    return f"{modifiers} {return_type} {method.name}({', '.join(params)}){throws}".strip()


def extract_body(source: str, method) -> str:
    """
    Extract the raw method body text from source using javalang position info.
    javalang provides line/column positions on AST nodes.
    We use the method's position to find the opening brace and extract to
    the matching closing brace.

    Returns empty string if position info is unavailable.
    """
    if method.position is None:
        return ""

    lines  = source.splitlines()
    start  = method.position.line - 1  # javalang is 1-indexed

    # Find the opening brace from the method start line
    body_lines = []
    depth      = 0
    in_body    = False

    for line in lines[start:]:
        for ch in line:
            if ch == "{":
                depth += 1
                in_body = True
            elif ch == "}":
                depth -= 1
        body_lines.append(line)
        if in_body and depth == 0:
            break

    return "\n".join(body_lines)


# ── missing tag detection ─────────────────────────────────────────────

def find_missing_class_tags(existing_doc: str | None) -> list[str]:
    if existing_doc is None:
        return MANDATORY_CLASS_TAGS
    return [t for t in MANDATORY_CLASS_TAGS if t not in existing_doc]


def find_missing_method_tags(method: dict) -> list[str]:
    """
    Determine which mandatory method-level elements are absent.
    Returns a list of tag names that Claude must add.
    """
    doc = method["existing_doc"] or ""
    missing = []

    # No summary at all
    if not doc.strip():
        missing.append("summary")

    # @param required if method has parameters
    sig = method["signature"]
    has_params = "(" in sig and sig.split("(")[1].split(")")[0].strip() != ""
    if has_params and "@param" not in doc:
        missing.append("@param")

    # @return required if not void
    if "void " not in sig and "@return" not in doc:
        missing.append("@return")

    # @throws: only flag if body suggests throws but doc has none
    body = method["body_source"]
    if "throw new" in body and "@throws" not in doc:
        missing.append("@throws")

    # @pigeon.constraint: flag if body has super() or single-assign guards
    constraint_signals = ("super.", "throw new IllegalState", "if (started)", "if (!init")
    if any(s in body for s in constraint_signals) and "@pigeon.constraint" not in doc:
        missing.append("@pigeon.constraint")

    return missing


# ── prompt builders ───────────────────────────────────────────────────

def build_full_generate_prompt(record: dict) -> str:
    method_names = "\n".join(f"- {m['name']}" for m in record["methods"])
    return f"""Generate Javadoc blocks for the following Java 8 class from the pigeon framework.

TASK
Write:
1. One class-level Javadoc block with ALL mandatory tags.
2. One method-level Javadoc block for each public method listed in METHODS TO DOCUMENT.

OUTPUT FORMAT
Return the class block first, then each method block preceded by its marker:

/**
 * [class javadoc]
 */
METHOD: methodName1
/**
 * [method javadoc]
 */

ROLE HINT
{record['role_hint']}

METHODS TO DOCUMENT
{method_names}

SOURCE
```java
{record['source']}
```"""


def build_enrich_class_prompt(record: dict, missing_tags: list[str]) -> str:
    tags_list = "\n".join(f"- {t}" for t in missing_tags)
    return f"""The following pigeon class has an existing Javadoc block that is incomplete.
Append the missing @pigeon.* tags ONLY. Output one line per tag, starting with " * ".
Do NOT rewrite or rephrase any existing content.

EXISTING JAVADOC BLOCK
{record['existing_doc']}

MISSING TAGS
{tags_list}

ROLE HINT
{record['role_hint']}

SOURCE (for inference only — do not reproduce in output)
```java
{record['source']}
```"""


def build_enrich_methods_prompt(record: dict) -> str:
    """Build prompt for methods that have missing or incomplete Javadoc."""
    blocks = []
    for m in record["methods"]:
        missing = find_missing_method_tags(m)
        if not missing:
            continue

        existing_section = (
            f"EXISTING DOC:\n{m['existing_doc']}"
            if m["existing_doc"]
            else "EXISTING DOC: none"
        )
        missing_section = (
            f"MISSING TAGS: {', '.join(missing)}"
            if m["existing_doc"]
            else "WRITE: full method Javadoc block"
        )
        blocks.append(
            f"METHOD: {m['name']}\n"
            f"{existing_section}\n"
            f"SIGNATURE: {m['signature']}\n"
            f"{missing_section}\n"
            f"BODY:\n{m['body_source']}"
        )

    if not blocks:
        return ""

    methods_section = "\n\n".join(blocks)
    return f"""The following public methods in a pigeon class have incomplete or missing Javadoc.
For each method listed, output the required Javadoc. Precede each block with: METHOD: methodName

RULES
- Preserve any existing method Javadoc prose verbatim if shown.
- Append missing tags only when existing content is shown.
- Write a full block from scratch when EXISTING DOC is none.
- Output ONLY Javadoc blocks and METHOD: markers — no other text.

CLASS CONTEXT
Class: {record['fqn']}
Role:  derived from hint: {record['role_hint']}

METHODS
{methods_section}"""


# ── output parsers ────────────────────────────────────────────────────

def parse_full_generate_output(output: str) -> dict:
    """Split Claude full-generate output into class block + method blocks."""
    result  = {"class_doc": None, "methods": {}}
    parts   = re.split(r"^METHOD:\s*(\w+)", output, flags=re.MULTILINE)

    if parts[0].strip():
        result["class_doc"] = parts[0].strip()

    it = iter(parts[1:])
    for name, block in zip(it, it):
        result["methods"][name.strip()] = block.strip()

    return result


def parse_method_output(output: str) -> dict[str, str]:
    """Parse enrich-methods output into {method_name: javadoc_block}."""
    result = {}
    parts  = re.split(r"^METHOD:\s*(\w+)", output, flags=re.MULTILINE)
    it     = iter(parts[1:])
    for name, block in zip(it, it):
        result[name.strip()] = block.strip()
    return result


def inject_enrich_lines(existing_raw: str, new_lines: str) -> str:
    """Insert new tag lines before the closing */ of an existing block."""
    close = existing_raw.rfind("*/")
    if close == -1:
        return existing_raw + "\n" + new_lines
    return existing_raw[:close] + " " + new_lines.strip() + "\n */\n"


def insert_javadoc_into_source(source: str, record: dict, parsed: dict) -> str:
    """
    Insert generated class Javadoc and per-method Javadoc into source text.
    Keyed on class/method declaration lines — simple but effective for Java 8.
    """
    lines  = source.splitlines(keepends=True)
    output = []
    i      = 0

    while i < len(lines):
        line = lines[i]

        # Insert class doc before the class/interface declaration
        if parsed.get("class_doc") and re.search(
            rf"\b(public|abstract|final)\b.*\b{record['simple_name']}\b", line
        ):
            output.append(parsed["class_doc"] + "\n")
            parsed["class_doc"] = None  # insert once only

        # Insert method doc before matching method declaration
        for mname, mdoc in list(parsed["methods"].items()):
            if re.search(rf"\b{mname}\s*\(", line) and "public" in line:
                output.append(mdoc + "\n")
                del parsed["methods"][mname]
                break

        output.append(line)
        i += 1

    return "".join(output)


# ── Claude call ───────────────────────────────────────────────────────

def call_claude(user_prompt: str) -> str:
    response = client.messages.create(
        model      = MODEL,
        max_tokens = MAX_TOK,
        system     = SYSTEM_PROMPT,
        messages   = [{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text.strip()


# ── main entry point ──────────────────────────────────────────────────

def process_file(java_file: Path) -> None:
    """
    Process a single .java file:
      1. Parse with javalang → build ast_record internally
      2. Classify: complete / enrich / full-generate
      3. Call Claude as needed
      4. Write enriched Javadoc back to source
    """
    print(f"Processing: {java_file.name}")

    # Step 1 — extract everything from source via javalang
    record = extract_ast_record(java_file)
    if record is None:
        return  # parse failed — logged inside extract_ast_record

    source = record["source"]

    # Step 2 — classify class-level doc coverage
    missing_class_tags = find_missing_class_tags(record["existing_doc"])
    methods_needing_doc = [
        m for m in record["methods"] if find_missing_method_tags(m)
    ]

    nothing_to_do = (not missing_class_tags) and (not methods_needing_doc)
    if nothing_to_do:
        print(f"  SKIP (complete): {record['fqn']}")
        return

    # Step 3 — call Claude
    if record["existing_doc"] is None:
        # Full generate path — one call for class + all methods
        prompt  = build_full_generate_prompt(record)
        output  = call_claude(prompt)
        parsed  = parse_full_generate_output(output)
        new_source = insert_javadoc_into_source(source, record, parsed)

    else:
        new_source = source

        # Enrich class-level tags if needed
        if missing_class_tags:
            prompt      = build_enrich_class_prompt(record, missing_class_tags)
            new_lines   = call_claude(prompt)
            updated_doc = inject_enrich_lines(record["existing_doc"], new_lines)
            new_source  = new_source.replace(record["existing_doc"], updated_doc, 1)

        # Enrich / generate method-level docs if needed
        if methods_needing_doc:
            prompt   = build_enrich_methods_prompt(record)
            if prompt:
                output   = call_claude(prompt)
                method_docs = parse_method_output(output)
                # Insert each generated method doc into new_source
                for mname, mdoc in method_docs.items():
                    # Find the method's existing doc and replace, or insert
                    method = next((m for m in record["methods"] if m["name"] == mname), None)
                    if method and method["existing_doc"]:
                        new_source = new_source.replace(method["existing_doc"], mdoc, 1)
                    else:
                        # No existing doc — insert before the method declaration
                        new_source = re.sub(
                            rf"(\bpublic\b[^\n]*\b{mname}\s*\()",
                            mdoc + "\n    \\1",
                            new_source,
                            count=1,
                        )

    # Step 4 — write back to source file
    java_file.write_text(new_source, encoding="utf-8")
    print(f"  WROTE: {record['fqn']}")


# ── batch runner ──────────────────────────────────────────────────────

def process_source_tree(root: Path) -> None:
    """Walk a source tree and process every .java file."""
    java_files = sorted(root.rglob("*.java"))
    print(f"Found {len(java_files)} .java files under {root}")
    for java_file in java_files:
        process_file(java_file)


if __name__ == "__main__":
    import sys
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("src")
    process_source_tree(root)