## Lead context
Ordinal responses are ordered categories, and a proportional-odds model gives every cumulative cut the same covariate slope.

## Motivating example
Cuts with intercepts $1.2$ and $0.2$ share the slope $-1/2$. At $x=2$ the cumulative logits are $0.2$ and $-0.8$. A unit increase in $x$ multiplies both cumulative odds by $e^{-1/2}$.

## Intuition — One slope, several thresholds
Collapsing “severe” with “mild” is a coarser question than asking whether the response is severe. Both questions are binary, so each has a logit. If the covariate shifts those logits by different amounts, the effect of the covariate depends on which cut one chose. The proportional-odds model forbids that dependence: the cuts have different intercepts, and they share one slope. The intercepts must decrease as the cut moves up the scale, because a higher tail is a rarer event.

## Definition — Cumulative logits with a common slope
For ordered categories $1,\ldots,K$ and covariate value $x$,

$$
\operatorname{logit}\mathbb{P}(Y\ge k\mid x)=\beta_{0k}+x\beta,
\qquad k=2,\ldots,K,
$$

with $\beta_{02}\ge\beta_{03}\ge\cdots\ge\beta_{0K}$. Category probabilities are consecutive differences of these tails, and $\mathbb{P}(Y\ge 1)=1$. {{cite:nelder_wedderburn1972}} (§3.3, p. 379)

## Properties — The odds multiplier does not depend on the cut
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The odds of $\{Y\ge k\}$ are $\exp(\beta_{0k}+x\beta)$. Replacing $x$ by $x+1$ multiplies those odds by $e^{\beta}$. The factor does not contain $k$. The same step multiplies every cumulative odds, from the first cut above the bottom category to the top category. {{cite:nelder_wedderburn1972}} (§3.3, p. 379)
:::
:::

## Worked example — Two cuts, slope $-1/2$, at $x=2$
Take $\beta_{02}=1.2$, $\beta_{03}=0.2$ and $\beta=-1/2$. At $x=2$,

$$
\operatorname{logit}\mathbb{P}(Y\ge 2)=1.2-1=0.2,
\qquad
\operatorname{logit}\mathbb{P}(Y\ge 3)=0.2-1=-0.8.
$$

The tails are $\mathbb{P}(Y\ge 2)\approx 0.5498$ and $\mathbb{P}(Y\ge 3)\approx 0.3100$. The category probabilities are

$$
\mathbb{P}(Y=1)\approx 0.4502,\qquad
\mathbb{P}(Y=2)\approx 0.2398,\qquad
\mathbb{P}(Y=3)\approx 0.3100,
$$

and these three numbers sum to $1$. A unit increase in $x$ multiplies both cumulative odds by $e^{-1/2}\approx 0.6065$. {{cite:nelder_wedderburn1972}} (§3.3, p. 379) The intercept gap $1.2-0.2=1$ does not depend on $x$, so the ordering $\mathbb{P}(Y\ge 2)\ge\mathbb{P}(Y\ge 3)$ is kept at every $x$.

**Your turn.** Keep the same intercepts and slope, and evaluate the two logits at $x=0$. Which tail is larger?

::: {.callout-tip collapse="true" title="Answer"}
The logits are $1.2$ and $0.2$. Both tails are the expit of those numbers, and $1.2>0.2$ so $\mathbb{P}(Y\ge 2)>\mathbb{P}(Y\ge 3)$. The shared slope has not yet moved either logit.
:::

## Connections — Nominal labels, binary logit, and collapsing
[Nominal responses](nominal-responses.qmd) have no order, so they use a separate slope for each label against a baseline. The ordinal model is a stack of [logit links](logit-link.qmd), one per cumulative cut, tied together by the common slope. Collapsing adjacent categories changes the intercepts, because the cuts move, and it keeps the form of the equation. A model that gave each cut its own slope would be a different equation at each cut.
