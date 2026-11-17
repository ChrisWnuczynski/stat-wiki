## Motivating example
A regression can ask whether several predictors contribute jointly, even if no single coefficient looks decisive by itself. For example, three group means being equal imposes two independent contrasts. A general linear hypothesis states those restrictions explicitly and measures the loss of fit when they are imposed. Least squares estimates the unrestricted coefficients by minimizing residual sum of squares.{{cite:openintro2019}} (§9.1.2, including and assessing many variables)

## Definition
Assume $Y=X\beta+\varepsilon$, where $X$ is a fixed $n\times p$ full-column-rank matrix, $n>p$, and $\varepsilon\sim N(0,\sigma^2I_n)$. The most general affine restriction is $R\beta=r_0$, with $R$ a known rank-$r$ matrix; the formula below specializes to $r_0=0$. Dependent rows do not count as independent restrictions. For a general nonzero $r_0$, choose any $\beta_*$ satisfying the constraint and replace $Y$ by $Y-X\beta_*$ before applying the homogeneous geometry. The resulting test measures extra residual variation per restriction.{{cite:dodge2008}} (p. 200, Fisher distribution in regression and analysis of variance)

## Properties — Orthogonal sums of squares
Let $P_1$ project onto the unrestricted mean space $\mathcal C(X)$ and let $P_0$ project onto the mean subspace satisfying $R\beta=0$. Nestedness gives $P_1P_0=P_0P_1=P_0$. Therefore $P_1-P_0$ and $I-P_1$ are orthogonal projectors of ranks $r$ and $n-p$, with product zero. Under the null, both annihilate the true mean. Orthogonally rotating the normal error vector into bases of their ranges proves that
$$\frac{Y^\top(P_1-P_0)Y}{\sigma^2}\sim\chi^2_r,\qquad
\frac{Y^\top(I-P_1)Y}{\sigma^2}\sim\chi^2_{n-p},$$
independently. Their numerators are $RSS_0-RSS_1$ and $RSS_1$. Dividing each by its rank proves the stated $F$ distribution. The last step is the defining independent-chi-square ratio.{{cite:dodge2008}} (p. 200, mathematical aspects of the Fisher distribution)

## Worked example — A joint restriction
Suppose a fixed-design normal regression has $n=30$ observations and $p=4$ coefficients. Two independent restrictions increase residual sum of squares from $52$ to $70$. Then
$$F=\frac{(70-52)/2}{52/(30-4)}=4.5,$$
on $(2,26)$ degrees of freedom, with $p=0.02098$. The joint restriction is rejected at 5%. This comparison requires refitting the constrained model; setting two estimated coefficients to zero without refitting the others generally produces the wrong restricted residual sum of squares. The denominator estimates the residual variance using the unrestricted model.{{cite:dodge2008}} (p. 200, ratio distribution and regression application)

**Your turn.** For $n=20$, $p=3$, $r=1$, $RSS_1=34$ and $RSS_0=42$, calculate the test statistic and its reference degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
The unrestricted variance estimate is $34/17=2$. The extra sum of squares is 8, so $F=8/2=4$ on $(1,17)$ degrees of freedom, with upper-tail probability approximately $0.0617$.
:::

## Assumptions and limits
The ordinary exact test requires normal, independent, equal-variance errors, a suitable fixed design and a correctly specified mean. Residual plots can reveal curvature, changing spread or temporal structure. A large $R^2$ alone cannot validate those premises. Heteroscedasticity-robust Wald tests and correlated-error models use different variance estimates and reference arguments.{{cite:nist_model_fit2002}} (§4.4.4, graphical residual analysis)

## Connections
For a single restriction, the $F$ statistic equals the square of the corresponding $t$ statistic when both use the same residual variance estimate. In the four-point line below, the sums of squares are $10$ and $0.2$, so $F=98$ with only two denominator degrees of freedom. Its small $p$-value reflects a strong linear pattern under the model; four observations provide limited ability to diagnose that model.{{cite:dodge2008}} (p. 200, squared Student distribution)

## Lead context
A linear hypothesis restricts the mean vector of a normal linear model to a linear subspace. The comparison refits the model under that restriction and asks whether the increase in residual sum of squares is large relative to the unrestricted residual variance.

For one restriction the resulting $F$ statistic is the square of the usual $t$ statistic. For several restrictions there is no single coefficient whose $t$ statistic replaces the joint comparison.{{cite:dodge2008}} (p. 200, Fisher distribution in regression and analysis of variance)

## Intuition
With $n=30$ observations and $p=4$ unrestricted coefficients, two independent restrictions leave residual degrees of freedom $26$ under the full model. If the residual sum of squares rises from $52$ to $70$, the numerator mean square is $(70-52)/2=9$ and the denominator mean square is $52/26=2$. Their ratio is $F=4.5$ on $(2,26)$ degrees of freedom, with an upper-tail probability of about $0.02098$. The same arithmetic with one restriction, $n=20$, $p=3$, residual sums $34$ and $42$, gives $F=(42-34)/(34/17)=4$ on $(1,17)$ degrees of freedom and an upper-tail probability of about $0.0617$.{{cite:dodge2008}} (p. 200, ratio distribution and regression application)

## Interpretation
The numerator degrees of freedom are the number of independent restrictions, not the number of coefficients written in the unrestricted model. A redundant restriction that repeats one already imposed does not increase that count and does not change the fitted residual sum of squares. Zeroing a coefficient in the unrestricted fit, without refitting, does not produce the restricted residual sum of squares. The restricted fit is the projection onto a smaller subspace, and that projection has to be recomputed. A single restriction with $F=9$ on $(1,20)$ degrees of freedom matches an absolute $t$ statistic of $3$, because the one-degree-of-freedom $F$ is the square of $t$ when both use the same residual variance.{{cite:dodge2008}} (p. 200, squared Student distribution)

## Common misconceptions
A large $F$ statistic is evidence against the joint restriction under the normal linear model. It is not a list of which individual coefficients would be rejected by separate $t$ comparisons. Two coefficients can be jointly incompatible with a restriction while each one-at-a-time interval contains the restricted value, when the estimates are correlated. The comparison also assumes that the restricted model is nested in the unrestricted model and that the error variance is the same. Comparing two non-nested mean structures by an extra-sum-of-squares ratio uses the statistic outside the setting that gives it an $F$ reference distribution. A small tail probability does not say that the unrestricted model is true. It says that the extra residual sum of squares is hard to explain if the restriction holds and the normal assumptions are adequate.{{cite:nist_model_fit2002}} (§4.4.4, graphical residual analysis){{cite:openintro2019}} (§9.1.2, including and assessing many variables)

## Statistical use
The numerator degrees of freedom are the rank of the restriction, and the denominator degrees of freedom are the residual degrees of freedom of the unrestricted fit. With $n=30$ and $p=4$, two independent restrictions leave $26$ residual degrees of freedom. Residual sums of squares $52$ and $70$ produce
$$F=\frac{(70-52)/2}{52/26}=4.5$$
on $(2,26)$ degrees of freedom, with upper-tail probability about $0.02098$. With $n=20$, $p=3$, and one restriction, residual sums $34$ and $42$ produce $F=4$ on $(1,17)$ degrees of freedom and upper-tail probability about $0.0617$. A repeated copy of a restriction does not increase the rank and does not change the restricted residual sum of squares.

One restriction is also a $t$ comparison. An $F$ statistic of $9$ on $(1,20)$ degrees of freedom matches an absolute $t$ statistic of $3$ when both use the same residual variance. Zeroing coefficients in the unrestricted fit, without solving the restricted least-squares problem, does not produce the restricted residual sum of squares. The other coefficients generally move when the restriction is imposed.{{cite:dodge2008}} (p. 200, squared Student distribution)
