## Motivating example
A hospital counts arrivals in each of three hours. If a Poisson regression assigns the same mean to all three hours, it must compromise when the counts differ. A saturated comparison instead gives each hour its own mean and asks how much likelihood the simpler regression gives up. The saturated fit is useful precisely because it sets a common reference for models of the **same** observations and response family.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)

## Intuition
One free mean per independent observation can follow every observed response. That is a description of the sample, not an explanation of why the responses arose. A predictor model deliberately ties the means together through fewer parameters so that it can estimate a pattern and make predictions. Comparing their likelihoods measures the price of those constraints. In the usual GLM deviance, the saturated likelihood is the zero-discrepancy reference; a fitted model farther from it has a larger deviance. A zero training deviance says nothing by itself about prediction for a new patient or hour.{{cite:nelder_wedderburn1972}} (§2.3, pp. 375–376){{cite:rstats_glm2026}} (Value, deviance)

## Definition
For independent responses $y_1,\ldots,y_n$ in a specified response family, a saturated *mean* model lets each observation have its own mean $\tilde\mu_i$. For the ordinary Poisson and normal families, the maximum-likelihood choice is $\tilde\mu_i=y_i$; for a binomial count of $y_i$ successes in $m_i$ trials, the fitted mean count is $y_i$. A Bernoulli response of zero or one requires a boundary probability, so its saturation is a likelihood limit under a logit link rather than a finite logit coefficient. The number of independent mean parameters, not the mere number of symbols written in a formula, determines saturation.{{cite:nelder_wedderburn1972}} (§2.3, p. 375, complete model and deviance){{cite:rstats_family2026}} (Details, binomial response forms)

Holding any dispersion convention fixed, compare a constrained fit with the saturated fit using $D=2(\ell_{\mathrm{sat}}-\ell_{\mathrm{fit}})$ when dispersion is one. For an estimated or specified dispersion $\phi$, distinguish the unscaled deviance $D$ from the corresponding likelihood-ratio quantity $D/\phi$ where the family permits that representation. This comparison requires the same response family and the same observations in both likelihoods.{{cite:nelder_wedderburn1972}} (§2.3, pp. 375–376){{cite:rstats_glm2026}} (Value, deviance and null.deviance)

## Properties
Saturation gives the largest likelihood among mean fits in its family, so its deviance is zero and every constrained fit has nonnegative deviance. If model $M_0$ is nested in $M_1$, both fitted by maximum likelihood on the same data, the saturated reference cancels: $D_0-D_1=2(\ell_1-\ell_0)$ at unit dispersion. This identity explains why analysis of deviance compares successive fits. It does **not** by itself supply a chi-squared reference distribution; that approximation needs regularity, adequate information and an appropriate sampling model.{{cite:nelder_wedderburn1972}} (§§2.3–2.4, pp. 375–376)

For Poisson observations, a saturated mean of zero lies on the boundary. The convention $0\log0=0$ gives a finite deviance contribution at a zero count. For normal observations with known common variance, saturation removes the squared residuals; if variance is also allowed to shrink freely to zero for each perfectly fitted observation, the normal density becomes unbounded. The reference therefore depends on what is held fixed in the family and dispersion model.{{cite:nelder_wedderburn1972}} (§§2.3, 3.1, pp. 375–376)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a Poisson observation, $\ell(\mu;y)=y\log\mu-\mu-\log(y!)$. Its derivative is $y/\mu-1$, giving the maximum at $\mu=y$ for $y>0$; for $y=0$, $\ell=-\mu$ approaches its supremum as $\mu\downarrow0$. Subtracting the fitted log likelihood gives $2\{y\log(y/\hat\mu)-(y-\hat\mu)\}$, with the zero term interpreted by continuity. Nonnegativity follows because $\ell_{\mathrm{sat}}$ is the supremum over a model containing the constrained mean vector.

If $M_0\subseteq M_1$ and $D_j=2(\ell_{\mathrm{sat}}-\ell_j)$, subtraction yields $D_0-D_1=2(\ell_1-\ell_0)\geq0$. In the normal family with known variance $\sigma^2$, subtracting $-(y-\mu)^2/(2\sigma^2)$ at $\mu=y$ and $\mu=\hat\mu$ gives $(y-\hat\mu)^2/\sigma^2$. These are likelihood identities, independent of an asymptotic test approximation.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)
:::
:::

## Statistical use — Reading deviance
The null deviance uses an intercept-only mean fit as the constrained model; residual deviance uses the chosen predictor fit. Each retains the saturated likelihood as its reference. Their difference asks how much the predictors improved the maximized likelihood. The residual deviance asks a different question: how far the final model still lies from saturation. A large improvement can coexist with substantial remaining lack of fit. The number of residual degrees of freedom is usually the number of independent observations minus the rank of the fitted design matrix.{{cite:nelder_wedderburn1972}} (§2.3, pp. 375–376){{cite:rstats_glm2026}} (Value, deviance and null.deviance)

A saturated model is a useful *benchmark*, but fitting it as a final predictive model risks following noise. It can also obscure pooling: for a binomial count, one free probability per group is saturated at the grouped-count level, whereas treating all Bernoulli trials as separate observations changes the observation units and the comparison. State those units before interpreting a deviance.{{cite:rstats_family2026}} (Details, binomial response forms){{cite:nelder_wedderburn1972}} (§2.3, complete model)

## Worked example
Suppose independent Poisson counts are $y=(0,2,4)$. An intercept-only model has fitted mean $\hat\mu=(2,2,2)$, their sample average; the saturated means are $(0,2,4)$, with the first understood as a boundary limit. The three deviance contributions are $4$, $0$, and $2\{4\log(4/2)-(4-2)\}=8\log2-4\approx1.5452$. The total is $D=8\log2\approx5.5452$. The zero-count hour contributes most of the discrepancy. This is a likelihood comparison with a perfectly flexible Poisson mean model, not a probability that the intercept-only model is true.{{cite:nelder_wedderburn1972}} (§2.3, p. 375, Poisson deviance)

**Your turn.** For two independent Poisson counts $y=(1,3)$, fit one common mean and calculate the saturated means and total Poisson deviance. Which count has the larger contribution?

::: {.callout-tip collapse="true" title="Answer"}
The common mean is $\hat\mu=2$ and the saturated means are $(1,3)$. The first contribution is $2\{\log(1/2)+1\}\approx0.6137$; the second is $2\{3\log(3/2)-1\}\approx0.4328$. Their sum is about $1.0465$, so the smaller count contributes more even though each is one unit from its fitted mean. The Poisson likelihood is asymmetric around two on the count scale.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)
:::

## Common misconceptions
“Saturated” does not mean a model with many scientifically meaningful predictors: it means enough independent fitted mean values to reach the family likelihood maximum for the observations. Zero saturated deviance is automatic and is therefore no evidence that the response family describes the data well. A lower residual deviance after adding predictors is an in-sample comparison, not a guarantee of better predictions. Finally, a deviance difference is an exact likelihood identity under the stated setup, whereas its common chi-squared calibration is conditional on further assumptions.{{cite:nelder_wedderburn1972}} (§2.3, pp. 375–376)

## Assumptions and limits — When the benchmark changes
If observations are dependent, multiplying independent Poisson probabilities ignores that dependence, so a deviance computed from that product does not compare the intended joint models. If a binomial response records grouped counts, a “one probability per individual” fit uses a different data representation from one probability per group. If normal variance is unrestricted while a separate mean fits every observation, the likelihood can diverge as variance approaches zero. These cases require a clearly specified likelihood, observation unit and dispersion treatment before a saturated reference makes sense.{{cite:nelder_wedderburn1972}} (§§1.1, 2.3, pp. 370–371, 375)

## Connections
[Deviance](deviance.qmd) measures the likelihood gap from the saturated fit. [Null deviance](null-deviance.qmd) and [residual deviance](residual-deviance.qmd) use that same reference for two constrained mean models; [analysis of deviance](analysis-of-deviance.qmd) subtracts their values. [Overfitting](overfitting.qmd) explains why a nearly saturated training fit can generalize poorly.{{cite:nelder_wedderburn1972}} (§§2.3–2.4, pp. 375–376)

## History
Nelder and Wedderburn introduced the analysis of deviance in their 1972 account of generalized linear models. They described a progression from a minimal model toward a *complete* model that fits the data exactly, with each step trading better fit against greater complexity. Their complete model supplies the saturated reference used in current GLM terminology, while R's `glm` output keeps the null and residual deviances distinct.{{cite:nelder_wedderburn1972}} (§2.3, p. 375){{cite:rstats_glm2026}} (Value, null.deviance and deviance)
