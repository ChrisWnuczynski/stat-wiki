## Lead context
The independent sampling unit can contribute several dependent measurements. A marginal mean model and a joint probability model address different questions even when they use the same predictors.{{cite:liang_zeger1986}} (§1, pp. 13–14)

## Motivating example
At each independently sampled habitat, record presence of two species. Regressing each presence indicator on rainfall estimates how each marginal probability changes. Predicting whether both species occur at the same habitat additionally needs an association specification. Repeated responses from one unit cannot automatically be treated as independent observations.{{cite:liang_zeger1986}} (§1, p. 14)

## Properties — The feasible joint probabilities
Let $p_1=\mathbb{P}(Y_1=1)$, $p_2=\mathbb{P}(Y_2=1)$ and $q=\mathbb{P}(Y_1=Y_2=1)$. The four joint probabilities are
$$
q,\quad p_1-q,\quad p_2-q,\quad 1-p_1-p_2+q.
$$
Nonnegativity gives $\max(0,p_1+p_2-1)\le q\le\min(p_1,p_2)$. Thus two margins leave one association degree of freedom. For positive cells the odds ratio is
$$
\mathrm{OR}=\frac{q(1-p_1-p_2+q)}{(p_1-q)(p_2-q)}.
$$
This is the ratio of two conditional odds, consistent with the ordinary cross-product form.{{cite:dodge2008}} (p. 392, odds-ratio interpretation)

For regression, a generalised estimating equation has the form $\sum_i D_i^\top V_i^{-1}(Y_i-\mu_i)=0$, where independent units are indexed by $i$, $D_i=\partial\mu_i/\partial\beta^\top$, and $V_i$ is a working covariance. At the true mean parameter each residual has expectation zero. This explains why a wrong working correlation need not bias the estimating equation, while a wrong mean generally does. Consistency and the sandwich variance require regularity and an increasing number of independent units.{{cite:liang_zeger1986}} (§3.1, eqs. 5–8 and thm. 2, pp. 15–16)

## Worked example
Take $p_1=0.3$, $p_2=0.4$ and OR $=2$. The equation is
$$
q(0.3+q)=2(0.3-q)(0.4-q),\qquad q^2-1.7q+0.24=0.
$$
Only the smaller root is feasible: $q=(1.7-\sqrt{1.93})/2=0.15538$. The four cells are approximately $0.15538,0.14462,0.24462,0.45538$. They sum to one, reproduce the two margins and have cross-product ratio $2$. Independence instead gives $q=0.12$, so the same marginal regressions can coexist with different joint-event predictions.{{cite:dodge2008}} (p. 392, odds-ratio scale)

**Your turn.** With margins $0.7$ and $0.6$, find the feasible range of the joint success probability and its value under independence.

::: {.callout-tip collapse="true" title="Answer"}
The range is $[0.3,0.6]$. Independence gives $0.7\cdot0.6=0.42$.
:::

## Assumptions and limits
A sandwich covariance estimates uncertainty in fitted mean parameters; it does not recover an unspecified joint distribution. Nor does it repair informative missingness, dependence between units or omitted predictors in the mean. The basic GEE results assume an appropriate independent-unit asymptotic regime, and the paper's missing-observation discussion requires missing completely at random for the procedures stated there.{{cite:liang_zeger1986}} (§§2–3, pp. 15–16)

## Intuition
Two binary measurements on the same unit have three free probabilities once they are required to sum to one, but only two of those numbers are margins. The third is association. Knowing that each species occurs with a stated probability does not determine how often they occur together. Independence is one choice inside a feasible interval. An odds ratio of two is another choice, and it produces a different joint event probability even though the regressions for the separate margins can stay the same.{{cite:liang_zeger1986}} (§1, pp. 13–14)

## Definition
For a single pair, the joint distribution is the four probabilities of $(Y_1,Y_2)$. The margins $p_1$ and $p_2$ and the joint success probability $q$ determine the other three cells, and every cell must be nonnegative. That is the Fréchet bound $\max(0,p_1+p_2-1)\le q\le\min(p_1,p_2)$. For margins $0.7$ and $0.6$ the bound is $[0.3,0.6]$. Independence picks $q=0.42$, strictly inside the interval. At the upper endpoint $q=0.6$, the second variable is a success whenever the first is, and the cell probabilities are $0.6$, $0.1$, $0$ and $0.3$. The cross-product odds ratio is then undefined because a cell is zero. Association parameters are meaningful in the interior, where all four cells are positive.{{cite:dodge2008}} (p. 392, odds-ratio interpretation)

## Statistical use
A marginal regression models $p_1$ and $p_2$ as functions of covariates. A generalised estimating equation solves a weighted score for those mean parameters and can use a working correlation that is not the true one. If the mean is correct, each unit's residual has mean zero and the estimating equation remains unbiased. The sandwich variance then estimates the variability of that solution across independent units. The sandwich does not reconstruct $q$, and it does not correct a mean that omitted an important covariate. If the scientific question is the probability that both responses occur, the marginal fit has to be paired with an association model. If the question is only how each margin changes with rainfall, the association is a nuisance feature of the variance, not the target.{{cite:liang_zeger1986}} (§3.1, eqs. 5–8 and thm. 2, pp. 15–16)

## Common misconceptions
A working correlation labeled “exchangeable” or “independent” is not evidence that the responses are independent. It is a choice inside the estimating equation. Two margins equal to $0.3$ and $0.4$ do not force the joint success probability to be $0.12$; that product is the independence value, and an odds ratio of two moves it to about $0.155$. A robust standard error does not make a wrong mean right. It widens or narrows the reported uncertainty for the mean parameters the equation actually targets. Clusters that are not independent of one another, or observations missing for reasons tied to the unseen response, sit outside the basic justification.{{cite:liang_zeger1986}} (§§2–3, pp. 15–16){{cite:dodge2008}} (p. 392, odds-ratio scale)

## Connections
The odds ratio for a two-by-two probability table is the cross-product of the four cells, and it is also the ratio of the two conditional odds. Either description needs all four cells. A pair of marginal regressions supplies only the row and column totals of that table. Filling the table still requires one association number, such as the odds ratio or the joint success probability. Changing that number moves probability between the diagonal and the off-diagonal while leaving the fitted margins alone. A habitat where both species are present is one cell of the table, not a margin. Predicting that cell from rainfall therefore uses both the marginal fit and the association. Predicting each species separately can stop at the margins. The estimating equation and the sandwich variance are tools for the second question. They become tools for the first question only after the association model is stated and estimated.{{cite:dodge2008}} (p. 392, odds-ratio interpretation){{cite:liang_zeger1986}} (§1, p. 14)
