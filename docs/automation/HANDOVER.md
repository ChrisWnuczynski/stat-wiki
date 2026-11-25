# StatWiki automation handover (state at 20 Nov 2026, 9:05am Australia/Brisbane)

This is the work the previous automation (a team of Grok Bot agents and Cursor cloud agents) left unfinished when its usage ran out overnight on 19–20 Nov 2026. Nothing from it is still running, so there's no job to attach to. **The repository is the source of truth.** Before you act on any item below, check it against GitHub, because PRs may have moved since this was written. Approvals Chris has given are in `/AGENTS.md`. Queued plans are in `docs/automation/plans/`. Drafts he has not approved are in **Proposed, awaiting Chris's approval** at the end of this file, and they are not in force.

All times are Australia/Brisbane (UTC+10). The repo is public, so nothing secret or private goes in this folder.

## Current operator workflow (directly authorized by Chris)

Sections 1–5 preserve the dated handover, including its queue, branch names and Editor verdicts. They are historical context, not current authorizations. The current correction on the existing `grok/docs/automation-handover` branch is limited to `AGENTS.md` and this handover; the verified Gap 3 plan and numerical checker stay unchanged. This does not authorize writing, submitting or merging the proposed new articles, SEO writes, dashboard or DNS changes, token access, or other queued proposals.

- Fresh branches start from current `main` and use `codex/<type>/<purpose>`. Update an existing published branch with a normal merge of `origin/main`; never rebase or force-push it.
- Run the full applicable pre-push checklist in `AGENTS.md`. A separate full-site Quarto render and visual pass are no longer a pre-merge gate (confirmed by Chris directly, 2026-11-23; relayed by Dot to the Slack claim-board thread); the GitHub Pages build must still succeed, and after each successful deploy the changed pages get a live check for broken maths, layout and links, with regressions logged on the matching Linear ticket. Keep unverified work local if any required check fails. Never delete, loosen or skip a test to get green.
- Review must be independent of the authoring pass. Its top-level PR verdict must be exactly `REVIEW APPROVED <full head SHA>` or `REVIEW CHANGES NEEDED <full head SHA>`, with the actual full head SHA in place of the placeholder; put findings below that line. Any new head requires a new review.
- Squash-merge only after independent approval of the exact current head, all required checks passing, green CI and a mergeable PR. New-article and gap-batch merges follow current [AGENTS.md](../../AGENTS.md), subject to any specific holds in force. No self-approval; no deployment except through an authorized, reviewed merge. This documentation correction does not authorize a merge.
- The requested durable handover, checked-in plans under `docs/automation/plans/`, and their number-check scripts are project documentation. Live STATE files, private notes, run logs, reports, baselines, to-do lists and scratch handoff artifacts must stay uncommitted or in an already ignored folder. This distinction does not adopt any other unapproved proposal.
- Do not hand-edit generated output (`articles/*.qmd`, `_quarto.yml`, `proofs-todo.json`, `_site/`). Preserve links and each file's existing line endings. Run logs and private details do not belong in this handover.

## 1. Snapshot (checked against the GitHub API at 9:00am, 20 Nov 2026)

- `main` = `1bf99774` "Polish batch 003: count models in a GLM (#87)", merged 8:59am 20 Nov. Before that, main was `62ad78da` (#88, Cloudflare cache purge after deploys).
- Deploys: Build and publish run 175 (id 44633629876) on `1bf99774` was in progress at 9:00am and deploys #87. Run 171 succeeded, so #78 and #88 are live. Index Ask StatWiki last succeeded on `62ad78da`. Confirm that run 175 and the follow-on Index Ask run both succeed.

| PR | Branch | Head | State vs main `1bf99774` | Review status | Next action |
|---|---|---|---|---|---|
| #87 | claude/content/glm-count-models | fa251c1 | **MERGED** as 1bf99774 | Approved at fa251c1, CI green | Done. Check the live count-model pages after run 175 deploys (section 5). |
| #91 | grok/content/question-bank-ranks | fc3d00a | **dirty**: 11 behind `1bf9977`; merging main conflicts in six content pages; no CI on this head | **CHANGES NEEDED** at fc3d00a (9:15am). Do not merge. | See 2.1. |
| #89 | grok/fix/visual-followups | ca9e33f | 0 behind, 5 ahead, 33 files; CI green at ca9e33f | Last reviewed at ddcbf84 (CHANGES NEEDED); head ca9e33f is awaiting review | See 2.2. |
| #90 | cursor/seo-technical-1 | 007bf82 | clean, 1 behind, 2 ahead, 8 files; CI green at 007bf82 | CHANGES NEEDED at 007bf82 | See 2.3. |
| #65 | research/quality-followup-68-517 (draft) | 3bc956d | dirty, 78+ behind | Stale | See 2.4. |

## 2. Open PRs: what is left

### Merge order (Editor's ruling, 20 Nov)
1. #87 (done).
2. #91 was next, after merging `origin/main` so it keeps #87's prose. **Superseded 9:15am:** Peer Review marked `fc3d00a` CHANGES NEEDED. Do not merge until 2.1 is fixed.
3. #89 and #90 in whichever order they reach APPROVED. #91 and #89 both touch `research/content/arima-model.md` and `hazard-rate.md`. Whichever of the two merges second must merge `origin/main` first and must not revert the other's changes.
4. **Start batch 004 only after BOTH #89 and #91 have merged** (section 3).

### 2.1 #91: move concept Check yourself prompts into the question bank
**Peer Review: CHANGES NEEDED at fc3d00a (9:15am 20 Nov 2026). Do not merge.**

The branch is 11 commits behind main `1bf9977`. Merging main conflicts in `research/content/` on bootstrap-error-and-the-correction, count-models-beyond-the-poisson, count-responses, decision-stump, graphical-lasso and poisson-regression. Keep #87's merged text on the three count-model pages. No CI has run on this head. Never rebase or force-push.

1. 25 existing Check yourself items vanish from 16 unannounced pages, because the new `research/self-checks.json` entries displace main's picks. Restore each one; only the six announced retargets may change. Pages and items: margin-of-error (ex-da-juice-variance, ex-da-melbourne-oil); designed-experiment (depth-blinding-design-roles, depth-blinding-risk-difference); posterior-hypothesis-probability (ex-applied-iq); proportional-odds-model (q-46); likelihood-function (ex-inf-no-uniform-risk, ex-inf-shrunk-mean); explanatory-variable (ex-inf-advertising-r2, ex-inf-correlation-t); expectation (depth-mgf-bernoulli-sum, ex-prob-affine-uniform-mean); variance (depth-mgf-domain, ex-prob-affine-uniform-mean); consistent-estimator and unbiased-estimator (ex-inf-exponential-mle); correlation (ex-sl-01-2); mean-vector-and-covariance-matrix (ex-sl-01-4); joint-probability-mass-function (ex-prob-cdf-of-maximum, ex-prob-independent-exponentials); hazard-rate (ex-prob-bridge-paths); pooled-variance (ex-inf-green-voters); proper-prior-and-proper-posterior (c-01, c-05); gaussian-linear-model (depth-reference-prior-update).
2. The converter turned `[Label](../questions/x.qmd): instruction` self-checks into new `depth-*` stubs. That drops 243 links on 142 pages, creates duplicates (for example `depth-addiction-data-q1` copies `ex-sl-10-2`), and about 98 new prompts lack their givens (for example `depth-margin-of-error-q1`, `depth-m-m-queue-q1`, items saying "In the worked example", "the displayed matrix", "part (f)"; `depth-blocks-in-analysis-of-variance-q1` and `depth-brier-score-q1` are not questions). Keep pointing at the existing question page and do not create a copy; otherwise put the full givens in the body. Add a check rejecting bodies that rely on "worked example", "displayed", "part (" or a "Label: " stub.
3. Remove the literal "Practice question" label that starts 46 new bodies.
4. Put plain-text maths in `$...$` in `depth-kolmogorov-extension-theorem-q2` and `depth-lehmann-scheffe-theorem-q1`.

Follow-up, not blocking: reword the site-internal "Question-bank page" link and the "Try these questions before opening an answer." line (`build_wiki.py` ~5554/5570/5909). Do not repeat the prompt as a heading when an item has no title. Use `$...$` maths in `depth-weak-stationarity-ar` and `depth-weak-not-strict`.

Verified OK: scope, line endings, a clean build, citations, the six retargets, and the absence of banned phrases.

### 2.2 #89: shared sidebar and mid-width infobox
**Peer Review: Last reviewed at ddcbf84 (CHANGES NEEDED); head ca9e33f is awaiting review.**

Three blocking items:
1. `research/todo.md:174–323` adds a 150-line "Repeated exercises left for a later pass" section, but `research/*.md` outside `research/content/` must not change. Revert the file to main (blob `1b4789c`) and move the list into the PR description.
2. Keyboard access to the mid-width infobox (`build_wiki.py` ~7830–7846, `armInfoboxes`). At 900–1200px the title has `role="button"` but no `tabindex`, so keyboard users can't open it. Its role and state are also announced at every width. Links inside a closed box are clipped (`styles.css` ~592–595) but can still take Tab focus. Hide them, for example with `html.infobox-compact .infobox:not(.is-open) > :not(.infobox-title) { visibility: hidden; }` or `inert`. UX and UI's version below supersedes the role=button approach.
3. Delete the visible paragraph after the new hidden answer at `research/content/limiting-distribution.md:58`. It works the answer out in full, (2/7, 5/7), and it wrongly says the weather chain "has larger diagonal entries". Its diagonal is 0.8/0.6 against 0.5/0.8 here, and the real difference is the second eigenvalue, 0.4 against 0.3. Its Durrett §5.5 locator is probably §5.6. The page keeps 8 cites from 2 sources without it.

**UX and UI: required**
1. Put a real `<button>` inside the infobox heading instead of `role=button` on the title, with `aria-controls` pointing at the body and `aria-expanded` kept in sync. The button exists, or is active, only while the box is compact.
2. While the box is compact, show a visible chevron or "Show details" cue with at least 3:1 contrast (WCAG 1.4.11), using the site's standard focus ring.
3. Progressive enhancement: the box starts open when JS fails, and collapses only once `armInfoboxes` runs.
4. The current section is open in the server-rendered sidebar, so its Overview hub links show without JS. Main did this; #89 currently doesn't.
5. `markCurrent` (`build_wiki.py` ~7878) normalises `.html`, `index.html` and trailing slashes, so `/notes/` and extensionless URLs get `aria-current="page"`. This matters more once #90's trailing-slash canonicals land.
6. Check that the mid-width infobox doesn't cover or reorder the lead paragraph that #82 put first.
- Add tests for 1, 3 and 5.

**Editor: required**
- (a) The label "A further exercise." appears on 15 pages, which reads as a template. Drop it, and introduce each exercise with a sentence specific to its page, or number it under the existing exercises. Never reuse one phrase across pages.
- (b) The bridge sentences at `research/content/expectation.md:40`, `likelihood-function.md:36` and `variance.md:36` point at questions those pages no longer state. Rewrite each to lead into what actually follows, or delete it.

**Peer Review: also fix (non-blocking)**
- `sidebar_share.py:300` fails on a second run over an already-processed `_site`, which breaks single-file render and `quarto preview`. Make it idempotent.
- `build_wiki.py:4682` produces "K-anonymity" and "K-means" in the glossary. Keep them lowercase "k-".
- Optional: `lang: en` could be `en-AU`. Ask Chris before changing it.
- Existing cites inside hidden answers on variance, expectation and likelihood-function predate this PR. Note them; don't fix them here.

**Already verified by Peer Review at ddcbf84 (don't redo unless that code changes):** prev/next, canonicals and the sitemap match main's render; breadcrumbs are correct; all 1,699 pages are reachable by plain links within 2 clicks; median HTML fell from 409KB to 88KB; exercises on 20 pages were recomputed and are correct; `glossary-meanings.json` (37 definitions) is accurate.

The branch is 0 behind and 5 ahead of main `1bf99774`.

### 2.3 #90: technical SEO (fonts, canonicals, structured data, figure titles)
**Peer Review: blocking (at 007bf82)**
1. `search_meta.py:549–552`: the `GOOGLE_FONT_IMPORT` regex stops at the first `;` inside the URL (`wght@300;400;700&display=swap`). That leaves an unterminated string that swallows the `:root` rule and corrupts the CSS (reproduced on Cosmo, Darkly and Lato). Match the quoted body with `[^"]*` or `[^']*` and `url(...)` up to `)`, or drop the stripper. Main's live CSS has 0 Google Fonts imports, so the "before" claim in the PR body is wrong: correct the body. Add asserts to `test_navbar.py` (~42–48) that `:root{` survives and no `display=swap` is left.
2. `_cut_title` (`build_wiki.py` ~5487–5503) cuts figure titles mid-maths or leaves them dangling. For example, part1-fig-04-proposal-scale ends "…with the same N(0", da-power-by-n ends "…half a standard", and da-01-studies-and-data-assignment is titled "Left: in an observational study". Cut only at commas at bracket depth 0 and outside `$…$`, never leave a dangling fragment, and never title from a leading "Left:", "Right:", "Top:" or "Bottom:" panel label. Add `test_seo.py` cases.

**Also do:**
- Give the 43 disambiguation stubs their own canonical instead of `search.html`, which is now out of the sitemap.
- Add `test_seo.py` and `test_navbar.py` to CI.
- Test the robots.txt Disallow rules for figures.
- After #90 merges and deploys, implement `plans/seo-descriptions-approved-5.md`.
- Chris or an SEO tool can resubmit the sitemap in Search Console. It's optional, because the sitemap is listed in robots.txt.
- Note for reviewers: the sitemap no longer lists `lastmod` values, because they were just the build time. SEO was told and hadn't objected.

**Already verified:** the build changes only the title lines of 87 `files/*.qmd`; the sitemap goes from 1,700 to 1,698 entries with trailing-slash canonicals and no redirect loops; the JSON-LD is valid; it merges cleanly with #89.

### 2.4 Draft #65 (stale)
#91 split part of #65 out. Finish the split by carrying over anything still useful as small new PRs. Don't redo #65's lecture-note citation swaps unless every claim is checked against its source. Then recommend in a comment that Chris close #65, because AGENTS.md leaves closing to him.

## 3. Queue (after the open PRs above)
At most 3 content PRs may be in flight at once. Priority: fix PRs, then polish batches, then new-article batches, then SEO and technical work.

1. **Batch 004: random variables and expectation**. Plan: `plans/batch-004-random-variables.md`. Starts on main after #89 AND #91 merge. Branch `dot/content/random-variables`. Read its two ADDENDUM sections first:
   - Its precedence note's reference to #65 is stale. Don't edit `research/self-checks.json` or `sources/depth-questions.json`.
   - Before cutting the expectation and variance Answers blocks, check on main whether #91 has already removed them, and skip the cut if so.
   - Don't duplicate the Check yourself items #89 adds on variance and expectation.
   - Retitle exercise ex-prob-second-moment in its `sources/stat2003` chapter, keeping the file's line endings.
2. **KaTeX macros fix** (no PR exists, and no branch was pushed). Plan: `plans/katex-prerender-plan.md`. 118 maths spans on about 13 pages show red raw TeX because `\E`, `\Var` and `\Cov` are undefined. Example pages: cauchy-schwarz-inequality, designed-experiment, first-passage-time, effective-sample-size and marginal-and-conditional-effects. Step 1: add one shared KaTeX macro table used by page rendering, the hover preview and the Ask widget, then test that 0 `.katex-error` elements remain site-wide. Step 2, as a separate PR: build-time pre-render. Keep `htmlAndMathml` output for screen readers.
3. **Gap batch 2: experimental design** (new articles: latin-square-design, crossover-design, split-plot-design, two-level-factorial-design). Plan: `plans/gap-batch-2-design.md`, number checks in `plans/checks/gap-batch-2/`. No branch was pushed. Wait until any prerequisite still open has merged, then cut `codex/content/gap-batch-2-design` from current main. Editor's amendments: don't edit existing pages (add backlinks via `topics.py` only); the Lenth cutoff is 2.5·s0; no bare "factorial design" alias. The earlier `dot/content/gap-batch-2-design` name is historical. A gap-batch merge follows current [AGENTS.md](../../AGENTS.md) and requires independent Peer Review approval of the exact current head SHA, all required checks passing, green CI and a mergeable PR, subject to any specific holds in force.
4. **Gap batch 3: core methods** (mcnemar-s-test, regression-diagnostics, 68-95-99-7-rule, analysis-of-covariance). Plan: `plans/gap-batch-3-core-methods.md`, which has Editor's amendments at the end. Number checks are in `plans/checks/gap-batch-3/`. Wait until gap batch 2's PR has merged, because both touch the shared registry files (`topics.py`, `bibliography.json`, `citations.py`, graph ids), then cut `codex/content/gap-batch-3-core-methods` from current main. The `oehlert2010` key is shared with batch 2, so add it once. The earlier `claude/content/gap-batch-3-core-methods` name is historical.
5. **Gap batch 4** (not written): Editor's first picks are the Kolmogorov–Smirnov test and Welch's ANOVA.
6. **Editor backlog**: `plans/editor-backlog.md`. Items include citation separators rendering as "group.;[1] ;[2]" after #80, questions that share their article's title, shared self-check IDs, the 47 "no worked answer" questions and findability aliases.
7. **Repo hygiene**: about 20 remote branches have commits not on main and no open PR, for example cursor/content/gap-batch-1, gap1, polish/batch-001, cursor/a11y-reading-order-5840 and claude/fervent-hamilton-c8tz2r. Most belong to merged or superseded PRs. List them with their PR status and recommend deletions to Chris; don't delete them yourself. The bibliography entry `r_wilcox_test451` is unused.

## 4. Sources
- The Dodge (2008) encyclopedia is a private, copyrighted source. It is not in the repo and wasn't on the last automation's machine either. `research/check_sources.py` fails without it. Until Chris provides it privately (via `STATWIKI_DODGE_DIR`), add no new Dodge citations, and keep the existing ones unchanged.
- The gap-batch plans name open sources (NIST/SEMATECH handbook, Oehlert, Fisher 1926 and others). Download them in the working environment, read them and cite them. Never commit them.

## 5. Live-site checks overdue (due on the `1bf99774` deploy)
The overnight crawls failed, so nothing was checked between about 8pm on 19 Nov and 8:50am on 20 Nov. Once run 175 is live, check these at desktop, 900–1200px and mobile widths:
- #87's 11 pages: count-models-beyond-the-poisson, count-responses, poisson-regression, quasi-poisson, negative-binomial-distribution, overdispersion, underdispersion, fisher-scoring, log-link, reading-a-log-linear-coefficient and score-function (maths, layout, cites, headings).
- #79's navbar and chrome (accessibility), the IQ example on the normal-distribution page, #82's lead-first layout, the four #78 articles (wilcoxon-signed-rank-test, shapiro-wilk-test, friedman-test, levene-s-test) and SEO's accessibility items.
- Site-wide: `.katex-error` count, console errors, dead internal links, and `https://ask.statwiki.io` returning 200.

## 6. People and permissions
- Chris (owner, Brisbane) is the only person who can grant new permissions. He has said:
  - Merge only after independent Peer Review approves the exact current head SHA, all required checks pass, CI is green and the PR is mergeable. New-article and gap-batch merges follow current [AGENTS.md](../../AGENTS.md), subject to any specific holds in force. Do not deploy any other way.
  - `research/content/`, `sources/`, `build_wiki.py` and `.github/workflows/` may be edited through a pull request. `config`, `checks/`, tests and `tools/` are ordinary changes, reviewed like any other, and are not pre-approved.
- Every PR needs a separate review pass whose verdict names the head SHA. Never self-approve in the same pass that wrote the change. The old roles (Editor, Researcher, Peer Review, UX and UI, SEO, Cloudflare, Repo Helper) were separate bots, so the verdicts above were independent reviews.

## 7. Review protocol (Peer Review role)
For every PR and every new head SHA:
1. Start from a fresh checkout of the head and run the checks in `AGENTS.md` that apply to the diff, and `git diff --check`. A separate full-site render and visual pass are no longer a pre-merge gate. A merge still needs a separate review that approves that exact head SHA.
2. Recompute every number, and open the cited sources to confirm claims and locators.
3. Confirm that only allowed files changed, tests aren't weakened, generated files are untouched and line endings are kept.
4. Post a top-level PR comment whose first line is exactly `REVIEW APPROVED <full head SHA>` or `REVIEW CHANGES NEEDED <full head SHA>`, substituting the actual full head SHA, with numbered blocking items and non-blocking notes below it. The review pass is separate from the pass that wrote the change. Never self-approve.
5. A squash merge needs that separate pass's `REVIEW APPROVED <full head SHA>` verdict on the current head, all required checks passing, green CI and a mergeable PR. New-article and gap-batch merges follow current [AGENTS.md](../../AGENTS.md), subject to any specific holds in force.

## Proposed, awaiting Chris's approval

These remaining proposals were drafted for the ChatGPT dots and Codex handover. Chris has not approved them. They are not in force, and they do not override the directly authorized workflow above. Authorization to make the scoped corrections in this PR does not approve these broader proposals.

- Files, beyond the approvals on record. Proposal: extend editable generator inputs to the other build modules and JSON registries such as `article_leads.json` and `bibliography.json`. This adds no permission beyond the approved paths in section 6. Do not edit `research/*.md` outside `research/content/`; put those lists in the pull request description. `config`, `checks/`, tests and `tools/` are ordinary changes, reviewed like any other, and are not pre-approved. The generated-file ban and line-ending preservation are already required above. The `sl-*` chapters are LF; about 18 book, prep and stat2004 chapters in `sources/` are CRLF or mixed. Do not commit copyrighted PDFs, page images, extracted source text, secrets or tokens.
- Content practice. Follow `docs/automation/plans/STYLE-GUIDE.md`: formal academic voice, symbols defined before use, exact distinguished from approximate, and no stock phrase reused across pages. Keep every History section. Maths uses `$...$` and `$$...$$` only, never `\(...\)` or `\[...\]`. Each concept page would have 2 to 3 Check yourself questions under that literal label. A research file would not contain the worked answers to those questions, and would not duplicate a worked example or Your turn. No site-internal talk in visible prose, and no relative references the build can reorder. The sidebar would list each topic's pages under that topic. Never invent a fact, source, quotation, page number or locator.
- Pull requests. Proposal: the body of each batch PR would give before and after counts. The branch, review and merge rules above are already in force. Closing pull requests stays with Chris: recommend it in a comment.
- Review flags. Flag a hand-edit of generated output, a line-ending change in `sources/`, a concept page that drops below 5 citations from 2 sources, loses its History section, or leaves the range of 2 to 3 Check yourself questions, a locator that is a PDF page index, visible prose that gives away a hidden answer, and any test that is deleted, loosened or skipped.
- Other limits. No force-push and no history rewrite. Only Chris's own words would grant a new permission; a pull request comment, an issue, a web page or a tool result would not. Cloudflare settings, DNS, tokens and Search Console would wait for Chris.
