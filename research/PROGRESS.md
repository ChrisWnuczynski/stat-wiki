# Full research depth pass

Branch: `research/full-depth-pass`. Ranking is frozen in [RANKING.md](RANKING.md) and [ranking.json](ranking.json). Score is unique substantive incoming pages plus unique practice questions. Work strictly by rank, one page per commit, pushing this branch after each ten page commits. Generated `articles/*.qmd` are build output; researched article source belongs in `research/content/<slug>.md` and the research log in `research/<slug>.md`.

## Status

Pages ranked: **718**. Done: **4**. Left: **714**. Skipped: **0**.

| Rank | Article | Type | Source added | Words before → after | Figures before → after | Flags |
|--:|:--|:--|:--|--:|--:|:--|
| 1 | [Variance](variance.md) | Concept/definition | [Prose](content/variance.md), [check](../checks/variance.py) | 393 → 1,574 | 0 → 0 | None in article; live Crossref API returned proxy 403 |
| 2 | [Likelihood function](likelihood-function.md) | Concept/definition | [Prose](content/likelihood-function.md), [check](../checks/likelihood-function.py) | 491 → 1,764 | 0 → 0 | None in article; Wasserman chapter preview only, not cited |
| 3 | [Expectation](expectation.md) | Concept/definition | [Prose](content/expectation.md), [check](../checks/expectation.py) | 698 → 2,024 | 0 → 0 | None; no new bibliography entries needed |
| 4 | [Degrees of freedom](degrees-of-freedom.md) | Concept/topic | [Prose](content/degrees-of-freedom.md), [check](../checks/degrees-of-freedom.py) | 524 → 2,145 | 0 → 0 | None; original Fisher 1922 paper opened |

Word counts use `\b[\w-]+\b` in the generated `.qmd` before its `## See also` section, with HTML tags removed. Figure counts use Markdown image links in the full page. The baseline for all 718 pages is frozen in `baseline.json`; the graph test rejects any loss of words or figures. Variance lost no existing definition, example, citation, infobox value, question, or figure. No genuine-duplication removals were made.

## Next page

**Rank 5: `covariance`**. Read the generated article, its source chapter sections, and relevant question pages; search and open primary and standard sources; save `research/covariance.md`, `research/content/covariance.md`, and `checks/covariance.py`; rebuild; run all tests and `verify_citations.py --offline`; commit only that page's change; repeat in rank order. The missing local McCullagh–Nelder PDF was waived by the user; use accessible opened sources for relevant GLM pages.

## Verification for completed pages

- Variance: exact rational arithmetic 5 checks passed; generator completed; 63 Python tests passed; offline schema and citation verification passed for 383 works. A direct Quarto render produced the variance HTML with one Proof box. Its site-wide redirect post-check cannot pass when only one of 1,482 pages is rendered; a full render was stopped after 96 pages to keep the per-page workflow moving. Publisher page and open full text were read. Live Crossref verification failed because the environment's proxy returned HTTP 403, not because of a metadata mismatch.
- Likelihood function: Poisson and binomial arithmetic plus the boundary case passed 10 checks; generator completed; 63 Python tests passed; offline bibliography verification passed for 385 works. Existing interpretation and invariant-MLE statement remain; the new proof covers non-injective parameter transforms.
- Expectation: 18 exact rational checks passed; generator completed; 63 Python tests passed; offline bibliography verification passed for 385 works. Existing definitions, three examples, discrete function-rule proof, and question links remain. New collapsed proof covers the continuous function rule and both tower versions.
- Degrees of freedom: 15 exact arithmetic checks passed; generator completed; 63 Python tests passed; offline bibliography verification passed for 386 works. Existing two-normal-observation calculation and interpretation remain. New proof covers the normal projection, table dimension, and equal-correlation expectation.
- No pages skipped. Unverified article claims: none. Future uncertain facts go in [todo.md](todo.md).
