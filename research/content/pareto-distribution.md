## Motivating example
A claim size that is usually a little above a minimum, and occasionally enormous, is a poor match for a distribution whose variance is tied to its mean by a fixed factor. The Pareto law puts a power-law tail on values above a minimum $x_m$. The tail parameter decides whether the mean exists, and whether the variance exists, before any sample average is interpreted.{{cite:scipy_pareto2026}} (Notes, density $b/x^{b+1}$ for $x\ge 1$)

## Intuition
On the unit minimum, the density $b/x^{b+1}$ falls as a power, not as an exponential. A larger shape $b$ pulls probability toward the minimum. Scaling the minimum to $x_m$ stretches the axis and multiplies the density by $1/x_m$ in the usual way, which produces $\alpha x_m^\alpha/x^{\alpha+1}$ with $\alpha=b$. The survival probability is the remaining power $(x_m/x)^\alpha$. Moments are integrals of that tail, and the integral at infinity converges only when the power is steep enough.{{cite:scipy_pareto2026}} (Notes, standardised density and the scale parameter)

## Definition
SciPy's standardised Pareto density is $f(x)=b/x^{b+1}$ for $x\ge 1$ and $b>0$, which is the classical Pareto law with minimum $1$ and tail parameter $b$. The call `pareto.pdf(x, b, loc, scale)` is the density of $\mathrm{scale}\cdot Y+\mathrm{loc}$ where $Y$ has the standardised law. With $\mathrm{loc}=0$ and $\mathrm{scale}=x_m$, that is the law of $x_m Y$, density $\alpha x_m^\alpha/x^{\alpha+1}$ for $x\ge x_m$ and $\alpha=b$. Putting the minimum in `loc` instead of `scale` shifts a unit-minimum variable and is a different distribution.{{cite:scipy_pareto2026}} (Notes, `loc` and `scale`)

## Properties
For $x\ge x_m$, $\Pr(X>x)=(x_m/x)^\alpha$. The mean is $\alpha x_m/(\alpha-1)$ when $\alpha>1$, and is infinite when $\alpha\le 1$. The second moment is finite only for $\alpha>2$, and then
\[
\operatorname{Var}(X)=\frac{\alpha x_m^2}{(\alpha-1)^2(\alpha-2)}.
\]
At $\alpha=2.5$ and $x_m=1$ the mean is $5/3\approx 1.6667$ and the variance is $20/9\approx 2.2222$. At $\alpha=1.5$ and $x_m=1$ the mean is $1.5/0.5=3$ and the variance is infinite, because the factor $\alpha-2$ in the denominator has changed sign and the integral that would have produced it diverges.{{cite:scipy_pareto2026}} (Notes, shape $b$)

The median of the unit-minimum law solves $(1/m)^\alpha=1/2$, so $m=2^{1/\alpha}$. At $\alpha=2.5$ the median is $2^{0.4}\approx 1.3195$, below the mean $1.6667$. The mode is the minimum. The distribution is skewed right whenever the mean exists.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Integrate $\alpha x_m^\alpha u^{-\alpha-1}$ from $x$ to infinity, for $x\ge x_m$ and $\alpha>0$. The antiderivative is $-x_m^\alpha u^{-\alpha}$, and the boundary term at infinity vanishes, leaving $(x_m/x)^\alpha$.{{cite:scipy_pareto2026}} (Notes, the power in the standardised density)

For the mean, write $\mathbb E(X)=\int_{x_m}^\infty\Pr(X>t)\,dt$ plus the lower endpoint contribution already accounted for by starting the integral at $x_m$ when the support begins there: $\mathbb E(X)=x_m+\int_{x_m}^\infty(x_m/t)^\alpha\,dt$. The integral equals $x_m/(\alpha-1)$ when $\alpha>1$ and diverges when $\alpha\le 1$. Adding $x_m$ gives $\alpha x_m/(\alpha-1)$. The second-moment integral $\mathbb E(X^2)=2\int_{x_m}^\infty t\Pr(X>t)\,dt$ converges only for $\alpha>2$, and substituting the survival produces the variance formula. At $\alpha=2.5$ and $x_m=1$, $\alpha/(\alpha-1)=5/3$ and $\alpha/[(\alpha-1)^2(\alpha-2)]=2.5/(2.25\times 0.5)=20/9$.{{cite:scipy_pareto2026}} (Notes, shape parameter)
:::
:::

## Related distributions
The standardised law is the case $x_m=1$. Multiplying by $x_m$ is the scale change SciPy implements with `scale`, not with `loc`. An exponential tail is lighter than every Pareto tail: $e^{-\lambda x}x^{\alpha}\to 0$ as $x\to\infty$ for every fixed $\alpha$ and every $\lambda>0$. The Pareto survival is a power, so $\log\Pr(X>x)$ is linear in $\log x$ with slope $-\alpha$. An exponential survival is linear in $x$ on the log-survival scale. A plot that is straight against $\log x$ is the power-law pattern, not the exponential one.{{cite:scipy_pareto2026}} (Notes, support $x\ge 1$ before scaling)

## Statistical inference
The sample mean estimates $\alpha x_m/(\alpha-1)$ only when $\alpha>1$. If $\alpha\le 1$ the population mean is infinite and the sample mean grows with the largest observations rather than settling. If $1<\alpha\le 2$ the mean exists and the variance does not, so the usual standard-error formula $s/\sqrt n$ does not have a finite population counterpart. A tail parameter estimated from values above a chosen threshold is a model for that threshold, not automatically a model for the body of the distribution below it.{{cite:scipy_pareto2026}} (Notes, $b>0$ and the power-law density)

## Generating random samples
Draw $U$ uniformly on $(0,1)$ and set $X=x_m(1-U)^{-1/\alpha}$. Then $\Pr(X>x)=\Pr\bigl(U>1-(x_m/x)^\alpha\bigr)=(x_m/x)^\alpha$ for $x\ge x_m$. SciPy's `pareto.rvs(b, scale=x_m)` uses shape $b=\alpha$ and scale $x_m$. The call `pareto.rvs(b, loc=x_m)` shifts the unit-minimum law by $x_m$ and has support $[1+x_m,\infty)$ with a different density. The same inversion is what `ppf` does for the standardised law, followed by multiplication by `scale`. A simulation check that compares the sample variance with $20/9$ is a check for $\alpha=2.5$. It is not a check for $\alpha=1.5$, which has no finite variance to match.{{cite:scipy_pareto2026}} (Notes, `loc` and `scale`; Methods, `rvs` and `ppf`)

## Worked example
Take $\alpha=2.5$ and $x_m=1$. The mean is $2.5/1.5=5/3\approx 1.6667$. The variance is $20/9\approx 2.2222$. The median is $2^{1/2.5}=2^{0.4}\approx 1.3195$. The survival at $2$ is $2^{-2.5}=1/(4\sqrt 2)\approx 0.1768$. Fewer than one draw in five exceeds twice the minimum, while the mean sits only modestly above the median: the tail is heavy enough to lift the mean, and with $\alpha>2$ it is not heavy enough to destroy the variance.{{cite:scipy_pareto2026}} (Notes, standardised Pareto with shape $b$)

Now take $\alpha=1.5$ and the same minimum. The mean formula gives $3$. The variance formula's factor $\alpha-2=-0.5$ is a signal to stop: the second-moment integral diverges, and there is no finite variance to quote.{{cite:scipy_pareto2026}} (Notes, the shape must be read before a moment)

**Your turn.** For $\alpha=4$ and $x_m=2$, find the mean and $\Pr(X>4)$.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $4\times 2/(4-1)=8/3\approx 2.6667$. The survival is $(2/4)^4=1/16=0.0625$. Both moments exist, because $4>2$.{{cite:scipy_pareto2026}} (Notes, shape and scale)
:::

**Check yourself.**

1. Does the unit-minimum Pareto with shape $1$ have a finite mean?

::: {.callout-tip collapse="true" title="Answer"}
No. The integral $\int_1^\infty t^{-1}\,dt$ diverges, which is the $\alpha=1$ case of the mean integral. The formal ratio $\alpha/(\alpha-1)$ is undefined at $\alpha=1$.{{cite:scipy_pareto2026}} (Notes, power $b+1$ in the denominator of the density)
:::

2. Which SciPy call draws a Pareto random variable with minimum $5$ and shape $3$?

::: {.callout-tip collapse="true" title="Answer"}
`pareto.rvs(3, scale=5)`. The shape is the first argument and the minimum is `scale` when `loc` stays $0$. Using `loc=5` shifts the support to $[6,\infty)$.{{cite:scipy_pareto2026}} (Notes, `loc` and `scale`)
:::

3. At $\alpha=2.5$ and $x_m=1$, which is larger, the median or the mean?

::: {.callout-tip collapse="true" title="Answer"}
The mean, $5/3\approx 1.6667$, is larger than the median $2^{0.4}\approx 1.3195$. The right tail pulls the mean above the median.{{cite:scipy_pareto2026}} (Notes, shape $b$)
:::

## Common misconceptions
The second parameter in the classical formula is a tail index, not a rate. Increasing $\alpha$ thins the tail and, when the mean exists, pulls the mean toward $x_m$. Increasing a Poisson rate does the opposite to its mean. The two parameters are not interchangeable.{{cite:scipy_pareto2026}} (Notes, $b$ is a shape)

`loc` is not the minimum. SciPy's notes define the standardised support as $x\ge 1$ and then apply an affine transformation. The minimum of $x_m Y$ is $x_m$, implemented as `scale`. A location shift moves the left endpoint to $1+\mathrm{loc}$ only if `scale` stays $1$.{{cite:scipy_pareto2026}} (Notes, standardised form)

A finite sample mean is not evidence that the population mean is finite. With $\alpha=1.5$ the population mean is $3$ and the population variance is infinite; with $\alpha=0.5$ the population mean is infinite and a sample mean is still a finite number. The parameter, not the calculator, decides which moment exists.{{cite:scipy_pareto2026}} (Notes, $b>0$)

## Assumptions and limits — When the power-law tail is the wrong description
The support starts at $x_m$ and does not include values below it. A measurement of $0$, or a negative loss, is not a draw from this law. The survival formula $(x_m/x)^\alpha$ is for a single threshold and independent draws from that law. A threshold chosen after looking at the sample, a hard cap on the largest recordable value, or dependence between successive losses changes the tail that the formula describes. And $\alpha\le 2$ is not a minor caveat about a standard error: the usual $s/\sqrt n$ standard error is a statement about a finite variance, which this distribution then does not have.{{cite:scipy_pareto2026}} (Notes, support and the power)

## Connections
The [exponential distribution](exponential-distribution.qmd) is the light-tailed waiting-time law whose survival is exponential in $x$ rather than in $\log x$. A [sample mean](expectation.qmd) estimates the Pareto mean only for $\alpha>1$. The scale convention in software is the difference between `scale` and `loc` in `scipy.stats.pareto`.{{cite:scipy_pareto2026}} (Notes, `scale`)
