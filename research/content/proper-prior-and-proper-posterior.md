## Lead context
Normalisation is a mathematical condition on the whole parameter space, including its boundaries and tails.

## Motivating example
Suppose five independently inspected components include two failures. A prior for the failure probability may be uniform on the unit interval, or may put increasing weight near its endpoints. Both choices can be multiplied by the same binomial likelihood. The resulting curves need not both have finite area. Before reporting a posterior probability, one must establish that the area is positive and finite. Bayesian updating constructs a conditional distribution by dividing the joint distribution by its marginal normalising factor.{{cite:pishro_nik2014}} (§9.1.0)

## Definition — Two separate integrals
Relative to a specified measure $d\theta$, a proper prior satisfies $\pi(\theta)\geq0$ and $\int\pi(\theta)\,d\theta=1$. For observed data $y$, define
$$
m(y)=\int L(\theta;y)\pi(\theta)\,d\theta.
$$
The ordinary posterior density is $L(\theta;y)\pi(\theta)/m(y)$ when $0<m(y)<\infty$. The integration is over every possible parameter value; a finite value at a single estimate cannot establish integrability.{{cite:pishro_nik2014}} (§9.1.0, Bayesian statistical inference)

An improper prior is a nonnegative kernel with infinite total integral. It can still yield a proper posterior if its likelihood-weighted integral is finite and positive. Multiplying such a prior kernel by any positive constant cancels in the posterior ratio. It does not give the prior a probability interpretation. The Haldane kernel $[p(1-p)]^{-1}$ supplies a concrete example in which posterior propriety depends on the observed success count.{{cite:taraldsen2022_improper}} (§2, eqs. 4–5)

## Properties — Boundaries decide the beta example
For $x$ successes in $n$ independent Bernoulli trials and prior kernel $p^{a-1}(1-p)^{b-1}$, the posterior kernel is
$$
p^{a+x-1}(1-p)^{b+n-x-1},\qquad0<p<1.
$$
Its integral is finite precisely when $a+x>0$ and $b+n-x>0$. Near zero the integral of $p^r$ is finite exactly when $r>-1$; substituting $q=1-p$ gives the condition at the other endpoint. This explains why the Haldane choice $a=b=0$ needs both a success and a failure.{{cite:taraldsen2022_improper}} (§2, binomial example)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Split the integral at $p=1/2$. On the first half, $(1-p)^{b+n-x-1}$ is bounded above and below by positive constants, so integrability is determined by $p^{a+x-1}$. The second half has the corresponding condition after the substitution $q=1-p$. For positive resulting shapes the integral is the beta integral, and division by it produces a density of total mass one.
:::
:::

There is also a simple sufficient condition for a proper prior: if $0\leq L(\theta;y)\leq M<\infty$ throughout the parameter space, then $m(y)\leq M$. If the likelihood is positive on a set with positive prior probability, then $m(y)>0$. For discrete data the likelihood at a specified outcome is a probability and is at most one. For continuous observations it is a density, so that upper bound does not follow just from the word likelihood.{{cite:pishro_nik2014}} (§9.1.0, discrete and continuous posterior formulas)

## Worked example
For the five inspections and two failures, a uniform prior gives posterior kernel $p^2(1-p)^3$. Its integral is $1/60$, giving the density $60p^2(1-p)^3$, a $\operatorname{Beta}(3,4)$ distribution with mean $3/7$. The Haldane prior instead gives kernel $p(1-p)^2$, integral $1/12$, and posterior $\operatorname{Beta}(2,3)$ with mean $2/5$. Both posteriors are proper for these data. Their different means reflect different priors, rather than different normalisation conventions.{{cite:pishro_nik2014}} (§9.1.0);{{cite:taraldsen2022_improper}} (§2)

If all five inspections are failures, the Haldane posterior kernel is $p^4/(1-p)$. Its integral diverges at one. A plot on an interval ending short of one would conceal that divergence. A finite sequence of simulated draws cannot replace the integral check.{{cite:taraldsen2022_improper}} (§§1–2)

**Your turn.** With one failure and four successes, find the two beta shapes under a uniform prior and under the Haldane kernel. Are both posteriors proper?

::: {.callout-tip collapse="true" title="Answer"}
Counting failure as the Bernoulli success gives $x=1$ and $n=5$. The uniform prior gives shapes $(2,5)$, and the Haldane kernel gives $(1,4)$. Every shape is positive, so both posteriors are proper.
:::

## Connections — Probability statements require the normalised law
Posterior means, quantiles, and credible probabilities are computed from a proper posterior distribution. A kernel alone identifies relative weights; its integral decides whether those weights can be converted into probabilities. This distinction also explains why multiplying an improper prior by a constant is harmless for a proper posterior within one model but does not supply a uniquely scaled prior predictive density for comparisons between models.{{cite:pishro_nik2014}} (§9.1.0);{{cite:taraldsen2022_improper}} (§2, arbitrary prior constants)

## Check yourself
Work through the normalisation step before naming the distribution.

### A normal sample {#self-check-ex-improper-normal}
[Improper prior for a normal sample](../questions/ex-improper-normal.qmd): what conditions make the marginal variance posterior proper?

::: {.callout-tip collapse="true" title="Answer"}
With $n\geq2$ and $S=\sum_i(x_i-\bar x)^2>0$, integrating out the mean gives an inverse-gamma kernel with shape $(n-1)/2>0$ and scale $S/2>0$. If $S=0$, the exponential factor no longer controls the integral at zero, and the posterior is improper.
:::

### Integration versus substitution {#self-check-q-43}
[Conditional versus marginal](../questions/q-43.qmd): why does integrating out the normal mean change the variance shape?

::: {.callout-tip collapse="true" title="Answer"}
The Gaussian integral over the mean contributes a factor $v^{1/2}$. Multiplying it by the joint kernel changes the inverse-gamma shape from $n/2$ to $(n-1)/2$. Setting the mean equal to the sample mean does not contribute that factor and therefore gives a different distribution.
:::
