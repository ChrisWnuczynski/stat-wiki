## Lead context
The interquartile range is the distance between the third quartile and the first, so it measures the width of the middle half of a sample and ignores the most extreme quarter on each side.

## Motivating example
The values 1 through 9, together with a mistyped 100, have mean 14.5 and sample standard deviation 30.152. The middle half of the ordered sample is not that wide. Under the position rule $1+(n-1)p$, the first quartile is 3.25 and the third is 7.75, so the interquartile range is 4.5. Deleting the 100 changes the mean from 14.5 to 5 and the standard deviation from 30.152 to 2.739, while the interquartile range moves only from 4.5 to 4. A single bad keystroke dominates the standard deviation and barely moves the middle-half width.{{cite:nist_handbook2002}} (§1.3.5.6, the interquartile range uses the middle of the data){{cite:dodge2008}} (p. 266, interquartile range equals $Q_3-Q_1$)

## Intuition
Order the sample. The first quartile sits a quarter of the way along that order, and the third quartile sits three quarters of the way. Their difference is a length, in the units of the data, of the central half. It does not square deviations, so a point far in the tail cannot dominate it the way it dominates a variance. It also does not use only the minimum and the maximum, so it is not the range. NIST describes it as a scale measure aimed at the centre rather than at the tails, and groups it with the median absolute deviation when the tails are long.{{cite:nist_handbook2002}} (§1.3.5.6, “interquartile range”){{cite:dodge2008}} (p. 266, the interval containing the central half)

## Definition
For a distribution or a sample with first quartile $Q_1$ and third quartile $Q_3$, the interquartile range is $Q_3-Q_1$. That difference is the length of the interval holding the central 50% of the distribution. On a sample, the quartiles are sample quantiles at probabilities 1/4 and 3/4. The numerical value depends on the interpolation rule. The rule used here places the quantile of probability $p$ at position $1+(n-1)p$ in the ordered sample and interpolates linearly between the surrounding order statistics. That is the rule behind the numbers 3.25 and 7.75 above. This $1+(n-1)p$ position rule is Hyndman–Fan type 7, R's default [sample quantile](sample-quantile.qmd) convention, whereas [five-number summary and boxplot](five-number-summary-and-boxplot.qmd) uses the $p(n+1)$ rule, which is type 6.{{cite:r_stats_quantile}} (Details, Type 6 and Type 7) A different rule can move those quartiles by a fraction of the gap between adjacent observations. It does not change the definition $Q_3-Q_1$.{{cite:dodge2008}} (p. 266, Interquartile range){{cite:nist_handbook2002}} (§1.3.5.6, 75th percentile minus 25th percentile)

## Interpretation — What a change in the interquartile range is
In the ten-point sample the ordered values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 100. Position $1+9\times0.25=3.25$ lies a quarter of the way from the 3rd order statistic to the 4th, so $Q_1=3+0.25(4-3)=3.25$. Position $1+9\times0.75=7.75$ gives $Q_3=7+0.75(8-7)=7.75$. The outlier 100 is in neither of those positions. It would enter $Q_3$ only if it moved the upper order statistics that the position 7.75 actually uses. With $n=10$ it does not. The range, $100-1=99$, uses it immediately. The two scales answer different questions: how wide is the middle, and how far apart are the extremes.{{cite:nist_handbook2002}} (§1.3.5.6, the range uses only the extremes)

## Properties — A fence and a normal benchmark
Tukey's boxplot draws the box from $Q_1$ to $Q_3$ and extends whiskers to the last observations inside the fences $Q_1-1.5(Q_3-Q_1)$ and $Q_3+1.5(Q_3-Q_1)$. Here the upper fence is $7.75+1.5\times4.5=14.5$. The value 100 lies beyond it, and 9 does not. The fence is a drawing convention. It is not a test that 100 is a mistake. For a normal population with mean $\mu$ and standard deviation $\sigma>0$, write $\Phi$ for the standard normal cumulative distribution function. Its quartiles are $\mu-\sigma\Phi^{-1}(0.75)$ and $\mu+\sigma\Phi^{-1}(0.75)$, so the population ratio is $\mathrm{IQR}/\mathrm{SD}=2\Phi^{-1}(0.75)\approx2\times0.67449\approx1.349$. For comparison with the sample standard deviation divided by the interquartile range, take the reciprocal: $\mathrm{SD}/\mathrm{IQR}=\frac{1}{2\Phi^{-1}(0.75)}\approx0.7413$.

For the ten-point sample, $\mathrm{SD}/\mathrm{IQR}\approx30.15239/4.5\approx6.701$. This is much larger than the population normal benchmark for the same ratio, so the sample standard deviation is large relative to the interquartile range. In this example the value 100 inflates the standard deviation without changing the order statistics used for the quartiles. Such a comparison can flag observations for investigation, but it does not establish that the underlying distribution has heavy tails.{{cite:nist_handbook2002}} (§1.3.5.6, long tails and the interquartile range){{cite:dodge2008}} (p. 266, central half)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $x_{(1)}\le\cdots\le x_{(n)}$ be the ordered sample and set $h=1+(n-1)p$. Write $h=j+g$ with $j=\lfloor h\rfloor$ and $g=h-j\in[0,1)$. The interpolated quantile is $(1-g)x_{(j)}+g x_{(j+1)}$, with the understanding that $g=0$ returns $x_{(j)}$. For $n=10$ and $p=1/4$, $h=3.25$, so $j=3$, $g=0.25$ and $Q_1=(1-0.25)x_{(3)}+0.25 x_{(4)}$. For $p=3/4$, $h=7.75$, so $Q_3=(1-0.75)x_{(7)}+0.75 x_{(8)}$. Subtracting these linear functions gives $Q_3-Q_1$. Replacing $x_{(n)}$ does not change $Q_1$ or $Q_3$ unless the replaced point is one of $x_{(3)},x_{(4)},x_{(7)},x_{(8)}$, or the ordering itself changes which observations sit in those positions. In the example the point 100 occupies position 10 only, so the interpolated quartiles are functions of positions 3, 4, 7 and 8.{{cite:nist_handbook2002}} (§1.3.5.6, quartiles as the 25th and 75th percentiles){{cite:dodge2008}} (p. 266, $Q_3-Q_1$)
:::
:::

## Statistical use — Choosing a scale
Report the interquartile range, with the quartiles themselves, when the distribution is skewed or a few points may be wrong and the question is about the central half. Report the standard deviation when the data are close to normal and later steps, such as a $t$ interval, actually use that standard deviation. NIST's comparison is the practical one: the standard deviation is efficient for normal data and is not stable in long tails; the interquartile range is more stable and is not the most efficient normal-scale estimate. Comparing the two on the same sample, as in the ratio 6.701, is a diagnostic. It is not a formal test.{{cite:nist_handbook2002}} (§1.3.5.6, robustness of validity and when each scale is reasonable)

## Worked example
Ordered sample: 1, 2, 3, 4, 5, 6, 7, 8, 9, 100. Then $Q_1=3.25$, $Q_3=7.75$ and the interquartile range is $4.5$. The upper fence is $7.75+1.5\times4.5=14.5$, so 100 is plotted beyond the whisker and 9 is not. The mean is $(45+100)/10=14.5$ and the sample standard deviation is 30.152. After deleting 100 the nine values 1 through 9 have quartiles at positions 3 and 7, hence $Q_1=3$, $Q_3=7$ and interquartile range 4. Their mean is 5 and their sample standard deviation is $\sqrt{7.5}=2.739$. The middle-half width changed by 0.5. The standard deviation changed by 27.414.{{cite:nist_handbook2002}} (§1.3.5.6, tails distort the standard deviation more than a rank scale){{cite:dodge2008}} (p. 266, $Q_3-Q_1$)

**Your turn.** Five ordered observations are 2, 2, 5, 8, 8. Using position $1+(n-1)p$, find the two quartiles and the interquartile range.

::: {.callout-tip collapse="true" title="Answer"}
For $n=5$, the position at $p=1/4$ is $1+4\times0.25=2$, so $Q_1$ is the second order statistic, 2. The position at $p=3/4$ is $1+4\times0.75=4$, so $Q_3$ is the fourth order statistic, 8. The interquartile range is $8-2=6$. No interpolation is required, because both positions are integers.
:::

## Common misconceptions
The interquartile range is not half the range, and it is not twice the distance from the median to the upper quartile unless the two central quarters have the same length. For the ordered sample 1, 2, 3, 10, 11 the position rule gives $Q_1=2$, median 3 and $Q_3=10$. Then $Q_3-Q_1=8$, while $2(Q_3-\text{median})=14$. A large interquartile range does not mean the tails are heavy. It means the central half is wide. A standard deviation or range that is large relative to the interquartile range indicates a discrepancy between overall spread and central spread. It does not by itself identify a heavy-tailed population: sampling variation or a recording error can also produce such a discrepancy. In the worked example, the stipulated recording error accounts for the standard deviation 30.152 beside an interquartile range of 4.5. Finally, points beyond the 1.5-interquartile-range fence are not automatically errors. The fence is a plotting rule.

## Assumptions and limits — The quartile rule, and a sample of size three
The number $Q_3-Q_1$ is only as well defined as $Q_1$ and $Q_3$. Two software packages that interpolate differently can print two interquartile ranges for the same ten numbers. The normal benchmark $\mathrm{SD}/\mathrm{IQR}\approx0.7413$ uses population quartiles of a nondegenerate continuous normal law, with $\Phi^{-1}(0.75)\approx0.67449$. It is not an exact identity for a finite sample, even one drawn from that law. A sample ratio depends on sampling variation and the quartile rule, and it is defined only when the sample interquartile range is positive. For $n=3$ the positions at 1/4 and 3/4 fall inside the first gap and the last gap, so the interquartile range is a fraction of $(x_{(3)}-x_{(1)})$ and is no longer protected from the extremes. With observations 0, 0, 100, position $1+2\times0.25=1.5$ gives $Q_1=0.5\times0+0.5\times0=0$, and position $1+2\times0.75=2.5$ gives $Q_3=0.5\times0+0.5\times100=50$. The interquartile range is 50, half the range. At $n=3$ the interpolation that is supposed to describe the middle half reaches an extreme. The stability seen in the ten-point sample is a fact about where the quartile positions fall, and it is weaker in a sample this small.{{cite:nist_handbook2002}} (§1.3.5.6, the interquartile range as a scale for the centre)

## Connections
The [median](median.qmd) is the quartile at probability 1/2. A [five-number summary](five-number-summary-and-boxplot.qmd) displays the minimum, the two quartiles, the median and the maximum, and the box in a boxplot has width equal to the interquartile range. The [sample standard deviation](sample-variance-and-standard-deviation.qmd) is the scale that uses squared deviations. The [range](range.qmd) uses only the two extremes.{{cite:nist_handbook2002}} (§1.3.5.6, range, standard deviation and interquartile range){{cite:dodge2008}} (p. 266, quartiles)

## Check yourself

### Quartiles of a sample {#self-check-ex-da-nutrition-types}

A sample has first quartile 51 and third quartile 70. What is the interquartile range, and what is the upper 1.5-fence?

[Exercise](../questions/ex-da-nutrition-types.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The interquartile range is $70-51=19$. The upper fence is $70+1.5\times19=70+28.5=98.5$. An age beyond 98.5 would be drawn past the whisker. The fence is a drawing rule, not a statement that such an age is impossible.
:::

### A spread beside a mean {#self-check-ex-inf-milk-summaries}

Creatinine quartiles are 0.9 and 1.4. Compute the interquartile range and the upper fence, and say why the mean can sit well above the median while this range stays small.

[Exercise](../questions/ex-inf-milk-summaries.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The interquartile range is $1.4-0.9=0.5$. The upper fence is $1.4+1.5\times0.5=2.15$. A long right tail pulls the mean and the standard deviation and need not move $Q_1$ or $Q_3$ if the central order statistics stay put. That is the same mechanism as the value 100 leaving the interquartile range at 4.5.
:::

## History
The interquartile range is $Q_3-Q_1$, the length of the central half of the distribution. NIST's handbook places the same difference among the scale measures, contrasts it with the variance and the range, and recommends it when long tails make the standard deviation unstable. The factor 1.5 in the boxplot fence is a plotting convention attached to that length, not part of the definition of the length itself.{{cite:dodge2008}} (p. 266, Interquartile range){{cite:nist_handbook2002}} (§1.3.5.6, definition and robustness)
