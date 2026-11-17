## Motivating example
A fitted line may visibly slope upward while leaving most response variability unexplained. The coefficient of determination compares its squared residual error with the error of predicting every response by the sample mean. Its interpretation is relative to that baseline and to the observations on which the comparison is calculated.{{cite:cetinkaya_hardin2024}} (§7.2, describing the strength of a fit)

## Properties — The intercept makes the centred decomposition work
Let $\hat y=X\hat\beta$ be an ordinary least-squares fit whose design includes an intercept, and $e=y-\hat y$. The normal equations give $X^\top e=0$, so $\mathbf1^\top e=0$ and $(\hat y-\bar y\mathbf1)^\top e=0$. Expanding $y-\bar y\mathbf1=(\hat y-\bar y\mathbf1)+e$ yields
$$
SST=SSR+SSE,
\quad SST=\sum_i(y_i-\bar y)^2,
\quad SSR=\sum_i(\hat y_i-\bar y)^2.
$$
For $SST>0$, $R^2=1-SSE/SST=SSR/SST$ lies in $[0,1]$. This is a projection identity for the fitted sample; normally distributed errors are unnecessary for the identity.{{cite:prado_ferreira_west2021}} (§1.5.2, pp. 20–21){{cite:cetinkaya_hardin2024}} (§7.2, describing the strength of a fit)

For one predictor with an intercept, $\hat\beta_1=S_{xy}/S_{xx}$ and $SSR=\hat\beta_1^2S_{xx}$. Hence $R^2=S_{xy}^2/(S_{xx}S_{yy})=r^2$. Squaring removes the sign: strong negative and positive linear relationships can have the same $R^2$. A constant response makes the centred ratio undefined, and a constant predictor prevents identification of a separate intercept and slope.{{cite:cetinkaya_hardin2024}} (§7.2, describing the strength of a fit)

Adding columns to a least-squares design enlarges its fitted subspace. The previous fit remains available, so minimum training SSE cannot increase and training $R^2$ cannot decrease. This algebra does not guarantee better prediction on another sample. Without an intercept, the centred decomposition need not hold; on evaluation data, a fitted prediction can be worse than the constant baseline and give a negative $1-SSE/SST$.{{cite:prado_ferreira_west2021}} (§1.5.2, pp. 20–21)

## Interpretation — Explained variation is an account of a fit
A high value quantifies a reduction in squared error relative to the sample-mean baseline. It does not establish a causal effect, verify linearity, rule out influential observations or measure a coefficient's practical size. Residual plots and the scale of response errors supply information that the ratio discards. The word explained describes an arithmetic partition, whose usefulness depends on the model and study design.{{cite:cetinkaya_hardin2024}} (§§7.1–7.2)

## Worked example — A positive slope with modest explanatory power
Take $x=(0,1,2,3,4)$ and $y=(1,2,1,4,2)$. The sample means are $2$ and $2$, with $S_{xx}=10$, $S_{xy}=4$ and $S_{yy}=6$. The fitted line is $\hat y=1.2+0.4x$, with fitted values $(1.2,1.6,2.0,2.4,2.8)$. Its squared residuals sum to $4.4$, while $SSR=1.6$. Thus
$$
R^2=1-\frac{4.4}{6}=\frac4{15}=0.266667
=\frac{4^2}{10(6)}=r^2.
$$
The line accounts for about $26.7\%$ of the centred variation, leaving about $73.3\%$ in residuals.{{cite:cetinkaya_hardin2024}} (§7.2, describing the strength of a fit)

**Your turn.** On these same responses, evaluate the fixed prediction $\hat y_i=0$. What is $1-SSE/SST$?

::: {.callout-tip collapse="true" title="Answer"}
Its $SSE=1+4+1+16+4=26$, so $1-26/6=-10/3$. This fixed prediction is worse than predicting the sample mean. It is not the least-squares fit with an intercept.
:::

## Check yourself
### Derive the fitted line {#self-check-ex-inf-normal-equations}
[Normal equations for a straight line](../questions/ex-inf-normal-equations.qmd) supplies the orthogonality used in the decomposition.

::: {.callout-tip collapse="true" title="Answer"}
Differentiating SSE gives $\sum e_i=\sum x_ie_i=0$. These imply $b_0=\bar y-b_1\bar x$ and $b_1=S_{xy}/S_{xx}$. The Hessian is $2X^\top X$, positive definite when the predictor varies.
:::

### Recognise a different baseline {#self-check-ex-inf-line-through-origin}
[A line through the origin](../questions/ex-inf-line-through-origin.qmd) omits the intercept.

::: {.callout-tip collapse="true" title="Answer"}
The fitted slope is $\sum x_iy_i/\sum x_i^2$, with sampling mean $\beta$ and variance $\sigma^2/\sum x_i^2$ under the stated error model. Residuals need not sum to zero, so the centred $R^2=r^2$ identity does not automatically apply.
:::
