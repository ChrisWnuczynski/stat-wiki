## Motivating example
Two laboratory measurements may carry nearly the same information about a response. Least squares can fit the observed responses well while assigning one measurement a large positive coefficient and the other a large negative one. A small change in the sample can reverse those coefficients. Ridge regression accepts a little bias to stabilize their joint contribution and, often, predictions on new cases.{{cite:shalizi2025_truth_regression}} (Ch. 15, §§15.1 and 15.4, pp. 253–256, 265–268)

## Intuition
The least-squares objective has a broad, nearly flat valley when predictor columns are nearly collinear. A squared-coefficient penalty raises the valley away from the origin and picks a unique point. The fitted coefficients move toward zero, but their fitted combination need not become uninformative. The penalty acts on coefficients in the units used for the predictors, which is why centering and scaling predictors before fitting is consequential. The intercept represents the mean response at centred predictors and is normally left unpenalised.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 265–269){{cite:dodge2008}} (pp. 458–459, “Ridge Regression”)

## Definition
After centring the response and predictor columns, ridge chooses $\widehat\beta_\lambda$ to minimise $\|y-Xb\|_2^2+\lambda\|b\|_2^2$ for $\lambda\geq0$. This convention uses the *sum* of squared errors; if the first term is divided by $n$, the same numerical $\lambda$ gives a different fit. For $\lambda>0$, $\widehat\beta_\lambda=(X^\top X+\lambda I)^{-1}X^\top y$, even when $X$ lacks full column rank. At $\lambda=0$, one recovers the least-squares objective, but the inverse formula requires full column rank.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 265–267){{cite:dodge2008}} (p. 459, formula and domains)

## Interpretation
In a direction whose design eigenvalue is $d$, the ordinary least-squares coefficient is multiplied by $d/(d+\lambda)$ when $d>0$. Poorly informed directions, with small $d$, shrink more. A zero eigenvalue carries no information about its coefficient combination; ridge assigns that component zero. The eigenvalue shift to $d+\lambda$ makes the solution unique, but it cannot create information absent from the observations. No finite positive penalty generally sets an informed coefficient exactly to zero, unlike the lasso.{{cite:shalizi2025_truth_regression}} (Ch. 15, §§15.3–15.4, pp. 260–267){{cite:dodge2008}} (p. 459, ridge estimate)

## Properties
The gain in stability comes with bias. Under $Y=X\beta+\varepsilon$, $\E\varepsilon=0$ and $\operatorname{Cov}(\varepsilon)=\sigma^2I$, a fixed $\lambda>0$ gives $\E\widehat\beta_\lambda=(X^\top X+\lambda I)^{-1}X^\top X\beta$ and covariance $\sigma^2(X^\top X+\lambda I)^{-1}X^\top X(X^\top X+\lambda I)^{-1}$. A variance reduction need not reduce mean squared error for every true $\beta$; both terms matter. As $\lambda$ grows, the centred slopes approach zero and predictions approach the unpenalised intercept.{{cite:dodge2008}} (pp. 459–460, domains and MSE){{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 265–268)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiating $L(b)=\|y-Xb\|^2+\lambda\|b\|^2$ gives $\nabla L(b)=2(X^\top X+\lambda I)b-2X^\top y$. For any nonzero $v$, $v^\top(X^\top X+\lambda I)v=\|Xv\|^2+\lambda\|v\|^2>0$ when $\lambda>0$, so the stationary point is the unique minimum. Substituting $Y=X\beta+\varepsilon$ in its formula yields the stated expectation and covariance. If $X^\top X=V\operatorname{diag}(d_j)V^\top$, the estimate in direction $v_j$ is $v_j^\top X^\top y/(d_j+\lambda)$; compared with least squares for $d_j>0$, its multiplier is $d_j/(d_j+\lambda)$.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 265–267)
:::
:::

## Statistical use — Shrinking correlated coefficients
Choose predictor transformations and a scaling convention before tuning the penalty. Estimate predictive error for candidate $\lambda$ values with cross-validation, applying centring and scaling separately inside each training fold. If the final reported error is meant to estimate the performance of the whole tuning procedure, use a separate test set or an outer validation loop. The selected penalty is data dependent, so fixed-$\lambda$ sampling formulas should not be presented as though they automatically describe the tuned fit.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 267–268){{cite:dodge2008}} (p. 460, adaptive ridge caveat)

If the response truly depends on one sparse predictor among thousands, ridge keeps small nonzero weights on many others; a sparse method may be easier to interpret. If the mean relationship is strongly nonlinear, coefficient shrinkage does not repair the wrong functional form. With a predictor measured in millimetres beside one in kilometres, an unstandardised common penalty acts very differently on equivalent physical effects. And if $\lambda$ is tuned and evaluated on the same held-out folds without an outer assessment, the reported performance can be optimistic.{{cite:shalizi2025_truth_regression}} (Ch. 15, §§15.4–15.5, pp. 267–270)

## Worked example
Take two identical predictor columns, $X=\begin{pmatrix}1&1\\1&1\end{pmatrix}$, and $y=(1,3)^\top$. Then $X^\top X=\begin{pmatrix}2&2\\2&2\end{pmatrix}$ has eigenvalues $4$ and $0$, and $X^\top y=(4,4)^\top$. With $\lambda=1$, the ridge matrix is $\begin{pmatrix}3&2\\2&3\end{pmatrix}$, with determinant $5$, and $\widehat\beta_1=(0.8,0.8)^\top$. Its fitted values are $(1.6,1.6)^\top$. Least squares instead allows every pair summing to $2$, all of which fit $(2,2)^\top$; the penalty selects a stable symmetric pair while accepting more training error. The numbers also answer the linked matrix-invertibility question below.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 265–267)

**Your turn.** With a single centred predictor column satisfying $X^\top X=4$ and $X^\top y=8$, find the ridge slope for $\lambda=0,2,4$. What happens as the penalty grows?

::: {.callout-tip collapse="true" title="Answer"}
The slopes are $8/(4+0)=2$, $8/(4+2)=4/3$, and $8/(4+4)=1$. They move continuously toward zero as the penalty grows; the fitted intercept, if included before centring, is not penalised.
:::

## Common misconceptions
Ridge does not generally select variables by assigning exact zero slopes: it shrinks informed directions continuously. Its unique coefficient vector does not prove that highly correlated predictors have separately identifiable effects. A smaller training residual sum of squares is not the goal of penalisation; for positive $\lambda$ ridge can fit the training responses less closely than least squares. Finally, $\lambda$ is not scale free: changing from metres to millimetres without rescaling the corresponding penalty changes the solution.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 267–269)

## Connections
The [ordinary least-squares fit](ordinary-least-squares.qmd) supplies the unpenalised reference; [multicollinearity](multicollinearity.qmd) explains the unstable directions. The [ridge-matrix question](../questions/ex-sl-18-2.qmd) examines exact collinearity, while the [soft-threshold question](../questions/ex-sl-18-5.qmd) contrasts continuous ridge shrinkage with lasso selection. These questions expose different consequences of the penalty.{{cite:shalizi2025_truth_regression}} (Ch. 15, §15.4, pp. 265–269)

## History
Hoerl's 1962 work on correlated explanatory variables introduced the early ridge idea and its bias–variance compromise. Hoerl and Kennard's 1970 Technometrics paper gave the method its enduring formulation for nonorthogonal regression problems. The modern use of cross-validation makes that original stability idea a prediction method as well as a response to unstable coefficients.{{cite:dodge2008}} (p. 458, history; pp. 459–460, domains)
