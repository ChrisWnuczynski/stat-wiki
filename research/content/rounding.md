## Lead context
A sample of 30 people cannot be split into 14.25 people from one stratum and 7.5 from another. Every reported allocation, proportion and index score is a rounded number, and the rounding is part of the statistic that a reader sees.{{cite:dodge2008}} (p. 525)

## Motivating example
A population of 600 students is divided into strata of 285, 150, 90 and 75. A sample of 30 allocated in proportion to those sizes has exact shares 14.25, 7.5, 4.5 and 3.75. Those four numbers add to 30. Rounding each of them to the nearest integer by the half-up rule produces 14, 8, 5 and 4, which add to 31. The published representative allocation 14, 7, 5 and 4 adds to 30, because the share 7.5 was rounded down rather than up. The integers are a second decision, made so that the sample size stays 30.{{cite:dodge2008}} (p. 525)

## Intuition
Rounding replaces a number by the nearest multiple of a reporting unit, here the nearest integer. The error on each piece is at most half a unit, and the errors do not cancel in general. Four errors of a few tenths can push the sum of the rounded pieces a whole unit away from the rounded sum. A table of proportions has the same structure: each entry is rounded, and a row that should add to 1 can add to 1.001.{{cite:openintro2019}} (Ch. 2, §2.2.2)

## Definition
Rounding a positive number to the nearest integer by the half-up rule sends \(x\) to the integer closest to it, and sends a value that is exactly halfway between two integers to the larger one. In symbols, that value is \(\lfloor x+1/2\rfloor\). Applied separately to each coordinate of a vector, it need not preserve the sum. An allocation rule that must preserve a total chooses, among the integers near the exact shares, a vector whose coordinates add to the required total. The representative stratified sample does that: 14.25, 7.5, 4.5 and 3.75 become 14, 7, 5 and 4.{{cite:dodge2008}} (p. 525)

Displayed proportions are the same operation at a finer unit. The row proportion \(3496/8505\) is reported as 0.411. In the column-proportion table, the printed shares 0.851 and 0.150 of the margin add to 1.001, and the table is off by 0.001 because of that rounding.{{cite:openintro2019}} (Ch. 2, §2.2.2)

## Properties
If each of \(k\) positive numbers is replaced by its nearest integer, the sum of the rounded numbers differs from the rounding of the sum by an integer, and the difference is at most \(k/2\) in absolute value before the final integers are chosen. In the sample allocation the exact sum is 30 and the half-up sum is 31, a difference of 1. The optimal stratified allocation, using stratum sizes times stratum standard deviations 2451, 780, 198 and 105, has exact shares
\[
30\cdot\frac{2451}{3534}\approx 20.806,\quad
30\cdot\frac{780}{3534}\approx 6.621,\quad
30\cdot\frac{198}{3534}\approx 1.681,\quad
30\cdot\frac{105}{3534}\approx 0.891.
\]
Rounded to two decimals these are 20.81, 6.62, 1.68 and 0.89, which add to 30.00. Half-up rounding of those four numbers gives 21, 7, 2 and 1, and \(21+7+2+1=31\). The printed optimal allocation is 21, 6, 2 and 1, which adds to 30, because 6.62 was rounded down to 6 rather than up to 7. The same repair that changed 7.5 into 7 in the proportional split changes 6.62 into 6 here.{{cite:dodge2008}} (p. 525)

## Statistical use
Round an allocation when the unit of observation is a person or another indivisible case, and check that the integers add to the intended sample size. Round a proportion for display, and expect a printed row or column to miss its theoretical total by about one unit in the last place. Treat two index scores that agree after printing as possibly distinct: a rank can still separate them when the unrounded scores differ.{{cite:dodge2008}} (p. 525){{cite:openintro2019}} (Ch. 2, §2.2.2){{cite:abs_seifa2006}} (Glossary, “Rank”)

## Worked example
The proportional shares are
\[
\frac{285}{600}\cdot 30=14.25,\quad
\frac{150}{600}\cdot 30=7.5,\quad
\frac{90}{600}\cdot 30=4.5,\quad
\frac{75}{600}\cdot 30=3.75.
\]
Their sum is \(14.25+7.5+4.5+3.75=30\). Half-up rounding gives \(14+8+5+4=31\). Replacing the rounded 8 by 7 restores the total: \(14+7+5+4=30\). That is the representative allocation. The column-proportion display 0.851 and 0.150 is the other arithmetic: \(0.851+0.150=1.001\), which is 0.001 above 1.{{cite:dodge2008}} (p. 525){{cite:openintro2019}} (Ch. 2, §2.2.2)

**Your turn.** Round 2.5, 2.5 and 3.2 to the nearest integers by the half-up rule. What is the sum of the rounded values, and by how much does it exceed the sum of the exact values?

::: {.callout-tip collapse="true" title="Answer"}
Half-up rounding sends both values 2.5 to 3, and 3.2 to 3. The rounded sum is 9. The exact sum is 8.2, so the rounded sum is larger by 0.8.
:::

## Common misconceptions
Rounding each share to the nearest integer is a complete allocation only when those integers add to the required total. In the proportional example they add to 31, so one share has to be moved. A printed total of 1.001 is not evidence that the underlying counts failed to add up. The counts 3496, 3839 and 1170 add to the row total 8505, while the three-decimal proportions of a different margin can still miss 1 by 0.001. Two areas that display the same index score can still have different ranks, because the displayed score has been rounded.{{cite:openintro2019}} (Ch. 2, §2.2.2){{cite:abs_seifa2006}} (Glossary, “Rank”)

## Assumptions and limits
Half-up rounding is one convention. A half can be sent to the even integer, or toward zero, and each convention changes 7.5 or 4.5. The bound of half a unit on each piece assumes the reporting unit is 1. Rounding to two decimals, as in 20.81, leaves an error of at most 0.005 on that piece. None of these operations recovers the exact share from the printed integer. A sample size computed from a rounded intermediate such as 0.0085 can also disagree slightly with the exact ratio \(30/3534\), which is why the displayed 20.81 matches the exact 20.806 only after two-decimal rounding.{{cite:dodge2008}} (p. 525)

## Connections
[Ranking](ranking.qmd) can separate scores that rounding has made to look equal. [Summary statistics](summary-statistics.qmd) that are printed to a fixed number of decimals are rounded summaries. A [histogram](histogram.qmd) bins continuous measurements, which is a coarser kind of replacement of a number by an interval, and the binning decision is separate from rounding the printed counts.

## History
Sample-size formulas for stratified samples produce real numbers, and the passage from those numbers to a sample of people has been part of the worked examples of allocation since the sampling texts that record both proportional and optimal splits. The same practical step appears whenever a table of proportions is printed to three decimals and a margin that should be 1 is off by one unit in the last place.{{cite:dodge2008}} (p. 525){{cite:openintro2019}} (Ch. 2, §2.2.2)
