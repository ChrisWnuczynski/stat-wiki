## Lead context
The Cauchy law is symmetric about its location. That location is the median and the mode, and the mean and the variance are undefined.{{cite:dodge2008}} (p. 60)

## Motivating example
A standard Cauchy observation is as likely to fall outside the interval from minus one to one as inside it, yet the average of many such observations need not settle.{{cite:dodge2008}} (p. 60)

## Intuition — Heavy tails without a mean
The density $1/[\pi(1+x^{2})]$ decays only like $1/x^{2}$. That is heavy enough that $\int |x|f(x)\,dx$ diverges, so the expectation is not defined, and heavy enough that the sample average is not pulled toward a centre by the law of large numbers. The distribution is nevertheless symmetric about its location, and that location is the median. The first and third quartiles sit at one scale unit either side of the location: for the standard law they are $-1$ and $1$, and the probability between them is exactly $1/2$. The tails beyond those quartiles are not a small remainder.{{cite:dodge2008}} (p. 60)

## Definition
In the location-scale parameterisation, $X\sim\operatorname{Cauchy}(x_0,\gamma)$ has density $\gamma/[\pi((x-x_0)^{2}+\gamma^{2})]$ and distribution function $1/2+\arctan((x-x_0)/\gamma)/\pi$. The same law is also written with location $\alpha$ and dispersion $\theta$, so $\gamma$ here is his $\theta$. The median and the mode are the location. The quartiles are $x_0\pm\gamma$. The mean and the variance are undefined for every $\gamma>0$. Setting the degrees of freedom of a Student $t$ law equal to $1$ recovers the standard Cauchy density, which is the case $\alpha=0$, $\theta=1$.{{cite:dodge2008}} (p. 60)

The quantile function inverts the distribution function in closed form: the $p$-quantile is $x_0+\gamma\tan(\pi(p-1/2))$. That is why a uniform draw $U$ produces a Cauchy draw by $x_0+\gamma\tan(\pi(U-1/2))$. Draw $U$ uniformly on the open interval $(0,1)$: only the exact endpoints $0$ and $1$ are excluded, where the tangent is undefined. The default R `runif()` call never returns either endpoint, so no draw needs treatment there. A generator on $[0,1)$, such as Python's `random.random()`, can return an exact $0$: discard and redraw that draw, not nearby values. Do not push the draw away from the endpoints: rejecting near-endpoint draws, or clipping them into a narrower range, changes the heavy tails. For the standard law, discarding every $U$ outside $[0.01, 0.99]$ would make $|X|>\tan(0.49\pi)$ impossible — that cutoff is about $31.8205$ — although those outcomes carry probability exactly $0.02$ under the original law.

## Worked example
For a standard Cauchy random variable, $F(5)-F(-5)=2\arctan(5)/\pi$. Therefore
$$
P(|X|>5)=1-\frac{2\arctan(5)}{\pi}\approx 0.1257.
$$
About one observation in eight falls outside $[-5,5]$, even though half the probability already sits in $[-1,1]$. A normal law with any finite variance puts far less probability that far out. The Cauchy calculation uses only the distribution function; it does not require a mean.

**Your turn.** For location $2$ and scale $3$, state the median and the two quartiles.

::: {.callout-tip collapse="true" title="Answer"}
The median is $2$. The quartiles are $2-3=-1$ and $2+3=5$. They are the location plus or minus the scale, the same rule $\alpha\pm\theta$.
:::

**Check yourself.** A standard Cauchy sample of size $1$ is observed at $20$. Explain why the sample average, which is $20$, is not an estimate of a mean.

::: {.callout-tip collapse="true" title="Answer"}
The standard Cauchy law has no finite mean. The number $20$ is the sample median of a one-point sample, and it is a draw from a distribution whose centre, in the sense of the median, is $0$. Repeating the experiment does not produce averages that converge to $0$, because there is no expectation for them to converge to.
:::

**Check yourself.** The $t$ law with one degree of freedom and the standard Cauchy law are the same density. What happens to the $t$ variance formula $\nu/(\nu-2)$ at $\nu=1$?

::: {.callout-tip collapse="true" title="Answer"}
The formula requires $\nu>2$. At $\nu=1$ it is not applicable: the denominator is negative and the moment does not exist. That matches the Cauchy fact that the variance is undefined.
:::

## Connections
The [Student $t$ distribution](student-t-distribution.qmd) contains the standard Cauchy law at one degree of freedom, and its variance formula applies only for more than two degrees of freedom. The [normal distribution](normal-distribution.qmd) has a finite mean and variance, so sample averages from a normal population do settle; the Cauchy law is the standard illustration that a symmetric unimodal density need not grant that conclusion.{{cite:dodge2008}} (p. 60)
