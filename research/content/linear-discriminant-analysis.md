## Motivating example
A clinic has labelled records from two groups and must assign a new patient from a few measurements. A classifier that simply picks the nearest group mean treats a centimetre of change in every measurement alike. Linear discriminant analysis (LDA) instead uses the within-group variation to decide which differences are informative, while the group frequencies supply prior odds. Its line or hyperplane is the result of those choices, not an arbitrary straight-line fit.{{cite:james_islr2013}} (§4.4.1–4.4.3, pp. 138–144)

## Intuition
Suppose two measurements rise and fall together within each group. Moving along that common direction is less surprising than moving across it, even when the Euclidean distances are identical. LDA measures displacement through the inverse pooled covariance, then combines that evidence with the prior chance of each group. The two-class calculation below shows exactly how this can disagree with a Euclidean nearest-mean rule. The shared covariance gives each group the same elliptical shape; this is what lets their quadratic log densities differ by a linear expression.{{cite:james_islr2013}} (§4.4.3, pp. 142–144)

## Interpretation — A score is a log-odds comparison
For $G$ classes, compare the scores $\delta_g(\mathbf{x})=\mathbf{x}^{\mathsf T}\Sigma^{-1}\boldsymbol\mu_g-\tfrac12\boldsymbol\mu_g^{\mathsf T}\Sigma^{-1}\boldsymbol\mu_g+\log\pi_g$, replacing unknown quantities by training estimates in practice. Their differences are log posterior odds under the model; a score alone is not a posterior probability. With two classes, exponentiating and normalizing the two scores gives a probability for either class. A prior change shifts the intercept of the pairwise boundary without changing its direction, provided the class-conditional distributions stay fixed. Unequal error costs can move the decision threshold again, even with the same fitted probabilities.{{cite:james_islr2013}} (§4.4.1–4.4.3, pp. 138–144)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For class $g$, the multivariate normal log density plus $\log\pi_g$ is $-\tfrac12(\mathbf{x}-\boldsymbol\mu_g)^{\mathsf T}\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu_g)+\log\pi_g$ plus a normalizing term common to all classes. Expanding gives $-\tfrac12\mathbf{x}^{\mathsf T}\Sigma^{-1}\mathbf{x}+\delta_g(\mathbf{x})$. The first term cancels in every pairwise comparison, proving the score formula and linearity of the boundary. For labelled observations, within-class centring imposes one linear constraint in each of the $G$ classes, so the pooled scatter has rank at most $n-G$. Thus its ordinary inverse cannot exist when $p>n-G$; equality still needs full rank.{{cite:james_islr2013}} (§4.4.3, pp. 142–144)
:::
:::

## Statistical use
Estimate each class mean from its labelled cases and usually pool their within-class scatter using divisor $n-G$; estimate priors from class proportions only when those proportions represent the population to be classified. This last condition matters under case-control sampling or deliberate class balancing. The score then predicts the class with largest posterior probability under equal error costs. Inspect class-specific errors on separate validation data, because an impressive overall accuracy can conceal poor prediction for a rare class. The fitting formulas and a complete two-dimensional calculation follow.{{cite:james_islr2013}} (§4.4.2–4.4.3, pp. 140–145)

If groups have markedly different covariance matrices, the quadratic terms do not cancel; a quadratic discriminant model can represent a curved boundary that ordinary LDA cannot. With $n=90$, $G=2$, and $p=500$, pooled within-class scatter has rank at most $88$, so ordinary LDA cannot invert it without dimension reduction or regularization. Even with $p<88$, a nearly singular covariance can make the rule unstable. A balanced training set drawn from a population with rare class-2 cases also gives misleading posterior odds if its sample proportions are used as population priors. These are different failure mechanisms: shape, invertibility, and prevalence.{{cite:james_islr2013}} (§4.4.3–4.4.4, pp. 142–149)

## Worked example — The prior moves a boundary
Consider one measurement with class means $\mu_1=0$ and $\mu_2=2$, common variance $1$, and priors $\pi_1=0.8$, $\pi_2=0.2$. The class-2 minus class-1 score is $2x-2+\log(0.2/0.8)=2x-2-\log4$. The boundary is therefore $x=1+\tfrac12\log4\approx1.693147$. At $x=1.4$, the log odds are about $-0.586294$, giving class-2 posterior $1/(1+e^{0.586294})\approx0.357486$: classify as class 1. Equal priors would give posterior $1/(1+e^{-0.8})\approx0.689974$ and class 2. The measurement has not changed; the relevant population frequency has.{{cite:james_islr2013}} (§4.4.1–4.4.2, pp. 138–141)

**Your turn.** Keep these means, variance and priors, but classify $x=1.8$. Calculate the class-2 posterior as well as the class label.

::: {.callout-tip collapse="true" title="Answer"}
The score difference is $2(1.8)-2-\log4\approx0.213706$, so the class-2 posterior is $1/(1+e^{-0.213706})\approx0.553224$. It is just above one half: predict class 2.
:::

## Common misconceptions
A linear boundary does not say that the measurements are normally distributed without conditioning on class; normality is an assumption about each class distribution. LDA's pooled covariance is not automatically the maximum-likelihood covariance: divisor $n-G$ supplies an unbiased within-class estimate, while the likelihood divisor is $n$. Finally, the largest discriminant score is not itself a calibrated probability; probabilities require normalization of the exponentiated scores, and calibration can still fail when the Gaussian model or priors are wrong.{{cite:james_islr2013}} (§4.4.1–4.4.4, pp. 138–149)

## Connections
[Unequal priors](../questions/ex-sl-08-3.qmd) change the intercept in the two-class rule; [the fitted LDA model](../questions/ex-sl-08-7.qmd) asks how class means and pooled covariance are obtained; [high-dimensional LDA](../questions/ex-sl-18-7.qmd) probes the rank limit in a $500$-predictor example. [Quadratic discriminant analysis](quadratic-discriminant-analysis.qmd) allows separate covariances, while [Bayes classifier](bayes-classifier.qmd) names the ideal decision when the true class distributions are known.{{cite:james_islr2013}} (§4.4, pp. 138–149)

## History
Fisher's 1936 paper, *The Use of Multiple Measurements in Taxonomic Problems*, supplied an early discriminant-function treatment using Iris measurements. The Gaussian shared-covariance classifier here is a modern probabilistic formulation of linear discrimination.{{cite:fisher1936}} (§§I–II, p. 179){{cite:james_islr2013}} (§4.4, pp. 138–149)
