Used when javalang finds existing Javadoc but @fusion.* tags are missing. Claude receives the existing block verbatim and a precise list of which tags are absent. It appends only those tags — no rewriting.

# User prompt — enrich (class level)
The following Fusion class has an existing Javadoc block that is incomplete.
Your job is to append the missing @fusion.* tags ONLY.

**RULES FOR THIS TASK**
- Do NOT rewrite, rephrase, or remove any existing content.
- Do NOT output the full block. Output ONLY the missing tag lines.
- Output one tag per line, exactly as it would appear inside a Javadoc comment.
- Each line must start with " * " (space asterisk space).
- If a tag requires multiple entries (e.g. multiple @fusion.constraint),
  output one line per entry.

**EXISTING JAVADOC BLOCK**
```
{existing_javadoc_raw}
# The raw string from javalang's .documentation field, exactly as found.
```

**MISSING TAGS**
```
{missing_tags_list}
# e.g.
# - @fusion.role
# - @fusion.intent
# - @fusion.constraint
```

**ROLE HINT**
```
{role_hint}
SOURCE (for inference only — do not reproduce in output)
{full_class_source}
```

**EXPECTED OUTPUT EXAMPLE**

If missing tags were @fusion.role and @fusion.constraint, output exactly:
* @fusion.role        node_base
* @fusion.constraint  Must call super.onInit() as first statement of onInit()


---
# Missing tags derivation — compute in Python before the call
```
# Determine which @fusion.* tags are absent from existing Javadoc

MANDATORY_CLASS_TAGS = [
"@fusion.role",
"@fusion.intent",
"@fusion.tags",
"@fusion.lifecycle",
]

def find_missing_tags(existing_doc: str | None, node_kind: str) -> list[str]:
if existing_doc is None:
return MANDATORY_CLASS_TAGS   # full generate path, not enrich

     missing = []
     for tag in MANDATORY_CLASS_TAGS:
         if tag not in existing_doc:
             missing.append(tag)

     # @fusion.constraint is mandatory only if constraints are inferable
     # We leave this to Claude — do not add it to the missing list programmatically

     return missing   # empty list → skip this class, already complete

     ---
     User prompt — enrich (method level)
     The following public methods in a Fusion class have incomplete or missing Javadoc.
     For each method listed, output a complete method-level Javadoc block.

     RULES
     - Preserve any existing method Javadoc prose verbatim if shown.
     - Append missing tags only when existing content is shown.
     - Write a full block from scratch when no existing doc is shown.
     - Precede each block with: METHOD: {methodName}

     CLASS CONTEXT
     Class:  {fqn}
     Role:   {role}
     # Role informs what constraints are likely (e.g. node_base → super call likely)

     METHODS
     {per_method_block}
     # For each method, structured as:
     #
     # METHOD: subscribe
     # EXISTING DOC: none
     # SIGNATURE:    public void subscribe(Producer<E> producer)
     # BODY:
     #     if (this.producer != null) throw new IllegalStateException(...);
     #     this.producer = producer;
     #
     # METHOD: setLookback
     # EXISTING DOC:
     #     /** Sets the lookback window. */
     # MISSING TAGS: @param, @fusion.constraint
     # SIGNATURE:    public void setLookback(int bars)
     # BODY:
     #     if (started) throw new IllegalStateException(...);
     #     this.lookbackBars = bars;

```

# User prompt — enrich (method level)
The following public methods in a Fusion class have incomplete or missing Javadoc.
For each method listed, output a complete method-level Javadoc block.

**RULES**

- Preserve any existing method Javadoc prose verbatim if shown.
- Append missing tags only when existing content is shown.
- Write a full block from scratch when no existing doc is shown.
- Precede each block with: METHOD: {methodName}

**CLASS CONTEXT**
```
Class:  {fqn}
Role:   {role}
# Role informs what constraints are likely (e.g. node_base → super call likely)
```

**METHODS**
```
{per_method_block}
# For each method, structured as:
#
# METHOD: subscribe
# EXISTING DOC: none
# SIGNATURE:    public void subscribe(Producer<E> producer)
# BODY:
#     if (this.producer != null) throw new IllegalStateException(...);
#     this.producer = producer;
#
# METHOD: setLookback
# EXISTING DOC:
#     /** Sets the lookback window. */
# MISSING TAGS: @param, @fusion.constraint
# SIGNATURE:    public void setLookback(int bars)
# BODY:
#     if (started) throw new IllegalStateException(...);
#     this.lookbackBars = bars;
```

Four tabs — system prompt, full generate user prompt, enrich user prompt, and the Python orchestration. A few design decisions worth explaining:
Why role hint is computed in Python, not left to Claude. The extends/implements chain in the javalang AST is machine-readable — your code can determine role with near certainty before the Claude call. Giving Claude a pre-computed hint eliminates an entire category of wrong @fusion.role values and reduces the inference burden on a call that's already doing a lot.

Why full generate and enrich are separate user prompts but share one system prompt. The system prompt defines the schema, the inference rules, and the output contract once. The user prompt only needs to describe the specific task variant. This keeps the system prompt stable across all calls, which means you can cache it and reason about it consistently.

Why the enrich prompt asks for tag lines only, not the full rewritten block. If Claude rewrites the whole block it will paraphrase existing prose, introduce subtle differences, and you lose the developer's original intent. Returning only  * @fusion.constraint  ... lines that you splice in before the closing */ is safer and cheaper.

Why MAX_TOK = 2048. A full class with six public methods and complete Javadoc for each is comfortably under 1,000 tokens of output. 2048 gives headroom for larger classes without paying for a 4k or 8k allocation on every call.

# javadoc_system_prompt.md

process_file(java_file: Path) now takes only the file path and builds everything internally. Here's what changed structurally:

extract_ast_record(java_file) is the new first step — it runs javalang on the file and returns a self-contained dict with fqn, existing_doc, role_hint, methods (each with signature, existing doc, and body source), fields, and the raw source string. If javalang throws a JavaSyntaxError it logs and returns None cleanly.

derive_role_hint(node, kind) reads directly from the javalang AST nodes — node.extends, node.implements — rather than needing anything passed in. It covers the six role types and produces a fallback hint with diagnostic info when it can't determine the role confidently.

extract_body(source, method) uses javalang's position info (method.position.line) to locate the method in the raw source and extract its body by brace-depth counting. This is what lets Claude infer constraints without you having to pre-extract bodies separately.

find_missing_method_tags(method) also runs inline — it checks the method's existing_doc, signature, and body_source to determine what's missing, including detecting throw new in the body to flag a missing @throws.

The batch runner at the bottom (process_source_tree) just calls process_file(path) for every .java found under the given root — so the whole preprocessing run is python process_file.py src/.