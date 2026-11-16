## Motivating example

A clinic measures blood pressure several times per patient and wants the average change associated with treatment in its patient population. Readings from the same patient resemble one another, so an analysis that treats every reading as a new independent patient understates uncertainty. A marginal mean model describes the population-average association; generalised estimating equations (GEE) combine its residuals using a working within-patient covariance. This gives an estimable regression equation without specifying a full joint distribution for every patient's repeated outcomes.{{cite:liang_zeger1986}} (pp. 13–16, §§1–3)

## Definition — A weighted marginal score

For independent clusters indexed by $i$, write $\boldsymbol\mu_i(\boldsymbol\beta)=\mathbb E\mathbf Y_i$, $D_i=\partial\boldsymbol\mu_i/\partial\boldsymbol\beta^\top$, and $V_i$ for a positive-definite working covariance matrix of the observations in cluster $i$. GEE solves $\sum_iD_i^\top V_i^{-1}(\mathbf Y_i-\boldsymbol\mu_i)=0$. It uses a model for each marginal mean and variance and a working association between measurements in the same cluster. The matrix $V_i$ weights residuals; it need not be the true joint covariance for the regression target to be meaningful.{{cite:liang_zeger1986}} (pp. 14–16, §§2–3.1, eqs. 3, 5–6)

When $V_i$ is diagonal, the equation is the independence working score. An exchangeable working correlation uses one common correlation for every distinct pair within a cluster; an autoregressive structure makes correlation decrease with lag. Either choice may change finite-sample estimates and their precision. It is chosen for plausible efficiency, not to define the marginal mean itself.{{cite:liang_zeger1986}} (pp. 15–18, §§3–4)

## Intuition

At the true mean parameter, each residual vector has expectation zero. Multiplying it by a weight based on predictors and a working covariance leaves its expected contribution zero. Summing across independent clusters therefore gives an estimating equation centred at the desired parameter. Correlation affects how much independent information the cluster supplies, even though the separate readings can each have a familiar Bernoulli or Poisson marginal law. This is the same separation between mean and dependence that makes a quasi-score possible.{{cite:liang_zeger1986}} (pp. 14–16, §§2–3.1)

## Properties — Robust and model-based uncertainty

Let $U_i=D_i^\top V_i^{-1}(\mathbf Y_i-\boldsymbol\mu_i)$. For a fitted parameter, set $A=\sum_iD_i^\top V_i^{-1}D_i$ and $B=\sum_iU_iU_i^\top$. The cluster-sandwich covariance estimate is $A^{-1}BA^{-1}$. If the working covariance is correct, its large-sample middle term agrees with $A$, giving the model-based covariance $A^{-1}$. With a wrong working correlation, the sandwich uses observed cluster residual cross-products to estimate the variability of the score. It does not repair a wrong mean curve.{{cite:liang_zeger1986}} (pp. 15–16, §§2–3.1, Theorems 1–2 and variance estimate)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
At the true $\boldsymbol\beta_0$, a correctly specified mean gives $\mathbb E(\mathbf Y_i-\boldsymbol\mu_i)=0$ and hence $\mathbb E U_i(\boldsymbol\beta_0)=0$. With independent clusters and the regularity conditions of the GEE theorem, a central limit theorem applies to $\sum_iU_i(\boldsymbol\beta_0)$. Taylor-expand the equation $0=\sum_iU_i(\widehat{\boldsymbol\beta})$ around $\boldsymbol\beta_0$. Its leading derivative is $-A$, because the residual-dependent derivative has expectation zero. Thus $\widehat{\boldsymbol\beta}-\boldsymbol\beta_0\approx A^{-1}\sum_iU_i(\boldsymbol\beta_0)$, whose covariance is $A^{-1}(\sum_i\operatorname{Var}U_i)A^{-1}$. Replacing the unknown score covariance by the empirical sum $\sum_iU_iU_i^\top$ gives the sandwich. If $V_i=\operatorname{Cov}(\mathbf Y_i)$, then $\operatorname{Var}U_i=D_i^\top V_i^{-1}D_i$, so the middle term equals $A$. The statement is asymptotic as the number of independent clusters grows, not an exact small-sample identity.{{cite:liang_zeger1986}} (pp. 15–16, §§2–3.1, Theorems 1–2; Appendix)
:::
:::

## Worked example

Consider 30 independent patients, each measured twice for a binary response. Ten patients have outcomes $(1,1)$, ten have $(0,0)$, and ten have $(1,0)$. There are $30$ successes in $60$ readings, so an intercept-only marginal Bernoulli fit under working independence estimates $p=30/60=0.5$. Its naive standard error for $p$ is $\sqrt{p(1-p)/60}=\sqrt{0.25/60}\approx0.06455$. That calculation treats 60 readings as 60 independent contributions.{{cite:liang_zeger1986}} (pp. 14–16, §§2–3.1, independence and robust variance equations)

For a logit intercept $\beta=\log\{p/(1-p)\}=0$, each reading contributes derivative $p(1-p)=0.25$. The bread is $A=60(0.25)=15$. The cluster score is $1$ for each $(1,1)$ pair, $-1$ for each $(0,0)$ pair, and $0$ for $(1,0)$, giving meat $B=10(1)^2+10(-1)^2=20$. The sandwich variance of $\widehat\beta$ is $20/15^2=0.08889$. Multiplying its standard error by $dp/d\beta=0.25$ gives the cluster-robust standard error of $\widehat p$, $0.25\sqrt{0.08889}\approx0.07454$. The two standard errors differ because the observed outcomes cluster. Thirty clusters give only a rough large-sample illustration; the formula alone does not guarantee interval coverage.{{cite:liang_zeger1986}} (pp. 15–16, §§2–3.1, variance estimates)

**Your turn.** Twenty independent patients each have two binary readings. Ten have $(1,1)$ and ten have $(0,0)$. Estimate the common marginal probability and compare its naive independence standard error with the uncorrected cluster-sandwich standard error.

::: {.callout-tip collapse="true" title="Answer"}
There are $20$ successes among $40$ readings, so $\widehat p=0.5$. The naive standard error is $\sqrt{0.25/40}\approx0.07906$. The bread for the logit intercept is $A=40(0.25)=10$ and the meat is $B=20$, since every cluster's residual sum is $1$ or $-1$. The sandwich variance of the logit intercept is $20/10^2=0.2$; the delta-method standard error of $\widehat p$ is $0.25\sqrt{0.2}\approx0.11180$. Perfect agreement within each pair leaves information closer to 20 independent responses than to 40. With only 20 clusters, neither asymptotic standard error is a guarantee of exact coverage.{{cite:liang_zeger1986}} (pp. 15–16, §§2–3.1, working-independence sandwich)
:::

## Statistical use

GEE is suited to repeated or clustered outcomes when the population-average mean is the main target. The analyst specifies the outcome's marginal mean, a variance function, and a working correlation; then solves the estimating equation and reports cluster-based uncertainty. The number of independent clusters, rather than the total number of rows, drives the asymptotic argument. A well-chosen working correlation can improve efficiency, but the robust variance remains important when it is misspecified. The yarn example in the linked chapter has just two factories; it usefully shows how model-based and robust columns differ, but two clusters cannot support the usual large-cluster reassurance.{{cite:liang_zeger1986}} (pp. 13–20, §§1–5)

## Common misconceptions

GEE does not model the trajectory of a particular person in the way a random-intercept model does; its coefficients describe a marginal mean. A robust sandwich does not make every aspect of the fit robust: it targets covariance misspecification under a correctly specified mean and independent clusters. Coefficients need not remain numerically identical when the working correlation changes in a finite dataset. Nor is the working correlation a claim that the complete multivariate response distribution is known. These distinctions separate the target, the weights, the uncertainty calculation, and a full likelihood.{{cite:liang_zeger1986}} (pp. 13–16, §§1–3)

## Assumptions and limits — Where the guarantee fails

If treatment is omitted from the marginal mean while related to both outcome and follow-up schedule, the score is no longer centred at the intended parameter. If two factories are the only independent clusters, the empirical meat has too little information to justify a large-cluster normal approximation. If people with worsening outcomes systematically miss later appointments, the ordinary 1986 consistency result's missingness condition fails. And if clusters themselves share an unmodelled shock, summing their scores as though independent understates uncertainty. A different mean model, more clusters, or an explicit missing-data/dependence analysis is needed for these respective cases.{{cite:liang_zeger1986}} (pp. 15–16, §§2–3.1, missingness and asymptotic conditions)

## Connections

A [marginal model](marginal-model.qmd) defines the population-average mean; [working correlation](working-correlation.qmd) supplies efficiency weights. The [sandwich estimator](sandwich-estimator.qmd) measures score variability across clusters, and [quasi-likelihood](quasi-score-and-quasi-likelihood.qmd) provides the independent-data analogy. A [linear mixed model](linear-mixed-model.qmd) instead specifies latent subject effects and can answer subject-specific questions.{{cite:liang_zeger1986}} (pp. 13–16, §§1–3)

## History

Liang and Zeger's 1986 paper extended generalised linear model estimating equations to longitudinal responses using a working correlation and a cluster-sandwich variance. Their stated aim was regression on marginal responses without a full joint distribution for each subject. The paper distinguished working independence from more efficient covariance structures and made the large-number-of-subjects basis for inference explicit.{{cite:liang_zeger1986}} (pp. 13–16, §§1–3; pp. 19–20, §5)
