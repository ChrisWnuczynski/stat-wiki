## Motivating example

Suppose two populations have overlapping measurements but the population labels were not recorded. Treating each observed point as belonging entirely to its nearest population throws away information near the boundary; pretending that every possible label is equally plausible ignores the measured value. The expectation step of the EM algorithm uses the current mixture model to assign each point a *fractional* membership in each component. These memberships make the unobserved complete-data log likelihood usable in the following maximization step. Dempster, Laird and Rubin formulated the step for general incomplete-data likelihoods; mixture membership is a particularly transparent instance. {{cite:dempster_laird_rubin1977}} (§2, pp. 3–6, eq. 2.17; §4, mixtures)

## Intuition — What is averaged

Imagine that the component labels were visible. A labelled observation would contribute a term to just one component's log likelihood. When the label is missing, its unknown indicator is replaced by its conditional expectation under the *current* parameter. For a zero-one indicator, that expectation is the conditional probability of membership. The resulting objective is a weighted complete-data log likelihood, usually written $Q(\Psi;\Psi^{(k)})$. The second argument determines the weights; the first is the candidate parameter that the later M step will vary. Keeping those jobs separate is what makes the calculation an EM iteration rather than a circular substitution. {{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17)

## Definition — Conditional expectation at the current fit

Let $X$ denote observed data, $Z$ the missing labels, and $\ell_C(\Psi;X,Z)$ the complete-data log likelihood. At iteration $k$ the E step computes

$$
Q(\Psi;\Psi^{(k)})=E_{\Psi^{(k)}}\{\ell_C(\Psi;X,Z)\mid X\}.
$$

For independent observations from a finite mixture, $Z_{ih}$ is one if observation $i$ belongs to component $h$, and zero otherwise. If its current weight and density are $\pi_h^{(k)}$ and $f_h(x_i;\theta_h^{(k)})$, the *responsibility* is

$$
\tau_{ih}^{(k)}=E_{\Psi^{(k)}}(Z_{ih}\mid x_i)
=\frac{\pi_h^{(k)}f_h(x_i;\theta_h^{(k)})}
{\sum_{m=1}^{H}\pi_m^{(k)}f_m(x_i;\theta_m^{(k)})}.
$$

Provided the denominator is positive, each responsibility lies between zero and one and those for one observation sum to one. Substitution yields $Q=\sum_{i,h}\tau_{ih}^{(k)}[\log\pi_h+\log f_h(x_i;\theta_h)]$. The weights in this expression are fixed numbers during the M step, even though the candidate $\Psi=(\pi,\theta)$ varies. {{cite:dempster_laird_rubin1977}} (§2, p. 6, eq. 2.17; §4, finite mixtures)

::: {.callout-note collapse="true" title="Proof"}
Given $x_i$, the joint density of component $h$ and the observation is $\pi_h^{(k)}f_h(x_i;\theta_h^{(k)})$. Summing over all possible components gives the marginal density in the denominator. Bayes' rule gives the displayed ratio. Since $Z_{ih}$ is zero or one, its conditional expectation equals $\Pr_{\Psi^{(k)}}(Z_{ih}=1\mid x_i)=\tau_{ih}^{(k)}$. Linearity of conditional expectation then replaces each $Z_{ih}$ in the complete-data log likelihood by $\tau_{ih}^{(k)}$. Summing the ratios over $h$ cancels the common denominator, proving that the responsibilities for each $i$ sum to one.{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17)
:::

## Interpretation — Soft labels and effective counts

The number $\tau_{ih}^{(k)}$ is a posterior membership *under the current mixture*, not a measured proportion of a person and not a guarantee of a true biological or social class. Summing it over observations gives the effective count $N_h=\sum_i\tau_{ih}^{(k)}$ assigned to component $h$. These counts can be nonintegers because uncertainty has been carried forward rather than hidden by a hard assignment. In a Gaussian mixture, the same weights determine the next component means and covariance matrices. A point between two nearby component centres may contribute substantially to both; one far from all components may still have memberships summing to one, so the sum-to-one property is no test of adequate fit. {{cite:dempster_laird_rubin1977}} (§4, mixtures)

## Properties — Which parameter is held still

The E step updates a *function* $Q$ of candidate parameters, not the parameter estimate itself. With $\Psi^{(k)}$ fixed, the numerator and denominator defining each responsibility are evaluated once. The subsequent M step maximizes this $Q$ over $\Psi$; only after that update does the next E step recompute memberships. If the current mixture weights change, the memberships can change even with identical component densities. If two components have identical densities at $x_i$, their relative responsibilities equal their relative current mixing weights. A zero current weight gives zero responsibility to that component throughout the E step and, under the usual unconstrained weight update, can keep it extinct. {{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13)

## Statistical use

Mixture fitting, incomplete contingency tables, and other missing-data likelihood problems share the conditional-expectation idea even though their hidden variables differ. The computable $Q$ function often turns a difficult observed likelihood, which contains a logarithm of a sum or integral, into a weighted expression that separates across components. For a numerical implementation, evaluating log weights and log densities before normalization can prevent underflow when all ordinary-scale densities are tiny. That numerical precaution changes neither the conditional probabilities nor the model. After an E step, monitor the observed-data likelihood across *complete* EM iterations; the exact algorithm's monotonicity result does not say that the E step on its own raises it. {{cite:dempster_laird_rubin1977}} (§§2–3, pp. 5–8)

If a fitted two-normal mixture is applied to measurements with a heavy-tailed, unimodal distribution, it can assign confident-looking memberships even though neither normal component describes a real group. If one component's covariance collapses on a single point, its density can become arbitrarily high and the likelihood unbounded; soft labels do not fix that degeneracy. A component initialized at zero mixing weight receives no responsibility and may never revive. The formula also requires a positive observed-data density: an impossible observation under every component makes the denominator zero. These are model and optimization failures, not reasons to treat the hidden labels as known. {{cite:dempster_laird_rubin1977}} (§4, mixture examples)
## Worked example — Two overlapping normals

Take two normal components with current weights $1/2$ each, known variance $1$, and means $0$ and $2$. For $x=0$, the density under the first component is $\varphi(0)=0.39894$, while the second gives $\varphi(-2)=0.05399$. The common factors cancel, so its responsibility for component one is $1/(1+e^{-2})\approx0.880797$. At $x=2$ the roles reverse and that responsibility is $1/(1+e^2)\approx0.119203$. Across these two observations, the effective count for component one is exactly $1$; the second component also receives $1$. These are the inputs to the M step, not yet the updated means. A hard assignment would have labelled the points perfectly despite the positive probability of the other component in each case. {{cite:dempster_laird_rubin1977}} (§4, normal mixtures)

**Your turn.** Under the same current mixture, what is the responsibility for component one at $x=1$, and what does that value say about the observed label?

::: {.callout-tip collapse="true" title="Answer"}
The point is equally distant from the two current means and the weights and variances are equal. The two weighted densities are identical, so the responsibility is $1/2$. It expresses conditional uncertainty under the model; no label has been observed.
:::

## Common misconceptions

A responsibility near one is not proof that a component generated the point; it is a probability conditional on a model and its current parameters. The E step does not maximize $Q$; that is the M step's job. Fractional memberships are not arbitrary smoothing: they follow from the current joint density by Bayes' rule. Finally, the E step need not be “easy” just because its name includes *expectation*: for some missing-data models the conditional expectation needs approximation, and an approximate E step needs its own convergence analysis. {{cite:dempster_laird_rubin1977}} (§§2–3, pp. 5–8)

## Connections

The [complete-data likelihood](complete-data-likelihood.qmd) explains why the missing indicators appear linearly; [posterior membership](posterior-membership.qmd) names the conditional probability used here. The [M step](m-step.qmd) turns these fixed memberships into updated parameters, and the [monotonicity of EM](monotonicity-of-em.qmd) concerns the whole pair of steps. [K-means as a limiting case](k-means-as-a-limiting-case.qmd) replaces soft memberships by nearest-centre assignments under a specific small-variance limit, rather than by a general property of all mixture models. {{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13)

### Guided practice

**1. Which argument changes?** In $Q(\Psi;\Psi^{(k)})$, a colleague differentiates each responsibility with respect to $\Psi$ while doing the M step. Why does this fail to implement the stated EM update?

::: {.callout-tip collapse="true" title="Answer"}
The responsibilities were computed using $\Psi^{(k)}$, the fixed second argument. The candidate $\Psi$ occurs in the complete-data log likelihood inside $Q$. Differentiating the memberships as though they were functions of that candidate changes the objective and loses the two-step construction.
:::

**2. Equal densities.** Two components give the same density at an observation, but their current weights are $0.8$ and $0.2$. Are its two responsibilities equal?

::: {.callout-tip collapse="true" title="Answer"}
No. The common density cancels and the responsibilities are $0.8$ and $0.2$. Both the component density and the current mixture weight enter Bayes' numerator.
:::

## History

Dempster, Laird and Rubin's 1977 article named the expectation and maximization steps in a general approach to maximum likelihood with incomplete observations. The E step formed the conditional expectation of the complete-data log likelihood at the current estimate; the M step then maximized it. Their treatment included mixture distributions as one application and established a monotonic-likelihood property for the combined exact update. That history helps explain why a “soft clustering” calculation is only one instance of a broader missing-data method. {{cite:dempster_laird_rubin1977}} (§§1–4, pp. 1–13)
