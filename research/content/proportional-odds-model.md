## Lead context
A proportional-odds model gives every cumulative chance of a higher category the same slope, so one coefficient is a common odds multiplier.

## Motivating example
A grade recorded as low, middle, or high is ordered. Fitting a separate logistic slope for “middle or high” and another for “high” allows those two effects to disagree. The proportional-odds model keeps one slope and lets only the intercepts change with the cut.

## Intuition — Parallel cumulative logits
Write $\gamma_k(x)=\Pr(Y\ge k\mid x)$ for an ordered response $Y\in\{1,\ldots,K\}$. The model
$$
\operatorname{logit}\gamma_k(x)=\alpha_k+x^{\mathsf T}\beta,\qquad k=2,\ldots,K,
$$
uses the same $\beta$ at every cut. A unit increase in one covariate therefore multiplies the odds $\gamma_k/(1-\gamma_k)$ by the same factor $e^{\beta_j}$ for every $k$. {{cite:nelder_wedderburn1972}} (§3.3, p. 379) The intercepts must decrease as $k$ increases, because $\gamma_2(x)\ge\gamma_3(x)\ge\cdots$.

## Definition — One covariate, three categories
For $K=3$ and a single covariate,
$$
\operatorname{logit}\Pr(Y\ge 2\mid x)=\alpha_2+\beta x,\qquad \operatorname{logit}\Pr(Y\ge 3\mid x)=\alpha_3+\beta x,
$$
with $\alpha_2\ge\alpha_3$. Then $\Pr(Y=2\mid x)=\Pr(Y\ge 2\mid x)-\Pr(Y\ge 3\mid x)$. {{cite:nelder_wedderburn1972}} (§3.3, p. 379)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The odds of $\{Y\ge k\}$ are $e^{\alpha_k+\beta x}$. Replacing $x$ by $x+1$ multiplies those odds by $e^{\beta}$, and the factor does not depend on $k$. If $\alpha_2<\alpha_3$, then at $x=0$ one would have $\Pr(Y\ge 2)<\Pr(Y\ge 3)$, which contradicts $\{Y\ge 3\}\subset\{Y\ge 2\}$.
:::
:::

## Worked example
Take $\alpha_2=-1$, $\alpha_3=-2$, and $\beta=0.5$. At $x=2$,
$$
\operatorname{logit}\Pr(Y\ge 2)=0,\qquad \operatorname{logit}\Pr(Y\ge 3)=-1,
$$
so $\Pr(Y\ge 2)=1/2$ and $\Pr(Y\ge 3)=1/(1+e)\approx 0.268941$. The category probabilities are $\Pr(Y=1)=1/2$, $\Pr(Y=2)\approx 0.231059$, and $\Pr(Y=3)\approx 0.268941$. A unit increase in $x$ multiplies both cumulative odds by $e^{0.5}\approx 1.649$. {{cite:nelder_wedderburn1972}} (§3.3, p. 379)

**Your turn.** At $x=0$ with the same coefficients, compute $\Pr(Y\ge 2)$ and $\Pr(Y\ge 3)$, and check that the first is larger.

::: {.callout-tip collapse="true" title="Answer"}
$\Pr(Y\ge 2)=1/(1+e)\approx 0.268941$ and $\Pr(Y\ge 3)=1/(1+e^2)\approx 0.119203$. The inequality $0.268941>0.119203$ is the intercept ordering $\alpha_2>\alpha_3$.
:::

## Connections — Other cumulative links
The [logit link](logit-link.qmd) is the function applied to each cumulative probability. Replacing it by the complementary log-log link gives a proportional-hazards form with the same parallel-slope idea and a different coefficient reading. A model that lets $\beta$ depend on $k$ is no longer proportional odds. The [odds](odds.qmd) $\gamma/(1-\gamma)$ are what the common factor multiplies.

