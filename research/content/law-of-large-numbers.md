## Statement
The statement concerns an independent, identically distributed sequence $X_1,X_2,\ldots$ with a finite common mean $\mu$. Write $S_n=\sum_{i=1}^nX_i$. The strong law gives $S_n/n\to\mu$ almost surely; the weak law says that the chance of a fixed-size error tends to zero. A finite variance is enough for the elementary weak-law bound below, but is not required for the iid strong law when $\mathbb E|X_1|<\infty$. The displayed strong-law formula must therefore be read together with these sampling assumptions.{{cite:siegrist2022_lln}} (§6.3, Weak and Strong Laws of Large Numbers)

## Motivating example
A run of ten fair-coin tosses can have an unbalanced fraction of heads. If the tosses are independent and identically distributed, adding many more makes a persistent large discrepancy less likely. The figure shows twenty possible runs: they need not move steadily toward one half, and some wander away from it temporarily. The theorem concerns the limiting fraction over arbitrarily long runs, not a guarantee for the next hundred tosses.{{cite:siegrist2022_lln}} (§6.3, Empirical Probability)

## Intuition — From averages to limits
The average $\overline X_n=S_n/n$ has mean $\mu$. Under finite variance $\sigma^2$ and independence, its variance is $\sigma^2/n$: noise from separate observations partly cancels when we average. Chebyshev's inequality turns that shrinking variance into an explicit probability bound. The weak law controls the error probability at each separate $n$. For a general sequence, convergence in probability alone does not rule out infinitely many fixed-size excursions. For example, independent indicators $Y_n\sim\operatorname{Bernoulli}(1/n)$ converge in probability to zero, yet equal one infinitely often almost surely by the second Borel–Cantelli lemma, since $\sum_n1/n=\infty$.{{cite:durrett2019}} (pp. 70, 75) These indicators are not iid running averages. For the iid running average here, $\mathbb E|X_1|<\infty$ ensures the strong law: along almost every single infinite sequence, for every fixed $\varepsilon>0$, all sufficiently late averages satisfy $|\overline X_n-\mu|<\varepsilon$. Thus fixed-size excursions eventually stop, almost surely.{{cite:siegrist2022_lln}} (§6.3, Sample Mean; Weak and Strong Laws)

## Key results
For an event $A$, take $X_i=\boldsymbol1\{\text{outcome }i\in A\}$. Then $S_n/n$ is its observed relative frequency and $\mu=\Pr(A)$. This is Bernoulli's frequency version of the law. The same argument applies pointwise to the empirical distribution function $F_n(x)$ by using $X_i=\boldsymbol1\{Y_i\le x\}$. Pointwise convergence at each fixed $x$ is weaker than uniform convergence of the entire curve.{{cite:siegrist2022_lln}} (§6.3, Empirical Probability; Empirical Distribution Function)

The central limit theorem answers a different question. The law of large numbers sends the unscaled average toward $\mu$; a central limit theorem describes the distribution of a suitably scaled error, often $\sqrt n(\overline X_n-\mu)$. A sample of dependent observations can still have an averaging theorem, but its conditions and error rate must be checked rather than borrowed from the iid formula.{{cite:siegrist2022_lln}} (§6.3, Weak and Strong Laws)

## Proof
For iid variables with finite variance $\sigma^2$, linearity gives $\mathbb E\overline X_n=\mu$ and independence gives $\operatorname{Var}(\overline X_n)=\sigma^2/n$. For every $\varepsilon>0$, Chebyshev's inequality yields
$$
\Pr(|\overline X_n-\mu|>\varepsilon)
\leq\frac{\sigma^2}{n\varepsilon^2}\longrightarrow0.
$$
This proves the finite-variance weak law. It does not by itself prove almost-sure convergence, because the bounds $1/n$ do not form a summable series over all $n$. The iid strong law needs a further argument and is recorded separately.{{cite:siegrist2022_lln}} (§6.3, Weak and Strong Laws, weak-law proof)

## Statistical use
Sample proportions and means are consistent estimates under the sampling assumptions. For example, if Poisson counts are independent with common mean $\theta$, their average approaches $\theta$, which explains the consistency conclusion in [A Poisson mean](../questions/ex-inf-poisson-mle.qmd). In [Normal mean, known variance](../questions/ex-norm-mean.qmd), the large-sample posterior discussion assumes a sample average approaching its data-generating mean. Neither application means a realized estimate is unbiased or close for every small dataset; the law describes limiting behavior.{{cite:siegrist2022_lln}} (§6.3, Sample Mean; Empirical Probability)

## Common misconceptions
A larger sample does not force the running average to move closer to $\mu$ at every step: one more zero can pull a coin's head fraction down. The weak law does not give an exact finite-sample probability, and its Chebyshev bound can be very loose. Almost-sure convergence does not assert that every conceivable sequence converges; exceptional sequences may have probability zero. Finally, the law does not imply that individual observations become less variable as $n$ grows.{{cite:siegrist2022_lln}} (§6.3, Weak and Strong Laws)

If $X_i=Y$ for every $i$, where $Y$ is a single fair Bernoulli draw, then $S_n/n=Y$ forever; its expectation is one half, yet the average never settles at one half. Perfect dependence defeats the iid conclusion. If the $X_i$ are independent standard Cauchy draws, their average is still standard Cauchy for every $n$: the mean does not exist, and averaging does not concentrate. Even when the theorem applies, an unrepresentative sampling frame creates bias relative to a different target population.{{cite:siegrist2022_lln}} (§6.3, Weak and Strong Laws)

## History
Jakob Bernoulli's *Ars Conjectandi*, published in 1713, established the frequency form for repeated Bernoulli trials. Later formulations extended the claim beyond binary outcomes and distinguished convergence in probability from convergence along almost every sequence. The modern iid strong law covers integrable observations, whereas the familiar Chebyshev proof of the weak law uses finite variance.{{cite:dodge2008}} (p. 39, “Bernoulli's Theorem”){{cite:siegrist2022_lln}} (§6.3, Weak and Strong Laws)

## Worked example
For a fair coin, $\mu=0.5$ and $\sigma^2=0.25$. After $100$ independent tosses, Chebyshev gives $\Pr(|\overline X_{100}-0.5|>0.1)\le0.25/(100\cdot0.1^2)=0.25$. The exact probability of the same event is $\Pr(H\le39\text{ or }H\ge61)\approx0.035200$, where $H\sim\operatorname{Bin}(100,0.5)$; in R, `2 * pbinom(39, 100, 0.5)`. The cutoffs are $39$ and $61$, not $40$ and $60$, because the bound's event is strict: $H=40$ gives a head fraction of exactly $0.4$, a difference of exactly $0.1$ rather than more than $0.1$. Counting that boundary (a difference of *at least* $0.1$) would give $0.056888$, the probability of a different, larger event. The bound is valid but deliberately conservative.{{cite:siegrist2022_lln}} (§6.3, Empirical Probability; Weak and Strong Laws)

**Your turn.** For $400$ independent fair-coin tosses, use Chebyshev's inequality to bound the probability that the head fraction differs from one half by more than $0.1$. What does the bound say, and what does it leave open?

::: {.callout-tip collapse="true" title="Answer"}
The bound is $0.25/(400\cdot0.1^2)=0.0625$. Thus the chance of a deviation greater than $0.1$ is no more than $6.25\%$ under the fair, independent-trial model. It does not say the chance equals $6.25\%$ or that any one run must lie within the band. The exact probability of the same strict event, $H\le159$ or $H\ge241$, is about $0.0000484$, illustrating how loose this variance-only bound can be.
:::
