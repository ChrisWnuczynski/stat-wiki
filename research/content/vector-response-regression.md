## Lead context
The independent sampling unit can contribute several dependent measurements. A marginal mean model and a joint probability model address different questions even when they use the same predictors.{{cite:liang_zeger1986}} (§1, pp. 13–14)

## Motivating example
At each independently sampled habitat, record presence of two species. Regressing each presence indicator on rainfall estimates how each marginal probability changes. Predicting whether both species occur at the same habitat additionally needs an association specification. Repeated responses from one unit cannot automatically be treated as independent observations.{{cite:liang_zeger1986}} (§1, p. 14)

## Properties — The feasible joint probabilities
Let $p_1=P(Y_1=1)$, $p_2=P(Y_2=1)$ and $q=P(Y_1=Y_2=1)$. The four joint probabilities are
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
