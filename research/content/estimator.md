## Lead context
The rule is fixed before seeing the data; applying it to one sample produces an estimate. Repeating the sampling procedure would generally produce a different number, so the estimator's sampling distribution describes its precision and bias. The choice of rule matters because two reasonable estimators of the same quantity can have different errors under the same model.{{cite:wang2025_foundations}} (Ch. 12, §15; Ch. 13, §§15–16)

## Motivating example
The ten-thermometer calculation produces a compliance estimate of $0.4$. Before testing those ten items, however, the sample proportion was a random variable: another draw from the stock could have produced three, five, or more compliant items. The difference between that random rule and the observed number is why statistical uncertainty attaches to an estimate.{{cite:wang2025_foundations}} (Ch. 12, §15)

## Intuition
An estimator is like a recipe whose ingredients are the future sample values. Its target is a population quantity that is unknown during calculation. The recipe must be computable from the data and known constants; it may be chosen by maximum likelihood, matching moments, minimising loss, or another stated criterion. A useful recipe is evaluated across repeated samples from a specified model.{{cite:wang2025_foundations}} (Ch. 12, §§15–17; Ch. 13, §21)

## Definition
Here $X_1,\ldots,X_n$ are random observations and $\theta$ is a fixed but unknown parameter of their sampling distribution. The notation $\widehat\theta=T(X_1,\ldots,X_n)$ emphasizes that the statistic $T$ estimates $\theta$; once the data are observed as $x_1,\ldots,x_n$, its realised estimate is $t=T(x_1,\ldots,x_n)$. Its calculation uses data and known constants.{{cite:wang2025_foundations}} (Ch. 12, §15)

The target and sampling model are part of the statement. The sample mean can estimate a population mean under many models, while the largest observation can estimate a uniform distribution's endpoint under a different model. Calling either number simply “an estimate” leaves out what it estimates and how its error is assessed.{{cite:wang2025_foundations}} (Ch. 12, §§15, 17.6)

## Properties
For any estimator $\widehat\theta$ with a finite second moment, its bias at $\theta$ is $\operatorname{Bias}_\theta(\widehat\theta)=\mathbb E_\theta\widehat\theta-\theta$. Its mean squared error is

$$
\operatorname{MSE}_\theta(\widehat\theta)=\mathbb E_\theta[(\widehat\theta-\theta)^2]
=\operatorname{Var}_\theta(\widehat\theta)+\operatorname{Bias}_\theta(\widehat\theta)^2.
$$

Here $\mathbb E_\theta$ and $\operatorname{Var}_\theta$ refer to repeated sampling when the true parameter is $\theta$. An unbiased estimator has zero bias at every allowed parameter value, but low bias alone does not imply low mean squared error. This identity makes the accuracy–precision tradeoff explicit.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §§16–17)

For independent identically distributed observations with mean $\mu$ and variance $\sigma^2<\infty$, the sample mean $\overline X=n^{-1}\sum_{i=1}^n X_i$ is unbiased for $\mu$ and has variance $\sigma^2/n$. Thus its standard error is $\sigma/\sqrt n$; replacing $\sigma$ by a data-based estimate produces an *estimated* standard error. This sampling spread decreases as the sample size grows.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §§16–17)

For independent Bernoulli observations $X_i\in\{0,1\}$ with success probability $p$, the sample proportion $\widehat p=n^{-1}\sum_iX_i$ has mean $p$, variance $p(1-p)/n$, and the same expression for mean squared error. It converges in probability to $p$ as $n$ grows. It is also the maximum-likelihood estimator for this Bernoulli model when $0\le p\le1$, including the all-zero and all-one boundary samples. The ten-thermometer estimate applies this rule under an independent-trials model.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §§16–17)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set $m=\mathbb E_\theta\widehat\theta$. Writing $\widehat\theta-\theta=(\widehat\theta-m)+(m-\theta)$, squaring, and taking expectations gives $\mathbb E_\theta[(\widehat\theta-m)^2]+(m-\theta)^2$: the cross term vanishes because $\mathbb E_\theta(\widehat\theta-m)=0$. This proves the mean-squared-error identity. For independent, identically distributed $X_i$ with mean $\mu$ and variance $\sigma^2$, linearity gives $\mathbb E\overline X=\mu$, and independence gives $\operatorname{Var}(\overline X)=n^{-2}\sum_i\operatorname{Var}(X_i)=\sigma^2/n$.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §§16–17)

In the Bernoulli case, each $X_i$ has mean $p$ and variance $p(1-p)$, giving the stated mean, variance, and zero-bias mean squared error by the preceding calculation. For any $\varepsilon>0$, Chebyshev's inequality yields $\mathbb P_p(|\widehat p-p|\ge\varepsilon)\le p(1-p)/(n\varepsilon^2)\to0$, which proves consistency. If $s=\sum_i x_i$ successes are observed, the likelihood is proportional to $p^s(1-p)^{n-s}$. For $0<s<n$, its log derivative $s/p-(n-s)/(1-p)$ vanishes at $p=s/n$ and the second derivative is negative there. For $s=0$ it decreases over $[0,1]$, attaining its maximum at $0$; for $s=n$ it increases, attaining its maximum at $1$. Thus $s/n$ is the maximum-likelihood estimate in all cases.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §§16–17)
:::
:::

## Statistical use
Choose an estimator for a stated target and model, then report its realised value with an uncertainty measure suited to the sampling plan. For a sample mean, the [standard error](standard-error.qmd) describes repeated-sample spread. To compare candidate estimators, inspect bias, variance, mean squared error, and the consequences of model misspecification. The sampling frame determines the population from which the sample is drawn.{{cite:wang2025_foundations}} (Ch. 13, §§15–17){{cite:nist_glossary2002}} (Glossary, “standard error” and “sampling frame”)

## Worked example
Suppose 44 of 100 independently sampled devices pass inspection. The sample-proportion estimator gives the observed estimate $44/100=0.44$ of the population pass probability $p$. Under the Bernoulli model its estimated standard error is $\sqrt{0.44(1-0.44)/100}\approx0.0496$. If the true $p$ were $0.5$, the *actual* sampling standard deviation of this estimator would instead be $\sqrt{0.5(1-0.5)/100}=0.05$. The first number is computed from the sample; the second uses a hypothetical true value for comparison.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §17.1)

**Your turn.** A separate independent Bernoulli sample has 18 successes in 30 trials. Give the sample-proportion estimate and its estimated standard error. Is that one observed estimate itself an unbiased estimator?

::: {.callout-tip collapse="true" title="Answer"}
The estimate is $18/30=0.6$, and its plug-in estimated standard error is $\sqrt{0.6(0.4)/30}=\sqrt{0.008}\approx0.0894$. Unbiasedness belongs to the *random rule* $\widehat p$, whose expectation is $p$ under repeated Bernoulli sampling; it is not a property of the single observed number $0.6$.{{cite:wang2025_foundations}} (Ch. 12, §15; Ch. 13, §16.2)
:::

## Common misconceptions
An estimator is a random rule before data collection, while an estimate is the rule's realised value. Unbiasedness does not mean every estimate is close to its target: the sampling variance also matters. A standard error measures sampling spread, not systematic model error or a nonrepresentative sampling frame. Different estimators may trade bias against variance, and no one numerical estimate can reveal that tradeoff without a model.{{cite:wang2025_foundations}} (Ch. 12, §15; Ch. 13, §§15–16)

## Assumptions and limits
The Bernoulli calculation assumes independent trials with one common success probability. Independence removes the covariance terms when calculating the sample proportion's variance. The estimated standard error substitutes the observed proportion for the unknown probability; if all observations are zeros or all are ones, that substitution gives zero. Such an estimate calls for care because other probability values can still produce the same sample.{{cite:wang2025_foundations}} (Ch. 12, §17.4; Ch. 13, §17.1)

## Connections
An estimator is a [statistic](statistic.qmd) used for a parameter-estimation goal; the sample range is a statistic but need not estimate the parameter under discussion. [Bias](bias-of-an-estimator.qmd) is the difference between an estimator's sampling mean and its target. [Mean squared error](mean-squared-error.qmd) combines squared bias and variance. [Maximum likelihood](maximum-likelihood.qmd) is one construction rule, as the Bernoulli proof shows, while [consistency](consistent-estimator.qmd) is a long-run property of a sequence of estimators.{{cite:wang2025_foundations}} (Ch. 12, §§15–17; Ch. 13, §16)

## History
In his 1922 paper on theoretical statistics, Ronald Fisher separated the problem of estimating unknown population parameters from the sampling behaviour of functions computed from observations. This made it natural to study a data-based rule and its repeated-sample properties rather than treating an observed number as self-explanatory. This distinction guides the interpretation of a reported estimate.{{cite:fisher1922}} (pp. 309, 313–316, 366–367)

Point-estimation courses now distinguish the rule used before data collection from its numerical result, then compare candidate rules using bias, variance, and mean squared error. In the thermometer example, a reported proportion is interpreted through the sampling model that produced it.{{cite:wang2025_foundations}} (Ch. 12, §15; Ch. 13, §§15–16)
