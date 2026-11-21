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

## Check yourself

### The proportional-odds assumption {#self-check-c-25}

What does the proportional-odds assumption say about the slopes at different cutpoints?

::: {.callout-tip collapse="true" title="Answer"}
The slope vector is the same at every cut, so a unit change in a covariate multiplies every cumulative odds by the same factor $e^{\beta_j}$.
:::

### Nominal and ordinal responses {#self-check-c-24}

What is the difference between a nominal response and an ordinal response, and what does a baseline-category logit compare?

::: {.callout-tip collapse="true" title="Answer"}
Nominal categories have no intrinsic order. Ordinal categories are ordered, without requiring equal gaps. A baseline-category logit compares each category probability with a fixed reference, $\log(p_k/p_0)$, and those slopes need not be equal. Proportional odds instead uses nested events $\{Y\ge k\}$ and one shared slope.
:::
### Multinomial logistic regression {#self-check-q-46}

[Multinomial logistic regression](../questions/q-46.qmd)

**[10 marks]**

A response has categories $0,1,2$, with probabilities $p_0(x),p_1(x),p_2(x)$. Consider $$\log\frac{p_1(x)}{p_0(x)}=\alpha_1+\beta_1x,
\qquad
\log\frac{p_2(x)}{p_0(x)}=\alpha_2+\beta_2x.$$

**(a)** Derive expressions for all three probabilities and verify that they sum to one. **[4 marks]**

**(b)** Interpret $e^{\beta_1}$. **[2 marks]**

**(c)** Derive $\log[p_2(x)/p_1(x)]$. **[2 marks]**

**(d)** If category $1$ becomes the reference category, express the new intercepts and slopes in terms of the original parameters. Do the fitted probabilities change? **[2 marks]**

:::::::: {.callout-tip collapse="true" title="Answer"}

**Definitions.** $p_0(x),p_1(x),p_2(x)$ are probabilities of three mutually exclusive, exhaustive categories, summing to one. With category 0 as baseline, define $\eta_j(x)=\log\{p_j(x)/p_0(x)\}=\alpha_j+\beta_jx$, for $j=1,2$. These are baseline-category log ratios, not one-versus-rest logits $\log\{p_j/(1-p_j)\}$. The predictors are finite, so all fitted probabilities are positive.

**(a) The three probabilities.** Exponentiating the model equations gives $$p_1(x)=e^{\eta_1(x)}p_0(x),\qquad
p_2(x)=e^{\eta_2(x)}p_0(x).$$ Since the probabilities sum to one, $$p_0(x)\{1+e^{\eta_1(x)}+e^{\eta_2(x)}\}=1.$$ With $D(x)=1+e^{\eta_1(x)}+e^{\eta_2(x)}$, $$\boxed{p_0(x)=\frac1{D(x)},\qquad
p_1(x)=\frac{e^{\eta_1(x)}}{D(x)},\qquad
p_2(x)=\frac{e^{\eta_2(x)}}{D(x)}.}$$ All are positive and their sum is $D(x)/D(x)=1$.

**(b) Interpretation of $e^{\beta_1}$.** For a one-unit increase in $x$, $$\boxed{
\frac{p_1(x+1)/p_0(x+1)}{p_1(x)/p_0(x)}=e^{\beta_1}.
}$$ Thus $e^{\beta_1}$ is the multiplicative change in the odds of category $1$ relative to category $0$. It is not generally the multiplier for $p_1(x)$ itself, or for the odds of category $1$ against *all* other categories combined.

**(c) Comparing categories 2 and 1.** Subtract the two original log-ratio equations: $$\boxed{
\log\frac{p_2(x)}{p_1(x)}
=\log\frac{p_2(x)}{p_0(x)}-\log\frac{p_1(x)}{p_0(x)}
=(\alpha_2-\alpha_1)+(\beta_2-\beta_1)x.
}$$

**(d) Taking category 1 as the reference.** The two new equations are $$\log\frac{p_0(x)}{p_1(x)}=-\alpha_1-\beta_1x,
\qquad
\log\frac{p_2(x)}{p_1(x)}
=(\alpha_2-\alpha_1)+(\beta_2-\beta_1)x.$$ Thus the new intercept and slope are $(-\alpha_1,-\beta_1)$ for category $0$, and $(\alpha_2-\alpha_1,\beta_2-\beta_1)$ for category $2$. The fitted probabilities do **not** change: this is a reparametrisation. For example, $$p_1(x)=\frac1{1+e^{-\eta_1(x)}+e^{\eta_2(x)-\eta_1(x)}}
=\frac{e^{\eta_1(x)}}{D(x)},$$ which is the original expression, and the other probabilities follow by their corresponding ratios.

::::::::
