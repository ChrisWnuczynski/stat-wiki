## Lead context
The response records a person's explanation of addiction, so the fitted categories describe reported opinions rather than a clinical diagnosis.

## Motivating example
A survey asks whether addiction reflects weak will, disease or both. These are three different responses, and the category labelled “both” is still one response to the question. A multinomial regression can compare how their probabilities vary with age, gender and academic status without assigning a numerical distance between the opinions. Models for a single exclusive label differ from models allowing several labels on one record.{{cite:zhang_d2l2023}} (§4.1.1, classification and one-hot responses)

## Definition — What the observations measure
The `catdata` package represents the survey in a data frame with $712$ rows. Its response `ill` uses codes $0$, $1$ and $2$ for weak-willed, disease and both. The remaining variables encode gender, age and academic status. These codes identify categories; they do not make the response a measured numerical score.{{cite:r_catdata_addiction2026}} (Description and Format)

A baseline-category model sets
$$
\eta_1(x)=\log\frac{p_1(x)}{p_0(x)},\qquad
\eta_2(x)=\log\frac{p_2(x)}{p_0(x)}.
$$
Solving the ratios together with $p_0+p_1+p_2=1$ gives
$$
(p_0,p_1,p_2)=\frac{(1,e^{\eta_1},e^{\eta_2})}{1+e^{\eta_1}+e^{\eta_2}}.
$$
This is a softmax parameterisation with the baseline score fixed at zero. Adding the same function to all three scores changes no probability, so choosing a baseline removes that redundancy.{{cite:zhang_d2l2023}} (§4.1.1.1–4.1.1.2, eqs. 4.1.2–4.1.3)

## Interpretation — Odds ratios and probability changes
A coefficient in $\eta_1$ describes a change in disease-versus-weak-willed odds, holding the other predictors fixed. Exponentiating that coefficient gives an odds multiplier. It is not a probability multiplier: changing either nonbaseline score changes the shared denominator and therefore all three probabilities. Pairwise comparisons not involving the baseline use $\log(p_2/p_1)=\eta_2-\eta_1$.{{cite:zhang_d2l2023}} (§4.1.1.2, softmax probabilities)

The conditional log likelihood for independent exclusive responses is a sum of the observed category scores minus their log normalisers. Its negative is a cross-entropy objective. The log-sum-exp term is convex, so the negative log likelihood is convex in the regression coefficients. Convexity does not itself guarantee that a finite maximiser exists for every dataset.{{cite:zhang_d2l2023}} (§4.1.2.1, log likelihood){{cite:boyd_vandenberghe2004}} (§3.1.5, pp. 72–74, log-sum-exp)

## Worked example
Using the fitted coefficients, a male aged forty with academic indicator zero has
$$
\eta_1=-1.1607+0.0299(40)=0.0353,\qquad
\eta_2=-2.0156+0.0421(40)=-0.3316.
$$
Normalising $(1,e^{0.0353},e^{-0.3316})$ gives
$$
(p_0,p_1,p_2)\approx(0.363147,0.376195,0.260658).
$$
Changing the academic indicator to one adds $1.6220$ and $1.0673$ to the two scores. The probabilities become approximately $(0.120018,0.629511,0.250471)$. Disease-versus-weak-willed odds are multiplied by $e^{1.6220}=5.063207$, but the disease probability changes from about $0.376$ to $0.630$, not by a factor of five. The category-two probability decreases slightly even though its baseline odds increase, because category one becomes much more probable.

The pairwise academic-status odds multiplier for both versus disease is $e^{1.0673-1.6220}=0.574245$. These are conditional associations in the survey model. The equations alone do not identify the effect of changing anyone's educational status.

**Your turn.** What are the three probabilities when both baseline log odds equal zero?

::: {.callout-tip collapse="true" title="Answer"}
All unnormalised weights equal one. Dividing by their sum gives $(1/3,1/3,1/3)$. A zero baseline log odds means equal probabilities for that comparison, not zero probability of the category.
:::

## Connections — Changing the reference category
Choosing disease as the reference gives scores $\log(p_0/p_1)=-\eta_1$ and $\log(p_2/p_1)=\eta_2-\eta_1$. The coefficients and their verbal comparisons change, while the fitted probabilities do not. This follows directly by dividing every softmax weight by $e^{\eta_1}$.{{cite:zhang_d2l2023}} (§4.1.1.2, normalisation)

Missing responses and predictors also affect which records contribute to a fit. The full data frame and the complete cases used by a particular fitting formula need not have the same size. The numerical comparisons here use the stated fitted model and coding, so a different reference category or record selection must be accounted for when reproducing them.
