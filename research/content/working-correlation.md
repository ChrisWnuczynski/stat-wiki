## Motivating example
Repeated measurements on the same child tend to move together. A regression that treats each visit as an independent child may still estimate the right population mean trend, but its ordinary standard errors use the wrong amount of information. Generalised estimating equations, or GEE, describe the mean separately from a *working correlation* within each child. This matrix gives the fitting algorithm a way to weight correlated observations while leaving room for the chosen pattern to be only an approximation.{{cite:liang_zeger1986}} (§§1–3, pp. 13–16)

## Intuition
The independent units in GEE are clusters, such as children; visits within one child form a vector. A working correlation says how those visits are related for the purpose of weighting their residuals. Independence gives an identity matrix. Exchangeable correlation gives every pair the same value. An autoregressive pattern makes adjacent visits more correlated than distant ones. These choices affect efficiency and the model-based variance, while a cluster-based sandwich variance estimates uncertainty from the observed cluster residuals under the usual large-cluster-count conditions.{{cite:liang_zeger1986}} (§§3–5, pp. 15–19)

## Definition
For cluster $i$, write its response vector $\mathbf Y_i$, marginal mean $\boldsymbol\mu_i(\boldsymbol\beta)$, diagonal marginal variance matrix $A_i$, and a proposed correlation matrix $R_i(\boldsymbol\alpha)$. The *working covariance* is $V_i=A_i^{1/2}R_i(\boldsymbol\alpha)A_i^{1/2}/\phi$ in Liang and Zeger's dispersion convention. With $D_i=\partial\boldsymbol\mu_i/\partial\boldsymbol\beta^{\mathsf T}$, the GEE is

$$
U(\boldsymbol\beta)=\sum_i D_i^{\mathsf T}V_i^{-1}(\mathbf Y_i-\boldsymbol\mu_i)=\mathbf0.
$$

The correlation is called *working* because the estimate can target the marginal mean parameter even if $R_i$ is not the true within-cluster correlation. The matrix must still be a valid, invertible correlation matrix for the equation as written. A wrong correlation can waste precision; it does not rescue a wrong mean model.{{cite:liang_zeger1986}} (§3.1, eqs. 5–6, pp. 15–16)

## Interpretation — Separate mean from association
The regression coefficient in a marginal model describes a population-average response, not necessarily a child's conditional change after fixing a latent random intercept. Working independence, exchangeable and first-order autoregressive matrices are alternative ways to weight the residual vector after the marginal mean and variance functions have been specified. A sandwich estimator replaces the correlation-dependent model-based covariance for $\hat{\boldsymbol\beta}$ with empirical outer products of the cluster contributions. Under the stated regularity conditions and enough independent clusters, correct specification of the marginal mean can support consistent regression and sandwich-variance estimates even when the working correlation is wrong.{{cite:liang_zeger1986}} (§§2–3, pp. 14–17)

The word “robust” has a narrow meaning here. If a treatment effect is omitted from the mean or follow-up depends on unobserved responses, changing the correlation matrix cannot correct the estimating equation's expectation. A handful of clusters gives a noisy empirical sandwich. The asymptotic argument is driven by many independent clusters, with suitable control of their sizes and leverage; one giant cluster is not a substitute for many children.{{cite:liang_zeger1986}} (§§2–3 and 6, pp. 14–17, 21–22)

## Properties — Common working patterns
Working independence has $R_i=I$. An exchangeable $m\times m$ matrix has ones on the diagonal and a common off-diagonal value $\rho$. Its eigenvalues are $1-\rho$ with multiplicity $m-1$ and $1+(m-1)\rho$ once, so it is positive definite exactly when $-1/(m-1)<\rho<1$. At either endpoint it is singular. For four visits, $\rho=-0.5$ makes one eigenvalue $1+3(-0.5)=-0.5$ and is impossible for a correlation matrix. A first-order autoregressive matrix has entries $\rho^{|j-k|}$ for equally spaced visit order; it makes temporal spacing matter, unlike the exchangeable pattern.{{cite:liang_zeger1986}} (§4, Examples 1, 3 and 4, pp. 17–18)

::: {.callout-note collapse="true" title="Proof"}
For the exchangeable matrix $R=(1-\rho)I+\rho\mathbf1\mathbf1^{\mathsf T}$, every vector orthogonal to $\mathbf1$ is an eigenvector with eigenvalue $1-\rho$, while $R\mathbf1=\{1+(m-1)\rho\}\mathbf1$. Requiring all eigenvalues strictly positive gives the stated bounds. For an intercept-only GEE with unit marginal variances and clusters of sizes $m_i$, $D_i=\mathbf1$ and $\mathbf1^{\mathsf T}R_i^{-1}=\mathbf1^{\mathsf T}/[1+(m_i-1)\rho]$. Solving $U(\mu)=0$ gives $\hat\mu=\{\sum_i\sum_j y_{ij}/[1+(m_i-1)\rho]\}/\{\sum_i m_i/[1+(m_i-1)\rho]\}$. Thus different working correlations can change the fitted mean when cluster sizes differ, while the matrix must remain invertible.{{cite:liang_zeger1986}} (§§3.1 and 4, eqs. 5–6 and exchangeable example)
:::

## Statistical use — Choosing and checking a structure
Independence is simple and can be a reasonable starting matrix when within-cluster dependence is weak. Exchangeable correlation is compact when no pair of visits has a privileged distance. Autoregressive correlation is useful when near visits tend to be more alike, provided the ordering and intervals make that claim plausible. A more flexible matrix uses more association parameters and can be unstable with sparse clusters. One can compare fitted working correlations and residual patterns, but the main scientific model is still the marginal mean. Liang and Zeger describe the potential efficiency gain from a working matrix closer to the true association and give examples where the gain varies with correlation strength and design.{{cite:liang_zeger1986}} (§§3–5, pp. 15–20)

If a child's unobserved poor-health visit is more likely to be missing, the observed cluster residuals may not represent the intended population mean; Liang and Zeger's basic consistency discussion assumes noninformative missingness. If only four children are followed, the empirical sandwich has too few independent contributions for its large-sample approximation to be reliable. If a mean model omits an age trend, a sophisticated autoregressive working matrix cannot create the missing trend. These are different failures: selection, small independent sample size and mean misspecification.{{cite:liang_zeger1986}} (§§2–3 and 6, pp. 14–17, 21–22)

## Worked example
Suppose one child has two responses $(1,3)$, another has one response $5$, and the marginal mean is a common $\mu$ with unit variance. Under working independence, all three observations receive equal weight, so $\hat\mu=(1+3+5)/3=3$. Under exchangeable within-child correlation $\rho=0.5$, the two-response cluster contributes numerator $(1+3)/(1+0.5)=8/3$ and weight $2/(1+0.5)=4/3$; the singleton contributes numerator $5$ and weight $1$. The GEE solution is $(8/3+5)/(4/3+1)=23/7\approx3.285714$. The change comes from downweighting the correlated pair relative to the singleton, not from claiming the first child's visits are actually correlated by exactly $0.5$. A sandwich calculation for uncertainty would need many independent children; these two clusters only illustrate the weighting.{{cite:liang_zeger1986}} (§3.1, eqs. 5–6, pp. 15–16)

**Your turn.** Four equally spaced visits are assigned an exchangeable working correlation $\rho=-0.5$. Compute the two distinct eigenvalues and decide whether the resulting matrix can be used as a correlation matrix. What is the lower admissible boundary for four visits?

::: {.callout-tip collapse="true" title="Answer"}
The eigenvalues are $1-(-0.5)=1.5$, repeated three times, and $1+3(-0.5)=-0.5$ once. A negative eigenvalue rules out a correlation matrix. The lower positive-semidefinite boundary is $-1/(4-1)=-1/3$; at $-1/3$ the matrix is singular, so an inverse-based GEE requires a value strictly above it.
:::

## Common misconceptions
An exchangeable working matrix specifies equal pairwise correlations; permutation invariance of the full response law requires more. It does not make correlated visits independent units; the child remains the unit for the sandwich contributions. A robust sandwich variance does not repair an incorrect marginal mean or informative missingness. Finally, a closer working pattern can improve precision, but it does not guarantee smaller standard errors in every finite dataset, and an impossible correlation such as $-0.5$ for four exchangeable visits is not a harmless approximation.{{cite:liang_zeger1986}} (§§2–5, pp. 14–20)

## Assumptions and limits — A working correlation is not the true law
An exchangeable working matrix specifies equal pairwise correlations; permutation invariance of the full response law requires more. {{cite:liang_zeger1986}} (§§2–5, pp. 14–20)

## Connections
The working matrix is one ingredient of [generalised estimating equations](generalised-estimating-equations.qmd), alongside the marginal mean and variance. The [sandwich estimator](sandwich-estimator.qmd) uses cluster contributions to quantify regression uncertainty under correlation misspecification. [Exchangeable correlation](exchangeable-correlation.qmd) names one matrix pattern; [exchangeability](exchangeability.qmd) of a joint distribution is a stronger symmetry claim. Comparing them keeps the modeling and weighting roles clear.{{cite:liang_zeger1986}} (§§3–4, pp. 15–18)

## History
Liang and Zeger's 1986 paper introduced the term “working” for the within-subject correlation matrix in their generalized estimating equations, separating a marginal regression objective from a fully specified joint response law. Their examples compare independence, exchangeable and other structures and show why a plausible association model can improve efficiency without being essential to the mean estimate's large-sample target.{{cite:liang_zeger1986}} (§§1, 3–5, pp. 13–20)
