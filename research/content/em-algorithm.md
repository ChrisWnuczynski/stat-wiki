## Motivating example

A clinic records a sequence of binary test outcomes but does not know which of two testing machines produced each result. If the machine labels were recorded, estimating each machine's success rate would mean counting its successes and trials. Without those labels, each result has to contribute fractionally to both machines. The EM algorithm alternates between estimating those missing memberships from the current rates and refitting the rates from the fractional counts{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

## Intuition — Turning missing labels into weights

The observed-data likelihood sums over every possible value of the unobserved labels before taking a logarithm. The complete-data log-likelihood would be simpler because its indicator variables appear linearly. EM uses the current parameter to find each indicator's conditional expectation, then treats those expectations as fixed weights while improving the complete-data criterion. The weights are recalculated only after the parameter update. This is why the method can turn a difficult logarithm of a sum into a succession of familiar weighted fits{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

The E in EM is an *expectation*, not a rule that every missing value is filled in by one best guess. In a mixture, a point near two components may have appreciable responsibility for both. The M is a *maximisation* of the conditional expected complete-data log-likelihood, not necessarily of the observed likelihood in one direct step. When the M step merely increases rather than maximises that criterion, the iteration is often called generalized EM and still inherits a nondecrease argument under the same lower-bound construction{{cite:dempster_laird_rubin1977}} (§§2–3, pp. 5–8).

## Definition

Let $x$ be observed data, $z$ latent data and $p(x,z;\theta)$ a joint model. The observed log-likelihood is $\ell(\theta)=\log\sum_z p(x,z;\theta)$ for discrete $z$, with an integral in the continuous case. Given $\theta^{(k)}$, the E step forms $r_k(z)=p(z\mid x;\theta^{(k)})$ and $Q(\theta\mid\theta^{(k)})=\E_{r_k}[\log p(x,z;\theta)]$. The M step chooses $\theta^{(k+1)}$ to maximise $Q$, or at least increase it in generalized EM. The distribution $r_k$ stays fixed throughout that maximisation{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

The notation separates two roles that are easy to blur: $\theta^{(k)}$ defines how missing labels are averaged, whereas the first argument of $Q$ is the candidate being fitted. If the labels are observed, their conditional distribution is degenerate and the update reduces to the ordinary complete-data fit. If labels are latent, EM provides a tractable ascent method when the conditional expectations and weighted fit can be computed or approximated{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

## Properties

An exact E step followed by a nondecreasing M step cannot lower $\ell$. The proof uses a lower bound that touches the observed log-likelihood at the current parameter. It does not say that every parameter sequence converges, that the likelihood is bounded above, or that the eventual fit is the global maximum. In a Gaussian mixture, a component covariance can collapse around an observation and send the likelihood upward without yielding a useful finite-variance fit{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13).

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix $r_k(z)=p(z\mid x;\theta^{(k)})$ and write $H(r_k)=-\sum_z r_k(z)\log r_k(z)$. Jensen's inequality gives the lower bound
$$
F(\theta;r_k)=\sum_z r_k(z)\log p(x,z;\theta)+H(r_k)\leq\log\sum_z p(x,z;\theta)=\ell(\theta).
$$
At $\theta=\theta^{(k)}$, $p(x,z;\theta^{(k)})/r_k(z)=p(x;\theta^{(k)})$ on the support of $r_k$, so Jensen's inequality is an equality: $F(\theta^{(k)};r_k)=\ell(\theta^{(k)})$. The entropy term does not depend on the candidate $\theta$. If the M step increases $Q=\sum r_k\log p(x,z;\theta)$, it increases $F$ as well. Therefore $\ell(\theta^{(k+1)})\geq F(\theta^{(k+1)};r_k)\geq F(\theta^{(k)};r_k)=\ell(\theta^{(k)})$. The same argument replaces sums by integrals when the relevant expectations exist{{cite:dempster_laird_rubin1977}} (§§2–3, pp. 5–8).
:::
:::

## Statistical use

For a finite mixture, the E step computes responsibilities: each component's weighted density at an observation divided by the sum of all components' weighted densities there. In the M step these responsibilities behave as fractional counts. New mixing proportions are effective component counts divided by sample size, and normal-component means are responsibility-weighted averages. The variance update uses the same weights about the *new* mean and divides by the effective count, because it maximises likelihood rather than correcting sample-variance bias{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

A practical fit records the observed log-likelihood at each iteration and checks that accepted updates do not reduce it. Several starting values are useful because the objective can have several stationary solutions. For normal mixtures, monitor component weights and covariance eigenvalues as well as the likelihood; a rising number can hide a collapsing component{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13).

In a normal mixture, the E step computes memberships from weighted densities and the M step freezes those memberships to update the parameters. The same model can have an unbounded likelihood when a component collapses. The arithmetic of the iteration is separate from the diagnostic limits of the fitted objective.{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures)

The bound requires the E-step conditional law to match the specified joint model and the M step to raise its expected complete-data criterion. An approximate E step can break the exact touching property, so observed likelihood must be checked separately. In a two-normal mixture with one mean placed at an observation and its variance driven toward zero, that component's density at the observation diverges; the unconstrained likelihood has no finite maximiser along that path. Changing start values does not remove this structural singularity{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13).
## Worked example

Two machines A and B are initially equally likely to have produced a test, with success probabilities $0.8$ and $0.3$. The observed sequence is success, success, failure. For each success, the E-step responsibility for A is $0.8/(0.8+0.3)=8/11\approx0.7273$. For the failure it is $0.2/(0.2+0.7)=2/9\approx0.2222$. These probabilities are fractional machine labels, not reconstructed facts about which machine actually produced each result{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

The effective A count is $2(8/11)+2/9=166/99\approx1.6768$ of the three tests, so the new A mixing proportion is $(166/99)/3=166/297\approx0.5589$. Holding the responsibilities fixed, its new success probability is the expected A successes divided by expected A tests: $(16/11)/(166/99)=72/83\approx0.8675$. B has effective count $131/99\approx1.3232$ and expected successes $6/11$, giving $(6/11)/(131/99)=54/131\approx0.4122$. The next E step would recompute memberships with these updated rates; it would not keep the old fractions indefinitely{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

**Your turn.** Start instead with mixing probabilities $0.6$ for A and $0.4$ for B, and success probabilities $0.7$ and $0.2$. For two successes and one failure, find A's responsibility for a success and a failure, then update only A's mixing probability.

::: {.callout-tip collapse="true" title="Answer"}
For a success, $r_A=0.6(0.7)/[0.6(0.7)+0.4(0.2)]=0.42/0.50=0.84$. For a failure, $r_A=0.6(0.3)/[0.6(0.3)+0.4(0.8)]=0.18/0.50=0.36$. A's effective count is $2(0.84)+0.36=2.04$, so its new mixing probability is $2.04/3=0.68$. The E-step probabilities remain fixed during this M-step calculation.
:::

## Common misconceptions

EM does not observe the missing labels; it averages over their current conditional distribution. “Never decreases likelihood” is not the same as “finds the global maximum,” and it says nothing by itself about parameter convergence. The responsibilities are not differentiated as functions of the candidate in the M step; doing so changes the objective. Finally, a high mixture likelihood is not necessarily a trustworthy fit if a component is collapsing onto a point{{cite:dempster_laird_rubin1977}} (§§2–4, pp. 5–13).

## Connections

The [complete-data likelihood](complete-data-likelihood.qmd) is the simple criterion EM averages, and [posterior membership](posterior-membership.qmd) supplies the weights in a mixture E step. The [M step](m-step.qmd) converts them into parameter estimates. [Monotonicity of EM](monotonicity-of-em.qmd) formalises the bound proved here, while [label switching](label-switching.qmd) shows why several parameter vectors can describe the same mixture density. These links matter when interpreting a fitted mixture rather than merely running its iteration{{cite:dempster_laird_rubin1977}} (§2, pp. 5–6, eq. 2.17; §4, mixtures).

## History

Dempster, Laird and Rubin's 1977 paper gave a general formulation of EM for maximum likelihood with incomplete observations. The general treatment puts latent mixture labels in the same framework as other kinds of incomplete data; Fraley and Raftery's later account applies it explicitly to mixture estimation. The monotone-likelihood result explained above is one reason that formulation became useful across models with unobserved components.{{cite:fraley_raftery2002}} (§3, p. 613, attribution and incomplete-data formulation)
