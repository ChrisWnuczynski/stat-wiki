## Motivating example — A contrast can be normal without an invertible map
An analyst often needs a difference, average or fitted linear predictor rather than every coordinate of a measurement vector. Such summaries use rectangular matrices and may reduce dimension. A change-of-variables proof requiring an inverse matrix would miss these common cases. Joint normality is stable under every fixed affine map, including maps whose output covariance is singular.{{cite:durrett2019}} (§3.10, pp. 201–203)

## Key results — Means and covariances follow the same map
Let $X\sim N_p(\mu,\Sigma)$, allowing $\Sigma$ to be positive semidefinite, and let $A$ be a fixed real $k\times p$ matrix. For a fixed $b\in\mathbb R^k$,
$$AX+b\sim N_k(A\mu+b,A\Sigma A^\top).$$
Normality of a scalar with zero variance means it is constant at its mean. A singular vector normal law is likewise a probability distribution, even though it has no Lebesgue density in the whole output space. The covariance formula holds for every random vector with finite second moments; the assertion that the transformed law is normal uses joint normality.{{cite:durrett2019}} (§3.10, construction of multivariate normal distributions and ex. 3.10.8)

## Proof
For any $t\in\mathbb R^k$, the scalar contrast of the transformed vector is $t^\top(AX+b)=(A^\top t)^\top X+t^\top b$. The defining contrast characterisation of a jointly normal vector makes this scalar normal, with mean $t^\top(A\mu+b)$ and variance $t^\top A\Sigma A^\top t$. As this holds for every $t$, the output vector is jointly normal with the stated parameters. Equivalently its characteristic function is
$$\mathbb E e^{it^\top(AX+b)}=\exp\{it^\top(A\mu+b)-\tfrac12t^\top A\Sigma A^\top t\}.$$
This argument needs no inverse of $A$ or $\Sigma$ and covers zero-variance contrasts directly.{{cite:durrett2019}} (§3.10, pp. 201–203 and ex. 3.10.8)

## Statistical use — Marginals, predictions and Gaussian mixtures over parameters
Choosing rows of the identity matrix obtains any marginal normal vector. Choosing a single row gives a normal linear predictor, with variance $a^\top\Sigma a$. Combining independent normal vectors gives another instance: stack the vectors, use a block-diagonal covariance, and select the desired sum. Independence is what removes the cross-covariance terms. If the vectors are jointly normal but correlated, the same linear-map rule still works with the full covariance matrix.{{cite:durrett2019}} (§3.10, multivariate normal laws and ex. 3.10.7)

In a Gaussian regression hierarchy, a conditional model $Y\mid\beta,v\sim N(X\beta,vI)$ and prior $\beta\mid v\sim N(m_0,vC_0)$ give $Y\mid v\sim N(Xm_0,v(I+XC_0X^\top))$. Write $Y=X\beta+\varepsilon$, with $\beta$ and $\varepsilon$ independent conditional on $v$, and apply the transformation rule to their stack. The extra covariance $vXC_0X^\top$ represents uncertainty in the coefficient vector. Integrating an additional uncertain variance can produce a Student distribution, so the Gaussian result applies conditional on the fixed variance level in this calculation.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, eq. 1.23 and prior predictive distribution)

## Worked example — A sum and a difference
Take $\mu=(1,2)^\top$, $\Sigma=\left(\begin{smallmatrix}4&1\\1&9\end{smallmatrix}\right)$ and $A=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$. Then $Y_1=X_1+X_2$ and $Y_2=X_1-X_2$ have mean $(3,-1)^\top$ and covariance
$$A\Sigma A^\top=\begin{pmatrix}15&-5\\-5&11\end{pmatrix}.$$
The covariance of the sum and difference is $\operatorname{Var}(X_1)-\operatorname{Var}(X_2)=-5$. It does not vanish simply because one contrast adds and the other subtracts. Their correlation is $-5/\sqrt{165}\approx-0.389249$.

**Your turn.** Set $Z=(X_1,2X_1)^\top$. Give its mean, covariance and covariance rank.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $(1,2)^\top$ and the covariance is $\left(\begin{smallmatrix}4&8\\8&16\end{smallmatrix}\right)$. Its rank is one because the second coordinate is twice the first. The vector remains jointly normal but lies on a line.
:::

## Common misconceptions — Normal coordinates need a joint assumption
Marginal normality of every coordinate does not suffice. Let $Z\sim N(0,1)$ and let $B$ be an independent fair sign. Then $Z$ and $BZ$ are both marginally standard normal, with covariance zero, but their squared values agree with probability one. The pair is dependent and is not jointly normal. The sum is zero whenever $B=-1$, giving an atom at zero that a nondegenerate scalar normal law cannot have. Thus a list of normal marginal models cannot justify Gaussian contrasts without a condition on their joint distribution.{{cite:durrett2019}} (§3.10, contrast characterisation and independence of jointly normal coordinates)
