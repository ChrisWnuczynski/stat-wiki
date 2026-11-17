

## Lead context

A list of scores still carries its units. Replacing each score by its place in the ordered list removes the units and leaves the order. That place is the rank, and the whole replacement is a ranking.{{cite:dodge2008}} (p. 502)

## Motivating example

Four collection districts can be compared by an index score without publishing the score’s formula in the comparison itself. Order the districts from the lowest score to the highest and number them 1, 2, 3 and 4. The district with rank 1 is the lowest-scoring district in that list. The same operation, applied to 37,457 collection districts, gives the highest-scoring district rank 37,457. Two districts that look tied after the scores are printed may still have different scores, and therefore different ranks, once the printed rounding is undone.{{cite:abs_seifa2006}} (Glossary, “Rank”)

## Definition

Given values \(X_1,\ldots,X_n\), the rank \(R(X_i)\) is 1 when \(X_i\) is the smallest value, 2 when it is the second smallest, and \(n\) when it is the largest. If several observations share a value, each of them receives the average of the ranks those positions would have occupied.{{cite:dodge2008}} (p. 502) The same convention, lowest score to rank 1 and then upward, is how an index score is turned into an area rank. A state rank restarts the count inside one state, so a district can be rank 79 in the country and rank 1 in its state.{{cite:abs_seifa2006}} (Glossary, “Rank” and “State rank, state decile, state percentile”)

Ranking keeps who is above whom and throws away by how much. A score of 8 and a score of 8.1 receive neighbouring ranks if nothing lies between them, just as a score of 8 and a score of 80 would. The procedure is useful when the measurement scale is arbitrary, or when a later calculation, such as a rank correlation, is defined on positions rather than on the original numbers. It is a poor summary when the gaps themselves are the scientific object.{{cite:dodge2008}} (p. 502)

The ranking uses only the order. Multiplying every score by 10, or adding 100, leaves the ranks unchanged, and so does any other strictly increasing transformation. A transformation that is not strictly increasing can create or break ties. Average ranks are a convention for ties. Another convention, such as assigning the minimum rank in the block to every tied observation, produces different numbers and a different sum. Procedures that assume one of those conventions should name it.{{cite:dodge2008}} (p. 502)

## Properties

For distinct values the ranks are a permutation of \(1,\ldots,n\), and their sum is \(n(n+1)/2\). Average ranks for ties preserve that sum, because a tied block that would have contributed \(k+(k+1)+\cdots+(k+m-1)\) contributes \(m\) copies of the average of those integers, which is the same total. Spearman’s rank correlation is then computed from the differences of these ranks, \(d_i=R(X_i)-R(Y_i)\),
\[
\rho=1-\frac{6\sum_{i=1}^n d_i^2}{n(n^2-1)},
\]
when there are no ties. With ties, the formula is replaced by one that corrects the rank variances.{{cite:dodge2008}} (p. 502)

## Statistical use

Rank the observations before a rank correlation or another procedure that should depend on order and not on the spacing of the scale. Rank areas when the published comparison is a place in a list, and keep the underlying score when two places are close enough that the order could be read too sharply. A rank inside a state answers a different question from a rank in the whole country.{{cite:dodge2008}} (p. 502){{cite:abs_seifa2006}} (Glossary, “Rank”)

## Worked example

The values 8, 3, 8 and 1 sort as 1, 3, 8, 8. The smallest receives rank 1 and the next receives rank 2. The two 8s occupy positions 3 and 4, so each receives the average rank \((3+4)/2=3.5\). In the original order the ranks are 3.5, 2, 3.5 and 1. Their sum is 10, which equals \(4\cdot 5/2\). The tie did not change the sum.{{cite:dodge2008}} (p. 502)

**Your turn.** Rank 4, 1, 4 and 9, using average ranks for the tie. Report the four ranks in the original order and their sum.

::: {.callout-tip collapse="true" title="Answer"}
The ordered values are 1, 4, 4, 9. The ranks are 1 for the unique 1, 2.5 for each 4, and 4 for the 9. In the original order the ranks are 2.5, 1, 2.5 and 4, and the sum is 10.
:::

## Common misconceptions

Rank 1 is the lowest score in this convention, which is the opposite of a prize list that calls the winner rank 1. A printed tie can be an artefact of rounding: two areas may show the same score on the page and still have distinct ranks from their unrounded scores. A state rank of 1 is the lowest area inside that state, and two states therefore each have an area with state rank 1. Those two areas need not have similar scores.{{cite:abs_seifa2006}} (Glossary, “Rank” and “State rank”)

## History

Spearman introduced the rank correlation in 1904, and with it the practice of replacing each observation by its place in the sample, rank 1 for the smallest. Average ranks for tied values are part of that calculation, because the simple difference formula assumes a rank for every observation. Official indexes later used the same lowest-to-highest numbering to publish a place for each area.{{cite:dodge2008}} (p. 502){{cite:abs_seifa2006}} (Glossary, “Rank”)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 13. Their total is 91, so their mean is 7.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 5.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Ranking has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 7.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Summary statistics](summary-statistics.qmd), [Rounding](rounding.qmd), [scatterplot](scatterplot.qmd).

Two further limits are algebraic. The sum of deviations from the mean 7.0 is zero, so the mean is the least-squares centre of these 13 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 7.0.

## Connections

Spearman’s coefficient is a correlation of ranks, and it is one reason ranks are computed at all. [Summary statistics](summary-statistics.qmd) keep the spacing that ranking discards. [Rounding](rounding.qmd) can make two different scores look equal and tempt a reader to treat them as tied. A [scatterplot](scatterplot.qmd) of the original scores still shows the gaps that the ranks have erased.
