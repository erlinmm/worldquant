Used when javalang finds no existing Javadoc on a class. The user prompt sends the full class source (signature + bodies) and requests both the class-level block and all public method blocks in one call.

---

# Generate Javadoc blocks for the following Java 8 class from the Fusion framework.

TASK
Write:
1. One class-level Javadoc block with ALL mandatory tags.
2. One method-level Javadoc block for each public method listed in METHODS TO DOCUMENT.

OUTPUT FORMAT
Return the class block first, then each method block preceded by its marker:
```
/**
* [class javadoc]
  */
  METHOD: {methodName1}
  /**
* [method javadoc]
  */
  METHOD: {methodName2}
  /**
* [method javadoc]
  */
```

# ROLE HINT
**{role_hint}**

```
# e.g. "This class extends SignalNode — use role: node_base"
# Derived by your Python code from the extends/implements chain before calling Claude.
```
# METHODS TO DOCUMENT
**{method_names_list}**
```
# e.g.
# - onInit
# - subscribe
# - emit
# - setLookback
```
# SOURCE

```java
{full_class_source}

# Full class source including method bodies.
# javalang cannot provide this directly — read the raw .java file for this class
# and pass the text between the class declaration and the closing brace.

Role hint derivation — compute this in Python before the call
# Derive role_hint from javalang AST before calling Claude
# Saves Claude from having to guess and reduces errors
```

```
def derive_role_hint(node) -> str:
extends   = getattr(node, 'extends',    None)
implements = getattr(node, 'implements', []) or []

    ext_name = extends.name if extends else ""
    imp_names = [i.name for i in implements]

    if "BaseNode" in ext_name or "SignalNode" in ext_name or "Node" in ext_name:
        return "This class extends a Node base class — use role: node_base"
    if any("Event" in n or "FusionEvent" in n for n in imp_names):
        return "This class implements a FusionEvent interface — use role: event"
    if node.name.endswith(("Config", "Params", "Settings")):
        return "This class is a config/parameter POJO — use role: config"
    if isinstance(node, javalang.tree.AnnotationDeclaration):
        return "This is an annotation declaration — use role: annotation"
    if any("Builder" in n for n in [node.name] + imp_names):
        return "This class builds a graph — use role: graph_builder"
    return "Role is unclear — infer from class body. Options: node_base, event, config, annotation, graph_builder, util"
```