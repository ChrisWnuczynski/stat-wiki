## Motivating example

A scientist has a normal measurement model for an unknown mean but no defensible finite range of means to put into a prior distribution. Assigning constant weight to every real value can still yield a well-defined posterior once measurements arrive. The constant weight itself cannot be a probability density: its area over the whole real line is infinite. The useful question is whether multiplying it by the likelihood produces a finite area{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53).

## Definition

Let $w(\theta)\geq0$ be a prior *weight* relative to a stated measure on the parameter space. It is improper when $\int_\Theta w(\theta)\,d\theta=\infty$. Given data $x$ and likelihood $L(\theta;x)$, set $Z(x)=\int_\Theta L(\theta;x)w(\theta)\,d\theta$. A posterior density exists from this construction exactly when $0<Z(x)<\infty$, in which case it is $L(\theta;x)w(\theta)/Z(x)$. Calling a kernel a posterior before checking $Z$ confuses a formula proportional to a density with a probability distribution{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53).

Propriety is tied to the likelihood, parameter space and observed data, not to the prior name alone. A flat weight $w(\mu)=1$ on the real line is improper, whereas a uniform density on a bounded interval is proper. The two may produce similar posterior calculations when the likelihood is concentrated well inside that interval, but an improper weight has no prior predictive distribution and cannot be sampled as a probability law. Even a proper posterior under one dataset does not establish propriety for all possible datasets{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53).

## Intuition — Why the normal mean can work

For independent $X_i\sim N(\mu,\sigma^2)$ with known $\sigma^2>0$, the likelihood in $\mu$ is proportional to $\exp\{-\sum_i(x_i-\mu)^2/(2\sigma^2)\}$. With $w(\mu)=1$ and at least one observation, completing the square yields $\mu\mid x\sim N(\bar x,\sigma^2/n)$. The likelihood supplies Gaussian decay at both ends of the real line. If there are no observations, the weight remains flat and there is no posterior probability distribution. When the variance is unknown too, then the normalising integral requires a nonconstant sample and adequate sample size.{{cite:sas_statug2009_prior_distributions}} (§Prior Distributions, “Improper Priors”){{cite:stan_users_guide_problematic_posteriors}} (§Problematic Posteriors, “Redundant intercepts”)

This calculation does not make a flat prior uniquely neutral. A density constant in $\mu$ is generally not constant after a nonlinear change of parameter, because a Jacobian enters the transformed density. Jeffreys' information-based rule was designed to behave coherently under one-to-one reparameterisations, but it can itself be improper and still requires a propriety check. {{cite:sas_statug2009_prior_distributions}} (§Prior Distributions, “Noninformative Priors” and “Jeffreys’ Prior”)

## Properties — A boundary that the likelihood cannot repair

The Haldane weight $w(\theta)=\theta^{-1}(1-\theta)^{-1}$ for a binomial success probability is improper at both boundaries. With $x$ successes in $n$ trials, multiplication by $\theta^x(1-\theta)^{n-x}$ leaves $\theta^{x-1}(1-\theta)^{n-x-1}$, a $\operatorname{Beta}(x,n-x)$ kernel.{{cite:taraldsen2022_improper}} (§2, binomial example) Its integral is finite only if $x>0$ and $n-x>0$. All-success and all-failure samples leave an uncovered boundary where the posterior integral diverges. This is a data-dependent failure, even though the algebraic update looks like a familiar conjugate family{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53).

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the known-variance normal model, $\sum_i(x_i-\mu)^2=\sum_i(x_i-\bar x)^2+n(\mu-\bar x)^2$. The first term is constant in $\mu$, so $L(\mu;x)w(\mu)$ is proportional to $\exp\{-n(\mu-\bar x)^2/(2\sigma^2)\}$. Its integral is positive and finite for $n\geq1$, and normalisation gives $N(\bar x,\sigma^2/n)${{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 51–52).

For the binomial model, the prior-likelihood product is $\theta^{x-1}(1-\theta)^{n-x-1}$. Near zero its integral behaves as $\int_0^\epsilon\theta^{x-1}\,d\theta$, finite precisely if $x>0$; near one it behaves as $\int_{1-\epsilon}^1(1-\theta)^{n-x-1}\,d\theta$, finite precisely if $n-x>0$. Under both conditions the beta integral normalises the kernel. Otherwise no finite normalising constant exists. 
:::
:::{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53)

## Statistical use

The first step is to write down the exact measure and parameterisation in which the prior is flat or otherwise defined. Next examine every tail and boundary of the prior-likelihood integral; a symbolic identification of a familiar density is enough only after its parameters lie in the proper range. In a model with several parameters, check directions along which the likelihood does not change. Two free intercepts entering only through their sum leave an infinite ridge under independent flat weights. Removing the redundant intercept or assigning proper priors can resolve this, but the resulting prior choice affects the model and should be stated.{{cite:stan_users_guide_problematic_posteriors}} (§Problematic Posteriors, “Redundant intercepts” and “Mitigating the invariances”)

An arbitrary positive multiplier in an improper prior cancels from one posterior, but it remains in a marginal likelihood. Thus comparing models by a Bayes factor generally requires properly normalised parameter priors or a separately justified construction. Posterior propriety alone is not a licence to treat the improper weight as a probability distribution for every Bayesian calculation{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53).

The all-success binomial sample above leaves a nonintegrable singularity at $\theta=1$. In the normal model, one observation with unknown mean *and* unknown variance under a joint scale weight can leave the variance unidentifiable, even though one observation suffices when variance is known. With two additive intercepts and a likelihood that depends only on their sum, no sample size removes the flat ridge in the difference of intercepts. These failures call for a changed model, an identified parameterisation or a justified proper prior, followed by a new propriety check.{{cite:stan_users_guide_problematic_posteriors}} (§Problematic Posteriors, “Redundant intercepts” and “Adding priors”)
## Worked example

Suppose four independent trials have three successes. Under the Haldane weight, the posterior kernel is $\theta^{3-1}(1-\theta)^{1-1}=\theta^2$, so the normalised law is $\operatorname{Beta}(3,1)$ with density $3\theta^2$ and mean $3/(3+1)=0.75$. Both success and failure were observed, so the likelihood suppressed the two problematic boundaries. If the fourth trial had been a success instead, the kernel would be $\theta^3/(1-\theta)$; its integral diverges at one. A formal “$\operatorname{Beta}(4,0)$” label is not a posterior distribution{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53).

**Your turn.** Three independent normal observations are $1,3,5$, and their common variance is known to be $9$. With the flat weight on $\mu\in\mathbb R$, find the posterior mean and variance. Why does this calculation yield a proper posterior?

::: {.callout-tip collapse="true" title="Answer"}
The sample mean is $3$ and $n=3$, so $\mu\mid x\sim N(3,9/3)=N(3,3)$. The likelihood decays as a Gaussian function of $\mu$ and has a finite positive integral. The prior weight alone does not.
:::

## Common misconceptions

An improper prior is not a very diffuse *probability* distribution; it has infinite mass. A recognisable posterior kernel is not automatically a valid posterior: the beta boundary parameters must be positive. A flat density does not stay flat under arbitrary reparameterisation. A proper posterior also does not make the original prior suitable for prior simulation or unqualified marginal-likelihood comparisons. These are different errors, each concerning a different mathematical operation.{{cite:sas_statug2009_prior_distributions}} (§Prior Distributions, “Noninformative Priors,” “Improper Priors” and “Jeffreys’ Prior”)

## Connections

A [flat prior](flat-prior.qmd) is improper when it assigns constant positive weight across an unbounded real line. [Beta-binomial conjugacy](beta-binomial-conjugacy.qmd) make updates algebraically recognisable, but a kernel at a boundary still needs an integral check. [A proper posterior](proper-prior-and-proper-posterior.qmd) are normalised probability laws, while a [likelihood function](likelihood-function.qmd) supplies the data-dependent factor that may make an improper weight usable. [Jeffreys prior](fisher-information.qmd) uses information to address parameterisation dependence and can also be improper.{{cite:sas_statug2009_prior_distributions}} (§Prior Distributions, “Conjugate Priors,” “Improper Priors” and “Jeffreys’ Prior”)

## History

Haldane's 1932 treatment of inverse probability led to the boundary-singular weight now bearing his name. Jeffreys later developed an information-based prior rule that transforms consistently with a change of parameter. Both developments supplied useful formal weights while leaving the posterior normalisation question essential in each application.{{cite:taraldsen2022_improper}} (§2, Haldane's binomial weight and its history)
