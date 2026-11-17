## Motivating example — Ask what an added term explains
A larger statistical model can fit a sample better simply because it has more parameters. Analysis of deviance compares a sequence of fitted models by measuring how much likelihood improves when terms are added. A useful table states the models being compared, the decrease in deviance, the change in design rank and the reference distribution used for calibration. Sequential rows answer questions about a specified order of model enlargement.{{cite:wuthrich_merz2022_glm}} (§5.3.3, model selection and sequential tables)

## Definition — The saturated likelihood cancels in a difference
Let $\ell_0$ and $\ell_1$ be maximised log likelihoods in nested models, with model one containing model zero. For a common known dispersion $\phi$, write unscaled deviance as $D_j=2\phi(\ell_{\mathrm{sat}}-\ell_j)$. Then
$$\frac{D_0-D_1}{\phi}=2(\ell_1-\ell_0).$$
Thus the scaled deviance decrease is the likelihood-ratio statistic. It is nonnegative because the larger parameter space includes every fit allowed by the smaller model. This comparison requires the same response data and compatible likelihood conventions. Deviances from unrelated likelihoods are not automatically comparable by subtraction.{{cite:wuthrich_merz2022_glm}} (§5.3.2, nested-model likelihood-ratio test)

## Properties — Dispersion changes the calibration
For regular identifiable models with an interior null and enough information, the likelihood-ratio statistic has an asymptotic chi-squared reference law with degrees of freedom equal to the parameter-rank difference. Boundaries, singular designs or incidental parameters can invalidate that reference. Small individual Poisson means also make residual-deviance chi-squared approximations unreliable in settings where increasing sample size does not cure the approximation. A nested-model difference and the deviance against a growing saturated model are different asymptotic comparisons.{{cite:wuthrich_merz2022_glm}} (§5.3.1, residual deviance and dispersion; §5.3.2)

For Gaussian linear models with common unknown variance, unscaled deviance is residual sum of squares. With reduced and full design ranks $r_0<r_1$, the statistic
$$F=\frac{(D_0-D_1)/(r_1-r_0)}{D_1/(n-r_1)}$$
has the exact $F_{r_1-r_0,n-r_1}$ null law under independent normal equal-variance errors. The denominator estimates dispersion from the full model. Using an estimated dispersion to form an F-type comparison in another GLM requires a separate approximation argument.{{cite:nist_oneway_anova}} (§3.2.3.1, mean-square ratio and assumptions)

## Worked example — The same decrease on two scales
Suppose two nested Gaussian fits use $n=20$ observations, with design ranks two and four, and residual sums of squares $50$ and $32$. The deviance decreases by $18$ for two added coefficients. If the error variance is known to be $\phi=2$, the scaled likelihood-ratio statistic is $9$. If the variance is instead estimated from the full fit, the mean square error is $32/16=2$ and the exact F statistic is $(18/2)/2=4.5$. These statistics use different reference distributions despite being based on the same fitted sums of squares.{{cite:nist_oneway_anova}} (§3.2.3.1)

**Your turn.** If a fifth independent design column lowers the full-model SSE from $32$ to $30$, what is the F statistic for adding that one column?

::: {.callout-tip collapse="true" title="Answer"}
The new residual degrees of freedom are $20-5=15$. The statistic is $(32-30)/(30/15)=1$.
:::

## Assumptions and limits — A selection path changes the question
When design columns are not orthogonal, the improvement from adding a term depends on the model already fitted. Tests of a block of related interactions differ from testing only the final interaction in a sequential table. Dummy columns for one categorical variable should be considered as a group when the question concerns that whole variable. Repeated stepwise choices also require caution in interpreting the nominal p-values as if the final model had been specified in advance.{{cite:wuthrich_merz2022_glm}} (§5.3.3, order-dependent selection)
