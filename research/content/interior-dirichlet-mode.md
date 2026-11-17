## Motivating example
A category-probability vector must lie on a simplex: its components are nonnegative and sum to one. Reporting a posterior mean produces one valid vector, but reporting a separate marginal mode for each category may produce numbers that do not sum to one. A joint mode solves one constrained optimization problem for the entire vector. The distinction matters when Dirichlet concentrations are modest.{{cite:blei_ng_jordan2003}} (§3, p. 996, eq. 1)

A Dirichlet model extends the beta model from a single share and its complement to several shares. Its positive concentrations control the shape near the simplex's faces as well as the density in its interior. Choosing a mode therefore requires checking those concentrations before applying a stationary-point formula.{{cite:ng_tian_tang2011_dirichlet}} (Ch. 1, introduction and §1.3)

## Statement
Let $P=(P_1,\ldots,P_K)$ have density proportional to $\prod_{k=1}^Kp_k^{\alpha_k-1}$ on $p_k>0$, $\sum_kp_k=1$. Put $\alpha_0=\sum_k\alpha_k$. If every $\alpha_k>1$, its unique joint density maximizer is
$$p_k^*=\frac{\alpha_k-1}{\alpha_0-K}.$$
The density is defined relative to a fixed $(K-1)$-dimensional simplex coordinate measure. A mode is a property of that density and its parameterization; a nonlinear reparameterization changes the density by a Jacobian and need not preserve its maximizing point.{{cite:blei_ng_jordan2003}} (§3, p. 996, eq. 1)

The denominator is positive under the stated assumptions. Subtracting one separately from each positive concentration gives positive numerators, and their sum is the denominator. Thus the formula defines an interior probability vector. Normalizing the concentrations themselves instead gives the Dirichlet mean, which answers a different decision problem.

## Intuition — Maximize under one total-share constraint
Taking logarithms converts the product into $\ell(p)=\sum_k(\alpha_k-1)\log p_k+$ a constant. Each positive coefficient penalizes taking its share toward zero. The constraint prevents increasing every share simultaneously, so the optimum balances those log slopes. The common Lagrange multiplier measures the marginal change in log density for a small relaxation of the total-share constraint.{{cite:blei_ng_jordan2003}} (§3, p. 996, Dirichlet density)

## Proof
Introduce a multiplier $\lambda$ for $\sum_kp_k=1$. The derivative condition is $(\alpha_k-1)/p_k=\lambda$. Summing $p_k=(\alpha_k-1)/\lambda$ gives $\lambda=\alpha_0-K$ and hence the displayed formula. The Hessian in the ambient positive orthant is diagonal with entries $-(\alpha_k-1)/p_k^2$. Its quadratic form is strictly negative for every nonzero direction, including directions whose components sum to zero. The log density is strictly concave on the simplex interior. It tends to minus infinity when any share approaches zero, so the stationary point is the unique global maximizer. This proves existence, interiority and uniqueness under precisely the stated concentration condition.

For a marginal coordinate, integrating the remaining shares gives $P_k\sim\operatorname{Beta}(\alpha_k,\alpha_0-\alpha_k)$. When both beta shapes exceed one, its mode is $(\alpha_k-1)/(\alpha_0-2)$. The denominator differs from the joint-mode denominator because integration and joint maximization are different operations. The beta density makes the marginal calculation directly checkable.{{cite:ng_tian_tang2011_dirichlet}} (§1.3, def. 1.1, eq. 1.5)

## Worked example
### Three summaries for three categories
For concentrations $(2,3,5)$, the total is ten. The joint mode is $(1/7,2/7,4/7)$, while the mean is $(1/5,3/10,1/2)$. The three marginal modes are $(1/8,2/8,4/8)$, whose sum is $7/8$. Reporting them together as a probability vector would violate the sum constraint. Each is a valid answer to a different one-dimensional marginal maximization. These calculations use the density and beta-marginal formulas above.{{cite:blei_ng_jordan2003}} (§3, p. 996, eq. 1){{cite:ng_tian_tang2011_dirichlet}} (§1.3, eq. 1.5)

If multinomial counts $(3,0,2)$ are observed, conjugacy changes the concentrations to $(5,3,7)$. The new joint mode is $(1/3,1/6,1/2)$. The zero observed count in the second category does not force its posterior mode to zero: its positive prior exponent remains part of the joint density. Whether such prior influence is scientifically suitable is a modeling question.

**Your turn.** For a three-category Dirichlet distribution with concentrations $(3,3,3)$, calculate the joint mode and the sum of the three marginal modes.

::: {.callout-tip collapse="true" title="Answer"}
The joint mode is $(1/3,1/3,1/3)$. Each marginal law is Beta(3,6), with mode $2/7$, so the three marginal modes sum to $6/7$.
:::

## Common misconceptions — Boundary cases need a separate analysis
If all concentrations equal one, the density is constant on the simplex interior, so every interior point is a mode. A zero-over-zero stationary formula cannot select one. If a concentration is less than one, its negative log-density exponent can make the density unbounded as that coordinate approaches zero; no finite interior maximizer follows. When a concentration equals one and the others exceed one, the largest limiting density can occur on the corresponding face. These conclusions follow by inspecting the powers in the density, rather than extending an interior formula beyond its assumptions.{{cite:blei_ng_jordan2003}} (§3, p. 996, eq. 1)

MAP estimates also depend on the chosen coordinate measure. Posterior probabilities of sets, posterior means and posterior modes are different summaries. A joint mode is useful when a single high-density configuration is wanted, while uncertainty statements still require more than its location.

For the concentrations $(2,3,5)$, the joint mode $(1/7,2/7,4/7)$ is a probability vector and the three marginal modes $(1/8,2/8,4/8)$ are not, because they sum to $7/8$. The same split appears after the count update to $(5,3,7)$: the joint mode $(1/3,1/6,1/2)$ sums to one, and a marginal beta mode uses the denominator $\alpha_0-2$ rather than $\alpha_0-K$.{{cite:blei_ng_jordan2003}} (§3, p. 996, eq. 1){{cite:ng_tian_tang2011_dirichlet}} (§1.3, eq. 1.5)
