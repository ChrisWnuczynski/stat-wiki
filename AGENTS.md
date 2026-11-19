# Local sources

The private Dodge (2008) source is outside this repo at `~/statwiki-sources/dodge2008/`. On a managed workspace where home is read-only, use `/workspace/statwiki-sources/dodge2008/` or set `STATWIKI_DODGE_DIR`. Before writing a new research page, run `python research/check_sources.py`; if it fails, stop and report the missing source. Search `index.tsv` for an entry name, then open its `pages/pdf-NNNN.txt` file; each file marks both the PDF page and the printed book page. The original PDF is there as `dodge2008.pdf`. Do not commit the PDF or extracted text.

- Use Dodge for orientation, history, and pointers to original papers.
- Cite only material actually read there, always with the printed page number: `{{cite:dodge2008}} (p. n)`.
- For named results and proofs, prefer the original paper or a standard textbook; check important claims against a second source.
- Write in your own words; never copy entries.

# Working on this repo (rules for bots and agents)

Cursor, Claude, and the research bots maintain this repository. Every change follows these rules.

- Never push to `main`. Open a pull request from a fresh branch cut off current `main`. Do not base that branch on another pull request's branch.
- Name the branch `<bot>/<type>/<short-purpose>`, for example `cursor/docs/agent-ground-rules`. Use a branch for one pull request only.
- One pull request, one purpose. The title and the description say what changed and why. Put a bulk content batch in a single pull request that names its range.
- A pull request that combines or continues others says `Supersedes #N` and closes the originals.
- Merge only when the checks are green and the pull request is mergeable. Squash-merge, then delete the branch.
- Do not commit scratch files: handoff notes, run logs, reports, baselines, or to-do lists. Put them in the pull request description, or in a folder already listed in `.gitignore` (research drafts go in `research/pending/`).
- A daily repo-manager bot labels, comments, and tidies branches that have been merged. Closing pull requests, and deleting work that has not been merged, is left to Chris.
