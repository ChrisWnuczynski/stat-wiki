## Lead context

Maximum likelihood sets a derivative to zero. The method of moments sets a sample average equal to a population average. Both are special cases of a more general instruction: write a function of the data and the parameter that has mean zero at the true parameter, and solve the sample version. That function is an estimating equation. Generalised estimating equations for clustered data are one family. They are not the whole idea.{{cite:hansen2010}} (Ch. 9, §9.1, p. 134){{cite:dodge2008}} (p. 184)

## Motivating example

A sample $y_1,\ldots,y_n$ has an unknown mean $\mu$. The deviations $y_i-\mu$ have mean zero at the true $\mu$, so the sample equation $\sum_i(y_i-\mu)=0$ is an estimating equation. Its solution is the sample mean. If a second, different function of $(y_i,\mu)$ also has mean zero, there are more equations than unknowns. No single $\mu$ will satisfy both sample equations exactly. The generalised method of moments replaces “solve” by “make the vector of sample averages as close to zero as a chosen weighting allows.” The mean example is the just-identified case, where close to zero means equal to zero.{{cite:hansen2010}} (Ch. 9, §9.1–§9.2, pp. 134–135)

## Intuition

An estimating equation encodes a fact that is true on average when the parameter is right, and false on average when it is wrong. The sample analogue is noisy, but the noise averages out as the sample grows, which is why a root of the sample equation can be a consistent estimator. The likelihood score is the estimating equation that comes from differentiating the log-likelihood. A moment restriction $E(z_i e_i)=0$ in a regression, with $e_i$ the error and $z_i$ an instrument, is an estimating equation that does not require a full density. Specifying the mean-zero function is weaker than specifying the whole distribution, and it is enough to define an estimator.{{cite:hansen2010}} (Ch. 9, §9.1, p. 134)

## Definition

Let $g(y,x,z,\theta)$ be an $\ell\times 1$ function of a $k\times 1$ parameter, with $\ell\ge k$, and let $\theta_0$ satisfy

$$
E\,g(y_i,x_i,z_i,\theta_0)=0.
$$

Models defined by a restriction of this kind are called moment condition models. In the statistics literature the same restrictions are called estimating equations. The sample analogue is the average $g_n(\theta)=n^{-1}\sum_i g(y_i,x_i,z_i,\theta)$.{{cite:hansen2010}} (Ch. 9, §9.1, p. 134)

When $\ell=k$, the method-of-moments estimator solves $g_n(\hat\theta)=0$. When $\ell>k$ the model is overidentified: there are more equations than free parameters, and an exact root need not exist. The generalised method of moments then minimises a weighted square length $n\,g_n(\theta)^\top W_n g_n(\theta)$ for a positive definite weight matrix $W_n$. If the weight is the identity, the criterion is $n$ times the squared Euclidean length of $g_n(\theta)$. In the just-identified case the minimiser is the exact root.{{cite:hansen2010}} (Ch. 9, §9.2, pp. 134–135)

A linear version is $y_i=x_i^\top\beta+e_i$ with $E(z_i e_i)=0$, so $g=z(y-x^\top\beta)$. Ordinary least squares is the case $z=x$, one estimating equation per coefficient, solved by the normal equations. An instrument vector longer than $x$ overidentifies the same coefficient.{{cite:hansen2010}} (Ch. 9, §9.1, p. 134)

## Properties

Under standard moment conditions the generalised-method-of-moments estimator is asymptotically normal, with a sandwich covariance that depends on the weight matrix and on the variance of the moment function. The weight that minimises the asymptotic variance is the inverse of that moment variance. A feasible estimator replaces the optimal weight by a consistent estimate of it and keeps the same limit. “Efficient” here means smallest asymptotic variance inside this class of weighting schemes, not smallest variance among all conceivable estimators.{{cite:hansen2010}} (Ch. 9, §9.3, p. 135)

The least-absolute-deviations fit has an estimating equation even though the criterion is not differentiable. The sample condition $n^{-1}\sum_i x_i\,\mathrm{sgn}(y_i-x_i^\top\hat\beta)=0$ is the moment equation whose population version is $E\bigl(x\,\mathrm{sgn}(e)\bigr)=0$ when the conditional median of the error is zero. Solving it is still estimation from an estimating equation. The absolute-deviation criterion is one way to arrive at that equation.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 110–111)

Generalised estimating equations for a longitudinal marginal mean are a particular system: a weighted residual for each cluster, summed to zero, with a working covariance inside the weight. They are estimating equations aimed at a marginal regression parameter. The general definition above does not require clusters, a working correlation, or a generalised linear mean.{{cite:hansen2010}} (Ch. 9, §9.1, p. 134)

## Statistical use

Use an estimating equation when the scientifically trusted restriction is a mean-zero function of data and parameter, and a full likelihood is either unavailable or not credible. Write $g$ so that its expectation really is zero at the parameter of interest. Check the dimensions. If there are as many equations as parameters, solve $g_n(\theta)=0$. If there are more, minimise a weighted quadratic in $g_n$ and report which weight was used. The sandwich variance is the companion standard error when the variance of $g$ is estimated from the sample rather than from a correctly specified likelihood.{{cite:hansen2010}} (Ch. 9, §9.2–§9.3, pp. 134–135)

A [method of moments](method-of-moments.qmd) estimator is the just-identified case. [Maximum likelihood](maximum-likelihood.qmd) solves the score equation, which is an estimating equation built from the log-density. [Generalised estimating equations](generalised-estimating-equations.qmd) are the clustered marginal-mean case. [Least absolute deviations](least-absolute-deviations.qmd) solve the sign equation for a conditional median. The [sandwich estimator](sandwich-estimator.qmd) is the variance formula that accompanies a root of an estimating equation when the second-moment matrix of $g$ is estimated directly.

## Worked example

The observations $2,4,6$ and the estimating function $g(y,\mu)=y-\mu$ have sample equation $(2-\mu)+(4-\mu)+(6-\mu)=0$, so $12-3\mu=0$ and $\hat\mu=4$, the sample mean. Suppose a second function $g_2(y,\mu)=y^2-(\mu^2+1)$ is added because a model claims $E(Y^2)=\mu^2+1$. At $\mu=4$ the second sample average is $(4+16+36)/3-(16+1)=18.667-17=1.667$, not zero. The two equations cannot be solved together. A one-parameter fit must compromise. With equal weight on the two sample averages after they are left in their raw units, the criterion $g_{n1}(\mu)^2+g_{n2}(\mu)^2$ is a generalised-method-of-moments objective. Its minimiser is not required to zero either coordinate. The just-identified estimator from $g_1$ alone remains $\hat\mu=4$, and it simply does not use $g_2$.{{cite:hansen2010}} (Ch. 9, §9.1–§9.2, pp. 134–135)

**Your turn.** Observations $1,3,8$. Solve the estimating equation $\sum_i(y_i-\mu)=0$. Then evaluate the sample average of $y_i^2-(\mu^2+1)$ at that solution. Is the second equation satisfied?

::: {.callout-tip collapse="true" title="Answer"}
The first equation gives $\hat\mu=(1+3+8)/3=4$. The second sample average is $(1+9+64)/3-(16+1)=74/3-17=7.666\ldots$, which is not zero. The second equation is not satisfied at the solution of the first.
:::

## Common misconceptions

An estimating equation is not a generalised estimating equation unless the mean-zero function is the clustered marginal score those equations use. Solving $g_n(\theta)=0$ is not maximum likelihood unless $g$ is the score of a correctly specified likelihood. Overidentification is not a defect to be ignored: extra valid equations can improve asymptotic precision, and extra invalid equations pull the estimator toward the wrong value. A weight matrix changes the estimator when there are more equations than parameters. It does not change the estimator in the just-identified case, where every nonsingular weighting still selects the unique root.{{cite:hansen2010}} (Ch. 9, §9.2–§9.3, pp. 134–135)

## Assumptions and limits

The population moment has to be zero at the parameter one intends to estimate. A restriction that fails, such as an instrument correlated with the error, defines an estimating equation for a different functional than the one the analyst named. Asymptotic normality wants enough moments and a derivative of $E g$ that has full rank at $\theta_0$. The optimal weight depends on the variance of $g$, which is estimated, so the finite-sample behaviour of a two-step weight can be poorer than the limit theorem suggests. A just-identified equation that uses only part of a valid restriction is consistent for the same parameter and need not be efficient.{{cite:hansen2010}} (Ch. 9, §9.1–§9.3, pp. 134–135)

## Connections

The [method of moments](method-of-moments.qmd) solves a just-identified estimating equation. [Maximum likelihood](maximum-likelihood.qmd) solves the score. [Generalised estimating equations](generalised-estimating-equations.qmd) are a marginal-mean system for clustered responses. [Least absolute deviations](least-absolute-deviations.qmd) solve a sign equation. The [sandwich estimator](sandwich-estimator.qmd) estimates the variance of a root without requiring the weight to be the true inverse variance of the score. [Asymptotic analysis](asymptotic-analysis.qmd) is what justifies the normal limit.

## History

Moment calculations are older than the name. Pearson’s method of moments matched sample moments to population moments, which is a just-identified estimating equation. Fisher’s maximum likelihood estimates set the score, another mean-zero function, to zero. The general formulation, a vector of functions with expectation zero at the true parameter, is what the statistics literature calls an estimating equation and what econometrics developed as a moment condition model. The generalised method of moments, whose large-sample theory was set out for possibly overidentified restrictions, minimises a weighted square of the sample moment instead of insisting on an exact root. Least squares, median regression, and clustered marginal models sit inside that pattern as particular choices of $g$.{{cite:dodge2008}} (pp. 184–185){{cite:hansen2010}} (Ch. 9, §9.1–§9.2, pp. 134–135; Ch. 7, §7.5, pp. 110–111)
