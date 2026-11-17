## Lead context
Ranking replaces each observation by its place in the ordered sample.

The smallest value receives rank \(1\), the next rank \(2\), and so on, unless a tie forces two or more values to share the places they jointly occupy. The average of those places is then the rank of each tied value. Spearman's rank correlation, introduced in 1904, is the oldest widely used statistic that works entirely with those places.{{cite:dodge2008}} (p. 502)

## Motivating example
Four finishing times, in minutes, are \(8\), \(3\), \(8\), and \(1\). The clock readings carry the size of the gaps: the two \(8\)s are five minutes behind the \(3\), and the \(1\) is only two minutes ahead of the \(3\). A rank summary throws the minutes away and keeps the order. The question it can still answer is who finished ahead of whom, including the fact that two runners finished together. It cannot answer how many minutes separated first from last.{{cite:dodge2008}} (p. 502)

## Definition
Order the sample from smallest to largest. If all \(n\) values are distinct, the ranks are \(1, 2, \ldots, n\) in that order, written back against the original positions. If several observations have exactly the same value, each of them receives the average of the ranks those positions would have taken. For two values tied at the top of a list of four, the places \(3\) and \(4\) average to \(3.5\), and both tied values are ranked \(3.5\).

Spearman's coefficient uses two such rankings. If there are many average ranks, the coefficient uses a correction. With \(g\) tied groups in the first sample, of sizes \(t_i\),
\[
S_x=\frac{n(n^2-1)-\sum_{i=1}^{g}(t_i^3-t_i)}{12},
\]
and likewise \(S_y\) for the second sample. The coefficient is then built from \(S_x\), \(S_y\), and the sum of squared rank differences. When there are no ties, each observation is a group of size \(1\), and \(t^3-t=0\), so the correction vanishes.{{cite:dodge2008}} (p. 502)

## Properties
The ranks of \(n\) observations, with average ranks for ties, still sum to \(n(n+1)/2\), the sum of the first \(n\) positive integers. Averaging the shared places is what keeps that identity. Giving every member of a tie the lowest place in the tie, or the highest, would change the sum.

For the times \(8\), \(3\), \(8\), and \(1\), the ordered values are \(1\), \(3\), \(8\), \(8\). The ranks in that order are \(1\), \(2\), \(3.5\), \(3.5\). Written against the original order they are \(3.5\), \(2\), \(3.5\), and \(1\), and
\[
3.5+2+3.5+1=10=\frac{4\cdot 5}{2}.
\]
The two \(8\)s were five minutes from the \(3\) and seven minutes from the \(1\). Their ranks differ from the rank of \(3\) by \(1.5\) and from the rank of \(1\) by \(2.5\). The rank gaps are not proportional to the time gaps. That disproportion is the point of the replacement: the scale of the measurement has been discarded.{{cite:dodge2008}} (p. 502)

A monotone transformation that does not change the order does not change the ranks. Replacing each time by its logarithm, or by any strictly increasing function, leaves \(3.5\), \(2\), \(3.5\), and \(1\) where they are. A transformation that is not monotone can change them.

## Statistical use
Use ranks when the scientific comparison is about order, or when the raw scale is arbitrary but the order is not. Spearman's coefficient then measures agreement between two rankings on a scale from \(-1\) to \(+1\). In the Reproducibility Project, original and replication effect sizes were positively associated, with Spearman's \(r=0.51\).{{cite:osc2015}} (Results) A rank test of location compares the ranks in two or more groups rather than the raw measurements, which limits the influence of one wild value: that value receives the last place, and the size of its excess over the next value never enters the statistic.

The price is power against alternatives that live in the spacing.{{cite:dodge2008}} (p. 502) If the groups differ by a shift on a scale that is already well measured, the raw measurements use that spacing and the ranks ignore it. Average ranks also need the tie correction in Spearman's formula once ties are common. Ignoring the correction treats tied values as if they had been distinct.{{cite:dodge2008}} (p. 502)

## Worked example
The times \(8\), \(3\), \(8\), and \(1\) have ranks \(3.5\), \(2\), \(3.5\), and \(1\) in that order, and the ranks sum to \(10\). The tied pair occupies places \(3\) and \(4\). Their average, \(3.5\), is the rank of each.

**Your turn.** Rank \(4\), \(1\), \(4\), and \(9\), using average ranks for the tie. Report the four ranks in the original order and their sum.

::: {.callout-tip collapse="true" title="Answer"}
The ordered values are \(1\), \(4\), \(4\), \(9\). The ranks in that order are \(1\), \(2.5\), \(2.5\), and \(4\). In the original order they are \(2.5\), \(1\), \(2.5\), and \(4\), and they sum to \(10\).
:::

## Common misconceptions
Rank \(1\) is the smallest value in the convention used here, not a judgement that the smallest value is the best. A race that scores the fastest time as first place is using the opposite orientation. The arithmetic of average ranks is the same after the orientation is reversed, but the number attached to a given runner is not.

A tie is not two observations with the same rank chosen arbitrarily. The average of the shared places is fixed by the places, not by a preference for the lower or the upper number. Assigning both of the tied \(8\)s the rank \(3\), and nobody the rank \(4\), would make the ranks sum to \(9\) rather than \(10\).

Spearman's coefficient is not the Pearson correlation of the raw values. It is a correlation of the ranks. Two series can have a modest Pearson correlation and a Spearman correlation of \(1\) when one series is a strictly increasing curve of the other.{{cite:dodge2008}} (p. 502)

## History
Spearman, a psychologist, introduced the rank correlation in 1904. Dodge calls it one of the oldest rank statistics. The average-rank rule for ties is part of the same definition: several observations with exactly the same value receive one shared rank, the average of the places they occupy, and the formula for the coefficient then corrects \(S_x\) and \(S_y\) by \(\sum(t^3-t)\).{{cite:dodge2008}} (p. 502)

## Connections
[Spearman's rank correlation coefficient](spearman-s-rank-correlation-coefficient.qmd) is the agreement measure built from two rankings. A rank transformation is a [data reduction](raw-data.qmd) that keeps order and discards spacing. The [median](median.qmd) is the middle place of the ordered sample, so it is already a function of ranks. Methods that replace measurements by ranks in order to limit the pull of a wild value sit with [robust statistics](robust-statistics.qmd).{{cite:dodge2008}} (p. 502)
