## Motivating example

A class is selected for unusually low scores on an initial test. Its average score may rise on a second test even without an effective intervention. Selection makes the initial score extreme; imperfect correlation allows the conditional prediction on the second score to be less extreme. Galton's analysis of stature supplied the historical setting for regression toward the mean.{{cite:galton1886}} (pp. 246–247){{cite:dodge2008}} (p. 451)

## Definition — Regression on a common standardised scale

Let $X,Y$ have finite positive variances. The best linear predictor of $Y$ from $X$ is
$$
\widehat Y=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X).
$$
In standard-deviation units its displacement is $\rho$ times the observed displacement of $X$. When $0<\rho<1$, an above-average observation predicts an above-average response closer to its own mean. In raw units the slope can exceed one if $Y$ has a sufficiently larger spread. Regression toward the mean is therefore a comparison of standardised deviations, rather than a universal raw-slope bound. The least-squares line estimates this linear prediction from a sample.{{cite:dodge2008}} (pp. 491–492)

## Properties — Why the prediction moves part of the way

Put $U=X-\mu_X$ and $V=Y-\mu_Y$. For a candidate slope $b$,
$$
E(V-bU)^2=\sigma_Y^2-2b\rho\sigma_X\sigma_Y+b^2\sigma_X^2.
$$
Completing the square gives its unique minimum at $b=\rho\sigma_Y/\sigma_X$, with residual mean square $\sigma_Y^2(1-\rho^2)$. Joint normality additionally makes this linear predictor the conditional mean; the least-squares minimisation itself only needs finite second moments.{{cite:dodge2008}} (pp. 491–492)

Regressing in the opposite direction gives slope $\rho\sigma_X/\sigma_Y$. The product of the two slopes is $\rho^2$, so the two lines are generally not algebraic inverses. Neither regression makes an individual move through time: they describe different conditional or predictive comparisons. Galton's central historical observation concerned how family-group averages differed from the population average.{{cite:galton1886}} (pp. 247–250)

## Worked example

Consider standardised initial and follow-up scores with correlation $0.6$, modelled as jointly normal. An initial score two standard deviations below average, $X=-2$, predicts follow-up mean $E(Y\mid X=-2)=0.6(-2)=-1.2$. The predicted improvement is $0.8$ standard deviations even with no intervention effect. The conditional standard deviation is $\sqrt{1-0.6^2}=0.8$, so individual follow-up scores still vary substantially around that mean.

For the height illustration with means $67$ and $68$ inches, equal standard deviations $2.7$ inches and correlation $0.5$, a father at $71$ inches predicts a son at $68+0.5(71-67)=70$ inches. A father at $63$ inches predicts $66$ inches. The deviations from the two means are halved; neither statement says all children of tall parents are shorter than their parents. These calculations apply the least-squares prediction formula.{{cite:dodge2008}} (pp. 491–492)

**Your turn.** In the score example, what follow-up mean is predicted after an initial score $X=2$?

::: {.callout-tip collapse="true" title="Answer"}
It is $1.2$, a predicted fall of $0.8$ standard deviations. The same model produces opposite apparent changes after selecting unusually low and unusually high initial scores.
:::

## Check yourself

### [Normal equations for a straight line](../questions/ex-inf-normal-equations.qmd) {#self-check-ex-inf-normal-equations}

Why does the fitted line pass through $(\bar x,\bar y)$?

::: {.callout-tip collapse="true" title="Answer"}
The derivative with respect to the intercept sets the sum of residuals to zero. Therefore $\bar y=b_0+b_1\bar x$, giving $b_0=\bar y-b_1\bar x$.
:::

### [Reading a correlation](../questions/ex-da-correlation-reading.qmd) {#self-check-ex-da-correlation-reading}

Does a large correlation establish that changing the predictor causes the predicted response change?

::: {.callout-tip collapse="true" title="Answer"}
No. Correlation describes association. A shared cause, selection, or another feature of the sampling process can produce the association; a causal conclusion needs additional design or assumptions.
:::
