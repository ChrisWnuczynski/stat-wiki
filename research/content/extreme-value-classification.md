## Lead context
Extreme-value classification sorts the possible limits of a sample maximum into three types, according to the shape of the upper tail.

## Motivating example
The average of exponential observations settles, after $\sqrt{n}$ scaling, near the mean. The maximum does something else. It marches off to infinity like $(\log n)/\lambda$, and the fluctuations around that moving level settle to a fixed shape. A Pareto tail marches off like a power of $n$ instead. A variable with a finite upper end does not march off at all: the maximum approaches the endpoint, and the gap to the endpoint is what has a limit. The three limits are different types.{{cite:nist_extreme_value}} (§8.1.6.3, extreme value distributions)

## Intuition — The tail writes the scale
Let $M_n$ be the maximum of $n$ independent copies with distribution function $F$. Then $\Pr(M_n\le x)=F(x)^n$. If $F(x)<1$, this probability tends to $0$ for any fixed $x$, so a non-degenerate limit needs a scale $a_n>0$ and a centre $b_n$ for which $(M_n-b_n)/a_n$ settles. The sequences are read off the tail. A level $u_n$ with about one exceedance in $n$ draws satisfies $n\Pr(X>u_n)\approx 1$. An exponential tail $e^{-\lambda u}$ puts $u_n$ near $(\log n)/\lambda$. A Pareto tail $x^{-\alpha}$ puts it near $n^{1/\alpha}$. A finite endpoint $x_F$ forces $u_n$ up against $x_F$.{{cite:nist_extreme_value}} (§8.1.6.3, bounded and unbounded cases)

## Definition — Three explicit limits
For exponential rate $\lambda$, with $b_n=(\log n)/\lambda$ and $a_n=1/\lambda$,
$$
\Pr\bigl((M_n-b_n)/a_n\le x\bigr)=\bigl(1-e^{-x}/n\bigr)^n\to e^{-e^{-x}}
$$
for every fixed real $x$. This is the Gumbel limit, the type NIST records as the Type I law for an unbounded extreme. For a Pareto tail $\Pr(X>x)=x^{-\alpha}$ on $x\ge 1$, with $a_n=n^{1/\alpha}$ and $b_n=0$,
$$
\Pr(M_n/a_n\le x)=\bigl(1-x^{-\alpha}/n\bigr)^n\to e^{-x^{-\alpha}},\qquad x>0,
$$
the Fréchet limit. For $X$ uniform on $(0,1)$, the gap $n(1-M_n)$ satisfies $\Pr(n(1-M_n)>y)=(1-y/n)^n\to e^{-y}$ for $y>0$, a Weibull extreme-value limit supported on the side of the endpoint. A finite upper bound changes both the centring and the support of the limit.{{cite:nist_extreme_value}} (§8.1.6.3, Type I and Weibull)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the exponential tail, $\lambda(b_n+a_n x)=\log n+x$, so the survival probability at that level is $e^{-x}/n$. Raising the distribution function to the $n$th power produces $(1-e^{-x}/n)^n$. For any fixed $a$, $(1-a/n)^n\to e^{-a}$, and here $a=e^{-x}$. The Pareto and uniform calculations are the same limit with $a=x^{-\alpha}$ and $a=y$. The general statement, that every non-degenerate affine limit of a maximum belongs to one of these three types, is not proved on this page.
:::
:::

## Worked example
For the exponential limit at $x=0$ and $n=20$,
$$
(1-1/20)^{20}=0.35849,\qquad e^{-1}=0.36788.
$$
The finite-$n$ value is already close to the Gumbel limit $e^{-e^{0}}=e^{-1}$. For the uniform gap at $y=1$ and $n=10$,
$$
(1-1/10)^{10}=0.34868,
$$
against the same limit $0.36788$. The approach is from below in both of these one-exceedance calculations.

**Your turn.** For a Pareto tail of index $\alpha=1$, with $a_n=n$ and $x=1$, compute $\Pr(M_{20}/20\le 1)$ exactly from the finite-$n$ formula and compare it with $e^{-1}$.

::: {.callout-tip collapse="true" title="Answer"}
The formula gives $(1-1/20)^{20}=0.35849$, the same number as the exponential case at $x=0$. The limit is again $e^{-1}=0.36788$. At this particular point the two tail formulas reduce to the same expression $(1-1/n)^n$.
:::

## Connections — Averages, lifetimes, and dependence
The [central limit theorem](central-limit-theorem.qmd) scales a sum. Extreme-value limits scale a maximum, and the scale is logarithmic, a power of $n$, or a gap to an endpoint, according to the type. [Exponential tails and the Gumbel law](exponential-tails-and-the-gumbel-law.qmd), [power-law tails and the Fréchet law](power-law-tails-and-the-frechet-law.qmd) and [a finite endpoint and a Weibull extreme-value law](a-finite-endpoint-and-a-weibull-extreme-value-law.qmd) are the three cases. NIST notes that a series system, which fails at the first component failure, has a minimum whose limit is Weibull when the component lifetimes are bounded below by zero.{{cite:nist_extreme_value}} (§8.1.6.3, series systems) Dependence can replace $n$ by a smaller count of independent excursions. The identity $F(x)^n$ uses independence.

## Check yourself

### A larger exponential sample
Compute $(1-1/50)^{50}$ and say whether it is closer to $e^{-1}=0.36788$ than $(1-1/20)^{20}=0.35849$ is.

::: {.callout-tip collapse="true" title="Answer"}
$(1-1/50)^{50}=0.36417$. The gap to $0.36788$ is $0.00371$, smaller than the gap $0.00939$ at $n=20$. The limit statement is visible in the arithmetic.
:::

### Which type has a finite upper end?
A measurement cannot exceed $1$, and one studies $n(1-M_n)$. Which of the three types is that limit, and why is it not Gumbel?

::: {.callout-tip collapse="true" title="Answer"}
It is the Weibull extreme-value type. The maximum is pressed against a finite endpoint, so the limiting variable lives on one side of $0$. A Gumbel limit is spread over the whole real line and comes from an unbounded light tail, not from a hard ceiling.
:::
