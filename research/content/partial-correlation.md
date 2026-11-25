## Lead context
Partial correlation is the correlation that remains between two variables after a linear adjustment for one or more others.{{cite:dodge2008}} (p. 412)

## Motivating example
Ice-cream sales and heat-related illness counts can rise in the same weeks. The two series are correlated, and neither is the mechanism of the other: both track temperature. A correlation computed after each series has been linearly adjusted for temperature asks how much association is left. If the adjusted series are nearly uncorrelated, the original correlation was the shared temperature track. If a large partial correlation remains, something other than that linear temperature term still ties the two series together.{{cite:dodge2008}} (pp. 412–413)

## Intuition — Correlate the residuals, not the raw series
Regress $X$ on $Z$ and $Y$ on $Z$, and correlate the residuals. A residual is the part of a variable that the linear function of $Z$ did not account for. The partial correlation is that residual correlation. When $Z$ is uncorrelated with each of $X$ and $Y$, both fitted slopes are zero, the residuals are the centred variables and, provided both residual variances are positive, the partial correlation equals the ordinary correlation. Independence of $Z$ from each variable is sufficient for zero slopes, but it is more than they mean: a flat linear fit says only that $Z$ has no linear association with the variable, not that $Z$ carries no information about it. When $X$ and $Y$ are each linearly tied to $Z$ and not otherwise, the residuals are weakly correlated and the partial correlation is near zero. Both extremes occur, and the quantity is still a linear association: the subtraction does not turn it into a causal effect.{{cite:dodge2008}} (pp. 412–413)

For more than one adjusting variable the same idea is applied in stages, or equivalently to the residuals from the multiple regression on all of them. In a multivariate normal model the residual correlation equals the conditional correlation given the adjusting variables. Outside that model the residual correlation remains defined whenever the second moments and the linear regressions exist and both residual variances are positive, and it need not equal the conditional correlation at every value of the conditioning variables. If one of the regressions fits exactly, its residual is a constant, its variance is zero, and the residual correlation is undefined rather than zero.

## Definition
For three variables, write $r_{xy}$, $r_{xz}$ and $r_{yz}$ for the ordinary correlations. The partial correlation of the $x$ and $y$ samples given $z$ is
$$
r_{xy\cdot z}=\frac{r_{xy}-r_{xz}r_{yz}}{\sqrt{(1-r_{xz}^{2})(1-r_{yz}^{2})}},
$$
provided neither $r_{xz}$ nor $r_{yz}$ has absolute value $1$.{{cite:dodge2008}} (p. 413) The same algebra with population correlations defines $\rho_{xy\cdot z}$. For a non-degenerate covariance, the partial correlation of two coordinates given all the others is the ordinary correlation of their residuals after linear regression on those others. In the precision matrix $K=\Sigma^{-1}$ that correlation equals $-K_{jk}/\sqrt{K_{jj}K_{kk}}$, so a negative off-diagonal entry is a positive partial correlation.

## Properties — The residual formula is the displayed fraction
The fraction is not an extra definition. It is what the residual correlation equals when the regressions on $Z$ are linear and the variables have been standardised.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Standardise $X$, $Y$ and $Z$ to mean $0$ and variance $1$, so that correlations and covariances agree. The least-squares coefficient of $Z$ in the regression of $X$ is $r_{xz}$, and the residual $X-r_{xz}Z$ has variance $1-r_{xz}^{2}$. Likewise $Y-r_{yz}Z$ has variance $1-r_{yz}^{2}$. Their covariance is
$$
\mathrm{E}\bigl((X-r_{xz}Z)(Y-r_{yz}Z)\bigr)=r_{xy}-r_{xz}r_{yz},
$$
because $\mathrm{E}(XZ)=r_{xz}$, $\mathrm{E}(YZ)=r_{yz}$ and $\mathrm{E}(Z^{2})=1$. Dividing the covariance by the square root of the product of the residual variances is the displayed formula. If $r_{xz}=r_{yz}=0$, the fraction collapses to $r_{xy}$.{{cite:dodge2008}} (p. 413)

For a non-degenerate normal vector the conditional covariance of coordinates $j$ and $k$ given the rest is the inverse of the corresponding $2\times 2$ precision block. That block has diagonal entries $K_{jj}$ and $K_{kk}$ and off-diagonal $K_{jk}$, so its determinant is $K_{jj}K_{kk}-K_{jk}^{2}$ and the off-diagonal of the inverse is $-K_{jk}$ over the determinant. The two conditional variances are $K_{kk}$ and $K_{jj}$ over the same determinant. Their correlation therefore simplifies to $-K_{jk}/\sqrt{K_{jj}K_{kk}}$.
:::
:::

The precision formula is the same fact after all the other coordinates, not only one $Z$, have been partialled out. The sign is negative because the off-diagonal precision entry appears with a minus sign in the conditional covariance of a normal vector. A positive partial correlation is a negative precision entry. Reading the sign of $K_{jk}$ as the sign of the partial correlation reverses the association.

## Statistical use — Marginal correlation and conditional association answer different questions
A marginal correlation answers whether two coordinates move together in the joint distribution. A partial correlation answers whether they still move together after a linear adjustment for the others. A Gaussian chain $X_1-X_2-X_3$ can have a nonzero marginal correlation between the ends and a zero partial correlation given the middle. Thresholding the marginal correlations estimates a different graph from the graph of nonzero partial correlations. In high dimension the partial correlations are functions of an estimated precision matrix, and a penalty or a selection rule that sets small entries to zero is estimating that graph, not certifying conditional independence in the population.{{cite:dodge2008}} (pp. 412–413)

## Worked example
Take population correlations $r_{xy}=0.8$, $r_{xz}=0.6$ and $r_{yz}=0.5$. The numerator is $0.8-0.6\cdot 0.5=0.5$. The denominator is
$$
\sqrt{(1-0.36)(1-0.25)}=\sqrt{0.64\cdot 0.75}=\sqrt{0.48}\approx 0.6928.
$$
The partial correlation is $0.5/0.6928\approx 0.7217$. The ordinary correlation $0.8$ shrinks, but it does not disappear: the product $0.6\cdot 0.5=0.3$ removes only part of the $0.8$. The same formula with $r_{xy}$ replaced by $0.3$ would give numerator $0$ and partial correlation $0$. That is the numerical version of “the observed correlation is accounted for by $Z$”.{{cite:dodge2008}} (p. 413)

A second check uses the precision matrix of a three-variable chain,
$$
K=\begin{pmatrix}1&-1/2&0\\-1/2&1&-1/2\\0&-1/2&1\end{pmatrix}.
$$
Its inverse has marginal correlation $1/3$ between the first and third coordinates, from the covariance entry $0.5$ and the two variances $1.5$. The partial correlation of those coordinates given the middle one is $-K_{13}/\sqrt{K_{11}K_{33}}=0$. The marginal association and the partial association disagree, as the formula allows.

**Your turn.** Correlations $r_{xy}=0.5$, $r_{xz}=0.5$ and $r_{yz}=0.5$. Compute $r_{xy\cdot z}$.

::: {.callout-tip collapse="true" title="Answer"}
The numerator is $0.5-0.25=0.25$. The denominator is $\sqrt{(1-0.25)^{2}}=\sqrt{0.75^{2}}=0.75$. The partial correlation is $0.25/0.75=1/3\approx 0.3333$.
:::

## Common misconceptions
Partial correlation is not ordinary correlation of the raw variables, and it is not a regression coefficient. The regression coefficient of $Y$ on $X$ given $Z$ carries the units of $Y$ per unit of $X$; the partial correlation is dimensionless. A partial correlation of zero does not say that $X$ and $Y$ are conditionally independent, except inside a joint normal model where uncorrelated residuals are independent residuals. It does not say that $Z$ causes $X$ or $Y$. The ice-cream pattern is a warning against that reading: adjusting for temperature can remove a correlation without identifying a mechanism.{{cite:dodge2008}} (pp. 412–413)

The sign error on the precision matrix is a separate slip. A negative $K_{jk}$ is a positive partial correlation. Quoting the precision entry as if it were the correlation reverses the direction.

## Assumptions and limits — Linear adjustment and a singular regression
The formula uses linear least squares. A U-shaped dependence on $Z$ can leave a large residual association that a linear adjustment does not remove, or it can create a linear partial correlation that a nonlinear adjustment would not. If $r_{xz}=\pm 1$, the residual of $X$ on $Z$ is zero and the denominator vanishes. There is then no partial correlation of $X$ with anything given $Z$, because $X$ is an affine function of $Z$.

The sample formula also estimates a population quantity only when the correlations are computed from a sample to which those second moments apply. A handful of points can make $r_{xy\cdot z}$ swing from large and positive to large and negative when one point moves. The algebra will still return a number. The number is not stable evidence of a direct linear relation.{{cite:dodge2008}} (p. 413)

## Connections
The [correlation](correlation.qmd) is the case with nothing partialled out. The [precision matrix](precision-matrix.qmd) packages every partial correlation given the rest, with a change of sign. In a [Gaussian graphical model](markov-random-field.qmd) a missing edge is a zero partial correlation and, under normality, a conditional independence. [Clique](clique.qmd) factorisation is the matching statement for a positive density on an undirected graph, and it is a different theorem from the three-variable fraction above.{{cite:dodge2008}} (pp. 412–413)

## Check yourself
### A product that cancels {#self-check-partial-zero}

If $r_{xy}=0.4$, $r_{xz}=0.8$ and $r_{yz}=0.5$, what is the numerator of $r_{xy\cdot z}$, and what does a zero numerator mean?

::: {.callout-tip collapse="true" title="Answer"}
The numerator is $0.4-0.8\cdot 0.5=0$. The partial correlation is $0$. The ordinary correlation equals the product of the correlations with $Z$, which is the residual-covariance calculation when the linear adjustment accounts for the whole association.
:::

### Precision sign {#self-check-partial-sign}

A precision matrix has $K_{12}=-0.3$, $K_{11}=1$ and $K_{22}=1$. What is the partial correlation of coordinates $1$ and $2$ given the rest?

::: {.callout-tip collapse="true" title="Answer"}
It is $-(-0.3)/\sqrt{1\cdot 1}=0.3$. The negative precision entry is a positive partial correlation.
:::

## History
Early users of correlation already knew a large bivariate correlation could be produced by a third variable, and Yule’s 1926 time-series example gave a clear numerical warning. The sample partial correlation is the correlation of the two least-squares residuals, and it equals the fraction in the three ordinary correlations. The three-correlation fraction is the closed form of that residual correlation.{{cite:dodge2008}} (pp. 412–413)
