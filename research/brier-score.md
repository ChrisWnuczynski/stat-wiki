# Research log: brier-score

Rank 498; batch AC.

Gneiting–Raftery published full §3 Ex1 p363 and zero-one score Ex4, plus §2.1 and §2.3 read. Pishro-Nik full §9.1.5 MMSE and variance decomposition read independently. Strict propriety proved by direct expansion. Explicit binary versus categorical factor-of-two convention; no software theory citation. Checks verify observed Brier, population decomposition, expected excess loss and actual heart-failure question numbers.

## Sources actually read

- `gneiting_raftery2007_scoring`: §3, Ex. 1, p. 363; §§2.3 and 3, pp. 362–363. https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf
- `pishro_nik2014`: §9.1.5; §9.1.5, minimum mean squared error; §9.1.5, variance decomposition. https://www.probabilitycourse.com/chapter6/6_1_5_random_vectors.php ; https://www.probabilitycourse.com/chapter9/9_1_8_bayesian_hypothesis_testing.php ; https://www.probabilitycourse.com/chapter9/9_1_5_mean_squared_error_MSE.php

## Verification

- All numerical sections executed successfully independently before final generated-content validation. `checks/brier-score.py` recomputes the examples and inspects generated citations, structure, hidden answers and real question links.
- 9 located citations across 2 proper works in the new prose. The generated page has 11 located inline citations across 2 proper works actually read.
- No tests, generator, bibliography or shared source input edited by this agent. Exact shared substitutions and any self-check map request are in ignored `research/pending/brier-score.json`.
- The successful Done517 build generated 718 articles and 626 questions. All15 AC checks, the generated-page citation/answer/structure audit, offline665-work bibliography verification and diff check passed. The full72-test run passed all517 calculation scripts and71 test methods; its single failure was a shared worked-example heading. After root repaired both affected headings, the exact previously failing method passed (1 test, 1.172s). The integration coordinator will run a fresh full build and full suite after merging all batches.
