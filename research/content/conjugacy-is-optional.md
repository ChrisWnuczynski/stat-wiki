## Motivating example
A prior can express a scientifically meaningful shape that is not preserved by multiplying by the likelihood. That changes the computation required to obtain the posterior, but does not invalidate Bayesian updating. Conjugacy is a useful algebraic property of a prior family relative to a sampling model. It is not a requirement that all reasonable prior beliefs belong to that family.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Conjugate Priors”)

## Definition — Posterior normalisation is the essential step
For a nonnegative prior density $\pi(\theta)$ and likelihood $L(\theta)$, a proper posterior density is $L(\theta)\pi(\theta)/Z$ when $0<Z=\int L(u)\pi(u)\,du<\infty$. Conjugacy means that this density belongs to the same chosen parametric family as the prior for every admissible observation. A named closed form can make summaries easy; without it, quadrature, grids or simulation can evaluate the same integrals.{{cite:taraldsen2022_improper}} (§4.1, conditional densities and Bayesian inference)

For bounded likelihoods, every proper prior gives a finite integral, though positive evidence also requires that prior and likelihood overlap. With unbounded likelihoods, posterior propriety needs separate attention. Conversely, an improper kernel can sometimes yield a proper posterior, but that requires checking the normalising integral. Numerical output that looks smooth does not itself prove that the underlying integral is finite.{{cite:taraldsen2022_improper}} (§§1, 4.1)

## Interpretation — A finite mixture stays interpretable
Consider a prior that is a mixture of two beta densities, $w\operatorname{Beta}(a_1,b_1)+(1-w)\operatorname{Beta}(a_2,b_2)$. Binomial data update each beta component conjugately, while their posterior weights are proportional to prior weights times component marginal likelihoods. The resulting posterior is generally a beta mixture rather than one beta distribution. This provides an exact computation for a richer prior without replacing it by a single convenient shape. The beta update follows from multiplying the powers of the success and failure probabilities.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Worked example — A two-component prior for a probability
Let the prior put equal weight on $\operatorname{Beta}(1,1)$ and $\operatorname{Beta}(3,1)$. Observe two successes in two independent Bernoulli trials. Their component evidence values are $1/3$ and $3/5$, since each is the prior expectation of $\theta^2$. Normalising their products with the equal prior weights gives posterior component weights $5/14$ and $9/14$. The posterior components are $\operatorname{Beta}(3,1)$ and $\operatorname{Beta}(5,1)$, so the posterior mean is $(5/14)(3/4)+(9/14)(5/6)=45/56\approx0.803571$. Every step uses the probability rule even though the answer is a mixture.{{cite:downey2020_thinkbayes2}} (Ch. 18, beta–binomial updating)

The normalising evidence for the mixture is $7/15$. Direct integration of $\theta^2\{1/2+(3/2)\theta^2\}$ gives the same value, providing a second route to the posterior weights and mean. When a closed-form mixture is unavailable, the corresponding integral ratio for the posterior mean remains valid.{{cite:taraldsen2022_improper}} (§4.1)

**Your turn.** What is the posterior probability that the second mixture component generated the parameter before the data were sampled?

::: {.callout-tip collapse="true" title="Answer"}
It is the posterior mixture weight $9/14$. This is a latent-component probability, distinct from the posterior mean of $\theta$.
:::

## Assumptions and limits — Check approximation error separately
A grid can miss a narrow peak or truncate material tail probability. Its resolution and range should be varied, and integral summaries compared where possible. In several dimensions the number of grid points grows multiplicatively, motivating methods that explore the posterior more selectively. Markov chain samples also require assessment of dependence and convergence. Choosing a nonconjugate prior therefore adds a computational task; it does not remove the modelling task or the need to check the resulting posterior.{{cite:downey2020_thinkbayes2}} (Ch. 18, introduction; Ch. 19, “Grid Approximation”)
