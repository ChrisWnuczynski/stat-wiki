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
The indicator selects those sample outcomes whose intervals would cover the proposed true value. This sum also explains the irregular changes in coverage of discrete procedures: inclusion changes when an endpoint crosses $p$. An exact binomial confidence construction controls coverage under its model, while an approximate rule still needs its approximation assessed. The distinction between actual and conservative confidence levels is part of set estimation.{{cite:siegrist2022_set_estimation}} (§8.1, confidence sets and conservative confidence level)

## Assumptions and limits
Coverage can change after inspecting the sample, choosing a model, dropping outliers, or selecting only “interesting” intervals for reporting. An unconditional guarantee does not automatically become a guarantee conditional on such selection. Bias from nonresponse or measurement error also persists when the formula accounts only for random sampling. After observation, the reported endpoints and a frequentist parameter are fixed; the repeated-sampling probability is a property of the procedure.{{cite:openintro2019}} (§5.2.5, interpreting intervals)
