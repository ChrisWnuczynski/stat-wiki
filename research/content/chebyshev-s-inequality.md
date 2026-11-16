## Motivating example
A filling machine produces bottles whose mean content is $500$ mL and standard deviation is $10$ mL, but its shape of variation has not been established. Chebyshev's inequality can still bound the chance that a bottle misses the mean by at least $25$ mL: the bound is $10^2/25^2=0.16$. It gives a guarantee from mean and variance alone, though it may be conservative for the actual process.

## Intuition
Variance is the average squared distance from the mean. If many outcomes were far away, those large squares would force the average upward. Therefore a small variance limits how much probability can sit far from the mean. The argument makes no normality or symmetry assumption. Its price for that generality is a broad bound: information about the distribution's shape can yield a much tighter answer.

The threshold must be read literally. With standard deviation $\sigma$ and a cutoff $k\sigma$, the bound is $1/k^2$ for $k>0$. At two standard deviations it promises at least $75\%$ of outcomes within the *open* central interval; it does not promise the familiar normal-model percentage. The bound can exceed one for $k<1$, in which case the trivial probability bound one is more useful.

## Definition
For a real random variable $X$ with finite mean $\mu$ and finite variance $\sigma^2$, Chebyshev's inequality states that for every $a>0$,
$$
\Pr(|X-\mu|\geq a)\leq\frac{\sigma^2}{a^2}.
$$
Equivalently, $\Pr(|X-\mu|<a)\geq1-\sigma^2/a^2$. The latter lower bound is informative when $a>\sigma$. A version with $>$ on the left also follows immediately because that event is contained in the event with $\geq$. The variance must be finite; no appeal to a vague notion of “typical spread” replaces that condition.

## Properties
The inequality is sharp with only a mean and variance specified. Let $X$ be $-2$ with probability $1/8$, $0$ with probability $3/4$, and $2$ with probability $1/8$. Then $\mu=0$, $\sigma^2=1$, and $\Pr(|X|\geq2)=1/4=\sigma^2/2^2$. Thus no uniformly smaller coefficient can replace the one in the inequality. In a particular smooth distribution the bound may be far from the true tail probability.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set $Z=(X-\mu)^2$, which is nonnegative. On the event $Z\geq a^2$ we have $Z\geq a^2$, so $\mathbb E Z\geq a^2\Pr(Z\geq a^2)$. Since $\mathbb E Z=\sigma^2$, division proves Chebyshev's inequality. For the three-point example, symmetry gives mean zero, and $\mathbb E X^2=(1/8)4+(1/8)4=1$; its two extreme points have total probability $1/4$, attaining the bound at $a=2$. For independent, identically distributed $X_i$ with variance $\sigma^2$, variance additivity gives $\operatorname{Var}(\overline X_n)=\sigma^2/n$. Applying the inequality to $\overline X_n$ yields $\Pr(|\overline X_n-\mu|\geq\varepsilon)\leq\sigma^2/(n\varepsilon^2)\to0$ for every $\varepsilon>0$, proving the finite-variance weak law in probability.
:::
:::

## Interpretation
The bound is about a random variable's distribution, not a confidence statement about a fixed parameter. Applied to a sample average, however, it explains why repeated independent observations can locate an unknown population mean: the average's variance shrinks with sample size. Independence enters that variance calculation, not Chebyshev's inequality itself. For correlated observations the average can retain substantial variance, and the same $1/n$ rate cannot simply be copied.

The threshold and the variance must be on compatible scales. If a standard deviation is $10$ mL, the variance is $100$ mL squared; comparing $10$ directly with $25^2$ gives the wrong bound. Translating or changing units preserves the inequality when the mean, threshold and variance are transformed together.

## Statistical use
Chebyshev's inequality is useful when only low-order moments are trustworthy or when a proof needs a distribution-free probability control. It can establish convergence of an unbiased estimator whose variance tends to zero and give conservative checks on simulation output. For an engineering or clinical decision, its bound should be reported as a worst-case guarantee from stated moments, then supplemented with distributional or empirical information if a sharper risk assessment is required.

## Worked example
Suppose independent observations have mean $10$ and variance $16$. For $n=64$, the sample mean has variance $16/64=0.25$ and standard deviation $0.5$. Chebyshev gives $\Pr(|\overline X_{64}-10|\geq1)\leq0.25/1^2=0.25$, so at least $75\%$ of such sample means lie strictly between $9$ and $11$. This does not assert that exactly a quarter fall outside. Nor does it require normal observations; finite variance and independence suffice for this calculation.

**Your turn.** Keep the same population mean and variance, but take $n=100$ independent observations. Bound the probability that their average differs from $10$ by at least $1$, and state a lower bound for the chance that it lies between $9$ and $11$.

::: {.callout-tip collapse="true" title="Answer"}
The average has variance $16/100=0.16$. Hence $\Pr(|\overline X_{100}-10|\geq1)\leq0.16$, and $\Pr(9<\overline X_{100}<11)\geq0.84$. Larger sample size improved this worst-case guarantee because the independent-sample variance fell from $0.25$ to $0.16$.
:::

## Common misconceptions
The bound is not a normal-model tail probability; it remains valid for skewed or discrete distributions but is often looser. It does not say the probability *equals* $\sigma^2/a^2$, except in special cases such as the three-point construction. Finite variance is essential, whereas independence is needed only for certain applications to sums. Finally, a bound above one is mathematically true but conveys no useful risk information.

## Assumptions and limits
A Cauchy variable has no finite variance, so the displayed ratio cannot be formed. If every observation in a proposed “sample” equals one common random shock $Z$, then $\overline X_n=Z$ and its variance does not shrink as $1/n$; the weak-law calculation above fails despite finite variance. And for a normal variable the actual two-standard-deviation tail is about $0.0455$, far below Chebyshev's $0.25$ bound, illustrating the cost of using moments alone. These failures involve existence, dependence and looseness separately.

## Connections
[Markov's inequality](markov-s-inequality.qmd) applied to squared deviation gives this result. The [law of large numbers](law-of-large-numbers.qmd) follows for independent finite-variance averages, while [variance](variance.qmd) supplies the needed moment. Stronger distribution assumptions can give sharper tail bounds; they should be stated rather than smuggled into a distribution-free claim.

## History
Dodge notes the name Bienaymé–Chebyshev inequality, reports Bienaymé's earlier paper on the topic, and lists Chebyshev's 1867 French publication among his principal works.{{cite:dodge2008}} (p. 68, “Chebyshev, Pafnutii Lvovich”) The two names reflect that history; the short proof above shows why the bound remains a basic tool in probability.
