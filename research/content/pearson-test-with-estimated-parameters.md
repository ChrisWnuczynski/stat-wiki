## Motivating example
A goodness-of-fit test for a specified Poisson mean asks a different question from a test that first estimates that mean from the observed cell counts. Fitting lets the model move towards the data, reducing the remaining discrepancy. The chi-square reference distribution must reflect that use of the data. Counting fitted parameters is useful only after identifying the sampling scheme, the cells and the estimator used to fit their probabilities.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, parameter estimation from bin counts)

## Statement

**Fitting consumes identifiable directions.**
Suppose $X\sim\operatorname{Multinomial}(n,p(\theta))$ with $k$ fixed cells and an $r$ dimensional parameter. At the true interior parameter, suppose the positive probabilities are smooth, their derivative matrix has rank $r$, and the grouped-data fit is asymptotically efficient. Then
$$T=\sum_{i=1}^k\frac{\{X_i-np_i(\widehat\theta)\}^2}{np_i(\widehat\theta)}\ \Rightarrow\ \chi^2_{k-1-r}.$$
The rank condition means that the bins distinguish all $r$ local parameter directions. The sample total accounts for the first lost degree of freedom and estimation accounts for the next $r$. Thus the reference distribution requires $k>r+1$.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, degrees of freedom and grouped likelihood)

The fitting method matters. Estimating parameters by maximising the grouped multinomial likelihood is covered by this result. A fit based on ungrouped observations need not have the same projection onto grouped count fluctuations. The formula $k-1-r$ should therefore accompany assumptions about the estimator, rather than being applied to every procedure with $r$ parameter symbols.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, maximum likelihood estimation based on bin counts)

## Intuition — The residual space after fitting
Under a fully specified null model, count fluctuations occupy a space of dimension $k-1$. Parameter changes move fitted probabilities along an $r$ dimensional tangent space inside it. Efficient estimation absorbs the component along that tangent space, leaving the perpendicular component as lack of fit. Pearson's statistic measures the squared length of that remaining component. This is analogous to estimating a mean before assessing the residual variation around it, but the geometry is weighted by the null probabilities.{{cite:openintro2019}} (§6.3, p. 235, a fully specified null uses k−1 degrees of freedom)

A concrete one-parameter model makes the distinction visible. Let the four probabilities be $(\theta,\theta,1/2-\theta,1/2-\theta)$, where $0<\theta<1/2$. Estimation adjusts the total probability allocated to the first pair versus the second pair. The remaining discrepancies compare the two categories within each pair. Because there are two such directions, the fitted statistic has two limiting degrees of freedom.

## Proof
Assume the multinomial central limit theorem and the efficient grouped-likelihood expansion. With $D=\operatorname{diag}(p)$, $q=\sqrt p$ and $A=D^{-1/2}\partial p/\partial\theta^T$, differentiation of $\sum p_i=1$ gives $q^TA=0$. The standardised count vector converges to a normal vector with covariance $P=I-qq^T$. The fitted residual has limiting covariance
$$P-A(A^TA)^{-1}A^T.$$
The two subtracted projections have orthogonal ranges and ranks $1$ and $r$. Their complement is an orthogonal projection of rank $k-1-r$. Choosing an orthonormal basis of its range expresses the limiting squared residual norm as a sum of $k-1-r$ independent squared standard normals. Positivity of the cell probabilities allows fitted denominators to converge to their true values.

## Worked example
### Two pairs of categories
Observe $(12,18,25,45)$ with $n=100$ under the four-cell model above. The grouped log likelihood depends on $\theta$ through $30\log\theta+70\log(1/2-\theta)$, so its maximum occurs at $\widehat\theta=0.15$. The fitted expected counts are $(15,15,35,35)$. Their Pearson contributions are $0.6$, $0.6$, $2.857143$ and $2.857143$, giving $T=6.914286$. On $4-1-1=2$ degrees of freedom, the upper-tail probability is $0.031520$. The remaining mismatch is strongest within the second pair.

**Your turn.** If the probabilities had been specified as $(0.15,0.15,0.35,0.35)$ before collecting these data, what would change?

::: {.callout-tip collapse="true" title="Answer"}
The statistic would still be 6.914286, but no parameter was fitted. Its reference distribution would have three degrees of freedom instead of two.
:::

## Common misconceptions — Grouping and estimation are part of the model
The number of bins and the dimension of the fitted parameter both influence the reference distribution. Pooling cells can improve expected counts while also removing information about parameters. If a pooled table cannot identify a parameter direction, subtracting the nominal parameter count is unjustified. Small expected counts and boundary estimates also fall outside the simple interior approximation.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, sufficient sample size and parameter estimation)

Passing a goodness-of-fit test does not select a unique distribution. It says that the observed grouped discrepancies are not unusually large under one specified family and analysis procedure. Dependence, selective binning or selective reporting can invalidate that interpretation even when the arithmetic is correct. The independence and expected-count conditions should be assessed before interpreting a tail probability.{{cite:openintro2019}} (§6.3, p. 235, independence and expected counts at least 5)

## Statistical use — Report how the expected counts were fitted
A reproducible fitted goodness-of-fit analysis specifies the fixed cell boundaries, the probability family, the estimation criterion and the reference degrees of freedom. Reporting the fitted expected counts alongside observations helps separate estimation from the remaining discrepancies. If a grouped likelihood was used, its cell probabilities must sum to one across the analysed sample space. The tail probability then refers to that declared grouped analysis rather than to every possible way of fitting the same named distribution.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, parameter estimation and critical region)

Estimating free parameters from the same table that is being tested spends those degrees of freedom relative to a fully specified multinomial null, when the fit is the usual regular one.
