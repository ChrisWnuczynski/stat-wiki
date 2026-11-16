# Likelihood function

Type: Concept/definition (its associated maximisation is a method).

## Existing material read

- `articles/likelihood-function.qmd` before the edit: definition, invariant-MLE property, interpretation, seven-in-ten binomial comparison, and 71 linked questions. Leading body: 491 words, no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd`, “Maximum likelihood,” including `def-likelihood-function`, the spark-plug and normal-mean examples, and the definition of maximum likelihood. Compared with the generated `notes/inf-02-estimation.qmd`.
- `article_extras.py`, the existing `likelihood-function` interpretation; `questions/ex-inf-poisson-mle.qmd` and `questions/ex-inf-exponential-mle.qmd`, including their existing answers.

## Sources opened and facts used

1. Fisher, R. A., “[On an Absolute Criterion for Fitting Frequency Curves](https://jhanley.biostat.mcgill.ca/bios601/Likelihood/FisherLikelihoodPaper1912.pdf),” *Messenger of Mathematics* 41 (1912), pp. 155–160, especially pp. 155–157. Read Fisher's motivation for replacing arbitrary fitting rules with a product of model density values and its log-sum form. Used for the first history paragraph only. Citation key `fisher1912_curve`.
2. Fisher, R. A., “[On the Mathematical Foundations of Theoretical Statistics](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf),” *Philosophical Transactions of the Royal Society A* 222 (1922), pp. 309–368, especially pp. 323–327. Read his formal maximum-likelihood construction, binomial illustration, distinction between likelihood and probability, and parameter-relabeling argument. Used for the definition, invariance proof, interpretation, and second history paragraph. Citation key `fisher1922`.
3. NIST/SEMATECH, [e-Handbook of Statistical Methods, §1.3.6.5.2 “Maximum Likelihood”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3652.htm), first published 2002. Read the likelihood-function and optimisation descriptions, use for censored data, sensitivity to initial values, and small-sample caveat. Used for statistical use and limits. Citation key `nist_handbook_mle2002`.
4. [Wikipedia: Likelihood function](https://en.wikipedia.org/wiki/Likelihood_function), opened for cross-check only and not cited. Also opened Wasserman's *All of Statistics* publisher preview of chapter 9, pp. 119–148; the full chapter was unavailable, so no facts were taken from or cited to it.

## Verification and decisions

- The joint-function definition and log-likelihood were checked against Fisher 1922 and the source chapter; the independence condition was kept explicit.
- The invariance proof uses the profile likelihood over fibres of $g$, so it covers non-injective transforms and proves the page's existing property. The boundary case was checked directly from the Poisson likelihood, consistent with the existing question answer.
- All numeric values in the new Poisson example, prompt, and retained binomial illustration were recomputed by `checks/likelihood-function.py`.
- Existing definition, invariant-MLE statement, interpretation, citations, and linked question bank were preserved. No figure or substantive text was removed.

## Correction pass

- Replaced unopened Fisher 1925 and Casella–Berger citations attached to the source definition with Fisher 1922, pp. 323–327. Added location-bearing citations to the researched prose and the existing interpretation in `article_extras.py`.
- Cited the motivating and worked examples and their hidden answers. The check now asserts the printed Poisson likelihood ratios, the binomial comparison, and the spark-plug values in the source chapter.
