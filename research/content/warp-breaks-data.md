## Motivating example
The warp-breaks observations compare two wool types and three tension levels using yarn-break counts from nine looms in each combination. A useful first question is whether tension is associated with the mean count and whether that association differs by wool type. A second question concerns uncertainty when observations are dependent. Those questions require different information: a table of recorded factors cannot by itself identify independent factories or a time ordering.

## Definition — The observational units and the model
The data frame contains $54$ rows, a count `breaks`, a wool factor `wool` with levels A and B, and a tension factor with levels L, M and H. Each row summarises breaks on a fixed length of yarn, described as one loom. The variable `wool` identifies material type. Renaming it `factory` in code does not establish that it records factories.

A log-mean model with low tension as reference is
$$\log\mu_i=\beta_0+\beta_M1\{M_i\}+\beta_H1\{H_i\}.$$
This model pools wool types when describing the mean. A model with `wool*tension` instead allows all six cell means to differ. A GEE adds a working covariance and a chosen clustering structure to the mean equation. Clusters must represent independent sampling units for the usual cluster asymptotic argument.{{cite:liang_zeger1986}} (§§2–3, pp. 14–16)

## Worked example — Start with the cell means
The observed means, in low/medium/high tension order, are approximately
$$\begin{array}{c|rrr}\text{wool A}&44.5556&24.0000&24.5556\\\text{wool B}&28.2222&28.7778&18.7778\end{array}.$$
Each mean uses nine observations. The low-to-medium mean ratio is about $0.5387$ for A and $1.0197$ for B. This descriptive difference in tension patterns is a reason to inspect an interaction rather than assume a common effect without checking it.

Pooling wool types gives tension means $36.3889,26.3889,21.6667$. The independent Poisson log-mean fit therefore has coefficients approximately $3.594263,-0.321320,-0.518488$. Its medium and high mean ratios are $0.725191$ and $0.595420$. These coefficients describe arithmetic mean counts under the specified log-link model; the exponential coefficient is a mean ratio.{{cite:liang_zeger1986}} (§2, marginal generalized linear mean model)

**Your turn.** A tension coefficient is $\log(0.75)$ in a log-mean model. If the reference fitted mean is $40$, what is the fitted mean at that tension? Does the coefficient describe an additive reduction of $0.25$ breaks?

::: {.callout-tip collapse="true" title="Answer"}
The fitted mean is $40(0.75)=30$ breaks. The coefficient describes multiplication by $0.75$, a $25\%$ reduction in the mean. The additive difference here is $30-40=-10$ breaks and depends on the reference mean.
:::

## Interpretation — What the GEE comparison demonstrates
The illustrative GEE calculations group observations by the two wool labels. For the exchangeable Poisson working covariance, the refitted coefficients are $3.594263,-0.321320,-0.518488$, the Pearson scale is $4.601903$, and the fitted within-label working correlation is $0.020890$. The model-based and sandwich standard errors are approximately $(0.090554,0.128082,0.136191)$ and $(0.158694,0.222706,0.064413)$. These are reproducible outputs of that clustering choice, not evidence that two independent factories were sampled.

An AR(1) working matrix applied in the recorded row order gives lag-one correlation $0.041260$ and coefficients $3.594983,-0.324560,-0.517878$. A Gaussian working variance with the same log mean and row-order AR(1) structure gives coefficients $3.594943,-0.324493,-0.518142$ and scale $141.1501$. These fits illustrate how working covariance choices affect equations and estimated uncertainty. The row order has no documented time interpretation in the data description, so a time-series interpretation of the AR(1) coefficient requires further provenance.{{cite:liang_zeger1986}} (§3, working covariance; §4, working-correlation examples)

## Assumptions and limits — Two labels do not provide a cluster limit
The usual GEE consistency and sandwich covariance results let the number of independent clusters grow. They do not establish a reliable Gaussian approximation from two clusters. A conspicuously small sandwich standard error can reflect the geometry of very few cluster scores. It should not be promoted to more trustworthy inference simply because it is labelled robust.{{cite:liang_zeger1986}} (thms. 1–2, pp. 15–16)

Nor does disagreement between two estimated standard errors prove the true covariance differs from every working model. Such disagreement can arise from sampling variation, mean misspecification and unstable covariance estimation. The data's dependence structure needs design information, while a larger collection of independent units would support the asymptotics. For independent count-model diagnostics, Pearson or randomized quantile residuals offer additional checks of fitted distributions, subject to fitting uncertainty.{{cite:dunn_smyth1996}} (§§2–3, residual definitions and fitted-parameter qualification)

## Statistical use — A reproducible teaching comparison
Keep the wool and tension labels visible, specify what grouping is being used, and distinguish a numerical GEE demonstration from an inferential analysis supported by a sampling design. For a factorial descriptive analysis, report the six means and inspect count variation. For a scientific population comparison, obtain the experimental randomisation and dependence information before deciding on a covariance estimator. Residual patterns can prompt further modelling, but their assessment also depends on discreteness and fitted-parameter effects.{{cite:dunn_smyth1996}} (§1, discrete response bands; §3, quantile residuals)
