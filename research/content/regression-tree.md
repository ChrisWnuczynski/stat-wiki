## Motivating example
A numerical response may change abruptly across a threshold and then remain roughly constant within each region. A regression tree can express such a rule using a sequence of questions about predictor values. Its leaves report numbers, whereas a classification tree reports categories or class probabilities. A piecewise-constant regression tree is especially transparent when a small partition gives a useful description of the response.{{cite:loh2011_trees}} (“Regression trees”, pp. 18–19)

## Definition — One fitted mean per terminal region
For disjoint terminal regions $R_1,\ldots,R_M$, a squared-error regression tree predicts
$$\widehat f(x)=\sum_{m=1}^M\bar y_m\,1\{x\in R_m\},$$
where $\bar y_m$ is the average training response among observations in region $R_m$. A binary split typically asks whether one predictor is below a threshold. Repeating those splits yields rectangular regions and a piecewise-constant prediction function. Other regression trees can fit linear or other parametric models inside leaves; the constant-leaf definition is one important case.{{cite:loh2011_trees}} (“Regression trees”, pp. 18–19)

For a fixed leaf containing responses $y_i$, expanding around their average proves that
$$\sum_i(y_i-c)^2=\sum_i(y_i-\bar y)^2+n_{\rm leaf}(c-\bar y)^2.$$
Therefore the average uniquely minimises that leaf's squared error when the leaf is nonempty. The same mean-minimisation calculation underlies an intercept-only least-squares model. A median, rather than a mean, minimises absolute error, so changing the loss changes the prediction rule.{{cite:openintro2019}} (§8.2, p. 317, sum of squared residuals){{cite:hastie_esl2009}} (pp. 349–350, §10.6, squared error, absolute error, and Huber loss)

## Properties — A greedy split solves a local problem
At a node, consider a predictor and a cut that divide its cases into left and right children. The candidate score is the sum of the two children's residual sums of squares around their respective means. The selected split gives the largest reduction relative to the parent's residual sum of squares. This is a local optimisation over candidate cuts, rather than a global search over every possible tree of a specified size.{{cite:loh2011_trees}} (Algorithm 1 and “Regression trees”, pp. 14 and 18)

If children have sizes $n_L,n_R$ and means $\bar y_L,\bar y_R$, the reduction can be written
$$\Delta=\frac{n_Ln_R}{n_L+n_R}(\bar y_L-\bar y_R)^2.$$
To derive it, apply the mean decomposition separately in each child using the parent mean as $c$. The within-child residual sums cancel, leaving the weighted squared separation between child means. The formula shows how separation and child sizes jointly affect a split, while minimum leaf-size constraints can exclude extreme partitions.

## Worked example — Four observations and three possible cuts
Let predictor values be $(1,2,3,4)$ and responses $(1,2,8,9)$. The parent mean is 5 and its residual sum of squares is 50. A cut at 2.5 creates leaf means 1.5 and 8.5. Each leaf contributes $0.5$ to residual sum of squares, so the total is 1 and the gain is 49. The other distinct cuts, at 1.5 and 3.5, each give total residual sum of squares $86/3=28.666667$. Thus the middle cut is best among these candidates.

For the chosen tree, a predictor value 2.2 receives prediction 1.5 and a value 100 receives prediction 8.5. The latter does not extrapolate a slope: a constant leaf keeps the same number however far a point lies beyond the observed range. This behaviour is a feature of the prediction rule, rather than evidence that the numerical response truly stops changing outside the sample.

**Your turn.** At the middle cut, compute the gain directly from the child sizes and means.

::: {.callout-tip collapse="true" title="Answer"}
There are two cases in each child, so the gain is (2×2/4)(8.5−1.5)²=49.
:::

## Statistical use — Control complexity and assess the full fitting rule
Further splits cannot increase the training residual sum of squares, but the decrease can reflect noise rather than useful predictive structure. Complexity control can use stopping constraints, pruning or a penalty that trades residual error against the number of leaves. The tuning criterion should assess predictions on data not used to fit the candidate partition.{{cite:loh2011_trees}} (Algorithm 1, pruning discussion and “Regression trees”)

A single tree can be unstable because a small sample change can alter an early split and therefore every later region. Averaging trees can reduce that instability, but it changes the fitted model and the interpretation of an individual split. A small tree can still be useful when the goal places substantial value on a compact decision rule.{{cite:loh2011_trees}} (discussion of ensemble methods and tree instability)

## Common misconceptions — Readable partitions do not establish causation
A split compares response patterns among cases with different predictor values. The thresholds and leaf means are fitted summaries of the available observations. Random assignment of a specified treatment is what makes a difference of means informative about an effect in the assigned units. A tree split does not perform that assignment, so a leaf contrast remains a description of the observed partition.{{cite:hernan_robins2020}} (Ch. 2, §2.1, randomization and exchangeability){{cite:loh2011_trees}} (“Regression trees”, pp. 18–19)

## Intuition — The gain formula balances separation and sample size
The reduction $\Delta=n_Ln_R(\bar y_L-\bar y_R)^2/(n_L+n_R)$ is large when the child means are far apart and when both children contain enough cases to make that separation stable in the training sum of squares. A cut that isolates one extreme response can have a large mean gap and a small size factor. In the four-point example the middle cut uses equal child sizes $2$ and $2$ and a mean gap of $7$, so $\Delta=(2\times2/4)\times49=49$. A cut after the first point uses sizes $1$ and $3$. The child means are $1$ and $19/3$, the squared gap is $(16/3)^2=256/9$, and the size factor is $3/4$, so the gain is $(3/4)\times(256/9)=64/3=21.333333$. That matches the residual calculation: the parent sum of squares is $50$ and the one-versus-three split leaves residual sum of squares $86/3$, a reduction of $50-86/3=64/3$. The middle cut wins because it separates two low responses from two high responses, not because it creates the most extreme child mean.{{cite:loh2011_trees}} (“Regression trees”, pp. 18–19)

## Interpretation — Absolute error changes the leaf summary
If a leaf is scored by the sum of absolute deviations, the minimising constant is a median of the responses in that leaf. For the responses $1,2,8,9$ the median of all four points is any number between $2$ and $8$; the usual lower-middle convention is not forced by the criterion, and every constant in $[2,8]$ has the same total absolute deviation $14$. After the middle cut, each child has responses that are symmetric about $1.5$ or $8.5$, so the child medians agree with the child means. The training absolute deviation falls from $14$ to $1+1=2$. A different loss can reorder candidate cuts even when this particular cut remains attractive. The squared-error tree and the absolute-error tree are different procedures once a leaf contains an asymmetric batch.{{cite:hastie_esl2009}} (pp. 349–350, §10.6, squared error, absolute error, and Huber loss)

## Connections
A [spline](spline.qmd) also builds a piecewise function, with smoothness constraints at the joins instead of a constant value on each rectangle. [Underfitting](underfitting.qmd) describes a predictor whose family cannot represent the mean structure that prediction needs. A regression tree with one split can be that kind of predictor when the response changes smoothly rather than in one jump. Growing further leaves reduces training error and still requires a separate assessment of prediction.{{cite:loh2011_trees}} (Algorithm 1, pruning discussion and “Regression trees”)
