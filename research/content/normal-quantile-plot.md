## Lead context
A normal quantile plot sets ordered observations against the normal scores they would have if the sample were exactly normal, so a straight line supports a normal shape and a curve argues against it.

## Motivating example
For $n=4$ the plotting positions $i/5$ are $0.2$, $0.4$, $0.6$ and $0.8$, with standard normal scores $-0.842$, $-0.253$, $0.253$ and $0.842$. Observations $8$, $9$, $11$ and $16$ are compared with the line for a normal sample of mean $10$ and standard deviation $2$.

## Intuition — Order on the vertical axis, normal scores on the horizontal
Sort the sample as $x_{(1)}\le\cdots\le x_{(n)}$. One plotting position gives the $i$th point the standard normal quantile of $i/(n+1)$. If the sample really is standard normal, those points fall near the line of slope one through the origin. If the sample is normal with mean $\mu$ and standard deviation $\sigma$, the same scores line up near $x=\mu+\sigma z$ instead. Tilt is a change of scale. Curvature is a change of shape.{{cite:dodge2008}} (p. 437, ordering and the reference quantiles)

## Definition — Sample quantiles against a reference
Arrange the data in increasing order and plot each ordered value against the standard normal quantile of $i/(n+1)$. The construction is a probability plot: one axis is the sample and the other is a theoretical distribution. A two-sample quantile–quantile plot, by contrast, plots the quantiles of one data set against the quantiles of another. When those two sets share a distribution, the points fall near a $45$-degree line. A pure shift of location moves that line up or down without bending it.{{cite:dodge2008}} (p. 437, the two construction steps){{cite:nist_qq_plot}} (§1.3.3.24, probability plot and the 45-degree line)

## Worked example
For $n=4$ the positions $i/5$ are $0.2$, $0.4$, $0.6$ and $0.8$. Their standard normal scores, to three decimals, are $-0.842$, $-0.253$, $0.253$ and $0.842$. A normal sample with mean $10$ and standard deviation $2$ would sit near $8.32$, $9.49$, $10.51$ and $11.68$. The observations $8$, $9$, $11$ and $16$ match the lower part of that line and then place the largest point at $16$ rather than about $11.68$. The plot bends up at the right: a long right tail. The extreme points are also the most variable, so one unusual value can bend a plot of only four points.{{cite:dodge2008}} (p. 437, ordered data and reference quantiles)

**Your turn.** For $n=3$ the positions $i/4$ are $0.25$, $0.5$ and $0.75$, with normal scores $-0.674$, $0$ and $0.674$. Where would a normal sample with mean $5$ and standard deviation $2$ sit, and what does the sample $3$, $5$, $9$ do at the top?

::: {.callout-tip collapse="true" title="Answer"}
The reference points are $5+2(-0.674)=3.65$, $5$, and $5+2(0.674)=6.35$. The sample matches the lower two places roughly and puts $9$ well above $6.35$, so the right tail is long.
:::

## Connections
The horizontal coordinates are quantiles of the [normal distribution](normal-distribution.qmd). A two-sample quantile plot answers whether two batches share a shape, including a shift of location or a change of scale. The ordered values are [sample quantiles](sample-quantile.qmd). Residual plots from a regression use the same picture to ask whether the errors look normal. The plot is a diagnostic, not a formal test: the extreme points move more than the centre.{{cite:nist_qq_plot}} (§1.3.3.24, shifts, scale and tails){{cite:dodge2008}} (p. 437, extremes)

