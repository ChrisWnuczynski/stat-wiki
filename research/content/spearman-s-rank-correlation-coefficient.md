

## Lead context

A straight-line correlation asks how tightly two numerical measurements rise together. When the information is the order of the values rather than their spacing, the matching summary uses the ranks. That summary is Spearman's rank correlation coefficient. {{cite:dodge2008}} (p. 502) {{cite:openintro2019}}

## Motivating example

Four students are ordered by hours of practice, 1 through 4, and separately by the judge's ranking of a performance. If the performance order is the same as the practice order, the two rankings agree completely. If the performance order is exactly reversed, they disagree completely. A coefficient that is \(+1\) in the first case and \(-1\) in the second is tracking the agreement of the ranks, not the size of the gaps between hours. {{cite:dodge2008}} (p. 502) {{cite:dodge2008}} (p. 503)

## Intuition

Replace each measurement by its place in line: rank 1 for the smallest, rank 2 for the next, up to rank \(n\). Where the places agree, the rank differences are near zero and the coefficient is near \(+1\). Where a high place on one variable is a low place on the other, the coefficient is near \(-1\). The original units have been discarded on purpose, which is why a monotone curve that is not a straight line can still produce a large rank coefficient. {{cite:dodge2008}} (p. 502) {{cite:openintro2019}}

## Definition

For paired samples \((X_1, Y_1), \ldots, (X_n, Y_n)\), let \(R_{X_i}\) be the rank of \(X_i\) among the \(X\) values, with rank 1 on the smallest, and let \(R_{Y_i}\) be the rank of \(Y_i\). The difference is \(d_i = R_{X_i} - R_{Y_i}\). Spearman's rank correlation coefficient is
\[
\rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}.
\]
{{cite:dodge2008}} (p. 502) Tied values receive the average of the ranks they share. {{cite:dodge2008}} (p. 502)

The coefficient lies between \(-1\) and \(+1\). {{cite:dodge2008}} (p. 503) The ordinary correlation \(R\) also lies between \(-1\) and \(1\), and it describes the strength of a linear relationship between the values themselves rather than between their ranks. {{cite:openintro2019}}

Rank the two columns, compute the \(d_i\), and insert them in the formula. The result is a description of monotone association in the sample. A test then asks whether an association of that size is surprising under independence. {{cite:dodge2008}} (p. 502) When the scientific question is specifically about a straight line, the correlation of the original values is the matching summary, and a residual plot is the check that a line was appropriate. {{cite:openintro2019}} {{cite:openintro2019}}

Spearman's coefficient is not the correlation of the raw measurements. It is the association of their ranks. A transformation that preserves order does not change it. A transformation that changes order does. {{cite:dodge2008}} (p. 502) {{cite:openintro2019}}

A value near \(+1\) is not a statement that the relationship is a straight line with slope 1. It is a statement that the orderings agree. {{cite:dodge2008}} (p. 503) {{cite:openintro2019}}

Charles Spearman, a psychologist, introduced the rank coefficient in 1904. It is one of the oldest rank statistics, and it is often called Spearman's \(\rho\). {{cite:dodge2008}} (p. 502)

## Properties

If the ranks agree, every \(d_i\) is 0, the sum of squares is 0, and \(\rho = 1\). If the ranks are perfectly reversed, the sum of squared differences reaches the value that makes \(\rho = -1\).

The coefficient is used as a test of independence between the two rankings. The bilateral null says the variables are mutually independent, against a positive or a negative association. A one-sided null keeps only one of those directions. Critical values come from the null distribution of the coefficient, tabulated for small \(n\). {{cite:dodge2008}} (p. 502) {{cite:dodge2008}} (p. 503)

As a nonparametric measure it applies to ordinal data, where the gaps between codes are not lengths, as well as to numerical data that have been replaced by ranks. {{cite:dodge2008}} (p. 503) {{cite:dodge2008}} (p. 439)

## Worked example

Four pairs have \(X\) ranks \(1, 2, 3, 4\) and \(Y\) ranks \(1, 2, 4, 3\). The differences are \(0, 0, -1, 1\). The squared differences are \(0, 0, 1, 1\), and they sum to 2. Here \(n(n^2 - 1) = 4 \times 15 = 60\), so
\[
\rho = 1 - \frac{6 \times 2}{60} = 1 - \frac{12}{60} = 1 - 0.2 = 0.8.
\]
{{cite:dodge2008}} (p. 502)

**Your turn.** The \(Y\) ranks are replaced by \(4, 3, 2, 1\), a complete reversal, and the \(X\) ranks stay \(1, 2, 3, 4\). What is \(\rho\)?

::: {.callout-tip collapse="true" title="Answer"}
The differences are \(-3, -1, 1, 3\). The squared differences sum to \(9 + 1 + 1 + 9 = 20\). Then \(\rho = 1 - (6 \times 20)/60 = 1 - 120/60 = 1 - 2 = -1\).
:::

## Assumptions and limits

The simple formula treats the ranks as a permutation, with average ranks inserted when there are ties. A large number of ties calls for a correction. The coefficient is then no longer the plain function of the \(d_i\) alone. {{cite:dodge2008}} (p. 502) Independence of the two rankings is the null of the test, not a finding the coefficient reports by itself. {{cite:dodge2008}} (p. 503) The coefficient does not estimate a slope in the original units, because the units were replaced by ranks.



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 10. Their total is 55, so their mean is 5.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 3.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Spearman s rank correlation coefficient has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 5.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Correlation](correlation.qmd), [Levels of measurement](levels-of-measurement.qmd), [variable](variable.qmd), [statistical model](statistical-model.qmd).

Two further limits are algebraic. The sum of deviations from the mean 5.5 is zero, so the mean is the least-squares centre of these 10 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 5.5.

## Connections

[Correlation](correlation.qmd) is the linear measure on the original values. [Levels of measurement](levels-of-measurement.qmd) explain why an ordinal code is a candidate for ranks rather than for a mean. The [variable](variable.qmd) is what gets ranked. A [statistical model](statistical-model.qmd) for a straight line is a different summary, one that keeps the spacing. {{cite:openintro2019}}
