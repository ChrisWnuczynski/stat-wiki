## Motivating example
A principal component analysis of many measurements can produce more axes than can be sensibly displayed. Before selecting a two-dimensional summary, an analyst needs to see how variation is distributed across the axes. A scree plot orders the component variances from largest to smallest. A steep initial decline followed by a flatter tail can suggest a compact summary, while a slow decline shows that a small number of axes will discard substantial variation.{{cite:bro_smilde2014_pca}} (“Selecting the number of components”, “Scree test”)

## Definition — Plot variances against their ordered indices
For eigenvalues $\lambda_1\ge\cdots\ge\lambda_p\ge0$ of the covariance or correlation matrix used in the analysis, the scree plot places component index $j$ on the horizontal axis and $\lambda_j$ on the vertical axis. Each height is a component variance, so the sum of all heights is the trace of the matrix. The fraction explained by the first $q$ axes is
$$C_q=\frac{\sum_{j=1}^q\lambda_j}{\sum_{j=1}^p\lambda_j},$$
provided the total variance is positive. A scree plot and a cumulative-variance plot display related information but answer different visual questions: one shows marginal contributions and the other their accumulated fraction.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.4–2.6)

The informal elbow rule looks for a transition from a steep decline to a comparatively flat sequence. It does not specify a unique numerical threshold, and a spectrum may show several plausible bends or none. Some analyses also inspect logarithms of eigenvalues to make small contributions visible, but zero eigenvalues cannot be placed on a logarithmic scale without an explicit convention.{{cite:bro_smilde2014_pca}} (“Scree test”, discussion of raw and logarithmic eigenvalues)

## Interpretation — The chosen preprocessing determines the spectrum
Covariance PCA uses variation in the recorded units. Correlation PCA uses standardised coordinates and has total variance $p$. Therefore the same physical measurements can produce different scree plots under the two choices. A rule based on an eigenvalue of one has a specific reference scale in correlation PCA, where one is the average eigenvalue; it has no comparable unit-free interpretation for arbitrary covariance matrices.{{cite:jolliffe_cadima2016}} (§2(c)(i), covariance versus correlation PCA)

A long tail of small values can reflect measurement noise, weak structure or a mixture of both. The visual bend alone does not identify a population rank. Sample eigenvalues fluctuate, especially when dimensions are large relative to sample size, and an exact zero can instead follow from the algebraic bound $\operatorname{rank}(S)\le n-1$. Interpreting a plot therefore requires the matrix dimensions and the sampling context as well as the shape.{{cite:bro_smilde2014_pca}} (“Selecting the number of components”, limitations of selection rules)

## Worked example — Marginal and cumulative contributions
Consider eigenvalues $(5,2,1,0.5,0.5)$, with total variance 9. The first two components account for $7/9=77.777778\%$ and the first three account for $8/9=88.888889\%$. A rule requiring at least 80% would choose three components. A rule requiring at least 90% would choose four, since their cumulative share is $8.5/9=94.444444\%$. Those rules are explicit and reproducible, but their target percentages express a chosen tolerance for reconstruction loss.

The raw spectrum drops by 3, then 1, then 0.5, then 0. The visual bend could be described as occurring after the first or second large step. That ambiguity is why it is useful to report the actual spectrum and cumulative shares rather than only the selected count. For a reconstructed training matrix, the sum of discarded covariance eigenvalues is the average squared reconstruction error using divisor $n-1$.{{cite:jolliffe_cadima2016}} (§2(a), rank reduction and total variance)

**Your turn.** What percentage is discarded if only the first two components are used?

::: {.callout-tip collapse="true" title="Answer"}
The discarded variance is 1+0.5+0.5=2, or 2/9=22.222222% of the total.
:::

## Statistical use — Select for the objective that will be assessed
For descriptive compression, an explained-variance target is directly relevant to the stated reconstruction objective. For prediction, the response can depend on a low-variance component. A visually attractive two-dimensional plot therefore does not establish that those two components are sufficient predictors. Choosing a predictive model requires an assessment that includes the whole fitting and component-selection procedure.{{cite:bro_smilde2014_pca}} (“Selecting the number of components”, cross-validation)

When comparing several choices of dimension, distinguish the observations used to select a dimension from those used to estimate its performance. The variance spectrum describes the explanatory matrix and contains no response information by itself. It is also useful to describe whether outliers dominate the leading axes and whether the directions are stable to plausible preprocessing choices.{{cite:jolliffe_cadima2016}} (§2(a), descriptive PCA; §3(c), robust PCA)

## Common misconceptions — Large variance is not an importance label
An eigenvalue measures variation along a particular direction under a specified metric. It does not measure causal importance, class separation or interpretability. A nearly constant but diagnostically useful variable can have little covariance variance, while an irrelevant large-scale measurement can dominate an unstandardised spectrum. A scree plot is one summary of an objective, rather than a substitute for identifying that objective.{{cite:jolliffe_cadima2016}} (§§2(a) and 2(c)(i))
