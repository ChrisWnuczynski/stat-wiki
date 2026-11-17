## Motivating example
A laboratory observes successes in repeated trials and wants one number to use in a quick calculation. The sample success fraction is a natural summary, but previous experience may make some values more plausible before the new trials. A maximum a posteriori (MAP) estimate selects the peak of the posterior distribution formed from both ingredients. It is useful for optimization and reporting a tentative centre, provided that the full posterior remains available when uncertainty matters.{{cite:gelman_bda2013}} (§2.3, pp. 32–33)

## Intuition
The likelihood ranks parameter values by how well they explain the data, whereas the prior expresses a distribution before those data. Bayes' rule multiplies them, then normalizes. Because the normalizing constant does not depend on the parameter, finding a posterior mode only requires maximizing the likelihood times the prior. Taking logarithms turns the product into a sum and often turns the prior term into a penalty. This is why MAP appears in regularised optimization.{{cite:gelman_bda2013}} (§§1.3, 2.3){{cite:tibshirani1996}} (§5, p. 277)

A peak is a density property. For a continuous parameter, the probability of any exact value is zero; a high density means that a *small neighbourhood in the chosen coordinates* receives relatively high probability. The peak may be broad or narrow, and two distant peaks can make one MAP value a poor picture of the posterior. A posterior mean, median, interval, or plot can answer a different question.{{cite:gelman_bda2013}} (§2.3, pp. 32–33)

## Definition — Calculating a MAP estimate
For observed data $y$ and a parameter $\theta$ with posterior density $p(\theta\mid y)$, a MAP estimate is any maximizer
$$
\widehat\theta_{\mathrm{MAP}}\in\operatorname*{arg\,max}_{\theta\in\Theta}p(\theta\mid y)
=\operatorname*{arg\,max}_{\theta\in\Theta}\{L(\theta;y)p(\theta)\},
$$
provided the maximum exists. The second expression uses a likelihood $L(\theta;y)$ and a prior density $p(\theta)$ defined relative to the stated parameterization and base measure. Ties can yield several MAP values. With a prior constant *in that same parameterization*, MAP and maximum likelihood have the same maximizers, subject to boundary and propriety issues. A uniform prior after transforming the parameter is generally a different prior.{{cite:gelman_bda2013}} (§§1.3, 2.3)

In a binomial model, $Y\mid\theta\sim\operatorname{Binomial}(n,\theta)$ and $\theta\sim\operatorname{Beta}(a,b)$ give $\theta\mid Y=y\sim\operatorname{Beta}(a+y,b+n-y)$. When both posterior shape parameters exceed one, differentiation gives
$$
\widehat\theta_{\mathrm{MAP}}=\frac{a+y-1}{a+b+n-2},\qquad
\mathbb E(\theta\mid y)=\frac{a+y}{a+b+n}.
$$
If a posterior shape parameter is at most one, the maximum may be on a boundary; the interior formula should then not be used without checking the density. This small model already shows why “posterior mode” and “posterior mean” are different summaries.{{cite:gelman_bda2013}} (§§2.1–2.3, beta–binomial example)

## Properties — Connection with penalised regression
For a normal linear model with known error variance, a centred independent normal prior on coefficients adds a squared-length term to negative log likelihood. With the loss scaled as squared error, its coefficient is $\sigma^2/\tau^2$, where $\tau^2$ is the prior coefficient variance. The resulting MAP is a ridge solution, so a tighter prior shrinks coefficients more strongly. Replacing the normal coefficient prior by independent Laplace densities adds a sum of absolute coefficient values and produces the lasso objective. These are statements about the mode under specific likelihoods and priors; they do not make every ridge or lasso tuning choice an empirically justified prior.{{cite:hoerl_kennard1970}} (§2, pp. 57–58){{cite:tibshirani1996}} (§5, p. 277)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the beta–binomial calculation, the posterior kernel is $\theta^{a+y-1}(1-\theta)^{b+n-y-1}$. When both exponents are positive, the derivative of its log is $(a+y-1)/\theta-(b+n-y-1)/(1-\theta)$. Equating this to zero gives $(a+y-1)/(a+b+n-2)$, and the negative second derivative makes it a maximum. The beta mean is $(a+y)/(a+b+n)$.

For normal regression, $-2\sigma^2$ times the log posterior kernel is $\lVert y-X\beta\rVert_2^2+(\sigma^2/\tau^2)\lVert\beta\rVert_2^2$ plus a constant. A Laplace prior with each marginal density proportional to $\exp(-\lambda|\beta_j|)$ instead replaces the second term by $2\sigma^2\lambda\sum_j|\beta_j|$. The minimizers are respectively the ridge and lasso forms under those loss conventions.{{cite:tibshirani1996}} (§5, p. 277)

The coordinate warning can be checked exactly. If $\theta\sim\operatorname{Beta}(2,2)$, its density is $6\theta(1-\theta)$ and peaks at $\theta=1/2$. Write the odds $\eta=\theta/(1-\theta)$, so $\theta=\eta/(1+\eta)$ and $|d\theta/d\eta|=(1+\eta)^{-2}$. The transformed density is $6\eta/(1+\eta)^4$, whose log derivative is $1/\eta-4/(1+\eta)$. It peaks at $\eta=1/3$, although the odds of the original mode are $1$. Thus maximizing a continuous density and then transforming need not equal transforming the distribution and then maximizing its density.
:::
:::

## Worked example
Suppose six of eight trials succeed, and the prior for the success probability is $\operatorname{Beta}(3,2)$. The likelihood contributes six successes and two failures, so the posterior is $\operatorname{Beta}(9,4)$. Its MAP is $(9-1)/(9+4-2)=8/11\approx0.7273$. The posterior mean is $9/13\approx0.6923$, while the maximum-likelihood estimate is $6/8=3/4=0.75$. The prior and data have shifted the posterior peak slightly below the sample fraction, and the mean lies farther below because it averages the entire left-skewed posterior. The three numbers answer distinct questions; none by itself describes posterior spread.{{cite:gelman_bda2013}} (§§2.1–2.3, beta–binomial calculation)

**Your turn.** Keep the $\operatorname{Beta}(3,2)$ prior, but suppose four of eight trials succeed. Find the posterior, its MAP and mean, and the sample proportion.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Beta}(7,6)$. Its interior MAP is $(7-1)/(7+6-2)=6/11\approx0.5455$, its mean is $7/13\approx0.5385$, and the sample proportion is $4/8=1/2=0.5$. The prior favours larger probabilities, so both posterior summaries exceed the sample fraction.
:::

## Common misconceptions
A MAP value is not the probability that the parameter equals that value: a continuous parameter has zero probability at every single point. MAP is not generally a posterior mean; the beta example gives different values, and the mean is the Bayes action under squared-error loss. A flat prior does not make MAP a parameterization-free version of maximum likelihood, because densities gain a Jacobian on transformation. Finally, a large MAP density does not imply a concentrated posterior; density height and posterior mass over a region differ.{{cite:gelman_bda2013}} (§2.3, pp. 32–33)

## Assumptions and limits — When it fails as a summary
For the $\operatorname{Beta}(2,2)$ distribution in the proof, the MAP probability is $1/2$ but the MAP odds are $1/3$, not the transformed value $1$. The difference is caused solely by the density Jacobian, so reporting a bare continuous MAP without coordinates can mislead. A two-peaked posterior has a second problem: its global mode can jump abruptly from one peak to the other after a small data change, while both regions still carry appreciable mass. Near a boundary, an interior beta-mode formula can return an invalid value if its shape conditions fail. In these cases, inspect the posterior distribution and state which parameterization and loss matter for the decision.{{cite:gelman_bda2013}} (§2.3, pp. 32–33)

## History — History and connections
Bayes' essay was published posthumously by Richard Price in 1763; the subsequent Bayesian framework uses prior information and a likelihood to obtain a posterior distribution. MAP is a later way to compress that distribution to a single mode, rather than the aim of Bayes' original essay. In modern regression, Tibshirani explicitly derived the lasso as a posterior mode with double-exponential priors, linking Bayesian modelling to penalised optimization. [Posterior point summaries](posterior-point-summaries.qmd) compare the mode with the mean and median, while [ridge regression](ridge-regression.qmd) and [lasso](lasso.qmd) show how different coefficient priors lead to different penalties.{{cite:dodge2008}} (p. 32, “Bayes, Thomas”; “Bayesian Statistics”){{cite:tibshirani1996}} (§5, p. 277)
