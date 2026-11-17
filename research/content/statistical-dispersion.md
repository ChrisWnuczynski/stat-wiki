## Lead context

A mean locates a batch of numbers and says nothing about whether they sit on top of that mean or are scattered far from it. Dispersion is the family of summaries that measure that scatter, in the centre of the batch, in the tails, or in both. A measure of central tendency without a measure of dispersion is an incomplete description: roads built for the mean traffic still jam on a holiday, and houses built for the mean wind still fail in a storm. The smaller the variability, the more representative the centre is of the batch.{{cite:nist_handbook2002}} (§1.3.5.6, “Scale, Variability, or Spread”){{cite:dodge2008}} (p. 341)

## Motivating example

Two examinations can have the same average grade and very different spreads. Five students scored 3.5, 4, 4.5, 3.5 and 4.5 on one exam and 2.5, 5.5, 3.5, 4.5 and 4 on another. Both averages are \(20/5=4\). The sample standard deviations, with divisor \(n-1\), are \(0.5\) and \(\sqrt{5/4}\approx 1.118\). The second exam is more dispersed, and the common mean does not say so. The same point is numerical in a smaller list, 2, 4, 4, 7 and 8. The mean is 5. The deviations are \(-3,-1,-1,2,3\), the sample variance is 6 and the range is 6. A second list with the same mean and a range of 0 would be five copies of 5. The mean cannot tell those lists apart.{{cite:dodge2008}} (pp. 507, 341)

## Definition

For observations \(Y_1,\ldots,Y_N\) with mean \(\bar Y\), the sample variance and standard deviation are
\[
s^2=\frac{1}{N-1}\sum_{i=1}^N(Y_i-\bar Y)^2,\qquad s=\sqrt{s^2}.
\]
The average absolute deviation is \(\sum |Y_i-\bar Y|/N\). The median absolute deviation is the median of \(|Y_i-\tilde Y|\), where \(\tilde Y\) is the median. The range is the largest value minus the smallest. The interquartile range is the 75th percentile minus the 25th percentile.{{cite:nist_handbook2002}} (§1.3.5.6, “Definitions of Variability”) These divide into two families: distances between two representative values, such as the range and the interquartile range, and averages of deviations from a central value, such as the standard deviation and the mean absolute deviation. The standard deviation is the member of the second family in widest use.{{cite:dodge2008}} (p. 341)

Spread has two pieces: how far the ordinary observations sit from the centre, and how far the extremes sit. Squaring distances emphasises the extremes. A point 2 units from the mean adds 4 to a sum of squares, and a point 10 units from the mean adds 100. Absolute deviations treat those distances as 2 and 10. The range ignores everything except the smallest and largest values. Choosing a measure is choosing which of those pieces should dominate.{{cite:nist_handbook2002}} (§1.3.5.6, “Definitions of Variability”)

## Properties

The variance and the standard deviation respond to both the centre and the tails, and the square gives the tails extra weight. The average absolute deviation and the median absolute deviation also use both regions, with less weight on extremes. The range uses only the two extremes. The interquartile range uses the middle half.{{cite:nist_handbook2002}} (§1.3.5.6) For the list 2, 4, 4, 7, 8 the sum of squared deviations from 5 is 24, so \(s^2=24/4=6\) and the average absolute deviation is \(10/5=2\). The median is 4, the absolute deviations from 4 are 2, 0, 0, 3 and 4, and their median is 2. The population standard deviation is the positive square root of \(\mathbb E[(X-\mathbb EX)^2]\). The coefficient of variation rescales a standard deviation by the mean, \(S/\bar x\) or \(\sigma/\mu\), and multiplies by 100, so the result does not depend on the unit of measurement.{{cite:dodge2008}} (pp. 95, 506)

## Statistical use

If a histogram or a normal probability plot looks close to a normal curve, the standard deviation is a reasonable single measure of spread. A normal sample of 10,000 draws had standard deviation 0.997, median absolute deviation 0.681 and range 7.87. A double-exponential sample had standard deviation 1.417, median absolute deviation 0.706 and range 17.556: the long tails inflated the standard deviation and the range more than the median absolute deviation. A Cauchy sample had standard deviation 998.389 and range 118953.6, while the median absolute deviation was 1.16. In that case the median absolute deviation describes the batch that the histogram shows, and the standard deviation does not, because a Cauchy law does not have a finite variance for the standard deviation to estimate.{{cite:nist_handbook2002}} (§1.3.5.6, “Normal Distribution”, “Double Exponential Distribution” and “Cauchy Distribution”)

On fifty loan interest rates the sample variance was 25.52 and the standard deviation was 5.05 percentage points, around a mean of 11.57%. Thirty-four of the fifty rates, 68%, lay within one standard deviation of the mean, and 48 of the fifty, 96%, lay within two. Those percentages are a description of that sample. They are close to the usual rough guide of about 70% and about 95%, and they are not a rule for every distribution. Three distributions can share a mean of 0 and a standard deviation of 1 and still have different shapes.{{cite:openintro2019}} (Ch. 2, §2.1.4)

The variance and standard deviation need a meaningful mean, and they are pulled by tails. For a Cauchy sample they are not a useful measure of the spread that the histogram shows. The range can only stay the same or grow as more observations are added, and it depends on the two most extreme points, so large samples make it a fragile summary. The median absolute deviation and the interquartile range are more stable under long tails and are less efficient when the data really are normal. A dispersion parameter in a generalised linear model is a variance factor in a likelihood, which is a different object from these descriptive measures.{{cite:nist_handbook2002}} (§1.3.5.6, “Robustness” and the Cauchy example){{cite:dodge2008}} (p. 449)

## Worked example

For 2, 4, 4, 7 and 8 the mean is \((2+4+4+7+8)/5=5\). The squared deviations are 9, 1, 1, 4 and 9, which add to 24. The sample variance is \(24/(5-1)=6\), and the sample standard deviation is \(\sqrt 6\approx 2.449\). The average absolute deviation is \((3+1+1+2+3)/5=2\). The range is \(8-2=6\). Using the divisor 5 instead of 4 would give \(24/5=4.8\), a different variance for the same five numbers.{{cite:nist_handbook2002}} (§1.3.5.6, variance formula){{cite:dodge2008}} (p. 448, range)

**Your turn.** For the seven family sizes 0, 0, 1, 1, 2, 3 and 6, compute the range. Then compute the average absolute deviation from the mean.

::: {.callout-tip collapse="true" title="Answer"}
The range is \(6-0=6\). The mean is \(13/7\). The average absolute deviation is \((13/7+13/7+6/7+6/7+1/7+8/7+29/7)/7=76/49\approx 1.551\).
:::

## Common misconceptions

Equal means are compatible with very different dispersions, so a comparison of centres leaves the spread unexamined. The range of the family sizes 0, 0, 1, 1, 2, 3 and 6 is 6, while six of the seven families have between 0 and 3 children. The range has answered a question about the extremes. A standard deviation is in the units of the data, and the variance is in squared units. The coefficient of variation is a percentage of the mean, and it is a different summary again. The rough guide that about 70% of the data lie within one standard deviation of the mean is a description of many roughly bell-shaped samples, not an identity.{{cite:dodge2008}} (pp. 95, 449){{cite:nist_handbook2002}} (§1.3.5.6, standard deviation){{cite:openintro2019}} (Ch. 2, §2.1.4)

## History

Pearson used the term standard deviation in a lecture to the Royal Society in 1893, used it again in the 1894 paper on asymmetrical frequency curves, and introduced \(\sigma\) for the population quantity. Gosset later insisted on keeping the sample standard deviation distinct from \(\sigma\). The range, the mean absolute deviation and the variance were already the other descriptive competitors around that scale. The study of variability had attracted astronomers first, because they were interested in the distribution of errors.{{cite:dodge2008}} (pp. 341, 506)

## Connections

The [sample variance and standard deviation](sample-variance-and-standard-deviation.qmd) are the squared and root members of this family. The [interquartile range](interquartile-range.qmd) and the [five-number summary](five-number-summary-and-boxplot.qmd) describe the middle and the extremes together. A [histogram](histogram.qmd) shows both the centre and the tails that the choice of measure is weighting. [Kurtosis](kurtosis.qmd) compares the tails with a normal curve after the standard deviation has been scaled out. A [standard score](standard-score.qmd) divides a deviation from the mean by a standard deviation, so the dispersion has been scaled out of the comparison.
