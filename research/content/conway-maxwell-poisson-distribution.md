## Lead context
The Conway–Maxwell–Poisson law keeps a count on the nonnegative integers and uses a second parameter to make the distribution tighter or wider than a Poisson law.

## Intuition — The factorial power changes the tails
A Poisson probability is proportional to $\lambda^{y}/y!$. Replacing the factorial by $(y!)^{\nu}$ leaves $\nu=1$ unchanged and changes every other case. When $\nu>1$, $(y!)^{\nu}$ grows faster than $y!$, so large counts are down-weighted and the distribution is tighter than the Poisson law with the same $\lambda$. When $0\le\nu<1$, large counts are down-weighted less, and the distribution is wider. The normalising constant is the series $Z(\lambda,\nu)=\sum_{j=0}^{\infty}\lambda^{j}/(j!)^{\nu}$, which equals $e^{\lambda}$ only at $\nu=1$. In this parameterisation $\lambda$ is not the mean, except in that Poisson case.

## Definition
The probability of a count $x\in\{0,1,2,\ldots\}$ is
$$
P(X=x)=\frac{\lambda^{x}}{(x!)^{\nu} Z(\lambda,\nu)},
$$
with $\lambda>0$ and $\nu\ge 0$, and with $\lambda<1$ when $\nu=0$ so that the series converges. The mean and the variance are the sums $\sum x\,P(X=x)$ and $\sum x^{2}P(X=x)-\bigl(\mathrm{E} X\bigr)^{2}$. At $\nu=1$ both equal $\lambda$. At the parameter pair in the worked example neither equals $\lambda$. At $\nu=0$ and $\lambda=1/2$ the series is geometric, the boundary case recorded with the distribution.

## Worked example
Take $\lambda=1$ and $\nu=2$, so the summand is $1/(x!)^{2}$. Truncating after $x=12$ changes nothing in the first six decimals: $Z(1,2)\approx 2.2796$. Then
$$
P(X=0)=\frac{1}{Z(1,2)}\approx 0.4387.
$$
The mean is $\approx 0.6978$ and the variance is $\approx 0.5131$. The variance is smaller than the mean, which a Poisson random variable cannot do, and smaller than $\lambda=1$, which is not the mean of this law. A Poisson random variable with mean $0.6978$ would have variance $0.6978$, about $1.36$ times the Conway–Maxwell–Poisson variance computed here.

**Your turn.** Set $\nu=1$ and $\lambda=1$. Identify the law and give $P(X=0)$ exactly.

::: {.callout-tip collapse="true" title="Answer"}
At $\nu=1$ the normalising series is $\sum_{j\ge 0}1/j!=e$, so $P(X=0)=e^{-1}\approx 0.3679$. The law is Poisson with mean $1$, and the variance equals the mean rather than falling below it.
:::

**Check yourself.** At $\lambda=1$ and $\nu=2$, the probability $P(X=0)\approx 0.4387$ exceeds the Poisson probability $e^{-1}\approx 0.3679$. Why does a larger probability at zero go with a smaller variance?

::: {.callout-tip collapse="true" title="Answer"}
The factor $(x!)^{2}$ in the denominator cuts off the right tail faster than $x!$ does. Probability moves toward zero and the small counts, so the mean falls below $1$ and the spread falls further, to about $0.5131$. A higher atom at zero is the left-hand sign of that tightening, not a second phenomenon.
:::

**Check yourself.** Why is a regression coefficient attached to $\log\lambda$ in this parameterisation not yet a statement about the mean count?

::: {.callout-tip collapse="true" title="Answer"}
Except at $\nu=1$, $\lambda$ is not $\mathrm{E}(X)$. In the worked example $\lambda=1$ and the mean is about $0.6978$. Multiplying $\lambda$ by a factor changes the mean by an amount that also depends on $\nu$, and that amount is not the same factor.
:::

## Connections
The [Poisson distribution](poisson-distribution.qmd) is the case $\nu=1$. The [negative binomial distribution](negative-binomial-distribution.qmd) can be wider than a Poisson law and cannot be tighter, because it is a mixture of Poisson rates. [Count models beyond the Poisson](count-models-beyond-the-poisson.qmd) sets these families next to a quasi-Poisson variance factor, which rescales standard errors and does not by itself name a probability function. The series $Z(\lambda,\nu)$ is the piece that makes the Conway–Maxwell–Poisson probabilities sum to one when the factorial power is not $1$.
