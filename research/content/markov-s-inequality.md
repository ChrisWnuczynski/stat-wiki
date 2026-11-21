## Lead context
Markov's inequality turns a mean into an upper bound on the probability of a very large nonnegative outcome, without using the shape of the distribution.

## Motivating example
A job has mean length $10$ minutes. With nothing else known, the chance it lasts at least an hour is at most $10/60=1/6$. The bound is often loose. If the variance is also known to be $25$, Chebyshev's inequality cuts the same tail to $25/50^2=0.01$. The improvement spends a second moment that Markov's inequality never sees.{{cite:durrett2019}} (Thm. 1.6.4, pp. 29–30)

## Intuition
On the event $\{X\ge a\}$ a nonnegative $X$ is at least $a$, and elsewhere it is at least $0$. So $X\ge a\,1_{\{X\ge a\}}$. Taking expectations gives $a\,\mathrm{P}(X\ge a)\le\mathrm{E} X$. The argument throws away all information except the mean and the threshold. That is why the bound survives for every distribution with that mean, and why it is rarely sharp for a smooth density.

Durrett states a more general comparison and remarks that some authors call the general form Markov's inequality, keeping the name Chebyshev for the second-moment case. The form on this page is the general comparison with $\varphi(x)=x$ and $A=[a,\infty)$.{{cite:durrett2019}} (Thm. 1.6.4 and the remark on p. 30)

## Definition
Let $X\ge 0$ and $a>0$. Then
$$
\mathrm{P}(X\ge a)\le\frac{\mathrm{E} X}{a},
$$
whenever the mean exists and is finite. If $a\le\mathrm{E} X$ the right-hand side is at least $1$ and the bound says nothing. If the mean is infinite the inequality is not on offer.

Applied to $(X-\mathrm{E} X)^2$ at level $\varepsilon^2$, the same argument is Chebyshev's inequality $\mathrm{P}(|X-\mathrm{E} X|\ge\varepsilon)\le\mathrm{Var}(X)/\varepsilon^2$.

## Interpretation — A bound, and when it is sharp
Equality holds for a two-point law that puts mass $p$ at $a$ and mass $1-p$ at $0$. Then $\mathrm{E} X=ap$ and $\mathrm{P}(X\ge a)=p$, so the ratio is exactly $p$. Any distribution that spreads the mass strictly between $0$ and $a$, or above $a$, makes the inequality strict. The bound is therefore a worst-case statement over all nonnegative laws with a given mean, not a typical tail for a named family.

For an exponential lifetime with mean $10$, the exact chance of lasting at least $60$ minutes is $e^{-6}\approx 0.002479$. Markov's $1/6\approx 0.1667$ is about $67$ times larger. The bound is valid and, for planning a hard deadline, much more conservative than the exponential calculation. Using it when the exponential model is justified throws away the memoryless structure.

## Properties
The comparison extends from $X$ itself to a nonnegative function of $X$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $X\ge 0$ and $a>0$. Then $X\ge a\,1_{\{X\ge a\}}$, because the two sides agree on $\{X\ge a\}$ and the right-hand side is $0$ elsewhere while $X$ is nonnegative. Taking expectations and using monotonicity yields $a\,\mathrm{P}(X\ge a)\le\mathrm{E} X$.{{cite:durrett2019}} (Thm. 1.6.4)

Durrett's general form replaces $X$ by $\varphi(X)$ for $\varphi\ge 0$ and replaces $a$ by the infimum of $\varphi$ on a set $A$. The proof is the same comparison of $\varphi(X)$ with that infimum times the indicator of $\{X\in A\}$. Chebyshev's inequality is $\varphi(x)=x^2$ and $A=\{|x|\ge\varepsilon\}$, after centring. The second-moment form $\varepsilon^2\mathrm{P}(|X|\ge\varepsilon)\le\mathrm{E} X^2$ is the case recorded as (1.6.1) in that section.{{cite:durrett2019}} (Thm. 1.6.4, pp. 29–30)

For the exponential check, a rate-$1/10$ law has survival $e^{-t/10}$, so $\mathrm{P}(X\ge 60)=e^{-6}$.
:::
:::

## Statistical use — From a moment to a probability
The inequality is the step from an $L^1$ or $L^p$ bound to convergence in probability. If $\mathrm{E}|X_n-X|\to 0$, then $\mathrm{P}(|X_n-X|>\varepsilon)\le\mathrm{E}|X_n-X|/\varepsilon\to 0$. A finite-variance weak law is the same step applied to the square of the centred average: the variance of the average is $\sigma^2/n$, and Chebyshev sends the tail to zero. The bound does not need independence beyond whatever was used to compute the mean or the variance. It also does not prove an almost-sure limit, because a bound of order $1/n$ need not be summable.

In a risk calculation the bound is a guarantee that holds uniformly over every nonnegative distribution with the stated mean. It is the right tool when the distribution is unknown and a hard upper limit is required. It is a poor summary of a tail one has already modelled.

## Worked example
Suppose $X\ge 0$ has mean $4$. Then $\mathrm{P}(X\ge 20)\le 4/20=0.2$. If in addition $\mathrm{Var}(X)=9$, Chebyshev's inequality gives
$$
\mathrm{P}(X\ge 20)=\mathrm{P}(X-4\ge 16)\le\frac{9}{16^2}=\frac{9}{256}\approx 0.0352.
$$
The second bound is about six times smaller. It can fail if the variance is not $9$: a Pareto-type law with mean $4$ and an infinite variance still obeys the Markov bound $0.2$, and Chebyshev's inequality does not apply.

Equality in the Markov bound is attained by $X=20$ with probability $0.2$ and $X=0$ otherwise. The mean is $4$, and $\mathrm{P}(X\ge 20)=0.2$.

A Poisson count with mean $2$ shows the other extreme. Markov's inequality still says $\mathrm{P}(X\ge 10)\le 2/10=0.2$. The Poisson tail is about $0.000046$. The bound is valid, and it is thousands of times the probability that the Poisson model actually assigns. Replacing the Poisson calculation by $0.2$ would badly overstate the chance of ten or more events.{{cite:durrett2019}} (Thm. 1.6.4)

**Your turn.** A nonnegative loss has mean $6$. Bound $\mathrm{P}(X\ge 15)$ and $\mathrm{P}(X\ge 4)$.

::: {.callout-tip collapse="true" title="Answer"}
$\mathrm{P}(X\ge 15)\le 6/15=0.4$. The threshold $4$ is below the mean, and $6/4=1.5$ exceeds $1$, so Markov's inequality gives no information. The probability is at most $1$ for a trivial reason that does not use the mean.
:::

## Common misconceptions
The inequality does not require independence, identical distribution, or a variance. Adding those assumptions can sharpen the bound, as Chebyshev does, but they are not hidden hypotheses of Markov's inequality.

The bound is one-sided and uses nonnegativity. Applying $\mathrm{E} X/a$ to a signed variable, or to a lower tail $\mathrm{P}(X\le a)$, is a different claim and can be false. A variable that is $-100$ with probability $0.5$ and $100$ with probability $0.5$ has mean $0$, and $\mathrm{P}(X\ge 100)=0.5$, while a naive ratio $0/100$ would say the tail is $0$.

A bound of $1/6$ is not an estimate of the probability. For the exponential law with the same mean the probability is about $0.0025$. Quoting $1/6$ as if it were the chance of a long job overstates the tail by a large factor whenever the true law is much lighter than the two-point equality case.

## Assumptions and limits — Where the mean is not enough
If $\mathrm{E} X=\infty$ the ratio is not a real number and the inequality, as stated, does not apply. A nonnegative variable can have an infinite mean and $\mathrm{P}(X\ge a)=1$ for every finite $a$, or a lighter tail. The mean no longer separates those cases.

If $a\le\mathrm{E} X$, the ratio is at least $1$ and the bound is vacuous. A mean of $6$ says nothing about $\mathrm{P}(X\ge 4)$ through this inequality, even though that event may be likely or unlikely.

The passage from $L^1$ convergence to convergence in probability uses the inequality at every $n$. It does not upgrade the conclusion to almost-sure convergence. The strong law needs a summable series or a truncation argument, not a single Markov bound.

Chebyshev's refinement is unavailable when the variance is infinite. A nonnegative law with finite mean and infinite variance is a concrete case: Markov still caps $\mathrm{P}(X\ge a)$, and the second-moment bound cannot be formed.

## Connections
[Chebyshev's inequality](chebyshev-s-inequality.qmd) is Markov's inequality applied to a squared deviation. The [weak law](law-of-large-numbers.qmd) is the Chebyshev bound on an average whose variance tends to zero. The [strong law](strong-law.qmd) needs a stronger argument, because these bounds need not be summable. Convergence in $L^1$ implies [convergence in probability](modes-of-convergence.qmd) by the inequality on this page, and the converse is false.{{cite:durrett2019}} (Thm. 1.6.4, pp. 29–30)

## History
The comparison of a nonnegative variable with a threshold times an indicator is the form proved as the general moment inequality in Durrett, who attaches Chebyshev's name to that general statement and notes that other authors call it Markov's inequality. The second-moment special case, under the name Bienaymé–Chebyshev, is $\mathrm{P}(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$.{{cite:durrett2019}} (Thm. 1.6.4, pp. 29–30){{cite:dodge2008}} (p. 298)
