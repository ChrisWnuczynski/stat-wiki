## Lead context
It gives the correct target on average across repetitions of a stated sampling procedure. This property helps diagnose systematic error and define fair comparisons among estimators, but it does not guarantee that any one estimate is close to the truth or has the smallest mean squared error.{{cite:rao1945}} (pp. 236–237){{cite:wang2025_foundations}} (Ch. 13, §§16.2–16.3)

## Motivating example
Suppose a device produces independent measurements with a stable mean. Their average changes from sample to sample, but its expectation is the device's true mean. That statement concerns the rule applied to *all possible samples*, not whether today's average equals the mean. The same distinction matters for variance: dividing a sum of squared deviations by $n-1$ corrects its repeated-sample expectation, while dividing by $n$ does not.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

## Intuition
Picture collecting a fresh sample many times from the same model and plotting each resulting estimate. An unbiased rule places the centre of that sampling distribution at the parameter it targets. It may still be wide, with many estimates far from the target. A small, deliberate bias can sometimes narrow the distribution enough to reduce mean squared error. The target, model, and set of possible parameter values must therefore be named whenever unbiasedness is asserted.{{cite:rao1945}} (pp. 236–237)

## Definition
Let $X=(X_1,\ldots,X_n)$ denote the random sample and $T(X)$ a statistic chosen before observing it. The defining condition says $T$ estimates a fixed parameter $\theta$ *unbiasedly* if $\mathbb E_\theta[T(X)]=\theta$ for **every** $\theta$ in the model's parameter space. Here $\mathbb E_\theta$ is expectation under repeated sampling when the model parameter is $\theta$; the observed number $T(x)$ is an estimate, not a rule with its own sampling bias. More generally, a rule for a target $h(\theta)$ is unbiased when $\mathbb E_\theta T=h(\theta)$ for every allowed $\theta$.{{cite:wang2025_foundations}} (Ch. 13, §16.2){{cite:rao1945}} (p. 236)

The condition cannot be assessed from one realised sample alone. It is possible for a rule to have zero bias at one parameter value yet be biased at all others. For example, a constant rule equal to $\theta_0$ has zero bias when $\theta=\theta_0$, but it is not unbiased over a parameter space containing other values.{{cite:wang2025_foundations}} (Ch. 13, §16.2){{cite:rao1945}} (p. 236)

## Properties
For independent identically distributed $X_i$ with finite mean $\mu$ and finite variance $\sigma^2$, the sample mean $\overline X=n^{-1}\sum_i X_i$ has expectation $\mu$ and variance $\sigma^2/n$. With $n\ge2$, the sample variance $s^2=(n-1)^{-1}\sum_i(X_i-\overline X)^2$ has expectation $\sigma^2$. These conclusions do not require a normal population. They explain why the denominator $n-1$ appears when variance is estimated after centring at a sample mean.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

The least-squares slope and intercept are unbiased in the simple-regression result when the observed predictor values $x_i$ are fixed, not all equal, and the response mean really is $\mathbb E(Y_i\mid x_i)=\beta_0+\beta_1x_i$. Correlated or unequal-variance errors do not by themselves change this expectation calculation, although they affect standard errors. The conditional mean and a full-rank design identify the coefficients whose expectations are calculated.{{cite:fox2016_regression}} (Ch. 6, §6.1.2, p. 109)

If $T$ has a finite second moment, $\operatorname{MSE}_\theta(T)=\operatorname{Var}_\theta(T)+\operatorname{Bias}_\theta(T)^2$. For an unbiased rule, MSE equals variance, so among unbiased candidates at the same parameter a smaller variance gives a smaller MSE. Among *all* candidates, a biased rule can have the smaller MSE, as the two-variance-estimator example demonstrates. The unbiased $s^2$ is convenient for familiar pivots, but the normal-model MLE variance can also be rescaled into an exact pivot; unbiasedness alone does not uniquely justify a choice.{{cite:wang2025_foundations}} (Ch. 13, §§16–17)

Unbiasedness does not generally survive a nonlinear change of target. Since $\mathbb E(\overline X^2)=\mu^2+\sigma^2/n$, squaring an unbiased estimator of $\mu$ produces a positively biased estimator of $\mu^2$ unless the variance is zero. Nor does $\mathbb E(s)=\sigma$ follow from $\mathbb E(s^2)=\sigma^2$; in a normal sample the standard deviation $s$ is biased low.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Linearity of expectation gives $\mathbb E\overline X=n^{-1}\sum_i\mathbb E X_i=\mu$. Independence makes the covariance terms vanish, giving $\operatorname{Var}(\overline X)=n^{-2}\sum_i\sigma^2=\sigma^2/n$. The identity $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$, obtained by expanding both sides, has expectation $n\sigma^2-n(\sigma^2/n)=(n-1)\sigma^2$. Dividing by $n-1$ proves $\mathbb E s^2=\sigma^2$; dividing by $n$ instead gives $((n-1)/n)\sigma^2$.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

For regression, set $\overline x=n^{-1}\sum_i x_i$ and $S_{xx}=\sum_i(x_i-\overline x)^2>0$. The least-squares slope is $\widehat\beta_1=S_{xx}^{-1}\sum_i(x_i-\overline x)Y_i$. Taking expectations conditional on these fixed $x_i$ gives $S_{xx}^{-1}\sum_i(x_i-\overline x)(\beta_0+\beta_1x_i)=\beta_1$: the constant term sums to zero and $\sum_i(x_i-\overline x)x_i=S_{xx}$. The intercept is $\widehat\beta_0=\overline Y-\widehat\beta_1\overline x$, so its expectation is $\beta_0$. No normality or independence of errors was used in either expectation calculation.{{cite:fox2016_regression}} (Ch. 6, §6.1.2, p. 109)

Write $m=\mathbb E_\theta T$. Expanding $T-\theta=(T-m)+(m-\theta)$, then taking the expectation of its square, removes the cross term and gives $\operatorname{MSE}_\theta(T)=\operatorname{Var}_\theta(T)+(m-\theta)^2$. Finally, $\mathbb E(\overline X^2)=\operatorname{Var}(\overline X)+(\mathbb E\overline X)^2=\sigma^2/n+\mu^2$. These identities prove both the bias–variance distinction and the nonlinear-transformation counterexample.{{cite:wang2025_foundations}} (Ch. 13, §§16.3, 17.1)

For the Rao–Blackwell construction, let $U$ be an integrable unbiased rule and $S$ a sufficient statistic. Sufficiency makes the conditional rule $U^*=\mathbb E(U\mid S)$ computable without the unknown parameter. The tower property gives $\mathbb E U^*=\mathbb E U$, and the law of total variance gives $\operatorname{Var}(U)=\mathbb E\{\operatorname{Var}(U\mid S)\}+\operatorname{Var}(U^*)\ge\operatorname{Var}(U^*)$ when these variances are finite.{{cite:rao1945}} (pp. 237–238){{cite:blackwell1947}} (pp. 105–107)
:::
:::

## Statistical use
Unbiasedness is a useful check when an estimator is intended to recover a repeated-sampling target such as a mean, variance, or regression coefficient. State the sampling model and assess its variance or standard error alongside bias. If an estimator is biased, compare its full mean squared error or another loss suited to the application before rejecting it. When estimating a transformed target, calculate the expectation of the transformed rule rather than assuming the untransformed rule's unbiasedness carries over.{{cite:rao1945}} (pp. 236–237)

## Worked example
Let $X_1,X_2$ be independent Bernoulli observations with success probability $p=1/2$. Their four equally likely pairs are $(0,0)$, $(0,1)$, $(1,0)$, and $(1,1)$. The unbiased sample variance $s^2=\sum_i(X_i-\overline X)^2/(2-1)$ takes values $0,1/2,1/2,0$. Its expectation is $1/4$, equal to the Bernoulli population variance $p(1-p)$. Dividing the squared deviations by $2$ instead gives values $0,1/4,1/4,0$ and expectation $1/8$. A single realised pair cannot reveal the expected value of either rule.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

**Your turn.** For $n=4$ independent observations with population variance $\sigma^2=9$, give the expectation of $s^2$ and of the uncorrected variance $n^{-1}\sum_i(X_i-\overline X)^2$.

::: {.callout-tip collapse="true" title="Answer"}
The first expectation is $9$. The second is $((n-1)/n)\sigma^2=(3/4)9=27/4=6.75$. These are repeated-sample averages, not predictions that either observed estimate must take those values.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)
:::

The [shrunken mean exercise](../questions/ex-inf-shrunk-mean.qmd) compares bias and mean squared error for two estimators.{{cite:wang2025_foundations}} (Ch. 13, §16.3)

## Common misconceptions
Unbiasedness means right *on average over samples*, not right for every sample. A smaller bias need not imply a smaller MSE. The unbiased sample variance $s^2$ does not make its square root unbiased for the standard deviation. A rule can be unbiased at one parameter and biased over the rest of the parameter space. The normality used to compare exact variance-estimator MSEs in the normal-model example is not needed for the sample-variance expectation proof.{{cite:rao1945}} (pp. 236–237){{cite:siegrist2022_sample_variance}} (§6.5)

## Assumptions and limits
The definition needs an expectation under a fully specified sampling model. The sample-mean result needs a finite mean; its variance formula needs finite variance and zero covariance between observations. The sample-variance expectation proof uses a common mean and variance with independent draws. Least-squares unbiasedness needs the conditional mean to have the stated linear form and the observed design to identify its coefficients. Bias calculations under a misspecified model may not describe the actual repeated-sampling behaviour.{{cite:siegrist2022_sample_variance}} (§6.5){{cite:fox2016_regression}} (Ch. 6, §6.1.2, p. 109)

## Connections
An [estimator](estimator.qmd) is a random rule for a parameter; its [bias](bias-of-an-estimator.qmd) measures the difference between its sampling mean and target. [Mean squared error](mean-squared-error.qmd) adds variance to squared bias. The [Rao–Blackwell theorem](rao-blackwell-theorem.qmd) constructs another unbiased rule by conditioning an unbiased rule on a sufficient statistic, with no greater variance, as shown in the proof. A minimum-variance claim therefore needs to specify the class of rules being compared.{{cite:rao1945}} (pp. 237–238){{cite:blackwell1947}} (pp. 105–107)

## History
Fisher's 1922 paper separated the problem of estimating unknown population parameters from the distribution of sample statistics. It made repeated-sample properties part of assessing an estimating rule. This set the stage for studying the expectation and spread of an estimator under repeated samples.{{cite:fisher1922}} (pp. 313–316)

In 1945 C. R. Rao explicitly examined estimators constrained to have expectation equal to their target and derived information-based variance limits. He also noted that a small bias can be worth accepting when it substantially reduces variance. This framed minimum variance as a comparison within the class of unbiased rules.{{cite:rao1945}} (pp. 235–238)

David Blackwell's 1947 paper showed how conditioning an unbiased estimator on a sufficient statistic preserves its expectation while reducing or retaining its variance. This provided a way to improve a rule without leaving the unbiased class. Modern point-estimation treatments keep the bias criterion alongside variance, MSE, and model assumptions when comparing estimators.{{cite:blackwell1947}} (pp. 105–110){{cite:wang2025_foundations}} (Ch. 13, §§15–16)
