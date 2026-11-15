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
4. Allen B. Downey, [*Think Bayes 2*, author-hosted notebooks](https://github.com/AllenDowney/ThinkBayes2), copyright 2020. Read chapter 3 on unnormalised posterior values, chapter 17 “Likelihood” for the normal-scale likelihood, and chapter 18 “What the Actual?” and “Binomial Likelihood” for conjugate kernel matching and the Beta–Binomial update. Citation key `downey2020_thinkbayes2`.
5. Stan Development Team, [*Stan Functions Reference*, “Inverse gamma Distribution”](https://github.com/stan-dev/docs/blob/2bc0e28/src/functions-reference/positive_continuous_distributions.qmd), source revision 4 November 2026. Read its shape-scale density and unnormalised log-density convention. Citation key `stan_functions2026`; the displayed normal-variance posterior then follows by the article's multiplication of the two kernels.

## Verification and decisions

- The posterior expression, variance-likelihood factors, and all 59 question links remain. No figure or worked example was removed.
- The new Definition names the variable of proportionality and defines $S_\mu$, which the original extracted passage left unexplained. The proof covers normalisation, relative values and modes, Beta–Binomial conjugacy, and the inverse-Gamma update under the explicitly stated known-mean and shape-scale conventions.
- `checks/kernel-of-a-density.py` verifies the Beta exponents, mean, Beta normaliser identity, binomial coefficient, and illustrative inverse-Gamma update.
- The 1763 paper is used as historical context for inverse probability, not credited with inventing modern kernel notation. The date of the term itself was not verified and is omitted.

## Correction pass

- The earlier log recorded Gelman and Raiffa–Schlaifer as citations but did not record either book as opened. Their citations on this article and in its extracted Bayesian-calculation paragraph were replaced with the Downey chapters and Stan density reference read above. The Bayes citation now points to the pages read for history only.
- Every new factual paragraph has a citation with a chapter, section, or page location. Removed a redundant modern-practice paragraph from History and an unsupported Metropolis–Hastings claim. The arithmetic check now asserts the exact values and kernel terms printed on the page.
