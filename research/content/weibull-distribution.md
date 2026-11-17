## Lead context
The Weibull distribution is a lifetime law whose shape lets the hazard rise, stay flat, or fall with age.

## Motivating example
A Weibull law with shape $1.5$ and scale $20$ hours has median about $15.66$ hours and mean about $18.05$ hours. At $t=20$ the survival probability is $e^{-1}$ and the hazard is $0.075$ per hour.

## Intuition — Ageing is a power of time
An exponential lifetime has a constant hazard, so it does not age. The Weibull family keeps a simple survival function and lets that hazard be a power of time. Shape above one means wear-out. Shape below one means early failures that then become rarer. Shape one returns the exponential law.{{cite:nist_weibull_handbook}} (§8.1.6.2, failure-rate shapes and the exponential case)

## Definition
**Shape and scale.** In the shape–scale form used here, a lifetime $T$ with shape $k>0$ and scale $\lambda>0$ has survival function $\Pr(T>t)=\exp\{-(t/\lambda)^k\}$ for $t>0$, density $(k/\lambda)(t/\lambda)^{k-1}\exp\{-(t/\lambda)^k\}$, and hazard $(k/\lambda)(t/\lambda)^{k-1}$. The mean is $\lambda\Gamma(1+1/k)$ and the median is $\lambda(\log 2)^{1/k}$. The same law is often written with shape $\gamma$ and characteristic life $\alpha$ in place of $k$ and $\lambda$.{{cite:nist_weibull_handbook}} (§8.1.6.2, reliability, hazard, mean and median)

## Properties
Setting the survival function equal to $1/2$ gives $(t/\lambda)^k=\log 2$, so the median is $\lambda(\log 2)^{1/k}$. At shape $k=1$ the hazard is the constant $1/\lambda$, the mean equals the scale, and the law is exponential.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The survival function equals $1/2$ when $\exp\{-(t/\lambda)^k\}=1/2$, so $(t/\lambda)^k=\log 2$ and $t=\lambda(\log 2)^{1/k}$. At $k=1$ the hazard formula collapses to $1/\lambda$, and $\Gamma(1+1/1)=\Gamma(2)=1$, so the mean equals $\lambda$.{{cite:nist_weibull_handbook}} (§8.1.6.2, median and the exponential case)
:::
:::

## Worked example
Take shape $k=1.5$ and scale $\lambda=20$ hours. The median is $20(\log 2)^{2/3}\approx 15.66$ hours. The mean is $20\Gamma(1+2/3)\approx 18.05$ hours, a little above the median, so the density has a right tail. At the scale time $t=20$ the survival probability is $e^{-1}\approx 0.3679$ and the hazard is $(1.5/20)(20/20)^{0.5}=0.075$ per hour.{{cite:nist_weibull_handbook}} (§8.1.6.2, median, mean, reliability and failure rate)

**Your turn.** Keep the scale at $20$ hours and set the shape to $1$. Find the mean, the median, and the hazard.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $20$ hours. The median is $20\log 2\approx 13.86$ hours. The hazard is the constant $1/20=0.05$ per hour.
:::

For shape $2$ and scale $10$, what is the survival probability at $t=10$?

::: {.callout-tip collapse="true" title="Answer"}
$(10/10)^2=1$, so the survival probability is $e^{-1}\approx 0.3679$. The median is $10\sqrt{\log 2}\approx 8.33$, which is below the scale.
:::

Shape $0.5$ and shape $2$ have the same scale. Which hazard falls with age?

::: {.callout-tip collapse="true" title="Answer"}
Shape $0.5$ is below one, so the hazard $(k/\lambda)(t/\lambda)^{k-1}$ has a negative power of $t$ and falls. Shape $2$ has a positive power and rises.
:::

## Connections
Shape one is the [exponential distribution](exponential-distribution.qmd) with rate $1/\lambda$, the lifetime with the [memoryless property](memoryless-property.qmd). The hazard formula is the general [hazard rate](hazard-rate.qmd) $f(t)/R(t)$ specialised to this survival function. A single shape cannot fall and later rise; a bathtub hazard needs more than one Weibull term. Shape two is the Rayleigh law for the length of a bivariate normal vector with independent coordinates of mean zero and equal variance.{{cite:nist_weibull_handbook}} (§8.1.6.2, exponential and Rayleigh cases)

::: {.callout-tip collapse="true" title="Answer"}
$(10/10)^2=1$, so the survival probability is $e^{-1}\approx 0.3679$. The median is $10\sqrt{\log 2}\approx 8.33$, which is below the scale.
:::
