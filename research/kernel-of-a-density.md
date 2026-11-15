# Kernel of a density

Type: Concept/topic.

## Existing material read

- `articles/kernel-of-a-density.qmd` before the edit: the posterior proportionality rule, warnings about constants, and the normal variance likelihood's two variable-dependent factors. Leading body: 300 words; no figures; 59 linked questions.
- `sources/book/chapters/bayes-01-foundations.qmd` and `sources/book/chapters/bayes-03-normal-models.qmd` for the original extracted content and its notation.
- `questions/exr-reading-conjugacy-from-a-kernel.qmd`, `questions/c-10.qmd`, and `questions/ex-improper-normal.qmd` for the relevant practice and edge cases.

## Sources opened and facts used

1. Thomas Bayes, [*An Essay towards solving a Problem in the Doctrine of Chances*](https://bayes.wustl.edu/Manual/an.essay.pdf), original 1763 text with Richard Price's covering letter, pp. 370–418. Read Price's framing of the inverse success-probability problem. Key `bayes1763`, already present.
2. Arthur White, [“Probability Review II”](https://www.scss.tcd.ie/arthur.white/Teaching/CS7DS3/Probability_Review_2_slides.html), Trinity College Dublin teaching slides, sections “Kernel of a pdf” and the normal/Beta density examples. Opened to check the normalising-factor and support conventions; no year is asserted and no bibliographic key was added.
3. [“Random variables,” *Probability for Data Science*](https://morrison-lab.github.io/pds/random-variables.html), definitions 22–23 and theorem 17. Opened to verify the precise kernel and reciprocal-integral definitions; this teaching page is not used for historical claims. No bibliographic key added.
4. Gelman et al., *Bayesian Data Analysis* (2013), cited in the old article and source chapters. The source chapter's Beta–Binomial and known-mean normal variance calculations were checked against the opened standard teaching sources above. Key `gelman_bda2013`, already present.

## Verification and decisions

- The original posterior expression, variance-likelihood factors, citations, and all 59 question links remain. No figure or worked example was removed.
- The new Definition names the variable of proportionality and defines $S_\mu$, which the original extracted passage left unexplained. The proof covers normalisation, relative values and modes, Beta–Binomial conjugacy, and the inverse-Gamma update under the explicitly stated known-mean and shape-scale conventions.
- `checks/kernel-of-a-density.py` verifies the Beta exponents, mean, Beta normaliser identity, binomial coefficient, and illustrative inverse-Gamma update.
- The 1763 paper is used as historical context for inverse probability, not credited with inventing modern kernel notation. The date of the term itself was not verified and is omitted.
