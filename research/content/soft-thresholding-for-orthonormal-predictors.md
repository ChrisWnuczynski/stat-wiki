## Motivating example
Several weak regression coefficients can look like noise, yet setting all of them to zero by a fixed cutoff creates an abrupt jump in fitted values. Soft thresholding both removes small coefficients and shrinks the survivors continuously. With orthonormal predictors, this operation solves the lasso exactly, one coordinate at a time.{{cite:parikh_boyd2014_proximal}} (§6.5.2, eq. 6.9, p. 188)

## Properties — The factor of two comes from the objective
Let $X^\top X=I$ and $b=X^\top y$. Expanding the raw residual sum of squares gives
$$
\|y-X\beta\|^2=\|y\|^2-\|b\|^2+\sum_j(\beta_j-b_j)^2.
$$
Thus minimising $\|y-X\beta\|^2+\lambda\sum_j|\beta_j|$ reduces to independent scalar minimisations. Dividing each by two identifies a proximal problem with threshold $\lambda/2$. For an objective whose residual term is already divided by two, the threshold is instead $\lambda$. The numerical threshold cannot be specified without the loss normalisation.{{cite:parikh_boyd2014_proximal}} (§1.1, eqs. 1.1–1.2; §6.5.2, eq. 6.9)

For a scalar coordinate, the subgradient condition is
$$
0\in2(\beta-b)+\lambda\partial|\beta|.
$$
At zero the absolute-value subgradient is $[-1,1]$, so zero is optimal exactly when $|b|\le\lambda/2$. Outside that interval the derivative gives $\beta=b-(\lambda/2)\operatorname{sign}(b)$. The strictly convex squared term makes the minimiser unique, including at the two threshold endpoints.{{cite:parikh_boyd2014_proximal}} (§6.5.2, soft-threshold operator)

## Interpretation — Three penalties, three behaviours
Under the same orthonormal design and raw residual loss, ridge gives $b_j/(1+\lambda)$. An $L_0$ count penalty gives either $b_j$ or zero: choosing $b_j$ costs $\lambda$, whereas choosing zero costs $b_j^2$, so the switch occurs at $|b_j|=\sqrt\lambda$. At equality both choices minimise the objective. Soft thresholding instead moves continuously through zero while shrinking every surviving magnitude. Ridge generally gives no exact zeros when $b_j\ne0$.{{cite:boyd_vandenberghe2004}} (§6.3.2, eq. 6.10, p. 306; Ex. 6.4, p. 310){{cite:parikh_boyd2014_proximal}} (§6.5.2, eq. 6.9)

## Worked example — The same data under two penalties
For $b=(2.4,-0.9,0.5,-0.1)$ and $\lambda=2$, lasso gives $(1.4,0,0,0)$, while ridge gives $(0.8,-0.3,1/6,-1/30)$. Hard thresholding at $\sqrt2$ gives $(2.4,0,0,0)$. Soft and hard thresholding select the same coordinate here but estimate its magnitude differently. At a raw lasso penalty of $4.8$, even the largest coordinate becomes zero.

**Your turn.** With the same $b$, use raw residual loss plus $2\|\beta\|_1+\|\beta\|^2$. Find the minimiser.

::: {.callout-tip collapse="true" title="Answer"}
The scalar condition outside zero is $2(\beta-b)+2\operatorname{sign}(\beta)+2\beta=0$. Soft threshold at one, then divide by two: the answer is $(0.7,0,0,0)$.
:::

## Connections — Coordinate descent beyond orthogonality
When predictors are correlated, $X^\top y$ cannot be thresholded once to obtain the joint lasso solution. Coordinate descent instead forms the partial residual after accounting for all other coefficients, applies a scalar soft threshold, and cycles through coordinates. A coordinate changes the residual seen by the next one. Elastic-net updates combine the threshold with a further multiplicative shrinkage.{{cite:friedman_glmnet2010}} (§2, eqs. 5–6){{cite:parikh_boyd2014_proximal}} (§6.5.3, p. 189)

## Check yourself

### Compare raw-loss conventions {#self-check-ex-sl-18-5}

[Practice question](../questions/ex-sl-18-5.qmd)

Compute ridge and lasso for the displayed $b$ and $\lambda=2$.

::: {.callout-tip collapse="true" title="Answer"}
Ridge divides all coordinates by three. Lasso soft-thresholds at one, leaving only $1.4$ in the first coordinate. Using threshold two would correspond to a different residual-loss normalisation.
:::

### Correlated columns change the calculation {#self-check-ex-sl-18-2}

[Practice question](../questions/ex-sl-18-2.qmd)

Two identical predictor columns both equal $(1,1)^\top$. For $y=(1,3)^\top$ and ridge penalty one, find the coefficients.

::: {.callout-tip collapse="true" title="Answer"}
$X^\top X$ has eigenvalues zero and four. Symmetry gives equal coefficients; solving $(X^\top X+I)\beta=X^\top y$ gives $(0.8,0.8)$. Unpenalised least squares only fixes their sum at two.
:::
