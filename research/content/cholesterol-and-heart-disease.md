## Motivating example

The hundred records pair a cholesterol measurement with a yes-or-no disease indicator and a sex label. On the plot, the individual outcomes remain binary even though the fitted disease probability changes smoothly with cholesterol. This makes the example useful for separating an observed response from a modelled conditional chance. The curve summarizes an association in these records; it does not turn an observational comparison into evidence that changing cholesterol would change a person's disease status.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, pp. 371–372, binomial mean and link)

## Intuition — From points to conditional probabilities

Vertical jitter moves plotted zeros and ones slightly so overlapping records can be seen. It does not change their Bernoulli values. The logistic curve describes the chance of disease at a specified cholesterol value and sex, and its vertical position should be read as a model prediction rather than an individual patient's outcome. When the probability is near one half, similar patients can have either outcome; near zero or one, one outcome is more common. The shaded cholesterol window shows where the reported data support interpolation more directly than extrapolation.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, pp. 371–372)

## Definition — Variables and fitted model

Each record has a continuous cholesterol value, a sex category and a binary disease response. The displayed fit uses a female baseline and an indicator for male sex; cholesterol enters linearly on the *log-odds* scale. A logit converts that unbounded fitted score to a probability in $(0,1)$. A one-unit cholesterol difference at the same sex therefore has the same fitted odds multiplier throughout the model, while its probability difference depends on the starting cholesterol value.{{cite:geyer2022_exp_family}} (§7.1, binomial natural parameter and inverse logit){{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380)

## Properties — Conditional comparisons

For the fitted equation, the cholesterol slope is $1.5842$, so a one-unit increase multiplies conditional odds by $e^{1.5842}\approx4.87539$. The sex coefficient is $-0.1094$, giving a male-to-female conditional odds ratio $e^{-0.1094}\approx0.89637$ at a common cholesterol value. These are comparisons *within the fitted model*, holding the other predictor fixed. Neither multiplier is a risk ratio, and the small conditional sex coefficient does not show that sex affects disease only through cholesterol.{{cite:geyer2022_exp_family}} (§7.1, logit natural parameter){{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380)

::: {.callout-note collapse="true" title="Proof"}
The fitted log odds for sex indicator $s$ and cholesterol $c$ have form $\eta(s,c)=\beta_0+\beta_s s+\beta_c c$. Since odds equal $e^{\eta(s,c)}$, raising $c$ by one while keeping $s$ fixed gives $e^{\eta(s,c+1)}/e^{\eta(s,c)}=e^{\beta_c}$. Changing $s$ from zero to one at fixed $c$ similarly gives $e^{\beta_s}$. Probability is $e^\eta/(1+e^\eta)$, a nonlinear function, so a constant odds multiplier does not imply a constant difference or ratio on the probability scale.{{cite:geyer2022_exp_family}} (§7.1, eqs. 7.1–7.5)
:::

## Interpretation — What the plot can show

The plotted disease outcomes tend to be more common at higher cholesterol values in this collection. The solid logistic curve keeps predictions inside probability bounds; the straight-line comparison is useful for seeing why an unrestricted mean model fails near the edges. The dashed curves reflect the displayed slope interval while holding the intercept fixed, so they are not a joint confidence band for every aspect of the regression. The figure can illustrate a model and an association. It cannot identify the sampling mechanism, establish representativeness of a broader population, or determine a causal effect from the plotted variables alone.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, 3.3, pp. 371–372, 379–380)

## Statistical use — Reading a prediction

For a female patient with cholesterol $5.5$, the fitted score is $-9.3203+1.5842(5.5)=-0.6072$, giving probability $1/(1+e^{0.6072})\approx0.35270$. At cholesterol $6.5$, the score is $0.9770$ and probability $\approx0.72651$. The probability rises by about $0.37381$, much less than the odds multiplier $4.87539$ might suggest to a reader who confuses odds with risk. The numerical predictions refer to specified covariate profiles and inherit every modelling and data-collection limitation of the fit.{{cite:geyer2022_exp_family}} (§7.1, inverse logit)

## Worked example

At cholesterol $6.5$, the female score is $0.9770$. For a male at the same cholesterol it is $0.9770-0.1094=0.8676$, giving fitted probability $\approx0.70425$ rather than the female $\approx0.72651$. The conditional probability difference is about $-0.02227$, while the conditional odds ratio is $0.89637$. The comparison is at a common cholesterol value; it does not compare the overall disease proportions of the two sex groups, whose cholesterol distributions may differ.{{cite:geyer2022_exp_family}} (§7.1, inverse logit and odds)

**Your turn.** Use the displayed fit to find the fitted disease probability for a male at cholesterol $5.5$. Compare it with the female probability at that same cholesterol and state which contrast is constant across cholesterol under this model.

::: {.callout-tip collapse="true" title="Answer"}
The male score is $-9.3203-0.1094+1.5842(5.5)=-0.7166$, so the fitted probability is $1/(1+e^{0.7166})\approx0.32814$. The female probability there is $\approx0.35270$, a difference of about $-0.02456$. The male-to-female *odds ratio* $e^{-0.1094}\approx0.89637$ is constant at a common cholesterol value; the probability difference is not.{{cite:geyer2022_exp_family}} (§7.1, logit interpretation)
:::

## Common misconceptions

Jittered points are still zero-one observations, not fractional disease measurements. The cholesterol slope describes a change in log odds, not a fixed increase in disease probability. A lower fitted male probability at one common cholesterol value does not imply a lower *marginal* disease rate for males in these data. The fitted association is not proof of a cholesterol intervention effect or of a pathway through sex. Finally, the intercept prediction at cholesterol zero is an extrapolation far outside the plotted range, not a clinically meaningful baseline patient.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, 3.3, pp. 371–372, 379–380)

## Assumptions and limits — What the records cannot establish

The collection method, sampling frame and clinical measurement protocol are not specified, so the hundred points cannot support a claim of population prevalence or a clinical risk rule for new hospitals. A hidden age difference could confound the cholesterol association, and repeated measurements on the same patient would violate the independent-Bernoulli reading. Disease misclassification would distort the fitted probabilities. The logistic line also assumes a straight cholesterol effect on the log-odds scale; a threshold or nonlinear relation would need a different predictor form. The plot and coefficients are useful for learning the model, with those limits kept attached to any interpretation.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, 3.3, pp. 371–372, 379–380)

## Connections

[Binary responses in a GLM](binary-responses-in-a-glm.qmd) explains the Bernoulli distribution and link. [Interpreting a logistic regression](interpreting-a-logistic-regression.qmd) develops conditional odds comparisons, while [deviance](deviance.qmd) and the [logit, probit and complementary log-log links](logit-probit-and-complementary-log-log-links.qmd) show how the same responses can be assessed under related models.{{cite:nelder_wedderburn1972}} (§§1–3.3, pp. 370–380)

### Guided practice

**1. Odds versus probability.** Does the fitted cholesterol odds multiplier of about $4.88$ mean that the fitted disease probability is multiplied by $4.88$ at each one-unit increase?

::: {.callout-tip collapse="true" title="Answer"}
No. For females the displayed fit gives probabilities about $0.35270$ at $5.5$ and $0.72651$ at $6.5$. Their ratio is about $2.06$, while the odds ratio is about $4.88$. A logistic model keeps probabilities below one as odds continue growing.{{cite:geyer2022_exp_family}} (§7.1)
:::

**2. Sampling claim.** Can the fitted curve establish the disease prevalence of an entire region from these hundred records?

::: {.callout-tip collapse="true" title="Answer"}
No. A prevalence estimate for a region needs a known target population and an appropriate sampling design or justified transport assumptions. The recorded relationship and fitted model alone do not supply those facts.
:::
