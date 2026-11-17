# Research log: bootstrap-error-and-the-correction

Rank 497; batch AC.

Efron published full paper §6 pp321–322 read, including eq6.12. Efron–Tibshirani1997 §§2–3 pp549–552 read for casewise estimator, training-size bias and memorisation failure. Existing course-hosted PDFs are published journal papers, not lecture notes. Checks calculate finite-n probabilities, OOB replicate count, casewise versus pooled weighting and .632 optimism counterexample.

## Sources actually read

- `efron_tibshirani1997_632plus`: §§2–3, pp. 549–552; §2, p. 550; §§2–3, pp. 551–552; §3, p. 552. https://sites.stat.washington.edu/courses/stat527/s13/readings/EfronTibshirani_JASA_1997.pdf
- `efron1983`: §6, pp. 321–322. https://sites.stat.washington.edu/courses/stat527/s13/readings/Efron_jasa1983.pdf

## Verification

- All numerical sections executed successfully independently before final generated-content validation. `checks/bootstrap-error-and-the-correction.py` recomputes the examples and inspects generated citations, structure, hidden answers and real question links.
- 7 located citations across 2 proper works in the new prose. The generated page has 11 located inline citations across 2 proper works actually read.
- No tests, generator, bibliography or shared source input edited by this agent. Exact shared substitutions and any self-check map request are in ignored `research/pending/bootstrap-error-and-the-correction.json`.
- The successful Done517 build generated 718 articles and 626 questions. All15 AC checks, the generated-page citation/answer/structure audit, offline665-work bibliography verification and diff check passed. The full72-test run passed all517 calculation scripts and71 test methods; its single failure was a shared worked-example heading. After root repaired both affected headings, the exact previously failing method passed (1 test, 1.172s). The integration coordinator will run a fresh full build and full suite after merging all batches.
