## Motivating example
Two density estimates can place the same most likely class on every observation while expressing very different uncertainty. A held-out log score asks whether the fitted distribution places adequate probability on what actually occurs. A candidate is fitted without each validation observation before its predictive density is evaluated there.{{cite:rasmussen_williams2006}} (§5.4.2, pp. 116–117)

## Intuition — Scoring the whole predictive distribution
For validation folds $I_1,\ldots,I_K$, let $\widehat f_{-k}$ denote a density fitted to observations outside fold $k$. The average log score is
$$
\mathrm{CV}=\frac1n\sum_{k=1}^K\sum_{i\in I_k}\log\widehat f_{-k}(x_i).
$$
Higher scores are better. This averages held-out log densities, rather than taking the logarithm of an average density. For a Gaussian predictive distribution, each term includes both a squared prediction error and the logarithm of its predictive variance.{{cite:rasmussen_williams2006}} (§5.4.2, eqs. 5.10–5.11, p. 116)

Every fitted operation belongs inside the training fold, including centring, feature selection and tuning. Reusing validation observations to choose a model makes the winning score optimistic as an estimate of the selected procedure's performance. An outer assessment loop or a final untouched test sample addresses that selection step.{{cite:cawley_talbot2010}} (§1, pp. 2079–2081)

## Properties — Probability, density and units
A discrete probability lies between zero and one, but a continuous density may exceed one. Positive continuous log scores are therefore possible. If $z=ax$ with fixed $a>0$, the transformed density at the corresponding point is $f_Z(z)=f_X(x)/a$. Every candidate's log score shifts by $-\log a$ and their ordering stays the same when all are evaluated in the same units. Model comparison requires a common observation space and a common dominating measure.{{cite:rasmussen_williams2006}} (§5.3, pp. 110–112)

## Worked example — One overconfident prediction
Suppose two candidates give probabilities $(0.8,0.7,0.1,0.6)$ and $(0.6,0.6,0.4,0.6)$ to four outcomes observed in validation. The average log scores are $-0.848307$ and $-0.612192$. The second candidate wins. The first assigns higher probability to two outcomes but pays a large cost for the outcome given probability $0.1$. This is the intended penalty for confidence in an event that does not occur. Logarithms of predictions should be evaluated numerically without rounding tiny probabilities to zero.

**Your turn.** Does replacing each average by its sum change which candidate wins?

::: {.callout-tip collapse="true" title="Answer"}
No. Both sums multiply the respective averages by the same positive validation sample size. Their ordering is unchanged.
:::

## Connections — Log score and relative entropy
When the true density is $f$, expected log score equals $\int f\log f-D(f\Vert\widehat f)$. The first term is independent of the candidate, so choosing a higher expected score chooses a smaller divergence. A finite validation sample estimates that expectation with sampling variation; it does not identify the true density exactly.{{cite:goodfellow_bengio_courville2016}} (§3.13, eqs. 3.50–3.51, pp. 72–73) Selection among many noisy scores can magnify that variation.{{cite:cawley_talbot2010}} (§2, pp. 2081–2084)

