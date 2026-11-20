## Lead context
Five numbers — the minimum, the two quartiles, the median, and the maximum — locate a sample’s centre, its middle half, and its extremes on one scale.

## Motivating example
Serum creatinine in a heart-failure cohort runs from 0.50 to 9.40 mg/dL, with the median at 1.10 and the quartiles at 0.90 and 1.40. The mean sits higher than the median because a few very large values pull it. A list of 299 readings hides that shape; the five numbers, and a box drawn between the quartiles, show it at once.{{cite:dodge2008}} (p. 55)

## Intuition — A box for the middle half
Order the sample. The median splits it in half. The first and third quartiles split each half again, so the interval from the first quartile to the third holds the central half of the observations. That interval is the interquartile range. A box plot draws it as the central rectangle, with the median marked inside and the minimum and maximum at the ends of the diagram.{{cite:dodge2008}} (pp. 55, 266, 440)

A second convention, the one used for the whiskers on this page, does not run them all the way to the minimum and maximum. Each fence lies 1.5 interquartile ranges beyond a quartile, and the whisker stops at the most extreme observation still inside that fence. Points past the fence are drawn one by one.

## Definition — Quartiles by the $(n+1)$ rule
For an ordered sample $x_1\le\cdots\le x_n$, the $j$th quartile is the sample value at position $j(n+1)/4$. If that position is the integer $i$, the quartile is $x_i$. If it is $i+k$ with $0<k<1$, the quartile is $x_i+k(x_{i+1}-x_i)$. The second quartile is the median. The five-number summary is then the minimum, the first quartile, the median, the third quartile, and the maximum.{{cite:dodge2008}} (pp. 55, 440)

The box runs from the first quartile to the third. With the 1.5-interquartile-range fences, the upper fence is the third quartile plus $1.5$ times their difference, and the lower fence is the first quartile minus that same multiple.

Different quartile rules move the box slightly. The serum creatinine quartiles 0.90 and 1.40 come from the software summary printed with that figure; they need not equal the $(n+1)/4$ positions for the same 299 numbers.

## Worked example
Take the ordered sample $4,7,8,9,12,15,40$, so $n=7$. Then $j(n+1)/4$ is $2$, $4$, and $6$ for $j=1,2,3$, all integers, and the quartiles are $x_2=7$, $x_4=9$, and $x_6=15$. The five numbers are $4,7,9,15,40$. The interquartile range is $15-7=8$, and the upper inner fence is $15+1.5\times 8=27$. The value $40$ lies beyond $27$, so a fenced boxplot draws the upper whisker only to $15$ and plots $40$ on its own. The lower fence $7-12=-5$ lies below every observation, so the lower whisker reaches the minimum $4$.{{cite:dodge2008}} (p. 440)

**Your turn.** For the ordered sample $2,5,6,8,9,11,30$, compute the five-number summary with the same $(n+1)/4$ rule, and say whether $30$ falls beyond the upper inner fence.

::: {.callout-tip collapse="true" title="Answer"}
$n=7$ again, so the quartiles are the 2nd, 4th, and 6th values: $5$, $8$, and $11$. The five numbers are $2,5,8,11,30$. The interquartile range is $6$ and the upper fence is $11+9=20$. Since $30>20$, that point is drawn beyond the whisker.
:::

## Connections — Shape, spread, and groups
The [median](median.qmd) is the middle of the five numbers, and the [interquartile range](interquartile-range.qmd) is the width of the box. A [histogram](histogram.qmd) shows the same sample with a choice of bins; the boxplot spends its ink on the quartiles and the extremes instead. Side-by-side boxes compare a quantitative measurement across groups, which compares several batches at once.{{cite:dodge2008}} (p. 55) A point beyond the fence is a candidate for a closer look, not a licence to delete the row.

## Check yourself

### Summaries of ten cartons {#self-check-ex-inf-milk-summaries}

For the ten milk-carton volumes $0.998$, $1.019$, $1.035$, $1.037$, $1.041$, $1.051$, $1.068$, $1.077$, $1.084$, and $1.102$, the lower quartile is defined as the median of the five values below the sample median, and the upper quartile as the median of the five above it. Report the median and the two quartiles.

::: {.callout-tip collapse="true" title="Answer"}
The ordered sample has ten values, so the median is $(1.041+1.051)/2=1.046$. The lower quartile is $1.035$ and the upper quartile is $1.077$. This hinge rule is not the $(n+1)/4$ formula, and the two recipes need not agree.
:::

### Skewness beside the boxplot {#self-check-ex-da-correlation-reading}

Serum creatinine in the same cohort has moment skewness about $4.4$ on the original scale and $1.6$ after logarithms. Does the smaller skewness prove that the log measurements are normal?

::: {.callout-tip collapse="true" title="Answer"}
No. The drop from about $4.4$ to $1.6$ still leaves positive moment skewness, and a skewness of zero would not imply normality either. A histogram or a normal quantile plot is needed to look at the shape.
:::
