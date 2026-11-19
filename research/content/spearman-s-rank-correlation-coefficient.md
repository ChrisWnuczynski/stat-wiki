## Lead context

A straight-line correlation asks how tightly two numerical measurements rise together. When the information is the order of the values rather than their spacing, the matching summary uses the ranks. That summary is Spearman's rank correlation coefficient, a nonparametric measure of the relation between two sets of data.

The ordinary correlation also lies between $-1$ and $1$, and it describes the strength of a linear relationship between the values themselves rather than between their ranks.{{cite:dodge2008}} (p. 502){{cite:openintro2019}} (Ch. 8, §8.1.4)

## Motivating example

Four students are ordered by hours of practice, 1 through 4, and separately by the judge's ranking of a performance. If the performance order is the same as the practice order, the two rankings agree completely. If the performance order is exactly reversed, they disagree completely. A coefficient that is $+1$ in the first case and $-1$ in the second is tracking the agreement of the ranks, not the size of the gaps between hours. A monotone curve that is not a straight line can still produce a large rank coefficient, because the original units have been discarded on purpose.{{cite:dodge2008}} (pp. 502–503){{cite:openintro2019}} (Ch. 8, §8.1.4)

## Intuition

Replace each measurement by its place in line: rank 1 for the smallest, rank 2 for the next, up to rank $n$. Where the places agree, the rank differences are near zero and the coefficient is near $+1$. Where a high place on one variable is a low place on the other, the coefficient is near $-1$. Positive association, in the rank sense, means large values of one variable tend to sit with large values of the other. Negative association means large values of one tend to sit with small values of the other. The coefficient is then a description of that monotone agreement, and a test asks whether an association of that size is surprising if the two rankings are independent.{{cite:dodge2008}} (pp. 502–503)

## Definition

For paired samples $(X_1, Y_1), \ldots, (X_n, Y_n)$, let $R_{X_i}$ be the rank of $X_i$ among the $X$ values, with rank 1 on the smallest, and let $R_{Y_i}$ be the rank of $Y_i$. The difference is $d_i = R_{X_i} - R_{Y_i}$. Spearman's rank correlation coefficient is

$$
\rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}.
$$


Tied values receive the average of the ranks they share. When many ties are present, a correction replaces the plain formula by

$$
\rho = \frac{S_x+S_y-\sum_i d_i^2}{2\sqrt{S_x S_y}},
$$


where $S_x$ and $S_y$ subtract a term in the cubed tie-group sizes from $n(n^2-1)/12$. With no ties, each observation is a group of size 1 and $S_x=S_y=n(n^2-1)/12$, which brings the corrected expression back to the plain formula. Charles Spearman, a psychologist, introduced the rank coefficient in 1904. It is one of the oldest rank statistics, and it is often called Spearman's $\rho$.{{cite:dodge2008}} (p. 502)

## Properties

The coefficient lies between $-1$ and $+1$. If the ranks agree, every $d_i$ is 0, the sum of squares is 0, and $\rho = 1$. If the ranks are perfectly reversed, the sum of squared differences reaches the value that makes $\rho = -1$. A value near zero is the case of no rank association. A value near $+1$ says the orderings agree. It does not say that the relationship is a straight line with slope 1 in the original units, because those units were replaced by ranks.{{cite:dodge2008}} (p. 503){{cite:openintro2019}} (Ch. 8, §8.1.4)

The coefficient is used as a test of independence between the two rankings. The bilateral null says the variables are mutually independent, against a positive or a negative association. A one-sided null keeps only one of those directions. Critical values come from the null distribution of the coefficient, tabulated for small $n$. The letter used for those critical values is not a Student $t$. As a nonparametric measure it applies to data that can be ordered, including ordinal codes whose gaps are not lengths, as well as to numerical data that have been replaced by ranks. The associated test does not assume a shape for the population distribution. When the scientific question is specifically about a straight line, the correlation of the original values is the matching summary, and a residual plot is the check that a line was appropriate.{{cite:dodge2008}} (pp. 502–503){{cite:openintro2019}} (Ch. 8, §8.1.1, §8.1.3, §8.1.4)

## Worked example

Four pairs have $X$ ranks $1, 2, 3, 4$ and $Y$ ranks $1, 2, 4, 3$. The differences are $0, 0, -1, 1$. The squared differences are $0, 0, 1, 1$, and they sum to 2. Here $n(n^2 - 1) = 4 \times 15 = 60$, so

$$
\rho = 1 - \frac{6 \times 2}{60} = 1 - \frac{12}{60} = 1 - 0.2 = 0.8.
$$


{{cite:dodge2008}} (p. 502)

**Your turn.** The $Y$ ranks are replaced by $4, 3, 2, 1$, a complete reversal, and the $X$ ranks stay $1, 2, 3, 4$. What is $\rho$?

::: {.callout-tip collapse="true" title="Answer"}
The differences are $-3, -1, 1, 3$. The squared differences sum to $9 + 1 + 1 + 9 = 20$. Then $\rho = 1 - (6 \times 20)/60 = 1 - 120/60 = 1 - 2 = -1$.
:::

## Assumptions and limits

The simple formula treats the ranks as a permutation, with average ranks inserted when there are ties. A large number of ties calls for the correction in $S_x$ and $S_y$. The coefficient is then no longer the plain function of the $d_i$ alone. Independence of the two rankings is the null of the test, not a finding the coefficient reports by itself. The coefficient does not estimate a slope in the original units. A transformation that preserves order does not change it. A transformation that changes order does. Observations that cannot be placed in an order at all, with no criterion that says which comes first, are outside the construction: the ranks have to be defined before $d_i$ is.{{cite:dodge2008}} (pp. 502–503)

## Connections

[Correlation](correlation.qmd) is the linear measure on the original values, the $R$ that OpenIntro defines from the standardised products $(x_i-\bar x)/s_x$ and $(y_i-\bar y)/s_y$. [Levels of measurement](levels-of-measurement.qmd) explain why an ordinal code is a candidate for ranks rather than for a mean. The [variable](variable.qmd) is what gets ranked. A [statistical model](statistical-model.qmd) for a straight line is a different summary, one that keeps the spacing. [Ranking](ranking.qmd) is the replacement of each observation by its place, which is the first step of the coefficient.{{cite:openintro2019}} (Ch. 8, §8.1.1, §8.1.4){{cite:dodge2008}} (p. 502)
