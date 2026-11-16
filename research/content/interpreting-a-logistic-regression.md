## Motivating example
A medical report might say that a fitted group coefficient doubles the odds of an event after accounting for age. Readers often want to know whether that means twice the event probability or a fixed increase in percentage points. Neither follows from the coefficient alone. Interpretation begins by fixing the comparison, identifying which outcome is coded as the event, and then converting the fitted odds back to probabilities at a stated baseline.{{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)

## Intuition
Logistic regression makes the **log odds** additive in predictors. One unit more of a covariate adds its coefficient to log odds, so it multiplies the odds by the coefficient's exponential. The event probability is recovered through a curved inverse-logit transformation. As a result, a fixed odds multiplier can correspond to a small probability change when an event is rare and a different change when it is common. The coefficient describes an association conditional on the other covariates in the model.{{cite:agresti_tarantola_varriale2023}} (§5.1, p. 156)

## Definition
For a binary outcome $Y$, let $p(z,x)=\Pr(Y=1\mid z,x)$, where $z$ is a group indicator and $x$ collects other predictors. In a no-interaction logistic model,
$$
\operatorname{logit}p(z,x)
=\log\frac{p(z,x)}{1-p(z,x)}
=\alpha+\beta z+\gamma^\top x.
$$
At a fixed $x$, changing $z$ from zero to one adds $\beta$ to log odds and multiplies the event odds by $r=e^\beta$. This is a **conditional odds ratio**. A continuous covariate coefficient has the same one-unit log-odds interpretation when the other predictors are held fixed; changing units changes what “one” means.{{cite:agresti_tarantola_varriale2023}} (§5.1, p. 156){{cite:nelder_wedderburn1972}} (§3.3, p. 379)

The intercept $\alpha$ is the log odds when every predictor in the model is zero, under the chosen reference categories. Its inverse logit is the corresponding model probability. If zero age, zero dose, or another baseline value lies outside the data's meaningful range, that probability is an extrapolation, even though the algebra is correct. Centering a predictor at a meaningful value can make the intercept interpretable without changing the model's predictions.{{cite:agresti_tarantola_varriale2023}} (§5.1, model equation, p. 156)

## Properties — Translating odds to probabilities
If the reference-group event probability at a chosen $x$ is $p_0$, an odds ratio $r$ implies
$$
p_1=\frac{r p_0}{1-p_0+r p_0}.
$$
The formula shows why $r$ alone does not specify a risk difference $p_1-p_0$ or risk ratio $p_1/p_0$. Those require a baseline probability. For a continuous predictor, the odds multiplier over a change of $d$ units is $e^{d\beta}$ under a linear logit with no interaction, while the probability change still depends on the starting predictor values.{{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)

Reversing the group contrast replaces $e^\beta$ by its reciprocal. Recoding the event from $Y=1$ to $Y=0$ also reverses the odds ratio. A statement such as “higher odds” is incomplete until both the outcome and reference group are named. With an interaction $\delta zx$, the group log odds ratio at covariate value $x$ is $\beta+\delta x$ rather than one constant $\beta$.{{cite:agresti_tarantola_varriale2023}} (§5.1, conditional group comparisons, p. 156)

## Statistical use — Reporting an effect
For an applied report, give the coding, the covariate contrast, and what was held fixed. Then present the fitted odds ratio alongside predicted probabilities for representative, observed covariate values. This makes the model's scale clear and allows the reader to assess practical size. A group odds ratio in an observational analysis describes a conditional association; interpreting it causally requires a design and assumptions beyond the regression equation.{{cite:agresti_tarantola_varriale2023}} (§§5.1–5.3, pp. 155–160)

An adjusted odds ratio need not equal the marginal odds ratio obtained by averaging over a covariate, even if the covariate is balanced across groups. This noncollapsibility is a property of the odds scale and must be distinguished from a change caused by confounding. Probability-scale contrasts at specified covariate values, or appropriately averaged predictions, can make the target comparison explicit.{{cite:agresti_tarantola_varriale2023}} (§§5.1, 5.3, pp. 156–160)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
At the same $x$, subtract the two linear predictors:
$$
\log\frac{p(1,x)}{1-p(1,x)}
-\log\frac{p(0,x)}{1-p(0,x)}=\beta.
$$
Exponentiating gives the odds ratio $r=e^\beta$. Write $p_0=p(0,x)$ and $p_1=p(1,x)$. The equation $p_1/(1-p_1)=r p_0/(1-p_0)$ implies $p_1(1-p_0+r p_0)=r p_0$, proving $p_1=r p_0/(1-p_0+r p_0)$. The denominator depends on $p_0$, so the probability change cannot generally equal $\beta$ or be determined by $r$ alone. If the linear predictor is $\eta=\alpha+\beta x$, then $p=e^\eta/(1+e^\eta)$ and differentiation gives $dp/dx=\beta p(1-p)$; the probability slope varies along the curve even when $\beta$ is constant.{{cite:agresti_tarantola_varriale2023}} (§5.1, p. 156)

For the separation counterexample below, suppose every observation with $z=0$ has $Y=0$ and every one with $z=1$ has $Y=1$. Taking $\alpha\to-\infty$ and $\alpha+\beta\to+\infty$ drives both fitted groups' correct-outcome probabilities toward one, so the Bernoulli likelihood approaches its supremum without a finite coefficient pair attaining it.
:::
:::

## Worked example
Consider a hypothetical event model for two groups at the same value of a background covariate. The reference group has event odds $1/3$, so its probability is $p_0=1/4$. Suppose the group coefficient is $\beta=\log 2$, an odds multiplier of $2$. The other group's odds are $2/3$, giving $p_1=(2/3)/(1+2/3)=2/5=0.4$. The risk ratio is $(2/5)/(1/4)=8/5=1.6$, and the risk difference is $2/5-1/4=3/20=0.15$, or 15 percentage points. “Twice the odds” is correct; “twice the probability” or a fixed probability increase is not.{{cite:agresti_tarantola_varriale2023}} (§5.1, analogous odds-versus-probability comparison, p. 156)

**Your turn.** At another fixed covariate value, the reference-group event probability is $1/5$ and a fitted group coefficient is $\log 3$. Find the other group's event probability, risk ratio, and risk difference. Explain which of these numbers is constant across covariate values under a no-interaction logistic model.

::: {.callout-tip collapse="true" title="Answer"}
The reference odds are $(1/5)/(4/5)=1/4$. Multiplying by $3$ gives odds $3/4$, hence $p_1=(3/4)/(1+3/4)=3/7\approx0.4285714$. The risk ratio is $(3/7)/(1/5)=15/7\approx2.1428571$, and the risk difference is $3/7-1/5=8/35\approx0.2285714$. The conditional odds ratio $3$ is constant for the stated group contrast when there is no interaction; the probability difference and ratio vary with the baseline probability.{{cite:agresti_tarantola_varriale2023}} (§5.1, p. 156)
:::

## Common misconceptions
An odds ratio is not generally a probability ratio: the worked example gives $2$ versus $1.6$. A coefficient is not a fixed probability increase: the inverse-logit curve changes slope with the baseline risk. “Adjusted” does not mean “causal”: adjustment controls only variables and assumptions actually represented. Finally, the intercept is not automatically a meaningful real-world baseline when zero-valued predictors are impossible. Each mistake changes a different part of the interpretation: scale, shape, causal claim, or reference point.{{cite:agresti_tarantola_varriale2023}} (§§5.1–5.3, pp. 155–160)

## Assumptions and limits — When a simple reading fails
If the true group difference changes with age, a model containing only a common group coefficient hides that interaction; the relevant odds ratio is age-specific. If all observed events occur in one group and none in the other, complete separation can make an ordinary maximum-likelihood coefficient diverge, so simply exponentiating a reported huge estimate is unstable. If a fitted probability is requested at a covariate value far outside the observed range, the logistic curve still returns a number between zero and one, but that algebra does not validate the extrapolation. Interpretation should name these limits along with the fitted contrast.{{cite:agresti_tarantola_varriale2023}} (§§5.1–5.3, pp. 155–160)

## Connections
[Odds ratio](odds-ratio.qmd) develops the group comparison independently of a regression model, while [logit link](logit-link.qmd) explains the transformation that makes the model additive. The answered bank problem [A binomial GLM and group coefficient](../questions/q-35.qmd) asks for a same-cholesterol comparison, and [the heart-failure odds exercise](../questions/ex-sl-10-2.qmd) translates a ten-year age contrast into both odds and probability scales. Those examples exercise the conditioning and scale distinctions without using the hypothetical groups above.{{cite:agresti_tarantola_varriale2023}} (§5.1, p. 156)

## History
Cox's 1958 analysis treated binary sequences whose success probabilities depend on explanatory variables. Nelder and Wedderburn subsequently placed the binomial logit within the generalised linear-model framework. Dodge's later encyclopedia entry presents the same model for binary outcomes and identifies the exponential of a binary-predictor coefficient as an odds ratio. The modern reporting question is how to accompany that odds-scale coefficient with probabilities that answer the practical comparison.{{cite:cox1958_logistic}} (pp. 215–216, binary-response setup){{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:dodge2008}} (pp. 319–320, “Logistic Regression”){{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)
