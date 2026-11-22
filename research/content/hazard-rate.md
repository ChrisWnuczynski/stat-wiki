## Motivating example

A device that has survived a year is a different risk population from a newly installed device. A lifetime density averages over devices that fail at every age; a hazard divides the local failure probability by the fraction still alive. The distinction is central when failure rates change with age.{{cite:siegrist_weibull2022}} (“The Basic Weibull Distribution”, failure-rate formula and its derivation)

## Definition — Conditional risk per unit time

For an absolutely continuous nonnegative lifetime, write $S(t)=P(T>t)$. At a point where the density and the relevant derivative exist, with $S(t)>0$,
$$
h(t)=\lim_{\Delta\downarrow0}\frac{P(t<T\le t+\Delta\mid T>t)}{\Delta}
=\frac{f(t)}{S(t)}.
$$
Hazard has units of inverse time and may exceed one. The probability over a finite interval is instead
$$
P(t<T\le t+\Delta\mid T>t)
=1-\exp\{-H(t+\Delta)+H(t)\},
\quad H(t)=\int_0^t h(u)\,du.
$$
The identity also describes the first-arrival lifetime of a nonhomogeneous Poisson process with deterministic rate $h$.{{cite:pishro_nik2014}} (§11.1.4, Poisson law for the increment $N(t+s)-N(t)$){{cite:siegrist_nhpp2022}} (“Arrival Times and Time Change”, first-arrival density and reliability formulas)

## Properties — Recovering the lifetime law

Since $S'=-f$, the derivative of $\log S$ equals $-h$. If $S(0)=1$, integration gives $S=e^{-H}$ and $f=he^{-H}$. For a proper lifetime with no probability of surviving forever, $H(t)$ must tend to infinity as $t\to\infty$. If that integral is finite, $e^{-H(\infty)}>0$ is the probability of an infinite lifetime. These statements follow directly from the survival identity and its limit.{{cite:siegrist_nhpp2022}} (“Arrival Times and Time Change”, first-arrival density and reliability formulas)

The Weibull family $S(t)=\exp[-(t/a)^k]$, for scale $a>0$ and shape $k>0$, has hazard $kt^{k-1}/a^k$. It decreases for $k<1$, is constant for $k=1$, and increases for $k>1$. Changing time units changes the numerical hazard, while the probability of the corresponding time interval stays the same.{{cite:siegrist_weibull2022}} (“The General Weibull Distribution”, reliability and failure-rate formulas)

## Worked example

Take $h(t)=2t$ per year for $t$ measured in years. Then $H(t)=t^2$ and $S(t)=e^{-t^2}$. At age one the hazard is $2$ per year, but the probability of failing during the next tenth of a year is
$$
1-\frac{S(1.1)}{S(1)}=1-e^{-0.21}\approx0.18942.
$$
The local linear approximation is $h(1)\times0.1=0.2$. It is only an approximation; both the growing hazard and the shrinking survivor population affect the exact interval probability. The median is $\sqrt{\log2}\approx0.83255$ years, and the mean is $\sqrt\pi/2\approx0.88623$ years.{{cite:siegrist_weibull2022}} (“The Basic Weibull Distribution”, quantile formula and mean formula)

**Your turn.** What is the probability of surviving from age one to age two, given survival to age one?

::: {.callout-tip collapse="true" title="Answer"}
It is $S(2)/S(1)=e^{-4}/e^{-1}=e^{-3}\approx0.04979$. It is a conditional survival probability, whereas $e^{-4}$ is survival from installation to age two.
:::

## Check yourself

### [Survival from the hazard](../questions/ex-prob-hazard-survival.qmd) {#self-check-ex-prob-hazard-survival}

Why is the integration constant zero in $\log S(t)=-H(t)$? Use this relation to find $P(T\le1)$ when $h(t)=2t$, and determine the hazard of a Weibull lifetime with shape $k=1$ and scale $a>0$.

::: {.callout-tip collapse="true" title="Answer"}
An absolutely continuous nonnegative lifetime has $P(T=0)=0$, so $S(0)=1$ and $\log S(0)=0$. An atom at zero would require its own initial survival factor.

For $h(t)=2t$, the cumulative hazard to 1 is 1, so $P(T\le1)=1-e^{-1}\approx 0.632121$. The Weibull hazard is $kt^{k-1}/a^k$; at $k=1$ this is the constant $1/a$.
:::

### [Five years of a component](../questions/ex-prob-component-five-years.qmd) {#self-check-ex-prob-component-five-years}

Find survival through five years for the constant hazard $0.1$ per year. For a component with constant hazard $0.2$ per year, find survival through ten years and the median lifetime.

::: {.callout-tip collapse="true" title="Answer"}
$H(5)=0.5$ and $S(5)=e^{-0.5}\approx0.60653$.

With hazard $0.2$ per year, the cumulative hazard to ten years is 2, so $S(10)=e^{-2}\approx 0.135335$. The median solves $0.2t=\log 2$, hence $t=(\log 2)/0.2\approx 3.465736$ years.
:::
### Paths and cuts of the bridge {#self-check-ex-prob-bridge-paths}

[Paths and cuts of the bridge](../questions/ex-prob-bridge-paths.qmd)

The bridge has minimal path sets $\{1,4\}$, $\{2,5\}$, $\{1,3,5\}$ and $\{2,3,4\}$. Write the structure function by the path formula, and expand it far enough to see the four path monomials. Say how the same system is drawn as a series arrangement of parallel modules, and as a parallel arrangement of series modules, if components may be duplicated in the drawing.

:::::::: {.callout-tip collapse="true" title="Answer"}

By the path formula,

$$
\varphi(\mathbf x)=1-(1-x_1x_4)(1-x_2x_5)(1-x_1x_3x_5)(1-x_2x_3x_4).
$$

Expanding, the terms of degree two and three are $x_1x_4+x_2x_5+x_1x_3x_5+x_2x_3x_4$, the four path monomials, followed by products of pairs of paths with alternating signs; reducing $x_i^2=x_i$ gives the polynomial in the chapter.

The path formula draws the bridge as four series branches, $1$–$4$, $2$–$5$, $1$–$3$–$5$ and $2$–$3$–$4$, placed in parallel. The cut formula draws it as four parallel modules, $\{1,2\}$, $\{4,5\}$, $\{1,3,5\}$ and $\{2,3,4\}$, placed in series. Both drawings repeat components, which is why the bridge itself is not a series–parallel system.

::::::::
