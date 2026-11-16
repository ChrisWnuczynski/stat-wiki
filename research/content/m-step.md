## Motivating example

A mixture model gives a probability that each observation belongs to each component, but those probabilities alone do not improve the fitted component means or weights. The maximization step of EM turns the E step's fractional memberships into a new parameter estimate. If an observation is believed to belong mostly to one component, it should influence that component more strongly than another; a weighted likelihood formalizes this idea. Dempster, Laird and Rubin named the M step as the maximization of an expected complete-data log likelihood, so the same principle also applies when the missing quantities are not mixture labels.{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures)

## Intuition — Fit complete data with fractional counts

If every label were known, a normal mixture's weights would be group proportions and its means would be group averages. With missing labels, the E step supplies a responsibility $\tau_{ih}$ between zero and one for observation $i$ and component $h$. The M step treats that value as a fractional count while maximizing the expected *complete-data* log likelihood. This is why its updates resemble familiar maximum-likelihood estimates with counts replaced by sums of responsibilities. The memberships are held fixed during this maximization; recomputing them inside the derivative would change the objective.{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixture examples)

## Definition — The optimization after expectation

Given current parameter $\Psi^{(k)}$ and the function $Q(\Psi;\Psi^{(k)})=E_{\Psi^{(k)}}[\ell_C(\Psi;X,Z)\mid X]$ from the E step, an exact M step chooses $\Psi^{(k+1)}\in\arg\max_\Psi Q(\Psi;\Psi^{(k)})$ over the allowed parameter space. For a finite mixture, the responsibilities are the fixed conditional expectations of the hidden component indicators. A generalized EM step may merely increase $Q$ rather than find its maximum; the word *exact* matters when claiming a maximizer. Any constraints on weights, means, or covariance matrices must be respected in this optimization.{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §3, generalized EM)

## Properties — Weighted likelihood updates

Write $N_h=\sum_i\tau_{ih}$ for component $h$'s effective count among $n$ observations. Because each observation's responsibilities sum to one, $\sum_hN_h=n$. For a normal mixture with freely estimated component weights, the M step gives $\pi_h^{(k+1)}=N_h/n$. For a positive effective count and a nonsingular covariance, its updated mean is $\mu_h^{(k+1)}=\sum_i\tau_{ih}x_i/N_h$. The maximum-likelihood covariance uses the weighted squared deviations divided by $N_h$; substituting $N_h-1$ would instead import a sample-covariance correction into a different objective. These expressions solve this particular mixture's $Q$ problem; a Poisson or censored-data model has a different M step.{{cite:dempster_laird_rubin1977}} (§§2, 4, pp. 5–6, 11–13)

::: {.callout-note collapse="true" title="Proof"}
The mixture-weight portion of $Q$ is $\sum_hN_h\log\pi_h$ subject to $\sum_h\pi_h=1$. A Lagrange multiplier gives $N_h/\pi_h=\lambda$, and summing $\pi_h=N_h/\lambda$ yields $\lambda=n$. For fixed positive definite covariance, the mean-dependent part is $-\frac12\sum_i\tau_{ih}(x_i-\mu_h)^\top\Sigma_h^{-1}(x_i-\mu_h)$. Its gradient vanishes when $\sum_i\tau_{ih}(x_i-\mu_h)=0$, giving the weighted mean. Maximizing in the precision matrix $\Theta_h=\Sigma_h^{-1}$ sets $N_h\Theta_h^{-1}=\sum_i\tau_{ih}(x_i-\mu_h)(x_i-\mu_h)^\top$, which gives the stated covariance update whenever that matrix is positive definite.

The likelihood increase of a *complete* exact EM update follows from the same fixed conditional distribution. Let $q_k(z)=p(z\mid X,\Psi^{(k)})$. Jensen's inequality gives $\log p(X\mid\Psi)\geq E_{q_k}\log p(X,Z\mid\Psi)-E_{q_k}\log q_k(Z)$. At $\Psi=\Psi^{(k)}$ this is equality. The second term does not depend on candidate $\Psi$, so an M step that increases $Q$ cannot decrease the observed log likelihood. Equality or increase does not establish a global maximum.{{cite:dempster_laird_rubin1977}} (§§2–3, pp. 5–8)
:::

## Interpretation — What a parameter update says

The updated mixing weight is a fraction of total *expected* membership, not necessarily a fraction of points with a hard label. The updated mean is pulled toward observations with high membership in that component. If two groups overlap, a boundary point can move both means. The covariance update uses the updated mean and accounts for the same fractional memberships. In a multivariate normal mixture, a covariance estimate must remain positive definite to represent a valid density; if the effective membership is too concentrated, the unconstrained update can become singular. The algebra makes the next fit conditional on the current soft labels, not on an assertion that the latent labels have become observed.{{cite:dempster_laird_rubin1977}} (§4, mixture examples)

## Statistical use — The iteration and its checks

One EM iteration computes the E-step distribution of missing data at $\Psi^{(k)}$, maximizes its expected complete-data log likelihood, and then evaluates the observed-data likelihood. The next E step uses the new $\Psi^{(k+1)}$. Maximization may be analytic, as with simple normal-mixture weights and means, or may require an inner numerical optimizer. If the inner solver stops early, check that the computed candidate actually increases $Q$ before relying on the generalized-EM ascent argument. An observed likelihood that has stopped changing does not by itself distinguish a global optimum, a local optimum, or a nearly singular mixture component. Compare starts, inspect covariance eigenvalues, and assess model adequacy against the observed data.{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13)

## Worked example — From memberships to parameters

Take observations $x_1=0$ and $x_2=2$. Suppose the E step supplies component-one responsibilities $\tau_{11}=0.8$ and $\tau_{21}=0.4$, so the component-two responsibilities are $0.2$ and $0.6$. The effective counts are $N_1=1.2$ and $N_2=0.8$, yielding new mixing weights $0.6$ and $0.4$. The component-one mean becomes $(0.8\cdot0+0.4\cdot2)/1.2=2/3\approx0.66667$; the component-two mean is $(0.2\cdot0+0.6\cdot2)/0.8=1.5$. If separate variances are estimated, their maximum-likelihood updates are $8/9\approx0.88889$ and $3/4=0.75$, respectively. These are conditional M-step calculations using supplied responsibilities; a subsequent E step would recompute the memberships from the updated mixture.{{cite:dempster_laird_rubin1977}} (§4, mixture examples)

**Your turn.** Keep $x=(0,2)$ but suppose the two component-one responsibilities are $0.75$ and $0.25$. Find both new mixing weights and both new means. Treat the variances as fixed.

::: {.callout-tip collapse="true" title="Answer"}
The component-one effective count is $0.75+0.25=1$, so its new weight is $1/2$. The complementary responsibilities are $0.25$ and $0.75$, also summing to one, so the second weight is $1/2$. The means are $(0.75\cdot0+0.25\cdot2)/1=0.5$ and $(0.25\cdot0+0.75\cdot2)/1=1.5$.{{cite:dempster_laird_rubin1977}} (§4, mixture examples)
:::

## Common misconceptions

The M step does not update the missing labels; it maximizes in model parameters with E-step weights fixed. A larger observed likelihood after one full EM iteration does not prove convergence to the global maximum. The $N_h$ divisor in a likelihood covariance update is not an accidental omission of an unbiasedness correction. A high responsibility is not a known class label, so a hard-group mean generally differs from the weighted update. Finally, *maximization* can mean a constrained numerical problem; the simple formulas rely on the stated normal-mixture assumptions.{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13)

## Assumptions and limits — Where the update breaks

If a component has $N_h=0$, its weighted mean divides by zero; a fitting procedure must handle that boundary explicitly. With an unrestricted Gaussian mixture, a component can concentrate on one observation as its covariance tends to zero, sending the likelihood upward without a finite optimum. If an M-step optimizer returns a candidate with lower $Q$ because it stopped prematurely, the standard ascent argument no longer applies. A fit to data drawn from a single skewed population can still find two apparently distinct normal components, but the parameter update cannot establish that two real populations exist. Initialization and constraints therefore matter alongside arithmetic correctness.{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13)

## Connections

The [E step](e-step.qmd) provides the conditional membership weights and the [complete-data likelihood](complete-data-likelihood.qmd) supplies the objective being averaged. [EM for a normal mixture](em-for-a-normal-mixture.qmd) uses the explicit weight, mean and covariance updates, while the [monotonicity of EM](monotonicity-of-em.qmd) explains the likelihood comparison across whole iterations. [Finite mixture models](finite-mixture-model.qmd) add questions of component interpretation and identifiability beyond the maximization itself.{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13)

## Check yourself

**1. What stays fixed?** While differentiating $Q(\Psi;\Psi^{(k)})$ to obtain new means, should the responsibilities be recalculated at each proposed mean?

::: {.callout-tip collapse="true" title="Answer"}
No. They were computed at $\Psi^{(k)}$ in the E step and are fixed weights in this M step. New responsibilities are computed only in the next E step.{{cite:dempster_laird_rubin1977}} (§2, p. 6, eq. 2.17)
:::

**2. A vanished component.** If $N_h=0$, can the ordinary weighted-mean formula estimate that component's mean?

::: {.callout-tip collapse="true" title="Answer"}
No. Its denominator is zero and the data provide no weighted contribution to that component in this update. The fitting procedure needs a boundary rule, constraint, or changed initialization; inserting a zero mean would be an arbitrary choice.{{cite:dempster_laird_rubin1977}} (§4, mixture examples)
:::

## History

In their 1977 presentation of the EM algorithm, Dempster, Laird and Rubin described the M step as choosing a new parameter to maximize the conditional expected complete-data log likelihood computed in the E step. Their general formulation covered several forms of incompleteness and included mixture distributions. The familiar weighted normal-mixture formulas are one concrete case of that broader maximization, not the definition of the method itself.{{cite:dempster_laird_rubin1977}} (§§1–4, pp. 1–13)
