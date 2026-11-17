# Neyman pearson lemma

Rank 416. Depth pass, batch X.

## Material checked

The randomized decision function, level constraint and likelihood-ratio comparison are proved directly; finite boundary randomization is solved as a linear program. Siegrist §9.5 and Boyd §§7.3.1–7.3.5 were read. The source claim that the largest conservative deterministic LR region must be optimal among all deterministic tests is corrected via root-applied shared input.

Frozen article baseline: 413 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `boyd_vandenberghe2004`: (§7.3.5, pp. 370–372); (§7.3.1–7.3.2, pp. 364–366); (§7.3.5, Fig. 7.4 and Ex. 7.4, pp. 371–372). [Full source](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf).
- `siegrist2022_lrt`: (§9.5, The Neyman–Pearson Lemma); (§9.5, proof of the Neyman–Pearson lemma). [Full source](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/09:_Hypothesis_Testing/9.05:_Likelihood_Ratio_Tests).
- `siegrist2022_testing`: (§9.1, power and uniformly most powerful tests). [Full source](https://www.randomservices.org/random/hypothesis/Introduction.html).

## Checks and validation

The independent check is `checks/neyman-pearson-lemma.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
