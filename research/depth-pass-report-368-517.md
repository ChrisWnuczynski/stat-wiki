# Depth pass, ranks 368–517

All 150 pages are complete in ten batches, U–AD. The pass adds located textbook and published-paper citations, checked numerical examples, hidden practice answers and two linked self-check questions on every page. Progress is 517 of 718 pages; next rank is **518**. The frozen ranking order and scores are unchanged.

The integration branch was rebased onto `0174906`, which includes PR #63. Covered legacy repairs were discarded. Three additional mathematical corrections clarify the geometric waiting-time tail, the Normal assumption behind a quadratic log-likelihood, and infinite passage times in finite reducible chains.

The 150 article bodies grew from **97,290 to 221,219 prose tokens** using the existing preservation test's counter. All **22 source figures** remain. Each target's preservation floor was raised to the current measured value; no previous word or figure floor was lowered.

## Validation

- `python build_wiki.py`: 718 articles, 626 question pages, 579 with answers.
- `python -m unittest discover`: **72 passed**, including execution of all **517 completed-page numerical scripts**.
- `python verify_citations.py --offline`: **665 works passed**.
- `git diff --check`: passed.
- A separate fresh build reproduced all **718 article files and the proof ledger byte for byte**.
- Independent recomputation covered **20 randomly selected pages**, two per batch, with **113 passing claim checks**; seed `20261117`.
- Consumed pending JSON files were removed. Private reference PDFs and extracted text remain outside the repository.

## Self-review gate

| Gate | Result |
|:--|:--|
| a — wording | 0 prohibited editorial/process uses. Four subject-matter matches were reviewed: an available comparison drug and retained MCMC draws/pairs. |
| b — hidden answers | 0 citations inside hidden answers. |
| c — self-checks | 150/150 have one literal Check yourself heading and two answered, linked question-bank questions. |
| d — sources | 0 lecture-note/slide references, including uncited reference items. Four manuals appear in six citations, all for software behavior or data. |
| e — citation depth | 1,592 located inline citations; 6–19 per page; every page has at least two independent proper works. Low-citation warnings fell from 52 to 39. |
| f — bibliography | 0 duplicate URLs or normalized title/year work entries. Book aliases and editions were grouped when counting independent sources. |
| g — structure | 150 distinct rendered heading combinations; largest combination is 1/150. |
| h — numbers | 20/20 random pages and 113/113 independent checks passed; assumptions and connective direction were reviewed. |
| i — Dodge | All 65 citations were checked against 33 printed pages and 26 entries; 0 unresolved locator or source-scope issues. |
| j — protected checks | All four tests added by #63 and its anchor assertion remain intact; `test_citations.py` is byte-identical. Approved source-identity updates affect six pre-existing branches, two source-key fixtures and five existing scripts. Three legacy scripts gain math assertions. No numerical, figure, question-link, infobox or content-length check was weakened or skipped. |

The machine-readable [audit](depth-pass-368-517-audit.json) records per-page citation counts, independent-work counts, question IDs and proof gaps. [Before/after metrics](depth-baseline-368-517.json) record every target's word and figure counts.

## Open items

**21 anchored proof gaps across 18 pages** remain explicitly recorded in [the proof overrides](proofs-todo-overrides.json). These concern general convergence, distributional calibration, extension, uniqueness, asymptotic or algorithmic path results; finite cases and worked examples are checked on the pages.

Three data/provenance items remain in [todo.md](todo.md):

- Bradley–Terry: the original 2024 NRL match-data fit was not recovered; displayed transformations and rounded comparisons are recomputed.
- Alon data: the exact preprocessing and cross-validation seed for the reported PCA/gene-selection fits remain unavailable; counts and gene-list overlaps are checked.
- Clotting data: values match R's published example; the historical Hurn attribution remains unverified.

The unidentified DasGupta graduate-probability manuscript is excluded from the bibliography; its publication identity remains a research item. Source-classification, locator and heading issues found during review were corrected in the generator inputs. The baseline refresh uses the unchanged preservation test's established counter.

No pages were skipped. No main merge, main push or deployment was performed.
