# Research log: anova-f-distribution

Rank 490; batch AC.

Taback §§5.3.1–5.3.7 full mathematical passage read; independent OpenIntro §7.5 and Pishro-Nik normal density supply interpretation and rotation argument. Full projection proof supplied. Checks verify orthogonality/ranks, exact toy SS/F and legacy corn arithmetic.

## Sources actually read

- `taback2022_design`: §§5.3.1–5.3.6; §§5.3.2–5.3.6; §5.3.6; §§5.3.6–5.3.7. https://designexptr.org/anovachapt.html
- `pishro_nik2014`: §6.1.5, normal random vectors. https://www.probabilitycourse.com/chapter6/6_1_5_random_vectors.php ; https://www.probabilitycourse.com/chapter9/9_1_8_bayesian_hypothesis_testing.php ; https://www.probabilitycourse.com/chapter9/9_1_5_mean_squared_error_MSE.php
- `openintro2019`: §7.5, comparing many means with ANOVA. Full author textbook repository /workspace/statwiki-sources/v/openintro, ch_inference_for_means/TeX/ch_inference_for_means.tex §7.5 and ch_regr_simple_linear/TeX/ch_regr_simple_linear.tex §§8.2,8.4

## Verification

- All numerical sections executed successfully independently before final generated-content validation. `checks/anova-f-distribution.py` recomputes the examples and inspects generated citations, structure, hidden answers and real question links.
- 7 located citations across 3 proper works in the new prose. The generated page has 8 located inline citations across 3 proper works actually read.
- No tests, generator, bibliography or shared source input edited by this agent. Exact shared substitutions and any self-check map request are in ignored `research/pending/anova-f-distribution.json`.
- The successful Done517 build generated 718 articles and 626 questions. All15 AC checks, the generated-page citation/answer/structure audit, offline665-work bibliography verification and diff check passed. The full72-test run passed all517 calculation scripts and71 test methods; its single failure was a shared worked-example heading. After root repaired both affected headings, the exact previously failing method passed (1 test, 1.172s). The integration coordinator will run a fresh full build and full suite after merging all batches.
