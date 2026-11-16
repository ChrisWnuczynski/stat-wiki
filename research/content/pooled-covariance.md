## Motivating example
Two species can have sharply different average flower sizes yet similar variation around each species mean. Combining all flowers and computing one covariance around the grand mean would mix the species gap with variation within a species. Pooling centres each group separately before combining its scatter. That gives an estimate of the shared within-group covariance needed for a two-sample comparison or a linear discriminant rule. Fisher's original iris analysis used within-species sums of squares and cross-products for precisely this separation.{{cite:fisher1936}} (§II, pp. 179–181){{cite:nist_poolcov1998}} (Description and Program 2)

## Intuition
Covariance describes how features vary together around a mean. If group means differ, the grand mean is the wrong centre for estimating the variability *inside* either group. Subtracting each group's own mean removes its location before the residual outer products are added. Each group loses one degree of freedom because its mean was estimated from the same observations; with $G$ nonempty groups and $n$ observations in total, the pooled divisor is $n-G$. Equivalently, if $S_g$ is the usual sample covariance of group $g$, the pooled matrix is $S=\sum_g(n_g-1)S_g/(n-G)$.{{cite:nist_poolcov1998}} (Description; Program 2, pooled formula)

The resulting matrix can be computed whether or not the group covariances are equal, but its interpretation as an estimate of one common $\Sigma$ relies on that assumption. A covariance matrix with different values for each class calls for a different model, such as quadratic rather than linear Gaussian discrimination. The divisor $n-G$ provides an unbiased estimate when independent groups truly share a covariance; maximum likelihood under a common Gaussian model uses divisor $n$ instead. These two conventions should not be silently interchanged.{{cite:nist_poolcov1998}} (Description and Program 2){{cite:clemmensen2011_sda}} (§2.1, pp. 3–4, pooled Gaussian estimator)

## Definition
For group $g$ with observations $\mathbf x_{gi}\in\mathbb R^p$, sample size $n_g$ and sample mean $\bar{\mathbf x}_g$, put $n=\sum_g n_g$. The general pooled covariance is

$$
S=\frac{1}{n-G}\sum_{g=1}^G\sum_{i=1}^{n_g}(\mathbf x_{gi}-\bar{\mathbf x}_g)(\mathbf x_{gi}-\bar{\mathbf x}_g)^\top,
\qquad n>G.
$$

The two-group formula above is its special case. Each outer product is a $p\times p$ matrix, so pooling retains cross-covariances as well as individual variances. The condition $n>G$ is needed for a nonzero divisor, and a usable ordinary inverse additionally needs full rank. The expression is a within-group estimate; it does not estimate the covariance of a population in which the group label itself varies and the means differ.{{cite:nist_poolcov1998}} (Description; Program 2)

## Interpretation
The pooled matrix also enters Hotelling's two-sample $T^2$ statistic. Under independent multivariate-normal groups with the same positive-definite population covariance, the group means and residual scatter have special normal and Wishart laws, making an exact $F$ reference law possible. Pooling without a shared covariance, normality, or a nonsingular $S$ does not retain that exact test calibration. These assumptions belong to the probability statement, not to the arithmetic operation of summing residual products.{{cite:nist_poolcov1998}} (Description and Applications){{cite:clemmensen2011_sda}} (§2.1, pp. 3–4, common-covariance Gaussian model)

## Properties
The pooled matrix is symmetric and positive semidefinite because $\mathbf v^\top S\mathbf v$ is a sum of squared within-group projected deviations divided by $n-G$. Its rank is at most $\min(p,n-G)$: centring each group makes one linear relation among its rows. Thus if $p>n-G$, an ordinary inverse cannot exist, regardless of the numerical covariance entries. Even with $p\le n-G$, collinear measured features can leave it singular. This matters for LDA and the $T^2$ formula, both of which ask for $S^{-1}$.{{cite:clemmensen2011_sda}} (§§1–2.1, pp. 1, 3–4, high-dimensional singularity)

Pooling is also related to a precise within/between decomposition. Let $A_g$ be group $g$'s scatter matrix and $\bar{\mathbf x}$ the grand mean. The total scatter around the grand mean is $\sum_g A_g+\sum_g n_g(\bar{\mathbf x}_g-\bar{\mathbf x})(\bar{\mathbf x}_g-\bar{\mathbf x})^\top$. The second term cannot be negative in any direction. A grand-mean covariance therefore includes variation from group locations that the pooled within-group covariance deliberately leaves out. The two covariance matrices also use different divisors, so their individual entries need not obey a simple entrywise inequality.{{cite:nist_poolcov1998}} ("Program 2", within and between matrices){{cite:fisher1936}} (§II, pp. 179–181, within-species scatter)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For each group, write $\mathbf x_{gi}-\bar{\mathbf x}=(\mathbf x_{gi}-\bar{\mathbf x}_g)+(\bar{\mathbf x}_g-\bar{\mathbf x})$. Summing outer products, the cross terms vanish because $\sum_i(\mathbf x_{gi}-\bar{\mathbf x}_g)=\mathbf0$. This gives the within/between decomposition. The same centring relation shows that the matrix of all $n$ within-group residual rows has rank at most $n-G$, hence its cross-product matrix $S$ has rank at most $\min(p,n-G)$. For any $\mathbf v$, $\mathbf v^\top S\mathbf v=(n-G)^{-1}\sum_{g,i}\{\mathbf v^\top(\mathbf x_{gi}-\bar{\mathbf x}_g)\}^2\ge0$, proving positive semidefiniteness.{{cite:nist_poolcov1998}} (Description and Program 2)

If observations within each group are iid with covariance $\Sigma$, then $\mathbb E\sum_i(\mathbf X_{gi}-\bar{\mathbf X}_g)(\mathbf X_{gi}-\bar{\mathbf X}_g)^\top=(n_g-1)\Sigma$: expand around the fixed population mean and subtract $n_g(\bar{\mathbf X}_g-\boldsymbol\mu_g)(\bar{\mathbf X}_g-\boldsymbol\mu_g)^\top$. Independence gives $\operatorname{Cov}(\bar{\mathbf X}_g)=\Sigma/n_g$. Summing over $g$ and dividing by $n-G$ proves $\mathbb E(S)=\Sigma$. This unbiasedness does not require normality, only the stated common covariance and finite second moments.{{cite:nist_poolcov1998}} (Description, pooled sample covariance)
:::
:::

## Statistical use
For LDA, the class means describe where groups sit, while the pooled covariance describes their shared within-class scatter. The resulting inverse weights directions by their variation: a difference along a low-variance direction can count more than the same raw distance along a high-variance direction. For two-sample Hotelling inference, the same pooled covariance scales the vector difference in sample means. Before either calculation, check class sizes, the matrix's rank, units of measurement, and whether a shared-covariance model is credible. If the matrix is singular, a pseudoinverse or regularized estimate changes the procedure and needs its own interpretation.{{cite:clemmensen2011_sda}} (§§1–2.1, pp. 1, 3–4){{cite:nist_poolcov1998}} ("Applications", Fisher discriminant example)

## Worked example
Take two groups of four two-dimensional observations. Group A has $(-1,0),(1,0),(0,-1),(0,1)$, with mean $(0,0)$. Group B has $(3,1),(5,1),(4,0),(4,2)$, with mean $(4,1)$. Each group's within-group scatter is $A_g=\begin{pmatrix}2&0\\0&2\end{pmatrix}$. With $n=8$ and $G=2$, pooling divides their sum by $6$, giving $S=\begin{pmatrix}2/3&0\\0&2/3\end{pmatrix}$. The grand mean is $(2,1/2)$, and the between-group scatter is $\begin{pmatrix}32&8\\8&2\end{pmatrix}$. Thus the covariance of all eight observations about that grand mean is $\frac17\begin{pmatrix}36&8\\8&6\end{pmatrix}$, far larger in the first coordinate than the pooled within-group value $2/3$. The groups differ mainly in location, which pooling is designed to remove from its covariance estimate.{{cite:nist_poolcov1998}} (Description and Program 2, pooling and between-group matrix)

**Your turn.** Group A has scalar measurements $1,2,3$ and group B has $5,6,7$. Find the pooled within-group variance and the ordinary sample variance of all six measurements about their grand mean. Which describes scatter within a group?

::: {.callout-tip collapse="true" title="Answer"}
The group means are $2$ and $6$, and each group's residual sum of squares is $2$. The pooled variance is $(2+2)/(6-2)=1$. The grand mean is $4$; the six squared deviations sum to $28$, so the ordinary combined sample variance is $28/(6-1)=5.6$. The value $1$ describes the within-group scatter; $5.6$ also reflects the gap between the group means.{{cite:nist_poolcov1998}} (Description, pooled versus ordinary covariance)
:::

## Common misconceptions
Pooling is not the same as computing covariance after discarding group labels: the latter includes between-group scatter. Dividing the pooled residual total by $n-1$ would ignore the separately estimated group means and generally lose unbiasedness under the shared-covariance model. A pooled matrix is not guaranteed invertible just because each class has observations; its rank cannot exceed $n-G$. And numerical pooling alone does not establish equal population covariances or normality. Those are model assumptions checked separately from matrix arithmetic.{{cite:nist_poolcov1998}} (Description and Program 2){{cite:clemmensen2011_sda}} (§§1–2.1, pp. 1, 3–4)

## Assumptions and limits — When pooling misleads
If one class has variance $1$ and another variance $100$ on the same scalar feature, their pooled variance is a weighted compromise and describes neither class well for class-specific prediction. If $p=5$ but two groups supply only $n=6$ observations total, the within-group rank is at most $6-2=4$, so $S^{-1}$ does not exist even when the measurements look varied. If observations within a group are correlated replicates, the simple unbiasedness proof and Wishart calibration no longer follow from iid sampling. These failures concern a common covariance, matrix rank and sampling independence, respectively.{{cite:nist_poolcov1998}} (Description, common pooling formula){{cite:clemmensen2011_sda}} (§§1–2.1, pp. 1, 3–4)

## Connections
The pooled covariance is the within-group scatter matrix divided by its residual degrees of freedom. Fisher's discriminant criterion compares between-group separation with within-group scatter, and Gaussian LDA estimates its shared covariance from that same within-group information. Hotelling's two-sample statistic applies the inverse pooled matrix to a mean difference. A grand-mean covariance answers a different question: how the entire mixed population varies when group membership is itself allowed to vary.{{cite:fisher1936}} (§§I–II, pp. 179–181){{cite:clemmensen2011_sda}} (§2.1, pp. 3–4)

## History
In his 1936 iris analysis, Fisher computed sums of squares and products of deviations from the means of two species, using fifty plants from each and reporting 98 within-species degrees of freedom. That calculation separated the species' mean difference from variation within species before choosing a discriminating linear combination. Modern pooled-covariance notation expresses the same within-group construction as a matrix and extends it to more groups and features.{{cite:fisher1936}} (§II, pp. 179–181){{cite:nist_poolcov1998}} (Description and Fisher-discriminant application)
