

## Lead context

Some tables record only the measurements. There is no column that says what the row turned out to be. Unsupervised learning is the body of methods for that table: describe how the measurements are arranged, without a response to predict.{{cite:james_islr2021}} (Ch. 12, pp. 495–496) {{cite:hastie_esl2009}} (pp. 485–486)

## Motivating example

Four points in the plane, $(2,0)$, $(-2,0)$, $(0,1)$ and $(0,-1)$, have no labels. The horizontal spreads are $2$ and $-2$. The vertical spreads are $1$ and $-1$. The sum of squared horizontal coordinates is $8$ and the sum of squared vertical coordinates is $2$, out of a total of $10$. A one-number summary that keeps the horizontal coordinate keeps $4/5$ of that sum of squares and discards $1/5$. Nothing in the file tells us whether the horizontal direction is the scientifically important one. The calculation only says where the points vary.{{cite:james_islr2021}} (Ch. 12, §12.2, pp. 497–498)

## Definition

Unsupervised learning, or learning without a teacher, observes $x_1,\ldots,x_N$ from a random feature vector $X$ and tries to infer properties of the distribution of $X$. No output $Y$ is supplied, so there is no conditional distribution of $Y$ given $X$ to estimate. In low dimension the density of $X$ itself can be estimated. In high dimension the practical targets are coarser: a low-dimensional set on which the points concentrate, or a mixture of simpler pieces, or regions of high probability described by a simple rule.{{cite:hastie_esl2009}} (pp. 485–487)

The same division can be stated with a finite sample. For each observation one sees features and no response, so a regression of a response on the features cannot be fit. The two tools developed at length are principal components, which represent the rows by a few coordinates of large variation, and clustering, which looks for subgroups.{{cite:james_islr2021}} (Ch. 12, pp. 495–496; Ch. 2, §2.1.4, pp. 26–28)

[Principal component directions](principal-component-directions.qmd) are one unsupervised reduction. [Cluster analysis](cluster-analysis.qmd) is the other standard summary, through [Lloyd's K-means algorithm](lloyd-s-k-means-algorithm.qmd) and [hierarchical clustering](hierarchical-clustering.qmd). Association rules, of which the [Apriori algorithm](apriori-algorithm.qmd) is the usual listing method, describe high-probability combinations in a table of binary items.{{cite:hastie_esl2009}} (pp. 486–487) {{cite:james_islr2021}} (Ch. 12, pp. 495–496, 514–515)

With a response, a loss says whether a rule worked. Without a response, that comparison is unavailable. What remains is a description of the feature distribution: where the density is high, which directions carry the variation, and whether the rows fall into clumps. Those descriptions are judged by whether they are stable and interpretable, not by a misclassification count. The difficulty of that judgement is why so many unsupervised procedures exist side by side.{{cite:hastie_esl2009}} (pp. 486–487)

For the four points $(2,0)$, $(-2,0)$, $(0,1)$ and $(0,-1)$, the coordinate means are zero. The sum of squares on the first coordinate is $2^2+(-2)^2=8$. The sum of squares on the second is $1^2+(-1)^2=2$. The total is $10$. The horizontal fraction is $8/10=4/5$. The vertical fraction is $2/10=1/5$. The first principal component of these four points is the horizontal direction, because no other unit direction has a larger sum of squared scores. Keeping that coordinate is a rank-$1$ reconstruction whose leftover sum of squares is $2$.{{cite:james_islr2021}} (Ch. 12, §12.2.1, pp. 497–498) {{cite:hastie_esl2009}} (p. 535, (14.53))

A clustering of the same four points would ask a different question: which rows form groups, not which direction has variance $4/5$. The two summaries can be computed from the same coordinates and they are not substitutes.{{cite:james_islr2021}} (Ch. 12, pp. 514–515)

There is no training error that goes to zero by memorising a label, because no label was recorded. A procedure that always returns two clusters has not been confirmed by a held-out response. It has produced a partition.{{cite:hastie_esl2009}} (pp. 486–487)

Use an unsupervised method to see the measurements before, or without, a response. A market study that records income, occupation, and shopping habits, and does not record who is a large spender, can still be clustered in the hope that the groups differ in spending. A gene-expression matrix can be reduced to two [principal component](principal-component-directions.qmd) scores so that the samples can be plotted at all. Those scores are also a preprocessor: a later [supervised learning](supervised-learning.qmd) fit may use them as inputs once a response becomes available.{{cite:james_islr2021}} (Ch. 2, pp. 26–28; Ch. 12, pp. 495–498)

The absence of a response changes the standard of proof. Cross-validation of a prediction error does not choose the number of clusters. A picture of the within-cluster criterion against the number of groups is a heuristic, and a comparison with uniform points in a rectangle around the data is one way to read that picture. Neither device is a test-set error.{{cite:hastie_esl2009}} (pp. 486–487, 519–520)

Unsupervised learning is not classification with the labels hidden in the analyst's desk. If the labels exist and are used, the problem is supervised. A clustering that is later compared with a cancer type may look confirmed, and the comparison is still not what the clustering optimised.{{cite:james_islr2021}} (Ch. 12, pp. 495–496; Ch. 1, pp. 4–5)

The direction with fraction $4/5$ is not automatically the direction that predicts a response one might collect tomorrow. Principal components ignore any response. A low-variance coordinate can be the predictive one.{{cite:james_islr2021}} (Ch. 6, §6.3.1, pp. 253–255; Ch. 12, pp. 497–498)

A hierarchy or a partition is not validated by the fact that the algorithm returned it. High-dimensional density estimates fail, and the coarser summaries that replace them do not carry a built-in measure of success.{{cite:hastie_esl2009}} (pp. 486–487)

The descriptions assume that the recorded features are the variables whose arrangement matters. A distance or a variance computed from a badly scaled feature answers a question about the units, not about the subject. The four-point fractions $4/5$ and $1/5$ would change if the vertical coordinate were multiplied by ten.{{cite:james_islr2021}} (Ch. 12, §12.2, pp. 497–498)

Density estimation in the ambient dimension is not available once $p$ is more than a few. The move to components, clusters, or association rules is a retreat to a simpler property of the distribution, and a simpler property can be the wrong property.{{cite:hastie_esl2009}} (pp. 485–487)

## Worked example

The points $(2,0)$, $(-2,0)$, $(0,1)$ and $(0,-1)$ are already centred. Horizontal sum of squares: $4+4=8$. Vertical sum of squares: $1+1=2$. Total: $10$. The leading principal component retains the fraction $4/5$. The second component retains $1/5$. A reconstruction that keeps only the horizontal coordinate replaces the four points by $(2,0)$, $(-2,0)$, $(0,0)$ and $(0,0)$, and the sum of squared reconstruction errors is $2$.

**Your turn.** What fraction of the sum of squares sits on the vertical coordinate?

::: {.callout-tip collapse="true" title="Answer"}
The vertical sum of squares is $2$ out of $10$, so the fraction is $1/5$.
:::

## Connections

[Supervised learning](supervised-learning.qmd) is the parallel enterprise with a response. [Cluster analysis](cluster-analysis.qmd) collects the partition and the tree, including [hierarchical clustering](hierarchical-clustering.qmd) and the [K-means criterion](k-means-criterion.qmd). [Dimensionality reduction](dimensionality-reduction.qmd) is the principal-component summary and its nonlinear relatives. [Classification](classification.qmd) begins only when a class label is present to be predicted.{{cite:james_islr2021}} (Ch. 12, pp. 495–496, 514–515) {{cite:hastie_esl2009}} (pp. 485–487)

## History

The organised contrast between learning with a teacher and learning without one is the framework of the statistical-learning texts: most of the early chapters are supervised, and the unsupervised methods are gathered in a later chapter. Principal components and clustering are the two unsupervised tools those introductions develop in full. Association rules were added for the special case of very high-dimensional binary shopping data, where a density estimate is hopeless and a list of frequent item sets is not.{{cite:hastie_esl2009}} (pp. 485–487) {{cite:james_islr2021}} (Ch. 12, pp. 495–496)
