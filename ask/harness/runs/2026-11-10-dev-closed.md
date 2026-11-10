# Answer check 2026-11-10

<!-- rescore -->
> **Rescored 2026-11-10 with `harness/rescore.ts`.** The first version of this report counted 28 judge replies it could not parse as "did not answer". All 28 gave a readable grade: the JSON was invalid only because of LaTeX backslashes inside it, and the grade was read from the saved text with no new model calls. The same fix recovered 11 citation verdicts. The correctness table, citation support and wrong answers below are corrected. The reasons of recovered grades are cut off where the saved text ends, and any doubt they raised about a worked answer was lost. Costs are unchanged.
<!-- /rescore -->

Prompt v1. Retrieval as in the Worker: k=8, page and section boosts on, threshold 0.41. Answers capped at 1200 tokens. Judge grok-4.7 (also an answer model, so it may favour its own answers; the owner's hand grades check this).

Closed mode removes the question's own worked answer (and copies of it) from retrieval, so the tutor has to teach from the chapters. Open mode is the index as it is in production.

## Correctness (dev questions with a worked answer)

| model | mode | n | correct | minor error | wrong | did not answer | correct or minor | judge unreadable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grok-4.20-0309-non-reasoning | closed | 94 | 66.0% | 10.6% | 23.4% | 0.0% | 76.6% | 0 |
| grok-4.7 | closed | 94 | 89.4% | 9.6% | 0.0% | 1.1% | 98.9% | 0 |
| grok-4.7@low | closed | 94 | 90.4% | 6.4% | 2.1% | 1.1% | 96.8% | 0 |

## Answers

| set | model | mode | n | cut off at the cap | at least one citation | invalid citation numbers | maths renders | said not covered | input tokens (mean) | output tokens (mean) | reasoning tokens (mean) | latency p50 / p95 s | cost per answer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bank | grok-4.20-0309-non-reasoning | closed | 100 | 1.0% | 98.0% | 3 answers | 100.0% | 1.0% | 3182 | 350 | 0 | 3.1 / 7.7 | $0.0046 |
| bank | grok-4.7 | closed | 100 | 1.0% | 87.0% | 3 answers | 100.0% | 17.0% | 4460 | 375 | 2386 | 23.3 / 84.2 | $0.0234 |
| bank | grok-4.7@low | closed | 100 | 0.0% | 88.0% | 3 answers | 100.0% | 14.0% | 4460 | 346 | 651 | 11.5 / 26.0 | $0.0131 |
| student | grok-4.7 | open | 50 | 0.0% | 96.0% | 2 answers | 100.0% | 4.0% | 4605 | 234 | 681 | 9.7 / 23.3 | $0.0128 |

## Citation support (sample of 40 cited sentences, grok-4.7)

supported: 27 · partly: 10 · not supported: 3 · unparsed: 0

## Worked answers the judge doubted (3)

These need a person to check. The judge can be wrong.

- `question:ex-sl-09-5` (grok-4.7, closed): The worked answer reports 1000 and 10 for LOOCV and 10-fold CV, omitting the final full-sample fit the question says to count, while including the analogous final steps in the nested total of 511.
- `question:ex-inf-fork-critical-value` (grok-4.7@low, closed): The worked solution sets 6×0.300/0.3 equal to 5.995, but that quotient is 6; 5.995 is the threshold obtained from the unrounded critical variance 0.29975.
- `question:ex-sl-09-5` (grok-4.7@low, closed): The worked answer states 1000 and 10 for leave-one-out and 10-fold, omitting the final training step that its own nested total of 511 includes, despite the instruction to count final training steps too.

## Wrong answers

- `question:ex-applied-logitnormal-mh` (grok-4.20-0309-non-reasoning, closed): The n=40 posterior mean of about 0.41 and equal-tailed interval (0.27, 0.56) disagree with the correct values near 0.432 and (0.29, 0.58).
- `question:ex-da-fruit-flies` (grok-4.20-0309-non-reasoning, closed): Part (a) expected counts are incorrect (e.g. AA No is 5.52, not 7.2); part (b) is right.
- `question:ex-da-pilot-width` (grok-4.20-0309-non-reasoning, closed): The tutor's stated sample size of 265 disagrees with the required size of more than thirteen thousand, and the later square is also miscomputed as about 13490 rather than 13456.
- `question:ex-da-shark-swim` (grok-4.20-0309-non-reasoning, closed): Part (a) reports 2404 females instead of the required 2416, and the critical-value adjustment used to get 2404 is neither needed nor correctly computed.
- `question:ex-gibbs-geom` (grok-4.20-0309-non-reasoning, closed): Both full conditionals are wrong: X|y is geometric, not binomial, and Y|x is Beta(\alpha+1 …
- `question:ex-inf-advertising-r2` (grok-4.20-0309-non-reasoning, closed): The residual standard error is miscomputed as 8.75 (square root of about 46 is ~6.8) and the stated CI does not follow from the tutor's own arithmetic or the correct SE.
- `question:ex-inf-expected-sample-variance` (grok-4.20-0309-non-reasoning, closed): The tutor falsely claims that the cross term vanishes when expanding the identity, which is mathematically incorrect.
- `question:ex-inf-fork-critical-value` (grok-4.20-0309-non-reasoning, closed): The critical variance 0.30 is right, but the power is given as about 0.36 instead of about 0.58.
- `question:ex-inf-interaction-ss` (grok-4.20-0309-non-reasoning, closed): The interaction residuals and sum of squares are incorrect (\pm1.5 and 18 instead of \pm1 …
- `question:ex-inf-ppv-screen` (grok-4.20-0309-non-reasoning, closed): The tutor equates 0.0196/0.1176 to 49/296≈0.165 (and false alarms ≈0.835), but the correct value is 49/294≈0.167 (about 83% false alarms).
- `question:ex-prob-sign-covariance` (grok-4.20-0309-non-reasoning, closed): The joint pmf table assigns the wrong probabilities to the (X,Y) pairs, and the covariance is given as 0 (and later recomputed as other incorrect values) rather than -3/4.
- `question:ex-prob-three-point-expectation` (grok-4.20-0309-non-reasoning, closed): The tutor computed the expectation as 11/6 rather than the correct value 3/2.
- `question:ex-sl-05-2` (grok-4.20-0309-non-reasoning, closed): The tutor reported au_{1}(1)=0.9997 and au_{1}(3)=0.0025 using a different mixture, not the worked values 0.6156 and 0.0107.
- `question:ex-sl-09-5` (grok-4.20-0309-non-reasoning, closed): The nested total is given as 461, omitting the final 10-fold selection over the 5 candidates (50 fits) that the worked answer includes to reach 511.
- `question:ex-sl-09-7` (grok-4.20-0309-non-reasoning, closed): In (a) the tutor calls the highest validation accuracy a minimum that is systematically lower than true performance, which reverses the optimistic selection bias.
- `question:ex-sl-14-1` (grok-4.20-0309-non-reasoning, closed): The derivative identities are shown correctly, but the maximum asked for is that of g'(z)=g(1-g), equal to 1/4 at z=0, not the supremum of g.
- `question:ex-sl-14-3` (grok-4.20-0309-non-reasoning, closed): The tutor stated an incorrect boundary equation \(x_1-2x_2=1\) (and wrong slope-intercept …
- `question:ex-sl-15-6` (grok-4.20-0309-non-reasoning, closed): The squared-error gradient at z=-1 is reported as about -0.394 rather than -0.287, so the claimed factor of roughly 600 is also incorrect.
- `question:ex-sl-17-5` (grok-4.20-0309-non-reasoning, closed): The tutor's claimed det(K)≈0.097 is false (the correct value is ≈0.346), so the check of the third leading principal minor is incorrect.
- `question:practice-bayes-factors-and-posterior-odds` (grok-4.20-0309-non-reasoning, closed): In (c) the tutor multiplies B10 by 1/5 instead of the prior odds 1/4, so the posterior probability is 2/7 rather than 1/3.
- `question:practice-equal-tailed-and-highest-density-intervals` (grok-4.20-0309-non-reasoning, closed): Part (b) places the minimum-width interval at the low-density end (0, √3/2) and calls 0 the mode, but the density 2θ increases on (0,1), so the HPD interval is [1/2, 1].
- `question:practice-gamma-regression-from-the-exponential-family-form` (grok-4.20-0309-non-reasoning, closed): In part (a) the five functions are misidentified: b and c still depend on k, and with e(φ)=1/k the stated form does not recover the log-density.
- `question:ex-prob-unit-square-max` (grok-4.7@low, closed): The tutor states that F_Z is 0 outside [0,1], but the CDF equals 1 for all z>1.
- `question:practice-random-slopes-and-changed-conclusions` (grok-4.7@low, closed): In (d) the tutor wrongly claims identical time trends also require the treatment main effect to be zero, whereas that comparison concerns only the interaction slope.

## Blind second grader

The owner's 40 hand grades were replaced by a blind second grader from a different model family (Claude). It graded 40 answers against the worked answers without seeing the model or the judge's grade. The 40 were drawn by model and by the judge's grade before the rescore, so they over-represent rare grades and are not a random sample. Grades are in `2026-11-10-dev-closed-second-grader.jsonl`.

| judge (rescored) | second grader: correct | minor error | wrong | did not answer |
| --- | --- | --- | --- | --- |
| correct | 24 | 0 | 0 | 0 |
| minor error | 5 | 3 | 0 | 0 |
| wrong | 0 | 4 | 3 | 0 |
| did not answer | 0 | 0 | 0 | 1 |

Same grade 31 of 40; same call on correct-or-minor 36 of 40. Where they differ the judge is always the stricter, including on grok-4.7@low, so there is no sign that the judge favours its own model family, and the correctness table above is more likely to understate than overstate.

## Cost

From the cost xAI reports with each request: answers $4.75, judging $3.01, total $7.77.

Every answer is in `2026-11-10-dev-closed.jsonl`; citation checks are in `2026-11-10-dev-closed-support.jsonl`.
