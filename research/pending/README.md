# Per-page additions during parallel research

Each worktree writes `research/pending/<slug>.json` instead of editing a shared
file. Only include fields needed by that page. Example:

```json
{
  "bibliography": {
    "new_source_key": {
      "authors": ["Surname, Initials"],
      "year": 2000,
      "title": "Exact title",
      "kind": "article",
      "venue": "Journal name",
      "doi": "10.example/identifier",
      "verification": {"source": "crossref", "id": "10.example/identifier"}
    }
  },
  "proofs_todo": [
    {"slug": "result-slug", "title": "Result title", "reason": "Specific missing proof"}
  ],
  "shared_changes": [
    {"file": "distributions.json", "description": "Exact change needed and why"}
  ]
}
```

The build and offline citation verifier include pending bibliography entries.
During integration, apply verified entries to `bibliography.json`, put unresolved
proofs in `research/proofs-todo-overrides.json`, implement any shared changes,
then remove the integrated pending files. The generated `proofs-todo.json` is
written by the build.
