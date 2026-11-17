## Lead context

Four districts lie in a line. Their values are 1, 2, 4, and 5. The large numbers sit next to each other, and so do the small ones. A correlation of the values with themselves is not defined in the ordinary way, because there is only one list. What can be computed is a correlation of each value with its neighbours.

Moran's \(I\) is that index. It is large and positive when similar values cluster, and negative when neighbours tend to be unlike. A single number does not say whether the map is surprising. That requires a comparison with maps in which the same values have been reassigned.{{cite:moraga2023}} (§8.1){{cite:rey_gds2020}} (§8.3.3)

## Motivating example

House prices, election shares, and disease rates are reported for areas. A choropleth map shows clusters, and the eye is quick to find them. The same values, painted onto the areas at random, also produce patches. People are good at seeing patterns, including patterns that a random painting would have produced. Moran's \(I\) measures the association that is actually in the neighbour relation, and a randomisation test asks how often a random painting would have produced an index at least as large. The areas stay where they are. Only the numbers move. That is the null used for the usual significance statement: a reassignment of the observed values, not a model in which new areas are drawn from an infinite population.{{cite:rey_gds2020}} (§8.3){{cite:moraga2023}} (§8.1)

On the Boston census tracts of 1978, the median prices of owner-occupied housing give a global Moran's \(I\) of about \(0.627\) under queen contiguity, against an expectation of about \(-0.002\). The positive index matches a map in which expensive tracts sit near expensive tracts. The expectation is near zero because, under no correlation, the formula centres near \(-1/(n-1)\), which for hundreds of tracts is a small negative number. A small positive index is therefore not automatically evidence of clustering. The distance from \(-1/(n-1)\) is the comparison.{{cite:moraga2023}} (§8.1 and §8.2)

## Intuition

Centre the values by subtracting their mean. A neighbour pair in which both deviations have the same sign contributes a positive product. A pair with opposite signs contributes a negative product. Weight each product by how strongly the two areas are treated as neighbours, add the products, and compare the total with the overall sum of squared deviations. The ratio is large when the map is smooth. Standardising the deviations does not change the ratio, because the scale appears in every product and in the sum of squares. The weights are a choice. A shared border, a distance band, or a fixed number of nearest areas will not give the same index.{{cite:moraga2023}} (§8.1){{cite:rey_gds2020}} (§8.3.1 and §8.3.3)

In a row-standardised weights matrix the spatial lag of an area is a weighted average of its neighbours. A Moran scatterplot puts the value on one axis and that lag on the other. The slope of the fitted line is Moran's \(I\). A positive slope means high values sit near high values and low values sit near low values. The sign of the values themselves is not the question. High next to high and low next to low both raise the slope.{{cite:rey_gds2020}} (§8.3.3)

## Definition

Let \(Y_1,\ldots,Y_n\) be the values on \(n\) areas, with mean \(\bar Y\), and let \(w_{ij}\) be a spatial weight, with \(w_{ii}=0\). Moran's \(I\) is
\[
I=\frac{n}{\sum_i\sum_j w_{ij}}\frac{\sum_i\sum_j w_{ij}(Y_i-\bar Y)(Y_j-\bar Y)}{\sum_i(Y_i-\bar Y)^2}.
\]
The denominator of the leading fraction is the sum of all weights. The fraction that follows is a weighted covariance of the values with their neighbours, divided by the variance of the values. Positive \(I\) means clustering of similar values. Negative \(I\) means that neighbours are dissimilar. Values usually fall between \(-1\) and \(1\), and the reference point under no spatial pattern is
\[
E[I]=-\frac{1}{n-1},
\]
not zero. An index significantly above that expectation is read as positive autocorrelation. An index significantly below it is read as negative autocorrelation.{{cite:moraga2023}} (§8.1){{cite:rey_gds2020}} (§8.3.3)

## Statistical use

The index is the standard global summary for a continuous variable on areas, after a binary join-count for presence and absence. It is reported with the weights, not as a bare number. For a large number of areas the centred index, divided by an estimated standard deviation, is compared with a standard normal reference. The alternative that does not use that normal approximation is Monte Carlo randomisation: reassign the observed values to the fixed areas, recompute \(I\), and repeat. The Monte Carlo \(p\)-value is the proportion of reassigned maps whose index is at least as extreme as the observed index, in the direction of the alternative.{{cite:moraga2023}} (§8.1 and §8.2){{cite:rey_gds2020}} (§8.3.3)

A local version \(I_i\) can be computed for each area. One definition is
\[
I_i=\frac{n(Y_i-\bar Y)}{\sum_j(Y_j-\bar Y)^2}\sum_j w_{ij}(Y_j-\bar Y),
\]
and the global index is proportional to the sum of the local indices. A global signal can therefore be opened into a map of where the association is strong. A high local index means the area is surrounded by similar values. A low local index means it is surrounded by dissimilar values. The local map still needs its own reference distribution, because a large \(I_i\) is not by itself a significance statement.{{cite:moraga2023}} (§8.4)

## Worked example

Four areas, A–B–C–D, are neighbours only along the line. The binary weights are 1 for each ordered neighbour pair and 0 otherwise, so \(S_0=\sum_i\sum_j w_{ij}=6\). The values are 1, 2, 4, and 5. Their mean is 3, and the deviations are \(-2,-1,1,2\). The sum of squared deviations is \(4+1+1+4=10\). The neighbour products, counting both directions, are
\[
2\bigl[(-2)(-1)+(-1)(1)+(1)(2)\bigr]=2(2-1+2)=6.
\]
Therefore
\[
I=\frac{4}{6}\cdot\frac{6}{10}=0.4.
\]
The positive value matches the map: low values share a border, and high values share a border. The expectation under the usual no-pattern reference is \(-1/3\), so \(0.4\) sits above that reference. With only four areas the normal approximation is not the tool the large-sample formula was built for. The sign and the arithmetic of \(I\) are still well defined.{{cite:moraga2023}} (§8.1)

**Your turn.** Keep the same four areas and the same weights. The values are now 1, 2, 2, and 1. What is Moran's \(I\)?

::: {.callout-tip collapse="true" title="Answer"}
The mean is 1.5 and the deviations are -0.5, 0.5, 0.5, and -0.5. The sum of squared deviations is 1. The sum of weighted neighbour products is -0.5. Then \(I = (4/6) \times (-0.5)/1 = -1/3\). Neighbours tend to lie on opposite sides of the mean.
:::

## Common misconceptions

A large \(I\) is not by itself a significance statement. The same values shuffled across the areas produce a cloud of indices, and the observed index is judged against that cloud. In the Boston tract calculation the expectation was about \(-0.002\), so the observed \(0.627\) is far from the null centre. A value of \(0.05\) on a map with the same expectation would be a different claim.{{cite:moraga2023}} (§8.2){{cite:rey_gds2020}} (§8.3.3)

A positive index means similar values are neighbours, not that the values are high. High next to high and low next to low both raise \(I\). Geary's \(C\) is a different global index of the same idea. It uses squared differences of the raw values rather than products of standardised deviations, and it need not be converted into \(I\) by a fixed formula. Getis and Ord's \(G\) is aimed at concentration of high or low values and does not pick up negative autocorrelation. Reporting one of them as if it were the others changes the question.{{cite:rey_gds2020}} (§8.3.4){{cite:moraga2023}} (§8.1)

## Connections

Moran's \(I\) is the areal index most often paired with Geary's \(C\) inside [spatial analysis](spatial-analysis.qmd). The [variogram](variogram.qmd) answers a related question for measurements at coordinates: how fast similarity decays with distance. An [autocorrelation function](autocorrelation-function.qmd) does the analogous job for a series ordered in time. A local Moran statistic is the map that the global index averages over. The spatial lag that appears in the Moran scatterplot is the same lag that a spatial regression uses as a predictor, which is why a global \(I\) is often the first summary before a spatial model is fitted. The weights remain part of the answer. A queen contiguity and a \(k\)-nearest-neighbour graph are different neighbour relations, and each produces its own \(I\).{{cite:rey_gds2020}} (§8.3.1 and §8.3.3){{cite:moraga2023}} (§8.1 and §8.4)
