## Lead context
The data illustrate how the shape of a binary-response model changes when age is allowed to enter through a smooth function.

## Motivating example
After spinal surgery, a clinician may ask whether the probability of postoperative kyphosis varies with age. A straight line on the log-odds scale imposes a monotone probability curve. A smooth age term allows a bend while leaving the response binary. These are different modelling restrictions, even when both use a logistic link.{{cite:hastie_tibshirani1986}} (§1, pp. 297–298)

## Definition — Outcomes, predictors, and units
In R's `rpart` package, `kyphosis` contains 81 observations. `Kyphosis` records whether the condition was present after the operation; `Age` is in months, `Number` counts involved vertebrae, and `Start` identifies the topmost vertebra operated on. The package attributes the dataset to *Statistical Models in S*. These definitions establish what the software data fields contain.{{cite:r_kyphosis2026}} (“Description”, “Format”, and “Source”)

For a Bernoulli outcome $Y$, a logistic model specifies $p(x)=P(Y=1\mid x)$ through $\log\{p(x)/(1-p(x))\}=\eta(x)$. The conditional mean is a probability and the conditional variance is $p(x)\{1-p(x)\}$. A linear logistic model takes $\eta(x)=\beta_0+\beta_1x$; an additive extension replaces selected linear terms by functions.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3, pp. 372, 379–380){{cite:hastie_tibshirani1986}} (§1, pp. 297–298)

## Interpretation — A curve and a conditional comparison
Writing $\eta=\beta_0+g(\mathrm{Age})$ preserves the logistic response family but changes the set of permitted age effects. A centring constraint on $g$ distinguishes its constant component from the intercept. The probability at the centre of the smooth is the inverse logit of the intercept; it is generally different from the average of all fitted probabilities. Averaging and applying a nonlinear inverse link are different operations.{{cite:hastie_tibshirani1986}} (§§2–3, additive predictors and generalized linear models)

An age-only curve is a comparison among these observed patients. Including `Number` and `Start` changes the question to a conditional comparison at specified surgical characteristics. Neither specification, by itself, turns the observed age association into the effect of assigning children to surgery at a different age. The distinction between a response model and its predictor specification is central to the GLM construction.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–372)

## Worked example
There are 17 `present` outcomes and 64 `absent` outcomes. The intercept-only maximum-likelihood fit therefore has
$$
\widehat p=\frac{17}{81}=0.209877,\qquad
\widehat\eta=\log\frac{17}{64}=-1.325670.
$$
Its fitted probability is the same for every patient. The log-odds are negative because the observed proportion is below one half. The binomial likelihood $p^{17}(1-p)^{64}$ is maximised at this proportion.{{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380)

This fit answers an overall frequency question; it cannot describe variation by age. It also differs from the intercept in a model with a centred smooth, where the nonlinear average need not equal the inverse logit of that intercept. The observed ages range from 1 to 206 months. Units matter: changing months to years changes the coefficient of a linear age term, while leaving fitted probabilities invariant after the corresponding rescaling.{{cite:hastie_tibshirani1986}} (§1, pp. 297–298)

**Your turn.** Convert the intercept-only fitted probability into odds, then recover the probability from those odds.

::: {.callout-tip collapse="true" title="Answer"}
The odds are $17/64=0.265625$. Dividing the odds by one plus the odds gives $(17/64)/(81/64)=17/81$.
:::
