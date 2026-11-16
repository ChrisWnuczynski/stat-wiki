# Maximum likelihood

Type: Concept/definition and estimation method.

## Existing material read

- `articles/maximum-likelihood.qmd` before the edit: definition, spark-plug comparison, normal and uniform examples, invariance statement and derivation, four worked examples, seven cited works, and 16 linked questions. Leading body: 2,000 words; no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd` and `sources/stat2004/chapters/inf-solutions.qmd` around the MLE definition, normal, uniform, and practice-answer calculations.
- `questions/ex-inf-normal-mle.qmd`, `questions/ex-inf-exponential-mle.qmd`, and `questions/ex-inf-poisson-mle.qmd`.

## Sources opened and facts used

1. Fisher, [“On an Absolute Criterion for Fitting Frequency Curves”](https://jhanley.biostat.mcgill.ca/bios601/Likelihood/FisherLikelihoodPaper1912.pdf), original 1912 paper opened in the likelihood-function research. Used for the first history paragraph. Key `fisher1912_curve`.
2. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf), original 1922 paper opened in this pass, especially pp. 323–327, for likelihood maximisation and invariance. Key `fisher1922`.
3. NIST/SEMATECH, [e-Handbook §1.3.6.5.2, “Maximum Likelihood”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3652.htm), opened for censored-data use, optimisation, and small-sample caveats. Key `nist_handbook_mle2002`.
4. He Wang, [*Foundations of Probability and Statistical Theory*](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/), Ch. 8 §9.6.2, Ch. 11 §19, Ch. 12 §§16–18 and §22, and Ch. 13 §§15–17, opened for order statistics, sufficiency, binomial/normal/uniform/exponential MLEs, invariance, and estimator comparison. Key `wang2025_foundations`.

The first draft and inherited blocks cited Casella and Berger (2002), Davison (2003), and Fisher (1925) without the relevant pages being opened. The corrected generated article uses located passages from Fisher (1912, 1922), Wang, and NIST for those claims. The Fisher (1925) publisher record establishes its publication, but does not support the mathematical statements that had cited it.

## Verification and decisions

- The spark-plug, normal, uniform, exponential, and Poisson calculations, invariance derivation, and all 16 question links remain. No figure or worked example was removed. The redundant link-only “Check yourself” section was removed because the questions remain in the generated question list.
- The collapsed proof checks independence factorisation, log-likelihood and constant factors, binomial boundary values, the nondegenerate normal optimum, the uniform boundary, and invariance for non-injective functions.
- The original source chapter treated a Uniform$(0,\theta)$ density as zero at $x=\theta$ but then asserted an MLE at the observed maximum. It now explicitly chooses an equivalent closed-endpoint density version, and explains that the open-endpoint version has only a supremum. The generated article's mathematics now matches its density convention.
- The normal calculation lacked its all-observations-equal edge case. The source chapter and its existing question answer now require nonzero observed spread for a finite MLE and explain the unbounded likelihood when the spread is zero.
- `checks/maximum-likelihood.py` recomputes the spark-plug probabilities, uniform comparison, censoring example, and boundary behaviour, and asserts the values printed on the generated page.
- A later citation-location scan found a one-sentence history preface injected by `article_extras.py` without a location. The researched History already states and cites the 1922 claim at pp. 323–327, so the duplicate preface was removed.
