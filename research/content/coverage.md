## Motivating example
Imagine a laboratory that reports an interval after each fresh sample. The relevant performance question is how often that entire rule captures the fixed population mean. Seeing one interval cannot reveal its success rate. Coverage belongs to the sampling procedure, including its model, sample size, selection steps and endpoint formula.{{cite:dodge2008}} (pp. 106–107, “Confidence Interval”)

## Definition
For a procedure $I(X)=[L(X),U(X)]$, define its pointwise coverage as $c(\theta)=P_\theta\{\theta\in I(X)\}$. Exact constant coverage means $c(\theta)=1-\alpha$ throughout the parameter space. A conservative confidence procedure may instead have $\inf_\theta c(\theta)\ge1-\alpha$. Discrete models commonly prevent equality at every parameter value. The nominal level is the advertised target; the actual coverage is determined by the rule and the data-generating model.{{cite:openintro2019}} (§5.2.2 and §5.2.5, constructing and interpreting confidence intervals)

## Properties — An exact normal calculation
For independent $N(\mu,\sigma^2)$ observations with known $\sigma$, consider
$$I_a(X)=\left[\overline X-a\sigma/\sqrt n,\overline X+a\sigma/\sqrt n\right].$$
The inclusion event is $|\sqrt n(\overline X-\mu)/\sigma|\le a$. Since the standardized mean is $N(0,1)$, coverage equals $2\Phi(a)-1$ for every $\mu$. Thus $a=1$ gives $0.6827$, $a=1.96$ gives $0.9500$, and $a=2$ gives $0.9545$. A wider interval has higher coverage in this nested family, at the expense of precision.{{cite:dodge2008}} (pp. 106–107, pivot construction)

When $\sigma$ is estimated, the normal multiplier must be replaced by a $t$ quantile for exact normal-sample coverage. Reusing $1.96$ with an estimated standard error and only ten observations gives $P(|t_9|\le1.96)=0.9184$, below its nominal 95%. This is a model calculation, distinct from a simulation estimate.{{cite:openintro2019}} (§7.1, one-sample means with the $t$ distribution)

## Worked example — Forty intervals are still random
With independent repetitions of an exact 95% rule, let $K$ count intervals that cover. Then $K\sim\operatorname{Bin}(40,0.95)$, so $E(K)=38$ and $\operatorname{SD}(K/40)=\sqrt{0.95(0.05)/40}=0.0345$. The figure's 38 successes agree with the target, but so can nearby counts. They do not demonstrate exact calibration. Its displayed intervals can be reproduced using the figure generator's normal draws and seed 28. The interpretation of a simulated capture fraction follows the repeated-sampling meaning of confidence.{{cite:openintro2019}} (§5.2.2, repeated intervals)

**Your turn.** A simulation of an exact 90% procedure uses one hundred independent samples. Find the expected number of misses and the standard deviation of the observed coverage fraction.

::: {.callout-tip collapse="true" title="Answer"}
The expected number of misses is $100(0.1)=10$. The standard deviation of the fraction covering is $\sqrt{0.9(0.1)/100}=0.03$.
:::

### Calibration across a parameter space
A single simulation setting estimates $c(\theta)$ at one chosen parameter, not its minimum over all possible parameters. For example, a proportion-interval rule may perform well near $p=1/2$ while failing near zero. For a binomial rule with endpoints $L_x,U_x$, its exact coverage curve can be calculated without simulation:
$$c(p)=\sum_{x=0}^n\mathbf1\{L_x\le p\le U_x\}\binom nxp^x(1-p)^{n-x}.$$
The indicator selects those sample outcomes whose intervals would cover the proposed true value. This sum also explains the irregular changes in coverage of discrete procedures: inclusion changes when an endpoint crosses $p$. An exact binomial confidence construction controls coverage under its model, while an approximate rule still needs its approximation assessed. The distinction between actual and conservative confidence levels is part of set estimation.

## Assumptions and limits
Coverage can change after inspecting the sample, choosing a model, dropping outliers, or selecting only “interesting” intervals for reporting. An unconditional guarantee does not automatically become a guarantee conditional on such selection. Bias from nonresponse or measurement error also persists when the formula accounts only for random sampling. After observation, the reported endpoints and a frequentist parameter are fixed; the repeated-sampling probability is a property of the procedure.{{cite:openintro2019}} (§5.2.5, interpreting intervals)

## Lead context
A confidence procedure is a rule that turns data into a set. Its coverage is the probability, before the data are seen, that the random set contains the fixed parameter.

For a normal mean with known standard deviation, the interval $\bar x\pm 1.96\sigma/\sqrt n$ has coverage $0.95$ at every mean. Replacing $1.96$ by $1$ drops the coverage to $2\Phi(1)-1\approx 0.6827$. Replacing it by $2$ raises the coverage to about $0.9545$. The interval computed from one sample either contains the mean or it does not. The probability $0.95$ describes the procedure.{{cite:dodge2008}} (pp. 106–107, “Confidence Interval”)

## Intuition
Suppose forty independent $95\%$ intervals are formed for the same normal mean. The number that contain the mean is $\mathrm{Binomial}(40,0.95)$. Its expectation is $38$ and its standard deviation is $\sqrt{40\times 0.95\times 0.05}\approx 1.378$, or about $0.0345$ as a proportion. Seeing $38$ successes in a figure is the expected count, not evidence that coverage was checked in a way that could have failed. A procedure can also be conservative: its coverage is at least the advertised level and is strictly greater for some parameter values. That happens with discrete distributions when the critical value cannot spend the error budget exactly.{{cite:openintro2019}} (§5.2.2, repeated intervals)

## Interpretation
Using a normal critical value when the standard deviation is estimated changes the coverage. For a $t$ interval with nine degrees of freedom, the multiplier $2.262$ is the $0.975$ quantile of $t_9$ and gives coverage $0.95$ for a normal sample. Using $1.96$ instead gives coverage about $0.9184$. The interval is narrower and the coverage is lower. In a simulation of $100$ intervals at nominal level $0.90$, the expected number of misses is $10$ and the standard deviation of the miss proportion is $0.03$. A simulation that always produces exactly $90$ hits has not estimated coverage; it has been arranged to display the nominal level.{{cite:openintro2019}} (§7.1, one-sample means with the $t$ distribution){{cite:dodge2008}} (pp. 106–107, pivot construction)

## Common misconceptions
Coverage is not the probability that the parameter lies in the interval already computed. That sentence treats the parameter as random and the interval as fixed, which is a posterior-probability statement and needs a prior. A second confusion is to read a single interval that missed the parameter as a broken procedure. At level $0.95$, misses are the $5\%$ the procedure was built to allow. A third confusion is to mix the coverage of the mean interval with the coverage of a prediction interval for a new observation. The prediction interval has to cover a random response, so it is wider, and its success probability is a different calculation. Overlapping intervals for two means can coexist with a difference interval that excludes zero, because the two one-sample intervals are not the test of the difference.{{cite:openintro2019}} (§5.2.5, interpreting intervals)
