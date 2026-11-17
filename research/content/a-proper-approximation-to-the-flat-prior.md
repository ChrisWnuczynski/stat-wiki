## Motivating example — A bound is a modelling decision
Suppose a sensor measures a real-valued offset and its likelihood is concentrated near the measured value. A uniform prior over a long interval can change very little across that likelihood, yet still assign probability zero to an offset just beyond an endpoint. The numerical width and centre of the interval therefore matter: a locally constant density does not remove prior information about support. Comparing several defensible intervals is a sensitivity analysis, rather than a search for one infinitely wide probability distribution.{{cite:downey2020_thinkbayes2}} (Ch. 5, “Sensitivity to the Prior”)

## Definition — Normalise before increasing the bounds
For a real location parameter, let $C>0$ and set $\pi_C(\mu)=(2C)^{-1}\mathbf1_{[-C,C]}(\mu)$. Its integral is one. The constant function $\pi(\mu)=1$ instead has infinite integral on the real line. It can serve as an improper prior kernel in a Bayesian calculation, but it cannot assign unconditional probabilities by normalising over the whole real line. Translation invariance characterises length measure up to a positive multiplier, rather than a uniform probability law on an unbounded line.{{cite:taraldsen2022_improper}} (§3.3)

The distinction is visible without considering data. For $0<M<C$, the mass of $[-M,M]$ under $\pi_C$ is $M/C$. That tends to zero as $C$ increases. Every bounded interval loses its mass, so the sequence is not approaching a probability distribution on the real line in the ordinary weak-convergence sense. To see the contradiction, a putative probability limit would need to assign zero mass to all bounded open intervals; their countable union covers the line. The total mass would then be zero. This argument concerns the normalised prior distributions, whereas multiplying their densities by $2C$ produces the different pointwise limit $1$.{{cite:taraldsen2022_improper}} (§3.3, shift-invariant location measure)

## Properties — A posterior limit can still be useful
Let $L(\mu)$ be a nonnegative likelihood with $0<Z=\int_{\mathbb R}L(u)\,du<\infty$. The posterior from the bounded prior is
$$p_C(\mu\mid y)=\frac{L(\mu)\mathbf1_{[-C,C]}(\mu)}{Z_C},\qquad Z_C=\int_{-C}^{C}L(u)\,du.$$
The factor $1/(2C)$ cancels. Because $Z_C\uparrow Z$, the total variation distance from $p(\mu\mid y)=L(\mu)/Z$ equals $1-Z_C/Z$. This follows by integrating the density difference separately inside and outside the interval. Thus a posterior can converge even while its sequence of proper priors has no probability limit. The integrability condition is essential. Proper restrictions and their limiting posterior are distinct objects.{{cite:bernardo2005_reference}} (Definition 3 and Examples 3–4)

This calculation also supplies an error criterion: choose bounds that exclude only a suitably small fraction of the likelihood integral. The relevant quantity is the omitted posterior mass, rather than the number of zeros in $C$. For a likelihood with multiple distant regions, a bound that looks broad near one region can still discard another. Prior checks should therefore investigate the entire parameter space that science allows.{{cite:downey2020_thinkbayes2}} (Ch. 5, “Sensitivity to the Prior”)

## Worked example — A triangular likelihood
Take the likelihood $L(\mu)=(1-|\mu|)\mathbf1_{[-1,1]}(\mu)$. Its total integral is one. For $0<C\le1$, direct integration gives $Z_C=2C-C^2$. At $C=1/2$ the bounded-prior posterior excludes mass $1/4$ from the full triangular posterior. At $C=1$ it agrees exactly, and every larger bound produces the same posterior. Nevertheless, the prior mass of $[-1,1]$ falls to $1/100$ when $C=100$. These two facts coexist because Bayesian normalisation uses the likelihood as well as the prior. The posterior calculation uses the ordinary conditional-density rule.{{cite:taraldsen2022_improper}} (§4.1)

**Your turn.** With this triangular likelihood and $C=1/4$, what is the total variation distance to the full triangular posterior?

::: {.callout-tip collapse="true" title="Answer"}
The included mass is $2(1/4)-(1/4)^2=7/16$, so the omitted mass and total variation distance are $9/16$.
:::

## Assumptions and limits — Diffusion does not guarantee propriety
If the likelihood has a positive lower bound on an infinite-measure region, its integral diverges and the preceding posterior limit is unavailable. A mixture likelihood can have exactly that behaviour. Moreover, posterior convergence for a fixed observation is weaker than a universal claim about all observations or all ways of expanding the support. Bounds should be justified and posterior propriety checked for the actual model.{{cite:bernardo2005_reference}} (Example 4)
