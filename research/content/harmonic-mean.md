## Lead context
Two investments can earn the same income at different rates, and the single rate that matches that income is not the ordinary average of the rates. The same reversal appears when equal sums of money buy goods at different prices: the average price per unit is the average that uses reciprocals.{{cite:dodge2008}} (p. 240)

## Motivating example
Three investments yield the same income at rates of 5%, 10% and 15%. The arithmetic mean of the rates is 10%. The rate at which the whole capital would have to be invested to produce the same total income is smaller, about 8.18%. A buyer who spends the same amount on coffee at 3, 2 and 1.5 euros per kilogram likewise pays an average of 2 euros per kilogram, which is the reciprocal average of the three prices rather than their arithmetic mean of about 2.17.{{cite:dodge2008}} (p. 240)

## Intuition
The harmonic mean asks how many units a fixed outlay buys, then divides the outlay by that quantity. A low price buys many units, so it pulls the average harder than a high price of the same outlay. A very small observation has a very large reciprocal and can move the result sharply. A very large observation has a small reciprocal and moves it much less. The arithmetic mean does the opposite: it is pulled by the large observations.{{cite:dodge2008}} (p. 240)

## Definition
For nonzero numbers \(x_1,\ldots,x_n\), the harmonic mean is
\[
H=\frac{n}{\sum_{i=1}^n 1/x_i}.
\]
When the numbers are positive it lies between the smallest and the largest, and it does not exceed the arithmetic mean.{{cite:dodge2008}} (p. 240) Survey weights are combined in the same way: the harmonic mean of person weights 100, 200 and 300 is the family weight obtained from those three people, reported as 164.{{cite:abs_lfs2008}} (Glossary, “Harmonic mean”)

## Properties
For two positive numbers \(a\) and \(b\),
\[
H=\frac{2ab}{a+b},\qquad \bar x=\frac{a+b}{2},
\]
and \(H\le\bar x\), with equality only when \(a=b\). The ordering extends to any positive list: the harmonic mean is at most the arithmetic mean, and both sit between the minimum and the maximum.{{cite:dodge2008}} (p. 240) A zero in the list makes a reciprocal undefined, so the mean is not defined for data that can be zero.{{cite:abs_lfs2008}} (Glossary, “Harmonic mean”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The difference of the two means is
\[
\bar x-H=\frac{(a+b)^2-4ab}{2(a+b)}=\frac{(a-b)^2}{2(a+b)}.
\]
The numerator is a square and the denominator is positive, so the difference is nonnegative and is zero only when \(a=b\). For the six positive numbers 1, 2, 3, 4, 5 and 100 the same ordering is numerical: the harmonic mean is about 2.62 and the arithmetic mean is about 19.17.{{cite:dodge2008}} (p. 240)
:::
:::

## Statistical use
Use the harmonic mean when each observation is a rate or a price and the natural total is a sum of reciprocals. Equal incomes at different interest rates combine at the harmonic mean of the rates. Equal expenditures at different prices per unit combine at the harmonic mean of the prices. Person weights inside one family are combined by the same formula when the family weight is that average of the person weights.{{cite:dodge2008}} (p. 240){{cite:abs_lfs2008}} (Glossary, “Harmonic mean”)

## Worked example
For the rates 5, 10 and 15,
\[
\frac15+\frac1{10}+\frac1{15}=\frac{6}{30}+\frac{3}{30}+\frac{2}{30}=\frac{11}{30},
\]
so
\[
H=\frac{3}{11/30}=\frac{90}{11}\approx 8.1818.
\]
The arithmetic mean is \((5+10+15)/3=10\). The gap is the effect of giving the 5% rate a larger reciprocal. For the coffee prices 3, 2 and 1.5 the same formula returns exactly 2, which is also the total cost divided by the total quantity when 200 euros is spent at each price.{{cite:dodge2008}} (p. 240)

**Your turn.** Three person weights are 100, 200 and 300. Compute the harmonic mean exactly, and give the value rounded to the nearest integer.

::: {.callout-tip collapse="true" title="Answer"}
The sum of reciprocals is \(1/100+1/200+1/300=11/600\). The harmonic mean is \(3/(11/600)=1800/11\approx 163.636\), which rounds to 164.
:::

## Common misconceptions
The harmonic mean is an average of the observations, and it answers a different question from the arithmetic mean. Replacing it by 10% in the investment example changes the income that the pooled capital would earn. It is also undefined when any observation is zero, because a reciprocal of zero is not a number. A large outlier does not dominate it the way it dominates the arithmetic mean: for 1, 6, 6, 6, 6 and 6 the harmonic mean is \(36/11\approx 3.27\) and the arithmetic mean is \(31/6\approx 5.17\).{{cite:dodge2008}} (p. 240)

## Assumptions and limits
The observations must be nonzero. The comparison with the arithmetic mean, and the reading in terms of prices and rates, uses positive numbers. A negative rate or a negative weight changes the meaning of the reciprocal sum, and the ordering between the harmonic and arithmetic means need not survive. The mean is also sensitive to observations that are much smaller than the rest, because their reciprocals are large.{{cite:dodge2008}} (p. 240){{cite:abs_lfs2008}} (Glossary, “Harmonic mean”)

## Connections
The arithmetic mean of the same numbers is the [summary](summary-statistics.qmd) that adds the values and divides by the count. The [median](median.qmd) resists a single large observation in a different way. When the scientific total is a sum of squared errors rather than a sum of reciprocals, the relevant average is a [variance](variance.qmd) calculation, not a harmonic mean.

## History
The relation that places the harmonic mean at or below the arithmetic mean for positive numbers is the property that makes the rate and price calculations work. The investment and equal-outlay examples are the classical settings in which that mean, rather than the arithmetic mean, reproduces the total income or the total quantity.{{cite:dodge2008}} (p. 240)
