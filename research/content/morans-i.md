

## Lead context

Four districts lie in a line. Their values are 1, 2, 4, and 5. The large numbers sit next to each other, and so do the small ones. A correlation of the values with themselves is not defined. What can be computed is a correlation of each value with its neighbours. Moran's I is that index. It is large and positive when similar values cluster, and negative when neighbours tend to be unlike. A single number does not say whether the map is surprising. That requires a comparison with maps in which the same values have been shuffled.

## Motivating example

House prices, election shares, and disease rates are reported for areas. A choropleth map shows clusters, and the eye is quick to find them. The same values, painted onto the areas at random, also produce patches. Moran's I measures the association that is actually in the neighbour relation, and a randomisation test asks how often a random painting would have produced an index at least as large. The areas stay where they are. Only the numbers move. That is the null used for the usual significance statement: not a model in which areas are independent draws from an infinite population, but a reassignment of the observed values.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3)

## Intuition

Centre the values by subtracting their mean. A neighbour pair in which both deviations have the same sign contributes a positive product. A pair with opposite signs contributes a negative product. Weight each product by how strongly the two areas are treated as neighbours, add the products, and compare the total with the overall sum of squared deviations. The ratio is large when the map is smooth. Dividing by a standard deviation instead of using raw deviations does not change the ratio, because the scale appears in every product and in the sum of squares. The weights are a choice. A shared border, a distance band, or a fixed number of nearest areas will not give the same index.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3)

## Definition

Let $Y_1,\ldots,Y_n$ be the values on $n$ areas, with mean $\bar Y$, and let $w_{ij}$ be a spatial weight, with $w_{ii}=0$. Moran's I is

$$
I=\frac{n}{\sum_i\sum_j w_{ij}}\frac{\sum_i\sum_j w_{ij}(Y_i-\bar Y)(Y_j-\bar Y)}{\sum_i(Y_i-\bar Y)^2}.
$$

The denominator of the leading fraction is the sum of all weights. The fraction that follows is a weighted covariance of the values with their neighbours, divided by the variance of the values. The same ratio is obtained if the deviations are replaced by standardised values, because the scale cancels. Positive $I$ means clustering of similar values. Negative $I$ means that neighbours are dissimilar.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3)

The index is not a property of the list of numbers alone. Change the weights and $I$ changes. If every weight is zero the expression is undefined, which matches the fact that a neighbour relation was never stated. Under a random reassignment of the observed values to the fixed areas, the index has a reference distribution that can be built by simulation: shuffle the values, recompute $I$, and repeat. The Monte Carlo p-value is the proportion of shuffled maps whose index is at least as extreme as the observed index, in the direction of the alternative. A local version $I_i$ can be computed for each area. The global index is proportional to the sum of the local indices, so a global signal can be opened into a map of where the association is strong.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3)

The weights are assumed, not estimated, in the basic index. A queen contiguity and a distance band answer different neighbour questions. The randomisation null keeps the areas fixed and permutes the values, so it does not describe a super-population from which new areas might be drawn. Dependence induced by a common missing covariate can look like spatial autocorrelation. The index is a summary of linear association between a value and its lag. A pattern in which extremes cluster, while moderate values do not, can be faint in $I$ and visible in another global index.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3)

Patrick Moran introduced the index for the reading of statistical maps. The 1948 paper on the interpretation of statistical maps and the 1950 paper on continuous stochastic phenomena are the two sources to which the modern formula is traced. Local indicators were added later so that a single $I$ could be decomposed by area. The scatterplot reading, in which $I$ is the slope of the value against its spatial lag, is the form in which the index is now usually explained.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3)

## Statistical use

The index is the standard global summary for a continuous variable on areas, after a binary join-count for presence and absence. It is reported with the weights, not as a bare number. In a row-standardised weights matrix the spatial lag of an area is a mean of its neighbours, and a Moran scatterplot puts the value on one axis and that lag on the other. The slope of the fitted line is Moran's I. Software that returns a normal approximation also returns an expectation and a variance under randomisation. In the Boston tract example that expectation was about $-0.002$, so a small positive index is not automatically evidence of clustering. The randomisation test does not require that normal approximation.{{cite:rey_gds2020}} (Ch. 8, §8.3.3){{cite:moraga2023}} (Ch. 8)

## Worked example

Four areas, A–B–C–D, are neighbours only along the line. The binary weights are 1 for each ordered neighbour pair and 0 otherwise, so $S_0=\sum_i\sum_j w_{ij}=6$. The values are 1, 2, 4, and 5. Their mean is 3, and the deviations are $-2,-1,1,2$. The sum of squared deviations is $4+1+1+4=10$. The neighbour products, counting both directions, are

$$
2\bigl[(-2)(-1)+(-1)(1)+(1)(2)\bigr]=2(2-1+2)=6.
$$

Therefore

$$
I=\frac{4}{6}\cdot\frac{6}{10}=0.4.
$$

The positive value matches the map: low values share a border, and high values share a border.{{cite:moraga2023}} (Ch. 8)

**Your turn.** Keep the same four areas and the same weights. The values are now 1, 2, 2, and 1. What is Moran's I?

::: {.callout-tip collapse="true" title="Answer"}
The mean is 1.5 and the deviations are -0.5, 0.5, 0.5, and -0.5. The sum of squared deviations is 1. The sum of weighted neighbour products is -0.5. Then I = (4/6) × (-0.5)/1 = -1/3. Neighbours tend to lie on opposite sides of the mean.
:::

## Common misconceptions

A large $I$ is not by itself a significance statement. The same values shuffled across the areas produce a cloud of indices, and the observed index is judged against that cloud. A positive index means similar values are neighbours, not that the values are high. High next to high and low next to low both raise $I$. Geary's $C$ is a different global index of the same idea and need not be converted into $I$ by a fixed formula.{{cite:rey_gds2020}} (Ch. 8, §8.3.3){{cite:moraga2023}} (Ch. 8)

## Connections

Moran's I is the areal index most often paired with Geary's $C$ inside [spatial analysis](spatial-analysis.qmd). The [variogram](variogram.qmd) answers a related question for measurements at coordinates: how fast similarity decays with distance. An [autocorrelation function](autocorrelation-function.qmd) does the analogous job for a series ordered in time. A local Moran statistic is the map that the global index averages over. Using a rate in place of a count, when population varies, is what keeps the index from rediscovering where the people live.{{cite:moraga2023}} (Ch. 8){{cite:dodge2008}} (p. 501)
