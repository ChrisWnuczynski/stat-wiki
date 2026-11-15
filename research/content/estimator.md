## Lead context
The rule is fixed before seeing the data; applying it to one sample produces an estimate. Repeating the sampling procedure would generally produce a different number, so the estimator's sampling distribution describes its precision and bias. The choice of rule matters because two reasonable estimators of the same quantity can have different errors under the same model.{{cite:fisher1922,lehmann_casella1998}}

## Motivating example
The ten-thermometer calculation retained below produces a compliance estimate of $0.4$. Before testing those ten items, however, the sample proportion was a random variable: another draw from the stock could have produced three, five, or more compliant items. The difference between that random rule and the observed number is why statistical uncertainty attaches to an estimate.{{cite:fisher1922}}

## Intuition
An estimator is like a recipe whose ingredients are the future sample values. Its target is a population quantity that is unknown during calculation. The recipe must be computable from the data and known constants; it may be chosen by maximum likelihood, matching moments, minimising loss, or another stated criterion. A useful recipe is evaluated across repeated samples from a specified model, rather than judged solely by whether one realised value looks plausible.{{cite:fisher1922,casella_berger2002}}

## Definition
Here $X_1,\ldots,X_n$ are random observations and $\theta$ is a fixed but unknown parameter of their sampling distribution. The notation $\widehat\theta=T(X_1,\ldots,X_n)$ emphasizes that the statistic $T$ estimates $\theta$; once the data are observed as $x_1,\ldots,x_n$, its realised estimate is $t=T(x_1,\ldots,x_n)$. The rule may return a vector for a vector-valued target. Neither the formula nor its observed evaluation may require knowing $\theta$ itself.{{cite:fisher1922,lehmann_casella1998}}

The target and sampling model are part of the statement. The sample mean can estimate a population mean under many models, while the largest observation can estimate a uniform distribution's endpoint under a different model. Calling either number simply “an estimate” leaves out what it estimates and how its error is assessed.{{cite:casella_berger2002}}

## Properties
For any estimator $\widehat\theta$ with a finite second moment, its bias at $\theta$ is $\operatorname{Bias}_\theta(\widehat\theta)=\mathbb E_\theta\widehat\theta-\theta$. Its mean squared error is

$$
\operatorname{MSE}_\theta(\widehat\theta)=\mathbb E_\theta[(\widehat\theta-\theta)^2]
=\operatorname{Var}_\theta(\widehat\theta)+\operatorname{Bias}_\theta(\widehat\theta)^2.
$$

Here $\mathbb E_\theta$ and $\operatorname{Var}_\theta$ refer to repeated sampling when the true parameter is $\theta$. An unbiased estimator has zero bias at every allowed parameter value, but low bias alone does not imply low mean squared error. This identity makes the accuracy–precision tradeoff explicit.{{cite:casella_berger2002,lehmann_casella1998}}

For independent identically distributed observations with mean $\mu$ and variance $\sigma^2<\infty$, the sample mean $\overline X=n^{-1}\sum_{i=1}^n X_i$ is unbiased for $\mu$ and has variance $\sigma^2/n$. Thus its standard error is $\sigma/\sqrt n$; replacing $\sigma$ by a data-based estimate produces an *estimated* standard error. These statements concern the sample mean, not every estimator.{{cite:casella_berger2002}}

For independent Bernoulli observations $X_i\in\{0,1\}$ with success probability $p$, the sample proportion $\widehat p=n^{-1}\sum_iX_i$ has mean $p$, variance $p(1-p)/n$, and the same expression for mean squared error. It converges in probability to $p$ as $n$ grows. It is also the maximum-likelihood estimator for this Bernoulli model when $0\le p\le1$, including the all-zero and all-one boundary samples. The retained ten-thermometer estimate is an application of this rule when independent draws from a large stock are a reasonable approximation.{{cite:casella_berger2002,wasserman2004}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set $m=\mathbb E_\theta\widehat\theta$. Writing $\widehat\theta-\theta=(\widehat\theta-m)+(m-\theta)$, squaring, and taking expectations gives $\mathbb E_\theta[(\widehat\theta-m)^2]+(m-\theta)^2$: the cross term vanishes because $\mathbb E_\theta(\widehat\theta-m)=0$. This proves the mean-squared-error identity. For independent, identically distributed $X_i$ with mean $\mu$ and variance $\sigma^2$, linearity gives $\mathbb E\overline X=\mu$, and independence gives $\operatorname{Var}(\overline X)=n^{-2}\sum_i\operatorname{Var}(X_i)=\sigma^2/n$.{{cite:casella_berger2002}}

In the Bernoulli case, each $X_i$ has mean $p$ and variance $p(1-p)$, giving the stated mean, variance, and zero-bias mean squared error by the preceding calculation. For any $\varepsilon>0$, Chebyshev's inequality yields $\mathbb P_p(|\widehat p-p|\ge\varepsilon)\le p(1-p)/(n\varepsilon^2)\to0$, which proves consistency. If $s=\sum_i x_i$ successes are observed, the likelihood is proportional to $p^s(1-p)^{n-s}$. For $0<s<n$, its log derivative $s/p-(n-s)/(1-p)$ vanishes at $p=s/n$ and the second derivative is negative there. For $s=0$ it decreases over $[0,1]$, attaining its maximum at $0$; for $s=n$ it increases, attaining its maximum at $1$. Thus $s/n$ is the maximum-likelihood estimate in all cases.{{cite:casella_berger2002,wasserman2004}}
:::
:::

## Statistical use
Choose an estimator for a stated target and model, then report its realised value with an uncertainty measure suited to the sampling plan. For a sample mean, the [standard error](standard-error.qmd) describes repeated-sample spread; an interval adds a calibrated multiplier. To compare candidate estimators, inspect bias, variance, mean squared error, and the consequences of model misspecification. A low error calculation under an assumed model does not certify that the sample represents the intended population.{{cite:casella_berger2002,nist_glossary2002}}

## Worked example
Suppose 44 of 100 independently sampled devices pass inspection. The sample-proportion estimator gives the observed estimate $44/100=0.44$ of the population pass probability $p$. Under the Bernoulli model its estimated standard error is $\sqrt{0.44(1-0.44)/100}\approx0.0496$. If the true $p$ were $0.5$, the *actual* sampling standard deviation of this estimator would instead be $\sqrt{0.5(1-0.5)/100}=0.05$. The first number is computed from the sample; the second uses a hypothetical true value for comparison.{{cite:casella_berger2002}}

**Your turn.** A separate independent Bernoulli sample has 18 successes in 30 trials. Give the sample-proportion estimate and its estimated standard error. Is that one observed estimate itself an unbiased estimator?

::: {.callout-tip collapse="true" title="Answer"}
The estimate is $18/30=0.6$, and its plug-in estimated standard error is $\sqrt{0.6(0.4)/30}=\sqrt{0.008}\approx0.0894$. Unbiasedness belongs to the *random rule* $\widehat p$, whose expectation is $p$ under repeated Bernoulli sampling; it is not a property of the single observed number $0.6$.
:::

## Common misconceptions
An estimator is a random rule before data collection, while an estimate is the rule's realised value. Unbiasedness does not mean every estimate is close to its target: the sampling variance also matters. A standard error measures sampling spread, not systematic model error or a nonrepresentative sampling frame. Different estimators may trade bias against variance, and no one numerical estimate can reveal that tradeoff without a model.{{cite:fisher1922,casella_berger2002}}

## Assumptions and limits
The definition of an estimator needs no independence, normality, or large sample. Those assumptions appear in its sampling properties and uncertainty formulas. The Bernoulli calculation assumes independent trials with one common success probability; drawing without replacement from a small stock has a different variance. The estimated standard error in the worked example is a plug-in calculation and can be unreliable near the probability boundaries or with very small samples.{{cite:casella_berger2002,wasserman2004}}

## Connections
An estimator is a [statistic](statistic.qmd) used for a parameter-estimation goal; the sample range is a statistic but need not estimate the parameter under discussion. [Bias](bias-of-an-estimator.qmd) is the difference between an estimator's sampling mean and its target. [Mean squared error](mean-squared-error.qmd) combines squared bias and variance. [Maximum likelihood](maximum-likelihood.qmd) is one construction rule, as the Bernoulli proof shows, while [consistency](consistent-estimator.qmd) is a long-run property of a sequence of estimators.{{cite:fisher1922,casella_berger2002}}

## Check yourself
Use [a Poisson mean](../questions/ex-inf-poisson-mle.qmd) to compare a maximum-likelihood estimate, unbiasedness, and consistency. Then try [a shrunken sample mean](../questions/ex-inf-shrunk-mean.qmd) to see why a small bias can sometimes reduce mean squared error. Both ask about a rule across samples, not just one realised value.

## History
In his 1922 paper on theoretical statistics, Ronald Fisher separated the problem of estimating unknown population parameters from the sampling behaviour of functions computed from observations. This made it natural to study a data-based rule and its repeated-sample properties rather than treating an observed number as self-explanatory. The present definition keeps that distinction between estimator and estimate.{{cite:fisher1922}}

Modern point-estimation treatments compare rules by properties such as bias and mean squared error under stated models. Lehmann and Casella's work develops those comparisons systematically, while the NIST glossary defines the sampling distribution and standard error used to describe an estimator's precision. The old thermometer exercise is a small concrete example of this general framework; its independence approximation is part of the model, not a historical claim.{{cite:lehmann_casella1998,nist_glossary2002}}
