# Posterior mean

Type: Concept/topic.

## Existing material read

- `articles/posterior-mean.qmd` before the edit: the posterior-mean definition; posterior-draw averages, variance and tail probability; two preserved definition blocks (posterior point summaries and credible-region constructions); the credible-regions figure; and 34 linked questions. Leading body: 509 words; one figure.
- `sources/book/chapters/bayes-01-foundations.qmd` around posterior summaries and its squared-error exercise, and `sources/book/chapters/bayes-02-beta-binomial.qmd` around its prior-weight identity and pseudo-count convention.
- `questions/ex-applied-mmse.qmd`, `questions/c-07.qmd`, `questions/exr-one-thousand-posterior-draws.qmd`, and `questions/exr-fruit-posterior.qmd`, including available answers.

## Sources opened and facts used

1. Thomas Bayes, [*An Essay towards solving a Problem in the Doctrine of Chances*](https://bayes.wustl.edu/Manual/an.essay.pdf), original 1763 text communicated by Richard Price. Price's introduction frames inference about an unknown chance from successes and failures. Used narrowly for History. Key `bayes1763`, already present.
2. Peter D. Hoff, [“Bayes estimators”](https://www2.stat.duke.edu/~pdh10/Teaching/581/LectureNotes/Static/bayes.pdf), Duke University lecture notes dated 10 October 2013. Read the Bayes-risk definition, posterior-risk minimisation, and normal-mean example. Key `hoff2013_bayes_estimators`, added here.
3. UC Berkeley STAT 210A, [“Bayes Estimation”](https://stat210a.berkeley.edu/fall-2024/reader/bayes-estimation.html). Read the posterior-risk and squared-error sections for a second derivation; no new bibliography entry, since the Hoff note is the cited teaching source.
4. Metropolis and Ulam, [“The Monte Carlo Method”](https://hedibert.org/wp-content/uploads/2013/12/1949MetropolisUlam.pdf), *JASA* (1949), original full text. Read its opening description of random-sampling methods. Used only for the computational history, not credited with MCMC or posterior-draw averaging. Key `metropolis_ulam1949`, already present.
5. Charles J. Geyer, [“Practical Markov Chain Monte Carlo”](https://www2.stat.duke.edu/homeweb/scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf), *Statistical Science* (1992), original text. Read the abstract and introduction on posterior integration and dependent-chain error. Key `geyer1992`, already present.
6. He Wang, [*Foundations of Probability and Statistical Theory*](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-20-bayesian-inference.html), published 31 December 2025. Read Chapter 20, especially §§24.1, 28–29, Example 11, Definition 34, Theorem 35, and Remark 37 for posterior point summaries, Beta updates, equal-tailed intervals, and highest-density regions. Key `wang2025_foundations`, added in this correction.

## Correction audit

- Replaced citations to Gelman, Raiffa and Schlaifer, Box and Tiao, and Jeffreys on the generated article because those books had not been opened. Page-specific citations now have locations in Hoff's note, Geyer's paper, Wang's book, or the two opened original papers. The inherited definition blocks are maintained in the source chapter, so their citations were corrected there.
- Replaced editorial references to the page's prior version with mathematical explanations. The two definition blocks, figure, questions, and worked numerical values remain.
- Checked Geyer's pagination against the publisher record: the paper is pp. 473–483; the longer scanned file includes the discussion and rejoinder.

## Verification and decisions

- The posterior draw formulas, both definition blocks, the credible-regions figure, and the 34 question links remain. Citations to unopened books were replaced with located citations to opened sources.
- The single collapsed proof gives the quadratic loss expansion and minimisation, Beta and normal conjugate mean identities, and the independent-draw law of large numbers; it states the separate ergodic condition for dependent draws. The preserved credible-region descriptions remain definitions and are not presented as new theorems here.
- `checks/posterior-mean.py` checks that the printed coin and normal values match the recomputed answers, and checks that the figure remains on the generated page.
- The existing Beta–Binomial lab explicitly shows how prior counts shift the posterior mean. Its page-specific entry was added to `LAB_FOR_TOPIC` in `topics.py` so the generator places a “Try it” callout on this article; no template or build-script logic changed.
- History covers Bayes's inverse-probability question, the decision-theoretic loss result, and later computation, with source locations.
