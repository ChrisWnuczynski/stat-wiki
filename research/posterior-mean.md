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

## Verification and decisions

- The old posterior draw formulas, both definition blocks, all citations, the credible-regions figure, and the 34 question links remain. No figure or original worked content was removed.
- The single collapsed proof gives the quadratic loss expansion and minimisation, Beta and normal conjugate mean identities, and the independent-draw law of large numbers; it states the separate ergodic condition for dependent draws. The preserved credible-region descriptions remain definitions and are not presented as new theorems here.
- `checks/posterior-mean.py` recomputes the coin and normal examples, challenge, and Beta(3,9) mean/mode behind the retained figure.
- The existing Beta–Binomial lab explicitly shows how prior counts shift the posterior mean. Its page-specific entry was added to `LAB_FOR_TOPIC` in `topics.py` so the generator places a “Try it” callout on this article; no template or build-script logic changed.
- History distinguishes Bayes's original inverse-probability problem from later decision-theoretic and computational developments. No unsupported inventor or date for the phrase “posterior mean” is asserted.
