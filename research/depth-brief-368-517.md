# Depth pass brief, ranks 368–517

This brief governs every batch of the 368–517 pass. Read `AGENTS.md`, `README.md` and this file before writing. The ranking is `research/RANKING.md` and `research/ranking.json`. Progress is recorded by the orchestrator in `research/PROGRESS-368-517.md`.

Tier: **lighter**. Each page is accurate, sourced, has complete examples, and has no padding. Depth goes into the mathematics and the examples, not into length. A typical page adds 600–1,300 words.

## Files a batch may create

For each slug in the batch, and nothing else:

| File | Purpose |
|---|---|
| `research/content/<slug>.md` | Page prose, read by `build_wiki.py` |
| `checks/<slug>.py` | Exact checks of every number printed in the page's examples, run against the generated article |
| `research/<slug>.md` | Research log: Checked, Assumed, Disputed, Sources read |
| `research/pending/<slug>.json` | Proposed changes to shared files, plus the page record |

Never edit shared files: `topics.py`, `bibliography.json`, `article_leads.json`, `article_extras.py`, `distributions.json`, `proofs-todo.json`, `research/self-checks.json`, `research/todo.md`, any `PROGRESS` file, `build_wiki.py`, tests, `sources/`. Never hand-edit `articles/*.qmd`; they are build output. Propose shared changes in the pending file. Do not spawn subagents. Do not push, merge to `main`, deploy or force-push.

## Build and test in a worktree

```
python3 build_wiki.py                      # about 90 s; the machine has 4 cores shared by 10 batches
python3 research/apply_pending.py --ranks <range> --overlay   # make proposed bibliography keys and leads visible to the build
python3 build_wiki.py
python3 research/check_depth_pass.py --ranks <range> --run-checks
python3 -m unittest discover
python3 verify_citations.py --offline
git diff --check
python3 research/apply_pending.py --restore  # always before committing
```

Build sparingly: once at the start, once after the first few pages, and at the end. Commit only your own files with explicit paths (`git add research/content/<slug>.md checks/<slug>.py research/<slug>.md research/pending/<slug>.json`). Never commit `bibliography.json`, `article_leads.json`, `proofs-todo.json`, `overview.qmd` or `labs/`, which the build or overlay rewrite.

## Sources

The Dodge (2008) source is not available in this pass. Do not cite `dodge2008` anywhere in new prose.

Open textbooks are extracted outside the repository at `/workspace/statwiki-sources/open/<book>/pages/pdf-NNNN.txt`. Search them with

```
python3 /workspace/statwiki-sources/open/find.py <book> "<regex>" [--context 2]
```

then open the page file and read the printed page number from its header or footer. Cite the printed page, never the PDF page.

| Folder | Key | Use for |
|---|---|---|
| `bda3` | `gelman_bda2013` | Bayesian models, priors, posterior simulation, grid approximation, label switching, empirical and hierarchical Bayes, Laplace approximation |
| `bishop` | `bishop2006` | Perceptron, LDA and Fisher's direction, kernels, SVM duals and slack, Gaussian processes, EM for mixtures, factor analysis, Laplace approximation, IRLS, boosting and exponential loss, committees, cross-validation |
| `durrett` | `durrett2019` | Measure-theoretic probability: convergence theorems, uniform integrability, characteristic functions, Kolmogorov extension, branching processes, Markov chains. Cite § and theorem numbers with the printed page. |
| `grinstead` | `grinstead_snell1997` | Elementary probability: total probability, equally likely outcomes, hypergeometric, Poisson limit, generating functions, random walks, Markov chains |
| `levinperes` | `levin_peres2017` | Finite Markov chains: irreducibility, period, stationary distributions, doubly stochastic matrices, hitting times |
| `mackay` | `mackay2003` | Gibbs' inequality, entropy, Ising model, Laplace approximation, Monte Carlo, perceptron capacity |
| `shalizi_ada` | `shalizi_ada2026` | Regression practice, smoothing, cross-validation, bootstrap, partially linear models, factor analysis, trees |
| `owen_nonunifrng`, `owen_mcmc` | `owen2013_mc` | Inverse transform, Box–Muller, acceptance–rejection, MCMC, thinning |

Web sources reachable from this machine (fetch with `curl -sSL`): the NIST/SEMATECH e-Handbook (`www.itl.nist.gov/div898/handbook/`), Siegrist's Random Services (`www.randomservices.org/random/`), Pishro-Nik (`www.probabilitycourse.com`), Hyndman and Athanasopoulos (`otexts.com/fpp3/`, key `hyndman_athanasopoulos2021`), arXiv, Project Euclid (open Annals papers such as Friedman's 2001 gradient-boosting paper), CRAN manuals (software behaviour only), and Complex Systems (Sejnowski and Rosenberg's NETtalk paper). Cite web sources by section number (`§8.1.6`) or numbered heading.

Not reachable: Hastie, Tibshirani and Friedman (ESL), James et al. (ISL), Efron and Hastie (CASI), Boyd and Vandenberghe, and the first chapters of Owen. Do not cite `hastie_esl2009`, `james_islr2021` or any other work for a claim you did not read in this pass. Never try to get past a bot check or CAPTCHA.

Before adding a bibliography key, search `bibliography.json` for the work. New works go in the pending file in the same schema (`authors`, `year`, `title`, `kind` of article/book/incollection, `venue` or `publisher`, `doi` or `url`, `verification` with source `crossref`, `crossref_container`, `openalex`, `openlibrary` or `archival_url`). Copy every field from the work itself; never guess a DOI, volume or page range. Name keys like the ones already there (`surname_topicYYYY`, `nist_<topic>`, `siegrist2022_<topic>`).

Citation rules:

- `{{cite:key}} (location)` after every sourced claim. The location starts with `§`, `Ch.`, `Thm.`, `Lem.`, `Cor.`, `Prop.`, `Def.`, `Ex.`, `Eq.`/`eq.`, `Alg.`, `Table`, `Fig.`, `App.`, `p.` or `pp.`.
- Cite only material you read in this pass. Never cite an abstract, a publisher contents page or lecture notes for a definition, example or proof. Software documentation supports software behaviour only.
- Named results and proofs: prefer the original paper or a standard textbook, and check an important claim against a second source when one is reachable.
- Write in your own words. Never copy sentences from a source, and never paste source text into an OpenAI prompt.
- If no good source is reachable, prove the claim on the page or drop it, and record the gap in the pending `todo` list. Never cite something weak to fill the gap.
- Never invent facts, citations, numbers, paths, DOIs or page numbers.

## Page rules

Every page, whatever its type, has:

1. `## Motivating example`: a concrete situation that needs the idea.
2. `## Worked example`: complete numbers, every step shown, then `**Your turn.**` with a problem and its answer in `::: {.callout-tip collapse="true" title="Answer"}`.
3. `## Check yourself`: 2 or 3 questions, each a `### Question title` followed by the question and its answer in `::: {.callout-tip collapse="true" title="Answer"}`. Use questions with definite answers. A page whose bank questions (see `questions/`) fit well may instead propose 2–3 bank ids in `self_checks` and omit this section; never both.
4. At least one topic-specific heading written `## Key — Display title`, for example `## Intuition — Why the tails decide`.
5. Sections chosen for the page type and topic. Do not paste a stock skeleton: `Statistical use` plus `Assumptions and limits` on every page is wrong. State limits as mathematics (a condition, a counterexample, a boundary case).

Allowed section keys and order, by template:

- Concept: Lead context, Motivating example, Intuition, Definition, Interpretation, Properties, Statistical use, Worked example, Common misconceptions, Assumptions and limits, Connections, Check yourself, History.
- Theorem (the article shows `| Statement | [Read statement](#statement) |`): Lead context, Motivating example, Statement, Intuition, Key results, Proof, Generalizations, Related concepts, Statistical use, Common misconceptions, Check yourself, History, Worked example. The Worked example joins the Examples section.
- Distribution (only `hypergeometric-distribution`): Lead context, Motivating example, Intuition, Definition, Properties, Related distributions, Statistical inference, Generating random samples, Worked example, Examples, Common misconceptions, Assumptions and limits, Connections, Check yourself, History.

Headings that must stay canonical (no ` — ` display title): Lead context, Motivating example, Worked example, Check yourself; theorem `Statement`; distribution `Definition`, `Related distributions`, `Statistical inference`; and `Intuition` and `Related concepts` on the result-depth pages `marginal-variance-posterior`, `sequential-coherence`, `bayes-action-for-two-hypotheses`, `beta-binomial-posterior-prediction`, `conditional-coefficient-posterior`, `direct-posterior-simulation`, `dirichlet-moments`, `full-conditionals-under-independent-priors`.

The generated page also carries the copied definition, statement, examples and figures from the course chapters. Read the generated `articles/<slug>.qmd` first. Do not repeat what it already says; extend it. If the copied material is wrong, say so in the pending `todo` (the source chapters are outside this pass) and write the page so that it is correct.

Lead context: one or two plain sentences that are appended to the generated lead line. No mathematics, no `$`, no bold. It must read as a continuation of the lead.

Theorem pages:

- A research `## Proof` section becomes the page's single collapsed proof box. It must prove exactly the stated result, under the stated conditions. Write it as a proof, not a sketch.
- Eighteen theorem pages in this range have no proof yet (they are in `proofs-todo.json`). Add a proof when a complete one fits in a short box; the build then drops the page from `proofs-todo.json`. When it does not fit, leave `## Proof` out and give a specific reason in the pending `proofs_todo` entry (`{"slug", "title", "reason"}`).
- When a page already has a proof, a research `## Proof` replaces it. Replace it only with a proof that is at least as complete.
- A concept page that uses a result it does not prove records the gap in the pending `todo` list, not in `proofs_todo`.

Proofs inside concept pages use

```
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
...
:::
:::
```

Voice and wording:

- Narrative textbook voice. Write as if the page always existed.
- Never write inherited, retained, existing, original, originally, kept, opened, "not a claim", "not claiming", or mention edits, earlier versions, or which sources were opened. `research/check_depth_pass.py` rejects these words in research prose.
- Connective words (because, so, therefore, however, despite, although, surprisingly) must match the logic they join.
- Links to other articles are relative: `[conditional independence](conditional-independence.qmd)`. Link only to pages that exist in `articles/`.
- British spelling, as in the surrounding pages.

## Checks

`checks/<slug>.py` recomputes every number printed in the page's examples, answers and self-checks with exact arithmetic (`fractions`, `sympy`) or a seeded simulation with a stated tolerance, and asserts that the printed strings appear in both `research/content/<slug>.md` and the generated `articles/<slug>.qmd` (text before `## See also`). Model it on `checks/polynomial-kernel.py`. End with `print("<slug> checks passed")`.

## OpenAI helper

`scripts/oai.py` saves Claude usage on routine drafting and gives an independent review. Set `export STATWIKI_OAI_CACHE=/workspace/stat-wiki/research/.oai-cache` so usage from every worktree lands in one log, and pass `--tag <batch letter>`.

- Drafts (`--tier draft --system scripts/oai-draft-system.md`): motivating-example scaffolds, Check yourself questions and answers, Your turn problems. Rewrite and verify every draft yourself.
- Review (`--tier review --effort medium --json --system scripts/oai-review-system.md`): send each finished `research/content/<slug>.md` (your own prose only) with the list of cited works. Fix real problems; note in the research log what the review found and what you changed or rejected.
- Cross-checks (`--tier review`): ask for an independent statement of a named result to compare with your reading.
- Never use it for final numbers (every number is checked in `checks/<slug>.py`), for citations or page numbers, or with copyrighted text (no Dodge, no textbook passages). If the API fails or runs out of quota, carry on without it and note it.
- Keep prompts short and batch several small requests into one prompt where possible.

## Pending file

```json
{
  "slug": "trend",
  "rank": 373,
  "batch": "U",
  "tier": "lighter",
  "type": "Concept",
  "sections": ["Lead context", "Motivating example", "Intuition", "Worked example", "Check yourself"],
  "words_before": 493,
  "words_after": 1420,
  "figures_before": 0,
  "figures_after": 0,
  "sources_read": ["Hyndman and Athanasopoulos 2021 §3.2"],
  "proofs": ["Least-squares slope of a linear trend"],
  "tests": ["checks/trend.py passed", "check_depth_pass ok"],
  "skipped": [],
  "unverified": [],
  "bibliography": {},
  "article_leads": {},
  "proofs_todo": [],
  "todo": [],
  "self_checks": [],
  "shared_edits": [],
  "oai": {"calls": 3, "prompt_tokens": 4200, "completion_tokens": 2600, "review": "minor: fixed one connective"}
}
```

- `words_before`/`figures_before`: from the batch prompt. `words_after`/`figures_after`: count the generated article before `## See also` with the regex in `research/check_depth_pass.py` (`prose_words`).
- `article_leads`: only for this slug, the full entry (`field`, `article`, `term`, `verb`, `description`, optional `"proper": true`), and only when the lead is wrong (for example a proper name in lower case).
- `todo`: one-line items for `research/todo.md`, each starting with the slug.
- `shared_edits`: free-form proposals for other shared files, as `{"file", "change", "reason"}`, applied by hand during integration.

## Research log

`research/<slug>.md`:

```
# <Term>

Rank N. Type: concept|theorem|distribution. Tier: lighter.

## Checked
## Assumed
## Disputed
## Sources read
## Review
```

## Finish

Run the full test list above with the overlay applied, then restore. Commit page by page (`Add a lighter depth pass for <term>`). Report: each page's status, sources read, proofs added or left open, unverified items, todo items, OpenAI calls and tokens, and anything that failed.
