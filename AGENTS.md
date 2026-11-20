# Local sources

The private Dodge (2008) source is outside this repo at `~/statwiki-sources/dodge2008/`. On a managed workspace where home is read-only, use `/workspace/statwiki-sources/dodge2008/` or set `STATWIKI_DODGE_DIR`. Before writing a new research page, run `python research/check_sources.py`; if it fails, stop and report the missing source. Search `index.tsv` for an entry name, then open its `pages/pdf-NNNN.txt` file; each file marks both the PDF page and the printed book page. The original PDF is there as `dodge2008.pdf`. Do not commit the PDF or extracted text.

- Use Dodge for orientation, history, and pointers to original papers.
- Cite only material actually read there, by printed page from `index.tsv`: `{{cite:dodge2008}} (p. n)`. Never cite a PDF page index. Letter-section openers carry no page number.
- For named results and proofs, prefer the original paper or a standard textbook; check important claims against a second source.
- Write in your own words; never copy entries.
- No citations in hidden answers.

# Working on this repo (rules for bots and agents)

Cursor, Claude, and the research bots maintain this repository. Every change follows these rules.

- Never push to `main`. Open a pull request from a fresh branch cut off current `main`. Do not base that branch on another pull request's branch.
- Name the branch `<bot>/<type>/<short-purpose>`, for example `cursor/docs/agent-ground-rules` or `dot/fix/infobox-keyboard`. Use a branch for one pull request only.
- One pull request, one purpose. The title and the description say what changed and why. Put a bulk content batch in a single pull request that names its range.
- A pull request that combines or continues others says `Supersedes #N` and recommends that Chris close the originals. Do not close them yourself.
- Merge only after a separate review approves that exact head SHA, the checks are green, and the pull request is mergeable. Squash-merge, then delete the branch.
- Do not commit scratch files: handoff notes, run logs, reports, baselines, or to-do lists. Put them in the pull request description, or in a folder already listed in `.gitignore` (research drafts go in `research/pending/`).
- A daily repo-manager bot labels, comments, and tidies branches that have been merged. Closing pull requests, and deleting work that has not been merged, is left to Chris.
- If usage runs out or a tool keeps failing, keep unverified work local, record the state, tell Chris once and pause. Push only if the full applicable checklist already passed.

# Before every push

Run the checks that apply to the diff and fix every failure. Do not weaken or skip a test to get green. Rendered and visual checks apply when the change affects rendered pages.

```
python build_wiki.py
python -m unittest discover -p 'test_*.py'
for f in checks/*.py; do python "$f" || echo "FAIL $f"; done
python check_overview_links.py
python verify_citations.py --offline
quarto render            # when the change affects rendered output
python tools/visual_check.py --site _site
git diff --check
```

Also run the Node tests listed in `.github/workflows/publish.yml` when the change touches `labs/`, `webr/`, `ask/` or search code. If `STATWIKI_DODGE_DIR` is unavailable, add no new Dodge citations.

# Approvals on record

Chris has said the following. This heading does not attribute any other note to him. Drafts he has not approved are in `docs/automation/HANDOVER.md` under "Proposed, awaiting Chris's approval", and they are not in force.

- Merge only after Peer Review approves the head SHA and CI is green. Do not deploy except by that approved merge.
- `research/content/`, `sources/`, `build_wiki.py` and `.github/workflows/` may be edited through a pull request. `config`, `checks/`, tests and `tools/` are ordinary changes, reviewed like any other, and are not pre-approved.

# Hard limits

- No external sign-ups, purchases or form submissions without Chris.

# Citations

- Each concept page keeps at least 5 citations from at least 2 independent sources, with locators. Section-only locators and "page n of 8" locators do not count toward the 5.
- Cite Dodge (`dodge2008`) only for material actually read, by printed page from `index.tsv` (`{{cite:dodge2008}} (p. n)`), never by PDF page index. Letter-section openers carry no page number. No citations in hidden answers. Use Dodge for orientation and history, not technical claims. Do not cite `sas2012_glm` Ch. 3 or Dodge biography or encyclopedia entries for technical claims.
