## Motivating example
A survey estimates mean household spending. Individual spending is skewed, so an exact normal-sample argument is doubtful, but a sufficiently informative independent sample can still support an approximately normal sample mean. The practical question is whether the standard error estimates the variability of that mean well enough for its interval to have useful coverage. Sample size alone cannot repair dependence, selection bias, or an infinite population variance.{{cite:openintro2019}} (§§5.1–5.2, sampling distributions and confidence intervals)

## Intuition — A pivot emerges as the sample grows
For iid observations with mean $\mu$ and $0<\sigma^2<\infty$, the central limit theorem gives $\sqrt n(\overline X-\mu)/\sigma\Rightarrow N(0,1)$. The sample variance $s^2=(n-1)^{-1}\sum(X_i-\overline X)^2$ converges in probability to $\sigma^2$. Consequently replacing $\sigma$ by $s$ does not alter the limiting normal law. This is a statement about a sequence of experiments as $n$ grows; it supplies no universal cutoff at which every skewed population becomes harmless.{{cite:durrett2019}} (§§2.4, 3.4.1, strong law and iid central limit theorem)

## Properties — Coverage and precision
The event that $\overline X\pm z_{1-\alpha/2}s/\sqrt n$ covers $\mu$ is exactly
$$\left|\frac{\sqrt n(\overline X-\mu)}s\right|\le z_{1-\alpha/2}.$$
Its probability tends to $1-\alpha$, because the limiting normal distribution is continuous at both endpoints. The interval is random before the observations; after observation its endpoints are fixed. Frequentist coverage concerns repetition of the sampling procedure, rather than a probability distribution assigned to the fixed parameter.{{cite:openintro2019}} (§5.2, interpreting a confidence interval)

For independent finite-variance observations, $s^2=n(n-1)^{-1}\{n^{-1}\sum X_i^2-\overline X^2\}$ converges to $E(X^2)-\mu^2$. Combining this with the central limit theorem proves the studentized limit by Slutsky's principle. If observations are correlated, $\operatorname{Var}(\overline X)$ contains covariance terms, so $s/\sqrt n$ generally estimates the wrong scale. If the variance is infinite, the stated normal limit can fail altogether.{{cite:durrett2019}} (§§2.4, 3.2, 3.4)

For a desired half-width $d$, a planning approximation using a provisional standard deviation $\sigma_0$ is $n\ge(z_{1-\alpha/2}\sigma_0/d)^2$, rounded upward. It assumes that the sampling design and variability estimate are credible. Four times as many observations halves the nominal half-width. Raising confidence increases the normal quantile and widens the interval at a fixed sample size.{{cite:openintro2019}} (§5.2, margin of error)

## Worked example — Fuel spending and a planning calculation
For $n=51$, mean $1136$ and sample standard deviation $178$, the estimated standard error is $24.924985$. Using the rounded normal multiplier $1.96$ gives a half-width $48.852972$ and endpoints $1087.147028$ and $1184.852972$. Rounded to whole dollars these are $(1087,1185)$. With the exact $t_{50}$ quantile $2.008559$, the endpoints are approximately $(1085.94,1186.06)$. Exact $t$ coverage requires a normal population; its small numerical difference from the normal interval does not establish that assumption.{{cite:openintro2019}} (§7.1, one-sample means and the t distribution)

Using $\sigma_0=178$ and seeking a half-width of $25$ dollars at the same rounded normal multiplier requires $n\ge194.74760704$, hence $195$ observations. This is a planning value conditional on the provisional standard deviation, rather than a promise about the future realized width.

**Your turn.** A sample has $n=100$, $\overline x=20$ and $s=5$. Find the normal-based 95% interval using $1.96$. How many observations give half its nominal margin at the same $s$?

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $0.5$, so the interval is $20\pm0.98=(19.02,20.98)$. A sample of $400$ gives half the nominal margin if the same variability estimate applies.
:::

## Common misconceptions
A large sample can estimate a biased sampling mechanism very precisely. A histogram helps inspect skewness and extreme observations, but cannot establish independence or representativeness. An interval for a population mean also differs from a prediction interval for a future household: individual spending keeps its population variability even as uncertainty about the mean shrinks.{{cite:openintro2019}} (§§1.3, 5.2)

## Statistical use — A different sample mean for every scientific target
A transformation can improve the shape of a distribution while changing the parameter being estimated. Averaging log spending estimates $E(\log X)$, rather than $\log E(X)$. Exponentiating an interval for the first target does not generally create an interval for the arithmetic population mean. The transformation and the target must therefore be selected together. Likewise, deleting unusually high households changes the estimand unless a principled sampling or contamination model explains the deletion.{{cite:openintro2019}} (§§5.1–5.2, sampling variability and interval interpretation)

The finite-variance condition is substantive. Consider a population concentrated mostly at small values with a very small probability of an enormous value. A large realized sample can miss that rare component and give a stable-looking mean and small sample standard deviation. The central limit theorem is a limiting statement for a fixed population; it does not guarantee a good approximation uniformly over every possible finite-variance population at a chosen finite size. Diagnostics, subject knowledge about tails and the sampling design therefore remain important when using a normal approximation.{{cite:durrett2019}} (§3.4.1, iid central limit theorem and its hypotheses)
