## Motivating example

A restaurant estimates the shares of orders in three categories. Knowing each expected share does not determine uncertainty in the difference between two shares: the shares add to one and cannot vary independently. Dirichlet moments supply both the marginal uncertainty and the cross-covariances. The distribution has density proportional to $\prod_k p_k^{\alpha_k-1}$ on the simplex, with every $\alpha_k>0$.{{cite:blei_ng_jordan2003}} (§3, p.996, Eq.1)

## Statement

Write $A=\sum_k\alpha_k$ and $m_k=\alpha_k/A$. For nonnegative integer powers $r_k$, with $r_+=\sum_k r_k$,
$$
 \E\!\left[\prod_kP_k^{r_k}\right]
 =\frac{\Gamma(A)}{\Gamma(A+r_+)}
   \prod_k\frac{\Gamma(\alpha_k+r_k)}{\Gamma(\alpha_k)}.
$$
This identity follows by integrating the Dirichlet density with its exponents shifted by $r_k$. In particular,
$$
 \operatorname{Var}(P_k)=\frac{m_k(1-m_k)}{A+1},\qquad
 \operatorname{Cov}(P_j,P_k)=-\frac{m_jm_k}{A+1}\quad(j\ne k).
$$
The covariance matrix is $[\operatorname{diag}(m)-mm^T]/(A+1)$; its rows sum to zero.{{cite:blei_ng_jordan2003}} (§3, p.996, Eq.1)

## Intuition — Composition and concentration

Total concentration and relative concentration play different roles. Multiplying every $\alpha_k$ by the same positive constant leaves the mean vector unchanged and changes the denominator of the covariance matrix. A larger total concentration therefore describes less uncertainty around the same composition. The multinomial likelihood adds category counts to these concentration parameters, linking this parametrisation directly to conjugate updating.{{cite:deisenroth_faisal_ong2020}} (§6.6.1, pp.208–210, Table6.2)

The negative pairwise covariances express the fixed-sum constraint. They do not imply that every contrast has small variance: subtracting two coordinates adds the magnitude of their negative covariance twice. For any fixed vector $c$,
$$
 \operatorname{Var}(c^TP)=
 \frac{\sum_km_kc_k^2-(\sum_km_kc_k)^2}{A+1}.
$$
This is nonnegative because its numerator is the variance of a variable taking values $c_k$ with probabilities $m_k$. It vanishes when all $c_k$ are equal.{{cite:blei_ng_jordan2003}} (§3, p.996, Eq.1)

## Proof

Let $B(\alpha)=\prod_k\Gamma(\alpha_k)/\Gamma(A)$. Multiplication by $\prod_kp_k^{r_k}$ changes the density kernel to that of a Dirichlet vector with parameters $\alpha+r$. Its integral is $B(\alpha+r)$, giving the ratio $B(\alpha+r)/B(\alpha)$. Apply $\Gamma(z+1)=z\Gamma(z)$ for the first and second moments. Subtracting the products of first moments proves the covariance formulas. The quadratic-form identity follows by expanding $c^T\operatorname{Cov}(P)c$.{{cite:blei_ng_jordan2003}} (§3, p.996, Eq.1)

## Worked example

For $P\sim\operatorname{Dirichlet}(2,3,5)$, $A=10$ and $\E(P)=(0.2,0.3,0.5)$. The variances are $(16,21,25)/1100$ and $\operatorname{Cov}(P_1,P_2)=-6/1100$. Consequently,
$$
 \E(P_1-P_2)=-0.1,\qquad
 \operatorname{Var}(P_1-P_2)=\frac{49}{1100}\approx0.04455.
$$
In contrast, $\operatorname{Var}(P_1+P_2)=25/1100=1/44$. The mixed moment $\E(P_1^2P_2)=3/220$. Doubling the three parameters leaves the mean unchanged and multiplies every variance by $11/21$. These calculations use normaliser ratios rather than an independence approximation.{{cite:blei_ng_jordan2003}} (§3, p.996, Eq.1)

**Your turn.** For $\operatorname{Dirichlet}(1,1,1)$, find the mean and variance of one share and the correlation between two different shares.

::: {.callout-tip collapse="true" title="Answer"}
Each mean is $1/3$, each variance is $1/18$, and each cross-covariance is $-1/36$. The correlation is therefore $-1/2$.
:::

## Related concepts

### Log probabilities

The expected logarithm is a different summary from the logarithm of the expected probability:
$$\E(\log P_k)=\psi(\alpha_k)-\psi(A).$$
Here $\psi$ is the derivative of $\log\Gamma$. Differentiating the log normaliser gives this identity. For the first share in the worked example it equals $-1.82897$, whereas $\log \E(P_1)=\log(0.2)\approx-1.60944$. The inequality agrees with concavity of the logarithm.{{cite:blei_ng_jordan2003}} (§A.1, p.1018)

## Statistical use

With category counts $n_k$, conjugate updating gives parameters $\alpha_k+n_k$. The resulting first moments give predictive probabilities for one further observation; cross-moments quantify uncertainty when categories are combined or compared. A joint interior mode, when every parameter exceeds one, is obtained by maximising $\sum_k(\alpha_k-1)\log p_k$ under $\sum_kp_k=1$, giving $(\alpha_k-1)/(A-K)$. Its difference from the mean reflects a different optimisation problem.{{cite:deisenroth_faisal_ong2020}} (§6.6.1, pp.208–210, Table6.2)
