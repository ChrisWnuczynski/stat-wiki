## Motivating example
Three measurements may move together even when the first and third share no association after the second is fixed. A Gaussian chain distinguishes these questions: a covariance entry describes marginal association, whereas a precision entry describes conditional association given all remaining coordinates. The conditioning set is part of the assertion.{{cite:shutta_etal2022_ggm}} (§§2.1–2.3)

## Intuition — Read the quadratic after conditioning
Write $Z=X-\mu$ and $K=\Sigma^{-1}$. The nonsingular Gaussian density is proportional to $\exp(-Z^\top KZ/2)$. Fix every coordinate except $i,j$. Terms involving the two unfixed coordinates have quadratic matrix
$$
K_{\{i,j\},\{i,j\}}=
\begin{pmatrix}K_{ii}&K_{ij}\\K_{ij}&K_{jj}\end{pmatrix}.
$$
Conditioning changes the linear terms and the mean, but this principal block is the conditional precision. Its inverse is the conditional covariance, rather than the corresponding principal block of $\Sigma$.{{cite:pishro_nik2014}} (§6.1.5, normal random vectors){{cite:shutta_etal2022_ggm}} (§2.2.1, eqs. 4–7)

## Proof
The conditional density has the form
$$
c\exp\{-\tfrac12K_{ii}z_i^2-K_{ij}z_iz_j-\tfrac12K_{jj}z_j^2+u_i z_i+u_j z_j\},
$$
where $u_i,u_j$ depend only on the fixed coordinates. Positive definiteness gives positive diagonal entries and a positive determinant. If $K_{ij}=0$, the exponential is a product of two integrable one-variable functions; its normalising constant also factors. This proves conditional independence. Conversely, independent conditional Gaussian coordinates have zero conditional covariance. Inverting the displayed $2\times2$ block gives conditional off-diagonal covariance $-K_{ij}/(K_{ii}K_{jj}-K_{ij}^2)$; its denominator is positive, so it vanishes only when $K_{ij}=0$. This proves both directions.{{cite:shutta_etal2022_ggm}} (§2.2.1, eqs. 4–7)

## Key results — Signs, regression coefficients and the conditioning set
The same inverse gives
$$
\rho_{ij\mid -\{i,j\}}=-\frac{K_{ij}}{\sqrt{K_{ii}K_{jj}}}.
$$
For the conditional law of a single coordinate, completing the square gives variance $1/K_{ii}$ and mean
$\mu_i-\sum_{j\ne i}(K_{ij}/K_{ii})(x_j-\mu_j)$.
Thus zero precision entries also identify zero coefficients in its Gaussian regression on all other coordinates. These equivalences require the joint Gaussian model. Zero covariance alone does not establish independence for arbitrary distributions, and an undirected association graph supplies no causal direction.{{cite:shutta_etal2022_ggm}} (§§2.2.2–2.3)

## Worked example

### Correlated endpoints with no conditional edge
Take a centred Gaussian vector with
$$
K=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix},\qquad
\Sigma=\frac14\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix}.
$$
Matrix multiplication gives $K\Sigma=I$. The marginal endpoint correlation is $(1/4)/(3/4)=1/3$. Nevertheless $K_{13}=0$, and conditional on $X_2=x$, the endpoints are independent $N(x/2,1/2)$ variables. In particular, their conditional covariance is zero. The adjacent partial correlations are $1/2$, while the endpoint partial correlation is zero.{{cite:shutta_etal2022_ggm}} (§2.2.1)

For comparison, $\Sigma=\left(\begin{smallmatrix}1&1/2&0\\1/2&1&0\\0&0&1\end{smallmatrix}\right)$ has precision $\left(\begin{smallmatrix}4/3&-2/3&0\\-2/3&4/3&0\\0&0&1\end{smallmatrix}\right)$. Its third coordinate is independent of the first two, and $\rho_{12\mid3}=1/2$. Here both covariance and precision isolate the third coordinate.{{cite:pishro_nik2014}} (§6.1.5)

**Your turn.** In the chain example, what is $\operatorname{Var}(X_1\mid X_2,X_3)$? Does its value equal the marginal variance?

::: {.callout-tip collapse="true" title="Answer"}
It is $1/K_{11}=1/2$, whereas the marginal variance is $\Sigma_{11}=3/4$. Observing the other coordinates reduces uncertainty in this example.
:::
