# Contributing
- Propose a new term or change with an issue first. Include a definition, one real deployment it describes, and why no existing term covers it.
- Terms describe patterns, never products. PRs naming a vendor in a term label will be asked to generalize.
- Term IDs are never reused or renamed. Deprecated terms stay with `deprecated: true` and a pointer to the replacement.
- Run `python scripts/validate.py` before opening a PR.
