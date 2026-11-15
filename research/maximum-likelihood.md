# Maximum likelihood

Type: Concept/definition and estimation method.

## Existing material read

- `articles/maximum-likelihood.qmd` before the edit: definition, spark-plug comparison, normal and uniform examples, invariance statement and derivation, four worked examples, seven cited works, and 16 linked questions. Leading body: 2,000 words; no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd` and `sources/stat2004/chapters/inf-solutions.qmd` around the MLE definition, normal, uniform, and practice-answer calculations.
- `questions/ex-inf-normal-mle.qmd`, `questions/ex-inf-exponential-mle.qmd`, and `questions/ex-inf-poisson-mle.qmd`.

## Sources opened and facts used

1. Fisher, [“On an Absolute Criterion for Fitting Frequency Curves”](https://jhanley.biostat.mcgill.ca/bios601/Likelihood/FisherLikelihoodPaper1912.pdf), original 1912 paper opened in the likelihood-function research. Used for the first history paragraph. Key `fisher1912_curve`.
2. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf), original 1922 paper opened in this pass, especially pp. 323–327, for likelihood maximisation and invariance. Key `fisher1922`.
3. Fisher, [“Theory of Statistical Estimation”](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/theory-of-statistical-estimation/7A05FB68C83B36C0E91D42C76AB177D4), publisher record for the 1925 follow-up. Only its publication and scope are used in history; full text unavailable. Key `fisher1925_est`.
4. NIST/SEMATECH, [e-Handbook §1.3.6.5.2, “Maximum Likelihood”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3652.htm), opened in earlier likelihood-function research for censored-data use, optimisation, and small-sample caveats. Key `nist_handbook_mle2002`.
5. The existing source chapter and its citations to Casella and Berger (2002) for binomial, normal, and uniform MLEs. Full book text unavailable; all new claims are derived in the collapsed proof and checked numerically. Key `casella_berger2002`.

## Verification and decisions

- Original spark-plug, normal, uniform, exponential, and Poisson calculations, invariance derivation, citations, and all 16 question links remain. No figure or worked example was removed.
- The collapsed proof checks independence factorisation, log-likelihood and constant factors, binomial boundary values, the nondegenerate normal optimum, the uniform boundary, and invariance for non-injective functions.
- The original source chapter treated a Uniform$(0,\theta)$ density as zero at $x=\theta$ but then asserted an MLE at the observed maximum. It now explicitly chooses an equivalent closed-endpoint density version, and explains that the open-endpoint version has only a supremum. The generated article's mathematics now matches its density convention.
- The normal calculation lacked its all-observations-equal edge case. The source chapter and its existing question answer now require nonzero observed spread for a finite MLE and explain the unbounded likelihood when the spread is zero.
- `checks/maximum-likelihood.py` recomputes the retained spark-plug probabilities, normal and uniform comparisons, new censoring example, and boundary behaviour.
