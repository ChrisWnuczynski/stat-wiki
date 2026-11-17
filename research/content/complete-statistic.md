## Motivating example
A count of successes can contain all the sample information about a Bernoulli probability, yet that alone does not say whether an unbiased estimate formed from the count is unique. In four independent trials the count $T$ is sufficient for $p$: once $T$ is known, the order of successes is irrelevant to the likelihood. Completeness adds a different guarantee. No nonzero function of $T$ averages to zero for *every* $p$ in $(0,1)$. Consequently, if two functions of $T$ estimate the same target without bias, they agree almost surely.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics and The Bernoulli Distribution)

## Intuition — What completeness rules out
At one particular value of $p$, many functions can have expectation zero: $T-4p$ is an example if $p$ were known. An estimator cannot use the unknown $p$, however. Completeness asks for one fixed function of the observed statistic whose expectation is zero throughout the model. Varying $p$ makes the distribution of $T$ sweep through enough different shapes that such a function must vanish. This is a property of the *family of distributions of $T$*, including its parameter space, rather than of a single observed count.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics)

## Definition
Let $T=T(X)$ be a statistic under a family $\{P_\theta:\theta\in\Omega\}$. It is **complete** if every measurable, integrable function $q$ that does not depend on $\theta$ satisfies

$$E_\theta\{q(T)\}=0\quad\text{for all }\theta\in\Omega
\quad\Longrightarrow\quad P_\theta\{q(T)=0\}=1\quad\text{for all }\theta\in\Omega.$$

The almost-sure qualification allows $q$ to differ from zero on values that the model never produces. Completeness says nothing on its own about whether $T$ preserves the sample information: that separate requirement is sufficiency.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics)

## Properties
For iid Bernoulli observations with $p\in(0,1)$, the sum $T=\sum_iX_i$ is both sufficient and complete. The same holds for the sum of iid Poisson observations when the rate varies over $(0,\infty)$. A full-rank natural exponential family with an open natural-parameter set has a complete natural sufficient statistic under the usual integrability conditions; restricting a family to a curved or finite parameter subset can destroy completeness.{{cite:siegrist2022_sufficient_complete}} (§7.6, The Bernoulli Distribution, The Poisson Distribution and Exponential Families)

The practical consequence is the Lehmann–Scheffé result. If $T$ is complete and sufficient and $h(T)$ is unbiased for $g(\theta)$, then it is the unique unbiased function of $T$ for that target and is the uniformly minimum-variance unbiased estimator among all unbiased estimators with finite variance. The Rao–Blackwell step supplies the variance comparison; completeness supplies uniqueness after conditioning.{{cite:siegrist2022_sufficient_complete}} (§7.6, Properties of Sufficient Statistics and Complete Statistics)

Basu's theorem gives a second consequence: a complete sufficient statistic is independent of every ancillary statistic, whose distribution is parameter-free. Thus the part of a sample that is irrelevant to the parameter cannot be a nonconstant function of a complete sufficient summary.{{cite:siegrist2022_sufficient_complete}} (§7.6, Ancillary Statistics)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For Bernoulli observations, the likelihood is $p^T(1-p)^{n-T}$, so factorisation makes $T$ sufficient. If $E_pq(T)=0$ for every $p\in(0,1)$, division by $(1-p)^n$ gives $\sum_{t=0}^nq(t){n\choose t}z^t=0$ for every $z=p/(1-p)>0$. A polynomial that vanishes on an interval has every coefficient zero; hence $q(t)=0$ for all possible $t$. For Poisson observations, $T\sim\operatorname{Poisson}(n\theta)$ and $e^{n\theta}E_\theta q(T)=\sum_{t\ge0}q(t)n^t\theta^t/t!$. If its expectation exists throughout an open interval and vanishes there, uniqueness of its power-series coefficients gives $q(t)=0$ for all $t$.

If $h_1(T)$ and $h_2(T)$ are unbiased for the same target, their difference has zero expectation at every parameter, so completeness makes them equal almost surely. For any other unbiased estimator $W$, sufficiency makes $E(W\mid T)$ a parameter-free statistic, unbiased for the same target. It therefore equals $h(T)$, while $\operatorname{Var}(W)=\operatorname{Var}\{E(W\mid T)\}+E\{\operatorname{Var}(W\mid T)\}\ge\operatorname{Var}\{h(T)\}$. For Basu's theorem, let $A$ be ancillary and $B$ any measurable set. Sufficiency makes $r(T)=P_\theta(A\in B\mid T)$ independent of $\theta$ as a function of $T$. Ancillarity makes $E_\theta r(T)=P_\theta(A\in B)=c_B$ independent of $\theta$. Completeness forces $r(T)=c_B$ almost surely, which is independence for every $B$.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics, The Bernoulli Distribution, The Poisson Distribution and Ancillary Statistics)
:::
:::

## Interpretation
Completeness is an identifiability condition for expectations of functions of $T$. If $h_1(T)$ and $h_2(T)$ have the same expectation function over the entire parameter space, completeness says they are the same statistic almost surely. It does not imply that every target has an unbiased estimator. For example, in $n$ Bernoulli trials, the expectation of any function of $T$ is a polynomial in $p$ of degree at most $n$, so no such function can be unbiased for $e^p$ across $(0,1)$.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics and The Bernoulli Distribution)

## Worked example
Suppose four independent trials yield $T=3$ successes. To estimate the probability $p^2$ that two new independent trials both succeed, use $h(T)=T(T-1)/\{4\cdot3\}$. The numerator counts ordered pairs of observed successes. Each of the $4\cdot3=12$ ordered pairs succeeds with probability $p^2$, so $E_ph(T)=p^2$. Here $h(3)=6/12=0.50$. The tempting plug-in estimate $(T/4)^2=9/16=0.5625$ has expectation $p^2+p(1-p)/4$, so it is generally biased upward. Since $T$ is complete sufficient, $h(T)$ is the unique unbiased function of $T$ and the UMVU estimate of $p^2$.{{cite:siegrist2022_sufficient_complete}} (§7.6, The Bernoulli Distribution and Complete Statistics)

**Your turn.** Five independent Bernoulli trials produce $T=2$. Estimate $p^2$ by the unbiased ordered-pair method, compare it with the squared sample proportion, and say which is UMVU.

::: {.callout-tip collapse="true" title="Answer"}
The ordered-pair estimate is $T(T-1)/\{5\cdot4\}=2/20=0.10$; the squared sample proportion is $(2/5)^2=0.16$. The former is unbiased for $p^2$ and, because the binomial count is complete sufficient for $p\in(0,1)$, is UMVU. The difference between these realised values alone does not establish bias; their expectations do.
:::

## Common misconceptions
Sufficiency is not completeness: a statistic can retain all likelihood information yet admit a nonzero unbiased estimator of zero. Completeness is also stronger than having zero expectation at a *single* parameter value; the condition must hold at every parameter value with the same $q$. Nor does a unique unbiased function of $T$ automatically become a Bayesian posterior estimate; the latter depends on a prior and loss function. Finally, complete sufficient does not mean that $T$ is independent of every other statistic: Basu's conclusion is limited to ancillary statistics.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics and Ancillary Statistics)

## Assumptions and limits
The parameter space matters. If a binomial model allows only $p=1/2$, the nonzero function $q(T)=T-n/2$ has expectation zero, so the count is not complete even though it is complete when $p$ ranges over an interval. A moving-support example shows a different failure. For iid $X_i\sim\operatorname{Uniform}(\theta,\theta+1)$ with $n\ge2$, the pair $T=(X_{(1)},X_{(n)})$ is minimal sufficient. Yet the range $R=X_{(n)}-X_{(1)}$ is a nonconstant function of $T$ with $E_\theta R=(n-1)/(n+1)$ for every $\theta$. Thus $q(T)=R-(n-1)/(n+1)$ disproves completeness. The range is ancillary; it could not be a nonconstant function of a complete sufficient statistic under Basu's theorem.{{cite:siegrist2022_order_statistics}} (§6.6, The Uniform Distribution){{cite:siegrist2022_sufficient_complete}} (§7.6, Ancillary Statistics)

## Connections
Sufficiency permits Rao–Blackwell conditioning without knowing the parameter, while completeness makes the resulting unbiased function unique. This is the route from a [sufficient statistic](sufficient-statistic.qmd) to a [UMVU estimator](uniformly-minimum-variance-unbiased-estimator.qmd). The [Poisson UMVU exercise](../questions/ex-inf-poisson-umvu.qmd) conditions on a Poisson sum; completeness of that sum explains why its unbiased conditional answer is the UMVU answer. The [Basu theorem](basu-s-theorem.qmd) instead combines completeness with [ancillarity](ancillary-statistic.qmd) to establish independence.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics, The Poisson Distribution and Ancillary Statistics)

## History
Lehmann and Scheffé's work on completeness and unbiased estimation established the role of complete sufficient statistics in selecting unique minimum-variance unbiased estimators. Basu subsequently connected complete sufficiency to independence from ancillary statistics. These results gave the abstract expectation condition two distinct uses: choosing estimators and separating parameter information from parameter-free variation.{{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics and Ancillary Statistics)
