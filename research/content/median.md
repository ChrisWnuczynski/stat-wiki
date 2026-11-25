## Lead context
Because it depends on rank rather than distance from the centre, the median can describe a typical observation when a few values lie far into a tail. It is also the halfway quantile of a distribution, so the same idea applies to a sample and to a probability model.{{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”){{cite:siegrist2022_quantiles}} (§3.6, “Special Quantiles”)

## Motivating example
Consider five recorded waiting times of 2, 4, 5, 8 and 100 minutes. The median is 5 minutes: two values are below it and two are above it. The mean is 23.8 minutes because the longest wait contributes heavily to the total. A summary of a typical wait and an estimate of total waiting time therefore answer different questions.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”){{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)

## Definition
Let $x_1,\ldots,x_n$ be realised numerical observations, and let $x_{(1)}\le\cdots\le x_{(n)}$ be the same observations in order. For odd $n=2k+1$, the sample median is $\tilde x=x_{(k+1)}$. For even $n=2k$, the two middle observations form the *median interval* $[x_{(k)},x_{(k+1)}]$; the usual reported median is its midpoint $\tilde x=\{x_{(k)}+x_{(k+1)}\}/2$. Here $k$ is an integer and $\tilde x$ denotes the reported sample value. It is the sample quantile at probability $1/2$ under the interpolation rule used here.{{cite:siegrist2022_order_statistics}} (§6.6, “Order Statistics,” “The Sample Median,” and “Sample Quantiles”)

For the population definition above, let $F_X(t)=\Pr(X\le t)$ be the cumulative distribution function. The median condition is equivalently $F_X(m-)\le1/2\le F_X(m)$, where $F_X(m-)=\Pr(X<m)$. A distribution may have more than one median: a fair Bernoulli variable has every $m\in[0,1]$ as a median. The lower quantile $\inf\{t:F_X(t)\ge1/2\}$ selects the smallest one.{{cite:siegrist2022_quantiles}} (§3.6, “Quantile Functions,” “Definitions,” and “Special Quantiles”)

## Interpretation
A median has at least half the observations at or below it and at least half at or above it, while the mean balances their numerical magnitudes. For an even sample with a nonempty gap between its two middle observations, every point strictly inside that gap has exactly half the observations strictly below it and half strictly above it; the endpoints are also medians but do not give that strict split. The midpoint is a reporting convention. In a population, a CDF jump from strictly below $1/2$ to strictly above $1/2$ gives a unique median, whereas a plateau at $1/2$ can give an interval of medians.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”){{cite:siegrist2022_quantiles}} (§3.6, “Quantile Functions”)

The median has the units of the observations. It can be useful for an asymmetric distribution because a large value in the right tail pulls the mean upward while its exact size does not determine the median. The NIST handbook contrasts normal, exponential, Cauchy and lognormal examples to show how centre summaries can differ with tail shape.{{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)

## Properties
For fixed observations, any point in the median interval minimizes $D(a)=\sum_{i=1}^n|x_i-a|$ over real $a$; when $n$ is odd, the interval reduces to the middle observation. Thus the usual even-sample midpoint is one absolute-error minimizer among many. The mean instead minimizes the sum of squared errors, which explains the different responses of the two summaries to an extreme observation.{{cite:schwertman_gilks_cameron1990}} (p. 38, Theorem and proof){{cite:siegrist2022_sample_variance}} (§6.5, “Measures of Center and Spread”)

For any constants $a$ and $b$, applying the same affine change $a+bx_i$ to every observation changes its median to $a+b\tilde x$. This follows from the reversed order when $b<0$ and the matching order when $b>0$; the midpoint of the central pair transforms the same way. For a nonlinear increasing transformation, the odd-sample median transforms directly, while the even-sample midpoint need not.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”)

For five ordered values $x_{(1)}\le\cdots\le x_{(5)}$, replacing one value by an arbitrarily large or small value leaves the new median somewhere between the old $x_{(2)}$ and $x_{(4)}$. In particular, replacing an already largest value by another larger value leaves the median unchanged. The mean can move without bound under that replacement. This is a precise sense in which the median resists a single extreme value.{{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Pair the ordered observations from the outside inward: $(x_{(1)},x_{(n)})$, $(x_{(2)},x_{(n-1)})$, and so on. For each pair $(u,v)$ with $u\le v$, $|u-a|+|v-a|$ is minimized at every $a\in[u,v]$. The innermost pair gives $[x_{(k)},x_{(k+1)}]$ when $n=2k$; with odd $n=2k+1$, the unpaired middle value makes $a=x_{(k+1)}$ the common minimizer. Hence these and only these middle points minimize $D(a)$. Squared-error minimization follows from $\sum_i(x_i-a)^2=\sum_i(x_i-\bar x)^2+n(a-\bar x)^2$, where $\bar x=n^{-1}\sum_i x_i$.{{cite:schwertman_gilks_cameron1990}} (p. 38, Theorem and proof){{cite:siegrist2022_sample_variance}} (§6.5, “Measures of Center and Spread”)

If $b>0$, sorting $a+bx_i$ preserves the order; if $b<0$, it reverses the order. In both cases the central observation or midpoint becomes $a+b\tilde x$, proving affine equivariance. For five values, after replacing one, at least three of the five new values are at or above old $x_{(2)}$ and at least three are at or below old $x_{(4)}$. The new third order statistic therefore lies in $[x_{(2)},x_{(4)}]$. A replacement of the maximum by a still larger value leaves the three central ranks in place.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”)
:::
:::

## Statistical use
Report a median when the question concerns a typical observed value and the distribution is skewed or has long tails. For a fuller description, pair it with quartiles and the interquartile range; a boxplot displays the median inside that middle-half interval. A mean is still useful when totals or additive costs are the target, so the choice of centre should follow the quantity being estimated.{{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”){{cite:siegrist2022_order_statistics}} (§6.6, “Sample Quantiles”)

For inferential work, distinguish the observed median $\tilde x$ from the population median $m$. Repeated random samples produce different observed medians. Their uncertainty depends on the sampling design and the distribution near its centre; an outlier-resistant point summary alone does not provide an interval estimate.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”){{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)

## Worked example
For the five waits $2,4,5,8,100$, the sample median is $5$ and the sample mean is $(2+4+5+8+100)/5=119/5=23.8$. If the longest wait is corrected to $1000$, the median stays $5$, while the mean becomes $1019/5=203.8$. At $a=5$, the original sum of absolute deviations is $3+1+0+3+95=102$; at $a=4$, it is $2+0+1+4+96=103$. The middle value has the smaller absolute-error sum.{{cite:schwertman_gilks_cameron1990}} (p. 38, Theorem and proof){{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)

For the even sample $2,4,8,100$, the reported median is $(4+8)/2=6$. Every $a$ from $4$ through $8$ gives the same absolute-error sum: at $a=6$ it is $4+2+2+94=102$, and at $a=4$ it is $2+0+4+96=102$. The interval of minimizers explains why the midpoint convention does not change the absolute-error property.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”){{cite:schwertman_gilks_cameron1990}} (p. 38, Theorem and proof)

**Your turn.** Find the median of $1,3,7,9,20$ and compare the total absolute deviations at $a=7$ and $a=3$.

::: {.callout-tip collapse="true" title="Answer"}
The middle ordered value is $7$. The absolute-deviation sum is $6+4+0+2+13=25$ at $a=7$ and $2+0+4+6+17=29$ at $a=3$, illustrating the median's minimising property.
:::

## Common misconceptions
An even-sample median need not be an observed value; it is commonly the midpoint of the two central observations. A population median need not be unique, especially with a discrete distribution. The median's resistance to tail magnitudes does not make every inference based on it insensitive to selection bias or dependence: those are properties of how data were gathered.{{cite:siegrist2022_order_statistics}} (§6.6, “The Sample Median”){{cite:siegrist2022_quantiles}} (§3.6, “Quantile Functions”){{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)

## Connections
The [sample quantile](sample-quantile.qmd) at probability $1/2$ is the sample median under the interpolation rule above. The [interquartile range](interquartile-range.qmd) measures the width of the middle half around the median; [five-number summaries and boxplots](five-number-summary-and-boxplot.qmd) display those quartiles and the median together. The [Cauchy distribution](cauchy-distribution.qmd) has a median even though its mean is undefined, illustrating why the two centre summaries can have different domains of use.{{cite:siegrist2022_order_statistics}} (§6.6, “Sample Quantiles”){{cite:nist_location2002}} (§1.3.5.1, “Measures of Location”)
