## Lead context

Ten measurements on each case are more than a scatterplot can show, and most of those measurements repeat a few underlying contrasts. Dimensionality reduction replaces the long list with a short list of coordinates that still carries most of the variation, or most of the shape, of the original list.{{cite:james_islr2021}} (Ch. 6, §6.3, pp. 252–255; Ch. 12, §12.2, pp. 497–498) {{cite:hastie_esl2009}} (p. 535, §14.5)

## Motivating example

Three points sit at $(1,1)$, $(2,2)$ and $(3,3)$. Two coordinates are written down for each point, and the second coordinate is a copy of the first. A plot needs only the position along the diagonal. The sum of squared distances from the mean $(2,2)$ is $4$, and every one of those four units lies along the direction $(1,1)$. A summary that keeps the horizontal coordinate and throws the vertical one away keeps only $2$ of the $4$. The reduction is honest when the discarded part is small, and it is a different analysis when the discarded part is half the variation.{{cite:james_islr2021}} (Ch. 12, §12.2.1, pp. 497–498)

## Intuition

Not every direction in a feature list is equally informative. Principal components look for the directions in which the points spread the most, then the most among the remaining directions, and they stop after a few of those directions. The coordinates of the points along the kept directions are the reduced representation. Projecting a point onto a line is the same operation as replacing the point by the closest point on that line.{{cite:james_islr2021}} (Ch. 6, §6.3.1, pp. 253–254) {{cite:hastie_esl2009}} (p. 535, (14.49)–(14.53))

## Definition

Dimension reduction, in the regression setting, builds $M$ new predictors from $p$ original ones, with $M$ smaller than $p$, and then fits the response using only the new predictors. The constraint can lower the variance of the fitted coefficients when $p$ is large relative to the sample size, at the price of a possible bias. If $M=p$ and the new predictors are linearly independent, nothing has been reduced, and the fit is ordinary least squares on the original features.{{cite:james_islr2021}} (Ch. 6, §6.3, pp. 252–253)

The usual construction is principal components. The first principal component of features $X_1,\ldots,X_p$ is the normalised linear combination
\[
Z_1=\phi_{11}X_1+\cdots+\phi_{p1}X_p,\qquad \sum_{j=1}^p\phi_{j1}^2=1,
\]
whose variance is as large as that normalisation allows. The loadings $\phi_{j1}$ are the direction. Later components are further normalised combinations, uncorrelated with the earlier ones, each with as much variance as remains.{{cite:james_islr2021}} (Ch. 12, §12.2.1, pp. 497–498, (12.1))

The same construction is the least-squares fit of an affine subspace of rank $q$. With centred points, the fitted subspace is the span of the first $q$ right singular vectors of the data matrix, and the reconstruction of each point is its orthogonal projection onto that subspace.{{cite:hastie_esl2009}} (p. 535, §14.5, (14.49)–(14.54))

A separate family of methods looks for a nonlinear manifold. Local multidimensional scaling and its relatives try to flatten a curved low-dimensional set that sits inside a high-dimensional feature space, using neighbourhoods rather than a single linear subspace. They are still dimensionality reduction: the output is a short list of coordinates for each point.{{cite:hastie_esl2009}} (pp. 572–573, §14.9)

## Properties

For the three collinear points, the centred vectors are $(-1,-1)$, $(0,0)$ and $(1,1)$. The total sum of squares is $1+1+0+0+1+1=4$. The unit diagonal direction $(1/\sqrt{2},1/\sqrt{2})$ gives scores $-\sqrt{2}$, $0$ and $\sqrt{2}$, and the sum of squared scores equals $4$. The fraction retained is $4/4=1$. The horizontal direction $(1,0)$ gives scores $-1$, $0$ and $1$, sum of squares $2$, and fraction $1/2$. The discarded sum of squares is $4-2=2$.

That comparison is the population version of the principal-component criterion: among unit directions, the diagonal maximises the sum of squared scores, and the reconstruction error of the rank-$1$ fit along that direction is $0$. The horizontal direction is a legal unit vector and a worse summary.{{cite:hastie_esl2009}} (p. 535, (14.53)) {{cite:james_islr2021}} (Ch. 6, §6.3.1, pp. 253–254)

In a regression, the reduced coordinates $Z_1,\ldots,Z_M$ are computed from the features and the response is then regressed on them. This is principal components regression when the coordinates are the leading components. The loadings in that construction are chosen from the features alone. They do not look at the response.{{cite:james_islr2021}} (Ch. 6, §6.3.1, pp. 253–255)

Use a reduction to look at a high-dimensional sample. With $p=10$ features there are $45$ pairwise scatterplots, and none of them contains more than two of the measurements. Two principal-component scores are one plot that has tried to keep the variation. The same scores are a preprocessor for a later [supervised learning](supervised-learning.qmd) fit, and a device for filling missing entries once a low-rank reconstruction is accepted.{{cite:james_islr2021}} (Ch. 12, §12.2, pp. 497–498)

The directions themselves are the subject of the page on [principal component directions](principal-component-directions.qmd). Choosing how many to keep is a separate decision: $M=p$ undoes the reduction, and a very small $M$ can throw away a direction that carried the response even though it carried little feature variance. Partial least squares is the alternative, inside the same two-step scheme, that does look at the response when it builds the coordinates.{{cite:james_islr2021}} (Ch. 6, §6.3, pp. 252–255)

## Worked example

The points $(1,1)$, $(2,2)$ and $(3,3)$ have mean $(2,2)$. Centred, they are $(-1,-1)$, $(0,0)$ and $(1,1)$. The total sum of squares equals $4$. Along the unit diagonal the three scores are $-\sqrt{2}$, $0$ and $\sqrt{2}$, and $(-\sqrt{2})^2+0+(\sqrt{2})^2=4$. The fraction of the sum of squares on that first component is $1$. Along the horizontal axis the scores are $-1$, $0$ and $1$, the retained sum of squares is $2$, and the fraction is $1/2$.

**Your turn.** If only the horizontal coordinate of these centred points is kept, what fraction of the sum of squares is retained, and what sum of squares is discarded?

::: {.callout-tip collapse="true" title="Answer"}
The retained fraction is $1/2$. The discarded sum of squares is $2$.
:::

## Assumptions and limits

The linear construction assumes that a flat subspace is a fair summary. Points that lie on a curve, such as a spiral or a bent arm of a digit, are poorly described by the first few singular vectors, which is why the nonlinear manifold methods exist. Those methods in turn assume that neighbourhoods in the feature space follow the manifold, and a neighbourhood that jumps to a different branch flattens the wrong thing.{{cite:hastie_esl2009}} (p. 535, §14.5; pp. 572–573, §14.9)

The fraction $1$ in the worked example is a statement about these three points. It is not a promise about a fourth point placed off the diagonal. A new point at $(1,0)$, centred against the same mean, is not reconstructed by the diagonal with error zero.{{cite:hastie_esl2009}} (p. 535, (14.50))

A reduction is not a [cluster analysis](cluster-analysis.qmd). Components summarise directions of variation. Clusters summarise groups of rows. Both can be drawn on the same picture, and they optimise different criteria.{{cite:james_islr2021}} (Ch. 12, pp. 514–515)

The first component is not the direction most aligned with a response, unless the response was used to choose it. Principal components regression can miss a low-variance feature that is the useful predictor. The variance ranking and the predictive ranking are different rankings.{{cite:james_islr2021}} (Ch. 6, §6.3.1, pp. 253–255)

Scaling changes the directions. A feature recorded in small units dominates the sum of squares if the columns are not put on a comparable scale. The three-point example hid that choice because the two coordinates were already on the same scale and were copies of each other.{{cite:james_islr2021}} (Ch. 12, §12.2, pp. 497–498)

## Connections

The coordinates and the directions are set out on [principal component directions](principal-component-directions.qmd). Using those coordinates before a regression is a step inside [supervised learning](supervised-learning.qmd). Using them to look at the features alone is part of [unsupervised learning](unsupervised-learning.qmd). [Cluster analysis](cluster-analysis.qmd) is the other standard unsupervised summary, and it groups points rather than directions.{{cite:james_islr2021}} (Ch. 12, pp. 495–498, 514–515)

Principal components, as a numerical fit of a low-rank affine model by least squares and the singular value decomposition, are the classical linear reduction.{{cite:hastie_esl2009}} (p. 535, §14.5) The regression use of the same scores, holding the response out of the construction of the loadings, is the dimension-reduction step developed for linear model selection.{{cite:james_islr2021}} (Ch. 6, §6.3, pp. 252–255) Nonlinear flattening of a manifold, by local multidimensional scaling and related neighbourhood methods, is a later addition aimed at structure that a flat subspace cannot keep.{{cite:hastie_esl2009}} (pp. 572–573, §14.9)
