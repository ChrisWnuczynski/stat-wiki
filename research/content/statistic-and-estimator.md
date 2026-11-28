## Lead context
The distinction separates a computable summary from the purpose assigned to that summary. An estimator is the rule before sampling; an estimate is its realised value.{{cite:dodge2008}} (pp. 185–186)

## Motivating example
Four independent coin tosses give $(1,0,1,1)$, with $1$ denoting a head. The number of heads is $3$, the sample proportion is $3/4$, and the sample variance with divisor $3$ is $1/4$. All three are statistics. Calling $3/4$ an estimate of the probability of a head adds an inferential purpose to a summary that can already be computed.{{cite:dodge2008}} (p. 517)

## Properties — Parameter-free formula, parameter-dependent law
For Bernoulli observations with success probability $p$, $K=\sum_iX_i$ has the binomial law. Thus $K$ is a statistic although $\mathbb{P}_p(K=k)$ depends on $p$. Requiring its law to be free of $p$ would impose the much stronger property of ancillarity. The parameter-free requirement concerns evaluation of the function, not its distribution.{{cite:dodge2008}} (pp. 44–45, 517)

An estimator need not be accurate, unbiased or unique. Under squared-error loss, its quality is measured by
$$
\E_p[(T-p)^2]=\operatorname{Var}_p(T)+\{\E_p(T)-p\}^2.
$$
To derive this decomposition, insert $T-p=(T-\E_pT)+(\E_pT-p)$, expand the square, and use $\E_p(T-\E_pT)=0$. The cross-term vanishes. Bias and variability are different contributions to the same risk.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, eqs. 5.20–5.21; §5.4.4)

## Worked example
Compare $\widehat p=K/4$ with $\widetilde p=(K+1)/6$. On the observed sample their estimates are $3/4$ and $2/3$. Since $\E_pK=4p$ and $\operatorname{Var}_pK=4p(1-p)$,
$$
\E_p\widehat p=p,\quad \operatorname{Var}_p\widehat p=\frac{p(1-p)}4,
\qquad E_p\widetilde p-p=\frac{1-2p}{6},\quad
\operatorname{Var}_p\widetilde p=\frac{p(1-p)}9.
$$
At $p=1/2$ both biases vanish, but their risks are $1/16$ and $1/36$. At $p=0$ the sample proportion has risk zero whereas the second rule always reports $1/6$ and has risk $1/36$. A comparison at one parameter value cannot establish uniform superiority. Point estimation treats an estimator as a function of the random data and evaluates its behaviour across repeated samples.{{cite:goodfellow_bengio_courville2016}} (§5.4.1, eqs. 5.18–5.19)

**Your turn.** If the four tosses are $(0,0,1,0)$, evaluate both estimators. Is $\sum_i(X_i-p)^2$ a statistic when $p$ is unknown?

::: {.callout-tip collapse="true" title="Answer"}
$K=1$, so the estimates are $1/4$ and $1/3$. The final expression contains the unknown $p$ and cannot be evaluated from the sample alone, so it is not a statistic.
:::

## Assumptions and limits
The formulas for expectations and variances above use independent Bernoulli sampling. The distinction between statistic and estimator applies to any sampling model in which a function of the observations is well defined: a fixed design, a known constant or auxiliary randomisation with a specified law can sit inside the procedure. An expression that still contains the unknown quantity being estimated is evaluated by a different rule, one that a data analyst can compute from the sample.{{cite:dodge2008}} (pp. 185, 517)

## Definition — A statistic is a function of the sample
Let the sample be a point $x$ in a sample space $\mathcal X$, and let a statistic be a function $T:\mathcal X\to\mathcal T$ that does not depend on the unknown parameter. The estimator is that function when the analyst assigns it the job of estimating a target $g(\theta)$. The estimate is the number or vector $T(x)$ once $x$ has been observed. For the four tosses $(1,0,1,1)$, the estimator $K/4$ and the estimate $3/4$ are different objects: the first is a random variable with a binomial sampling law, and the second is the value of that variable on this sample.{{cite:dodge2008}} (pp. 185–186)

The same function can be left as a summary. The sample variance with divisor $n-1$ is a statistic whether or not anyone uses it to estimate $p(1-p)$. Calling it an estimator adds a target and, with a loss function, a way to score the rule. Under squared error the score is the risk $\E_\theta[(T-g(\theta))^2]$. The bias–variance decomposition splits that risk into $\operatorname{Var}_\theta(T)$ and the squared bias, after the cross term vanishes because a centred random variable has mean zero.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, eqs. 5.20–5.21; §5.4.4)

## Interpretation — The law may depend on the parameter
For independent Bernoulli trials, $K=\sum_i X_i$ is a function of the sample alone, so it is a statistic. Its distribution is $\operatorname{Bin}(n,p)$, which depends on $p$. That dependence is the usual state of affairs for an estimator of $p$: the sampling experiment still contains $p$, while the formula that produces $K$ does not. A statistic whose distribution is free of $p$ is ancillary for $p$. Ancillary is a stronger property. The indicator that all four tosses are equal is a statistic; whether its distribution depends on $p$ is a separate calculation, and the calculation is not required before the indicator can be computed.

Consider $n=4$ and the two rules $\widehat p=K/4$ and $\widetilde p=(K+1)/6$. The second rule is the sample proportion after adding one success and one failure. Its expectation is $(4p+1)/6$, so its bias is $(1-2p)/6$. At $p=1/4$ the bias is $(1-1/2)/6=1/12=0.083333$, the variance is $(1/4)(3/4)/9=1/48=0.020833$, and the risk is $0.020833+0.083333^2=0.027778$. The unbiased rule has variance and risk $(1/4)(3/4)/4=0.046875$. At this particular $p$ the biased rule has the smaller risk. At $p=0$ the unbiased rule has risk $0$ and the biased rule has risk $1/36=0.027778$. The risk function is a curve, and a single point on that curve is one comparison.{{cite:dodge2008}} (pp. 44–45, 517)

## Intuition — Compute first, then name the target
An estimator is a recipe written before the sample arrives: “divide the number of heads by four”, or “add one success and one failure, then divide by six”. An estimate is what the recipe returns on the tosses in hand. The recipe can be scored by imagining it applied to many samples from a stated Bernoulli law. That score is the risk. Changing the loss, the sample size or the true $p$ changes the score. The arithmetic that turns $(1,0,1,1)$ into $3/4$ stays available throughout, because it never consults $p$.

The decomposition $\E[(T-p)^2]=\operatorname{Var}(T)+(\text{bias})^2$ explains why a small bias can be a bargain. The rule $(K+1)/6$ pulls every estimate toward $1/2$. Near $p=1/2$ the pull is small and the variance drops from $p(1-p)/4$ to $p(1-p)/9$. Far from $1/2$ the pull dominates. Squared-error comparisons make that trade visible as two nonnegative terms.

## Statistical use — Report the rule and the sampling model
A numerical summary becomes an inferential statement when three pieces are named together: the function of the data, the target it is aimed at, and the sampling model under which bias, variance or risk is calculated. For a binomial count the target is often $p$, the function is often $K/n$, and the model is independent Bernoulli trials with a constant success probability. A different divisor, a different prior pseudo-count, or a different loss produces a different estimator of the same target. Publishing $3/4$ without the rule leaves a reader unable to reconstruct which function was applied, and publishing the rule without a model leaves the risk curve unspecified.{{cite:dodge2008}} (p. 517){{cite:goodfellow_bengio_courville2016}} (§5.4.1, eqs. 5.18–5.19)

Interval procedures and tests are estimators of a different kind: they estimate a set or make a decision, and their operating characteristics are coverage and error probabilities. The point estimator $K/n$ remains inside many of those procedures as the centre of an interval or the numerator of a statistic. Its status as a statistic is settled by the formula, before those operating characteristics are derived.

## Common misconceptions
Dependence of the binomial probabilities on $p$ is sometimes treated as a defect in $K$. The probabilities describe repeated sampling. The map $(X_1,\ldots,X_n)\mapsto\sum_i X_i$ is free of $p$ on every point of the sample space. The sum remains a statistic, and $K/n$ remains an estimator of $p$, on samples where the estimate happens to be $0$ or $1$.

Another confusion treats the estimate as the estimator. The number $3/4$ cannot have a variance. The random variable $K/4$ has variance $p(1-p)/4$. Confidence statements, bias calculations and risk comparisons attach to the random rule. A single realised estimate is one point in that rule's sampling distribution.{{cite:dodge2008}} (pp. 185–186)

## Connections
Sufficiency sharpens the choice of statistic: for independent Bernoulli trials the sum $K$ carries the likelihood's dependence on $p$, and the order of the tosses drops out of the likelihood ratio. An estimator that is a function of $K$ can still be a poor estimator; sufficiency constrains the information used, and the risk function scores how that information is turned into a guess at $p$. The beta posterior mean $(K+1)/(n+2)$ is one such function, obtained by adding a uniform prior's pseudo-counts. Under squared error and that prior it has a Bayesian interpretation; under repeated Bernoulli sampling it is simply another estimator, with the bias and variance computed above.{{cite:dodge2008}} (pp. 44–45, 517){{cite:goodfellow_bengio_courville2016}} (§5.4.2, eqs. 5.20–5.21; §5.4.4)
