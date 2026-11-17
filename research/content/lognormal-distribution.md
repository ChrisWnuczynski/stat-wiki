## Motivating example

A repair bill can rise by a succession of percentage changes rather than a fixed number of dollars. Multiplicative changes add after logarithms are taken. If their combined log value is well described by a normal distribution, the original positive amount has a lognormal distribution. This model offers a direct way to calculate probabilities for high bills while keeping the distinction between a typical bill and the arithmetic average.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Moments)

## Intuition

Write $X=e^{\mu+\sigma Z}$ with $Z\sim N(0,1)$. The number $e^\mu$ is the median and a scale on the original measurement axis; $\sigma$ controls how spread and right-skewed the measurements are. Exponentiation turns a symmetric normal curve on the log axis into a positively skewed curve on the original axis. A high positive log deviation multiplies the measurement, whereas a comparably low log deviation cannot push it below zero. This asymmetry explains why the mean $e^{\mu+\sigma^2/2}$ is above the median $e^\mu$ whenever $\sigma>0$.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition, Distribution Functions and Moments)

The notation $\operatorname{Lognormal}(\mu,\sigma^2)$ refers to the mean and variance of $\log X$, not the mean and variance of $X$. In particular, setting $\mu=0$ does not make the original-scale mean zero. The two plots in the infobox use $\mu=0$ and $\sigma=0.6$: their PDF's long right tail and their CDF's slow approach to one both arise from that transformation. {{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Moments)

## Definition

Equivalently, $X$ is lognormal exactly when $Y=\log X$ is normal with mean $\mu$ and variance $\sigma^2$, with $\sigma>0$. For $x>0$, the CDF is $F(x)=\Phi((\log x-\mu)/\sigma)$; below zero it is zero. Its $p$-quantile is $\exp\{\mu+\sigma\Phi^{-1}(p)\}$. These formulas let a question about a positive threshold be answered on the standard-normal scale. The $1/x$ in the density is the Jacobian of the logarithm; omitting it does not give a properly transformed normal density.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Distribution Functions)

## Properties

The mode $e^{\mu-\sigma^2}$ lies below the median $e^\mu$, which lies below the mean $e^{\mu+\sigma^2/2}$ for positive $\sigma$. These are three different descriptions of a right-skewed distribution: the highest point of the density, its halfway probability point, and its average. At fixed $\sigma$, multiplying $X$ by a positive constant simply adds its logarithm to $\mu$ and scales all three locations by that constant.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Distribution Functions and Moments)

All real power moments exist: $\mathbb E(X^r)=e^{r\mu+r^2\sigma^2/2}$ for real $r$. Yet the ordinary moment-generating function of $X$ is infinite at every positive argument. Thus a collection of finite moments does not by itself imply a finite MGF near zero. The lognormal right tail is light enough for every power of $X$ to be integrable, but too heavy for $e^{tX}$ to be integrable when $t>0$. {{cite:siegrist2022_lognormal_distribution}} (§5.12, Moments)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $Y=\log X\sim N(\mu,\sigma^2)$. The inverse transformation is $x=e^y$ and $dy/dx=1/x$, so the normal density at $\log x$ multiplied by $1/x$ is the displayed lognormal density. Monotonicity of the logarithm gives $\Pr(X\leq x)=\Pr(Y\leq\log x)=\Phi((\log x-\mu)/\sigma)$ and its inverse gives the quantile formula. At $p=1/2$, $\Phi^{-1}(p)=0$, proving the median. Differentiating $\log f(x)$ yields $-1/x-(\log x-\mu)/(\sigma^2x)$, which vanishes at $x=e^{\mu-\sigma^2}$ and changes from positive to negative there, proving the mode.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Distribution Functions)

The normal exponential-moment formula gives $\mathbb E(X^r)=\mathbb E(e^{rY})=e^{r\mu+r^2\sigma^2/2}$. Setting $r=1,2$ gives the mean and, after subtracting the square of the mean, $\operatorname{Var}(X)=(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$. To see why the MGF is infinite for $t>0$, express $\mathbb E(e^{tX})$ as an integral over $y$: its positive integrand contains $\exp\{t e^y-(y-\mu)^2/(2\sigma^2)\}$. The $t e^y$ term eventually dominates the negative quadratic, so the integral diverges. {{cite:siegrist2022_lognormal_distribution}} (§5.12, Moments)
:::
:::

## Related distributions

Taking logarithms maps this family back to the normal family, but it does not make a lognormal model the same as a gamma GLM with a log link. Both can describe positive skewed responses and variance proportional to the squared mean in particular parameterizations, while their distributional tails and likelihoods differ. If independent $X_1$ and $X_2$ are lognormal, their product is lognormal because $\log(X_1X_2)=\log X_1+\log X_2$ is a sum of independent normals. Independence matters: $X_1=e^Z$ and $X_2=e^{-Z}$ each have a nondegenerate lognormal distribution, but their product is always one.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Related Distributions)

## Statistical inference

For iid positive observations, fit the normal model to $Y_i=\log X_i$ when its assumptions are credible. Exponentiating the fitted log mean estimates the original-scale median under that model. An original-scale mean estimate instead needs the log variance as well, through $e^{\mu+\sigma^2/2}$. A mean prediction without this adjustment is systematically below the lognormal mean, although it can be a useful estimate of a typical or median outcome. Inspect the log observations for strong non-normality and investigate zeros before applying the transformation.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Moments)

## Generating random samples

Generate a normal $Z$ and return $e^{\mu+\sigma Z}$. Repeated draws can be checked against the theoretical median $e^\mu$ and mean $e^{\mu+\sigma^2/2}$, but a small simulation may produce an unstable sample mean when the right tail is pronounced. If a software function expects the scale parameter on the original axis, supply $e^\mu$, not $\mu$; its shape argument corresponds to $\sigma$.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Moments)

## Worked example

Suppose repair costs follow a lognormal law with $\mu=\log100$ and $\sigma=0.4$, with costs measured in dollars. The median is $e^\mu=100$, the mean is $100e^{0.08}\approx108.33$, and the mode is $100e^{-0.16}\approx85.21$. For a cost over $150$, standardize its logarithm: $z=\log(150/100)/0.4\approx1.0137$. The chance is $1-\Phi(1.0137)\approx0.1554$. The 90th percentile is $100\exp\{0.4\Phi^{-1}(0.9)\}\approx166.97$, using $\Phi^{-1}(0.9)\approx1.2816$. The median, mean and high quantile answer different planning questions; quoting only a "typical" cost would conceal the upper-tail risk.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Distribution Functions and Moments)

**Your turn.** Suppose $\mu=\log50$ and $\sigma=0.2$. Find the median, mean and mode, and the probability that $X$ exceeds $50e^{0.2}$.

::: {.callout-tip collapse="true" title="Answer"}
The median is $50$, the mean is $50e^{0.02}\approx51.01$, and the mode is $50e^{-0.04}\approx48.04$. The threshold is one log-scale standard deviation above $\mu$, so $\Pr(X>50e^{0.2})=\Pr(Z>1)\approx0.1587$. That last probability is independent of $\mu$ because the threshold was specified relative to it.
:::

## Common misconceptions

The parameters $\mu$ and $\sigma$ are not the original-scale mean and standard deviation. Exponentiating $\mu$ gives the median, not the mean. The family is not closed under addition merely because independent normal variables are: addition of positive amounts does not become addition of their logarithms. A log link in a regression model also does not assert lognormal errors; the link describes a conditional mean, while a lognormal law describes the whole conditional response distribution.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition, Moments and Related Distributions)

## Assumptions and limits — When the lognormal model fails

A measured amount that can be zero with positive probability, such as a claim that is zero for most customers, cannot follow a pure lognormal law on all observations: this distribution has support only above zero. A mixture of two groups with very different normal log means generally has a two-component normal mixture after logging, not one normal law. And recording every value below a detection threshold as the threshold itself creates a point mass at that threshold, which the continuous lognormal density cannot describe. The worked tail probabilities require the entire fitted log-scale normal model, not merely positive data.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Distribution Functions)

## Connections

The lognormal law is a change of variables from the [normal distribution](normal-distribution.qmd), so its Jacobian explains the density and its normal quantiles give probabilities. Its variance is proportional to its squared mean at fixed $\sigma$: $\operatorname{Var}(X)/\mathbb E(X)^2=e^{\sigma^2}-1$. This resembles the mean–variance relation in a gamma model, while the families remain different. The lognormal also connects multiplicative errors to additive normal errors on the log scale.{{cite:siegrist2022_lognormal_distribution}} (§5.12, Definition and Moments)

## History

Early study of the lognormal form includes Galton and McAlister in 1879, who used products of positive variables and logarithms. Kapteyn and van Uven later estimated parameters graphically. This history explains why a distribution generated by multiplication became a standard companion to the normal law.{{cite:dodge2008}} (p. 321, Lognormal Distribution)
