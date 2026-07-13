- Python jsonschema documentation: https://python-jsonschema.readthedocs.io/
- Python jsonschema package releases: https://pypi.org/project/jsonschema/

## Use of external sources

When adding a requirement derived from an external source:

1. Link to the authoritative source.
2. Summarize rather than copy substantial text.
3. State whether the rule is mandatory in this repository or merely guidance.
4. Avoid implying certification or compliance.
"""
(root/'SOURCES.md').write_text(sources, encoding='utf-8')

