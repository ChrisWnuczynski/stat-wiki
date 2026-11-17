## Motivating example
Adding a predictor to a regression can only improve its maximised training likelihood, even when the predictor carries no useful signal. A criterion for choosing model complexity must ask whether the improvement is large enough to pay for estimating another parameter. BIC makes that comparison with a penalty that grows with sample size. Its particular penalty comes from approximating the integral of the likelihood over a model's parameter prior, rather than from an arbitrary preference for small models.{{cite:schwarz1978}} (§1, pp. 461–462){{cite:kass_raftery1995}} (§4.1.3, pp. 778–779)

## Intuition — Balancing fit and complexity
For a regular model, the likelihood peak becomes narrower as more independent data arrive. A parameter direction has width on the order of $n^{-1/2}$ around its fitted value; integrating rather than maximising the likelihood therefore reduces the model evidence by one such factor per identifiable direction. Taking logarithms turns the shrinking volume into the $d\log n$ penalty after multiplication by $-2$. Thus BIC rewards fit but charges for the volume of parameter values needed to obtain it.{{cite:schwarz1978}} (§3, pp. 463–464){{cite:kass_raftery1995}} (§4.1.3, pp. 778–779)

## Definition
For model $M_j$ with $d_j$ freely identifiable parameters, a maximised log-likelihood $\ell_j(\widehat\theta_j)$ computed on the same data, and an appropriate sample size $n$, write

$$\operatorname{BIC}_j=-2\ell_j(\widehat\theta_j)+d_j\log n.$$

Choose the candidate with the *smaller* BIC. The likelihood must include the same data and its full normalising constants under each candidate. The effective $n$ is the scale at which the likelihood curvature grows; for grouped binomial responses it can be the sum of trial denominators rather than the count of grouped rows. This distinction changes the penalty and must be settled from the sampling design.{{cite:kass_raftery1995}} (§§3.1 and 4.1.3, pp. 776–779)

## Properties
For two regular candidate models, $-\tfrac12(\operatorname{BIC}_1-\operatorname{BIC}_2)$ captures the growing terms in the log Bayes factor for model 1 against model 2. It omits bounded terms from prior densities, model probabilities and local curvature, so exponentiating it need not give an accurate numerical Bayes factor. Close BIC values are especially sensitive to what was omitted. A candidate's BIC is a comparison score, not a posterior model probability.{{cite:kass_raftery1995}} (§4.1.3, eq. 9, pp. 778–779)

The contrast with AIC clarifies the purpose. AIC charges $2d_j$, a fixed penalty derived for predictive risk under its assumptions; BIC charges $d_j\log n$ to retain the leading model-evidence term in regular large samples. Neither score tells us whether any candidate is scientifically adequate. For sufficiently large $n$, BIC usually requires a larger likelihood improvement to add a parameter.{{cite:schwarz1978}} (§§1 and 3, pp. 461, 464){{cite:drton_plummer2017}} (§1, preprint pp. 1–2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a fixed-dimensional regular model with an interior identifiable maximum and a smooth positive prior $\pi_j$, expand the log-likelihood near $\widehat\theta_j$ as $\ell_j(\theta)=\ell_j(\widehat\theta_j)-\tfrac12(\theta-\widehat\theta_j)^\top H_{n,j}(\theta-\widehat\theta_j)+o_p(1)$ on the $n^{-1/2}$ neighbourhood contributing to the integral. If $H_{n,j}/n$ tends to a positive-definite limit, Laplace integration gives

$$m_j(x)=\int e^{\ell_j(\theta)}\pi_j(\theta)\,d\theta
=e^{\ell_j(\widehat\theta_j)}\pi_j(\widehat\theta_j)(2\pi)^{d_j/2}|H_{n,j}|^{-1/2}\{1+o_p(1)\}.$$

Because $|H_{n,j}|=n^{d_j}|H_{n,j}/n|$, taking $-2$ logarithms yields $-2\log m_j(x)=-2\ell_j(\widehat\theta_j)+d_j\log n+O_p(1)$. The first two terms are BIC. For a comparison, subtracting the two log evidences leaves $\log\{m_1(x)/m_2(x)\}=-\tfrac12(\operatorname{BIC}_1-\operatorname{BIC}_2)+O_p(1)$. The remainder explains why this is a leading-order comparison rather than an exact Bayes factor.{{cite:schwarz1978}} (§3, pp. 463–464){{cite:kass_raftery1995}} (§§4.1.1–4.1.3, pp. 777–779)
:::
:::

## Worked example
Two models fitted to the same $n=150$ observations have maximised log-likelihoods $-210$ and $-205$, with $d_1=2$ and $d_2=4$. Since $\log150\approx5.010635$, their scores are $\operatorname{BIC}_1=420+2\log150\approx430.0213$ and $\operatorname{BIC}_2=410+4\log150\approx430.0425$. The simpler model wins, but by only $0.0213$ BIC units. The larger model gains five log-likelihood units for two extra parameters; it needs more than $\log150\approx5.010635$ to overcome the BIC penalty. This near tie is a reason to inspect the models and the prior-sensitive terms omitted by BIC, not to declare one overwhelmingly supported.{{cite:kass_raftery1995}} (§4.1.3, pp. 778–779)

**Your turn.** On the same $n=400$ observations, model 1 has $\ell_1=-500$ and $d_1=3$; model 2 has $\ell_2=-493$ and $d_2=5$. Compute both BICs and choose a model.

::: {.callout-tip collapse="true" title="Answer"}
Here $\log400\approx5.991465$. The scores are $1000+3\log400\approx1017.974$ and $986+5\log400\approx1015.957$. Model 2 has the smaller BIC by about $2.017$. Its seven-unit log-likelihood gain exceeds the two-parameter threshold $\log400\approx5.991465$. This comparison assumes both fits used the same observations and well-defined regular likelihood maxima.
:::

## Common misconceptions
BIC is not itself a probability that a model is true; posterior model probabilities also require model priors and appropriately computed marginal likelihoods. A lower BIC does not mean a better out-of-sample predictor in every problem: predictive criteria such as AIC and validation target a different question. Nor does the word “Bayesian” mean one has specified and checked a useful parameter prior; BIC discards its bounded contribution in a regular asymptotic calculation. Finally, counting every symbol in a model formula as a parameter can misstate the penalty when parameters are fixed, constrained or nonidentifiable.{{cite:kass_raftery1995}} (§§3.1, 4.1.3, pp. 776–779){{cite:drton_plummer2017}} (§1, preprint pp. 1–3)

## Assumptions and limits
The regular derivation needs an interior peak and information that is nonsingular in each parameter direction. In a two-component mixture whose means coincide, changing their mixture weight does not change the distribution; the information is singular and the ordinary Gaussian-volume argument fails. A mixture with an unconstrained covariance that collapses onto one data point may not even have a finite global likelihood maximum, so inserting a numerical local maximum into BIC does not repair the model. A grouped-binomial analysis with 20 groups of 50 trials illustrates a different pitfall: using $n=20$ because there are 20 rows gives a different penalty from using the 1,000 Bernoulli trials that drive the curvature. The appropriate choice depends on the fitted likelihood and dependence assumptions.{{cite:drton_plummer2017}} (§1, preprint pp. 1–4){{cite:kass_raftery1995}} (§4.1.3, p. 779)

## Connections
The [marginal likelihood](marginal-likelihood-and-bayes-factor.qmd) integrates over parameters, whereas the [likelihood](likelihood-function.qmd) entering BIC is maximised. The [Laplace approximation](laplace-approximation.qmd) connects the two under regularity. The [AIC](akaike-information-criterion.qmd) comparison and the answered [BIC-by-hand exercise](../questions/ex-sl-06-2.qmd) show how differing penalties can change a model choice. The [mixture-selection exercise](../questions/ex-sl-06-7.qmd) applies BIC but also asks why a better training fit need not predict better; its mixture setting requires the singularity caution above.{{cite:kass_raftery1995}} (§4.1.3, pp. 778–779){{cite:drton_plummer2017}} (§1, preprint pp. 1–4)

## History
Schwarz proposed his dimension penalty in 1978 by expanding a Bayesian model-choice integral for linear subfamilies of exponential families. He contrasted its growing penalty with Akaike's fixed parameter penalty. Kass and Raftery's 1995 review popularised the name Bayesian information criterion and emphasized that it is a rough log-Bayes-factor approximation: its omitted constants can prevent accurate factor estimates even in large samples. Later singular-model work made explicit why parameter count can fail to describe the evidence's asymptotic scaling when Fisher information loses rank.{{cite:schwarz1978}} (§§1–3, pp. 461–464){{cite:kass_raftery1995}} (§4.1.3, pp. 778–779){{cite:drton_plummer2017}} (§1, preprint pp. 1–4)
