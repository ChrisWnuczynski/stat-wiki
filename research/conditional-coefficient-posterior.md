# Research log: conditional-coefficient-posterior

Rank 500; batch AC.

Prado full §1.5.3.1 p21 exact conditional Normal and variance marginal read. GPML §2.1.1 pp8–10 normal-prior posterior square completion read independently; Pishro-Nik §6.1.5 supports linear combinations. State distinction: GPML fixed-variance normal prior is not cited as unknown-variance reference posterior source. Checks verify non-centred design covariance, square completion, slope marginal probability and bank example intervals.

## Sources actually read

- `prado_ferreira_west2021`: §1.5.3.1, p. 21; §§1.5.2–1.5.3.1, pp. 20–21. https://api.pageplace.de/preview/DT0400.9781498747042_A41590561/preview-9781498747042_A41590561.pdf
- `pishro_nik2014`: §6.1.5. https://www.probabilitycourse.com/chapter6/6_1_5_random_vectors.php ; https://www.probabilitycourse.com/chapter9/9_1_8_bayesian_hypothesis_testing.php ; https://www.probabilitycourse.com/chapter9/9_1_5_mean_squared_error_MSE.php
- `rasmussen_williams2006`: §2.1.1, pp. 8–10, eqs. 2.7–2.8. https://gaussianprocess.org/gpml/chapters/RW2.pdf ; https://gaussianprocess.org/gpml/chapters/RW3.pdf

## Verification

- All numerical sections executed successfully independently before final generated-content validation. `checks/conditional-coefficient-posterior.py` recomputes the examples and inspects generated citations, structure, hidden answers and real question links.
- 9 located citations across 3 proper works in the new prose. The generated page has 16 located inline citations across 3 proper works actually read.
- No tests, generator, bibliography or shared source input edited by this agent. Exact shared substitutions and any self-check map request are in ignored `research/pending/conditional-coefficient-posterior.json`.
- The successful Done517 build generated 718 articles and 626 questions. All15 AC checks, the generated-page citation/answer/structure audit, offline665-work bibliography verification and diff check passed. The full72-test run passed all517 calculation scripts and71 test methods; its single failure was a shared worked-example heading. After root repaired both affected headings, the exact previously failing method passed (1 test, 1.172s). The integration coordinator will run a fresh full build and full suite after merging all batches.
