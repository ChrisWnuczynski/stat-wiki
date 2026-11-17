## Lead context
Penalties make a model pay for large coefficients or a rough fitted curve, which can reduce variation in predictions across training samples. Their strength is a tuning choice: too little leaves a flexible fit unstable, while too much can suppress useful structure.{{cite:hoerl_kennard1970}} (§§1–2, pp. 55–58){{cite:tibshirani1996}} (§§1–2.1, pp. 267–269)

## Motivating example
Two nearly redundant predictors can give similar fitted responses under several different coefficient pairs. A small change in the training data may then alter the coefficients sharply. Ridge regression favours a coefficient vector of smaller squared length; the lasso favours smaller total absolute magnitude and may make one coefficient exactly zero. The choice affects both how the fitted relation is described and how it responds to new data.{{cite:hoerl_kennard1970}} (§§1–2, pp. 55–58){{cite:tibshirani1996}} (§§1–2.2, pp. 267–270)

## Definition
Let $\boldsymbol y\in\mathbb R^n$ be realised responses, $\boldsymbol X\in\mathbb R^{n\times p}$ a fixed design matrix whose rows contain the realised inputs, and $\boldsymbol\beta\in\mathbb R^p$ a coefficient vector. A penalised least-squares fit minimises
$$
Q_\lambda(\boldsymbol\beta)=\tfrac12\lVert\boldsymbol y-\boldsymbol X\boldsymbol\beta\rVert_2^2+\lambda P(\boldsymbol\beta),\qquad\lambda\ge0,
$$
where the first term measures residual squared error, $P$ is a nonnegative penalty, and $\lambda$ controls its strength. Ridge takes $P(\boldsymbol\beta)=\tfrac12\sum_{j=1}^p\beta_j^2$; the lasso takes $P(\boldsymbol\beta)=\sum_{j=1}^p|\beta_j|$. In an intercept model, the intercept is usually fitted separately and left unpenalised; predictor scaling must be specified because the penalty acts on coefficients rather than on predictions.{{cite:hoerl_kennard1970}} (§2, pp. 57–58){{cite:tibshirani1996}} (§§2.1–2.2, pp. 268–270)

The same construction can penalise a fitted function rather than a finite coefficient vector. In a smoothing spline, the integral of the squared second derivative charges for curvature while a data-fit term controls agreement with observations. A squared-weight penalty in a neural network instead charges for network parameters. These are different choices of what “complexity” means in a fitting problem.{{cite:reinsch1967}} (§§2–3, pp. 177–179){{cite:krogh_hertz1992}} (§1, eq. 1, p. 951)

## Interpretation
For $\lambda=0$, the objective is ordinary least squares. Increasing a positive $\lambda$ gives more influence to the penalty; the coefficient vector generally moves toward values favoured by that penalty, at the cost of a fit that may have a larger training residual. Ridge treats every direction smoothly, whereas the lasso's corner at zero can remove a predictor from the fitted equation.{{cite:hoerl_kennard1970}} (§§2–3, pp. 57–60){{cite:tibshirani1996}} (§§1–2.2, pp. 267–270)

If a predictor column is multiplied by $c\ne0$ and its coefficient divided by $c$, the fitted values stay the same but the coefficient penalty changes. Standardising columns before choosing a common penalty makes the tuning parameter more comparable across predictors; the transformations used for prediction must match those used at fitting.{{cite:tibshirani1996}} (§2.1, p. 268)

## Properties
For ridge with $\lambda>0$, the unique solution is $\widehat{\boldsymbol\beta}_{\mathrm{ridge}}=(\boldsymbol X^{\mathsf T}\boldsymbol X+\lambda I_p)^{-1}\boldsymbol X^{\mathsf T}\boldsymbol y$, where $I_p$ is the $p\times p$ identity matrix. The added positive diagonal makes the inverse exist even if the columns of $\boldsymbol X$ are dependent. The lasso objective is convex and always has at least one minimiser; its coefficient vector may not be unique with dependent columns, but its fitted response vector $\boldsymbol X\widehat{\boldsymbol\beta}$ is unique for squared-error loss.{{cite:hoerl_kennard1970}} (§2, eqs. 2.1–2.4, pp. 57–58){{cite:tibshirani1996}} (§2.1, pp. 268–269)

When $\boldsymbol X^{\mathsf T}\boldsymbol X=I_p$, write $z_j=(\boldsymbol X^{\mathsf T}\boldsymbol y)_j$ for the unpenalised coefficient in coordinate $j$. Ridge gives $\widehat\beta_j=z_j/(1+\lambda)$, while the lasso gives $\widehat\beta_j=\operatorname{sign}(z_j)(|z_j|-\lambda)_+$, where $(u)_+=\max(u,0)$. Thus ridge continuously scales each coordinate and the lasso sets it to zero when $|z_j|\le\lambda$.{{cite:tibshirani1996}} (§2.2, eqs. 3–4, pp. 269–270)

Under a normal response likelihood with fixed variance $\sigma^2$ and a centred normal coefficient prior with variance $\tau^2$, the posterior mode minimises a ridge objective with $\lambda=\sigma^2/\tau^2$ in the definition above. Independent centred Laplace priors with common scale $b$ instead produce a lasso objective with $\lambda=\sigma^2/b$. These identities concern a posterior *mode*; a full posterior also describes uncertainty over coefficient values.{{cite:tibshirani1996}} (§5, p. 277)

For plain gradient descent on $E(w)+\lambda\lVert w\rVert_2^2/2$, a step of size $\varepsilon$ multiplies the current weight vector $w$ by $1-\varepsilon\lambda$ before subtracting the data-loss gradient. An adaptive optimiser rescales gradient coordinates differently; adding an $L^2$ penalty to its gradient therefore need not equal a separate multiplicative weight-decay step.{{cite:krogh_hertz1992}} (§1, eqs. 1–2, p. 951){{cite:loshchilov_hutter2019}} (§2, Proposition 1 and eq. 1)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiating the ridge objective gives $\boldsymbol X^{\mathsf T}(\boldsymbol X\boldsymbol\beta-\boldsymbol y)+\lambda\boldsymbol\beta=0$. For nonzero $v$, $v^{\mathsf T}(\boldsymbol X^{\mathsf T}\boldsymbol X+\lambda I_p)v=\lVert\boldsymbol Xv\rVert_2^2+\lambda\lVert v\rVert_2^2>0$ when $\lambda>0$. The matrix is invertible and the stated ridge solution is unique. For the lasso, convexity and coercivity of $Q_\lambda$ when $\lambda>0$ give a minimiser. If two minimisers had distinct fitted vectors, their midpoint would have strictly smaller squared-error loss and no larger penalty, a contradiction. Coefficients may still differ along a null direction of $\boldsymbol X$.{{cite:hoerl_kennard1970}} (§2, eqs. 2.1–2.4, pp. 57–58){{cite:tibshirani1996}} (§2.1, pp. 268–269)

When $\boldsymbol X^{\mathsf T}\boldsymbol X=I_p$, complete the square to obtain $Q_\lambda(\boldsymbol\beta)=C+\sum_j\{(\beta_j-z_j)^2/2+\lambda P_j(\beta_j)\}$, where $C$ does not depend on $\boldsymbol\beta$. For ridge, $P_j(\beta_j)=\beta_j^2/2$ and the derivative gives $(1+\lambda)\beta_j-z_j=0$. For lasso, the subgradient condition is $0\in\beta_j-z_j+\lambda\partial|\beta_j|$: solving the positive, negative and zero cases gives the displayed soft-thresholding rule.{{cite:tibshirani1996}} (§2.2, eqs. 3–4, pp. 269–270)

For normal errors, minus the log likelihood contributes $\lVert\boldsymbol y-\boldsymbol X\boldsymbol\beta\rVert_2^2/(2\sigma^2)$ up to a constant. The centred normal prior contributes $\lVert\boldsymbol\beta\rVert_2^2/(2\tau^2)$; multiplying the sum by $\sigma^2$ gives ridge with $\lambda=\sigma^2/\tau^2$. A Laplace density proportional to $\exp(-|\beta_j|/b)$ contributes $\sum_j|\beta_j|/b$ and gives lasso with $\lambda=\sigma^2/b$. Finally, differentiating the squared-weight penalty gives $\lambda w$, so ordinary gradient descent yields $w^+=(1-\varepsilon\lambda)w-\varepsilon\nabla E(w)$. If an adaptive diagonal preconditioner $D$ scales the gradient, adding the penalty inside it yields $(I-\varepsilon\lambda D)w-\varepsilon D\nabla E(w)$; separate decay gives $(1-\varepsilon\lambda)w-\varepsilon D\nabla E(w)$. These differ when $D\ne I$.{{cite:tibshirani1996}} (§5, p. 277){{cite:krogh_hertz1992}} (§1, eqs. 1–2, p. 951){{cite:loshchilov_hutter2019}} (§2, Proposition 1 and eq. 1)
:::
:::

## Statistical use
Choose the penalty according to the task. Ridge can stabilise a fit with correlated predictors while retaining all of them; lasso can give a sparser description when coefficient selection matters. Standardise predictors within each training fold, tune $\lambda$ using validation or cross-validation data, and assess the selected procedure on observations that played no part in tuning. The best tuning value is tied to the chosen loss, preprocessing and target population.{{cite:hoerl_kennard1970}} (§§1–3, pp. 55–60){{cite:tibshirani1996}} (§§2.1, 4, 7.1, pp. 268–269, 273–280){{cite:cawley_talbot2010}} (§5.3, p. 2102)

A penalised coefficient is an estimate under the chosen criterion. For uncertainty intervals or claims about selected variables, account for the tuning and selection procedure rather than treating the fitted coefficients as if the procedure had been fixed in advance. Compare held-out predictions with an unpenalised fit when that comparison is feasible and scientifically relevant.{{cite:tibshirani1996}} (§§1, 4, pp. 267–268, 273–277){{cite:cawley_talbot2010}} (§§1, 5.3, pp. 2079–2081, 2102)

## Worked example
Take a centred two-coordinate problem with $\boldsymbol X=I_2$ and observed $\boldsymbol y=(3,0.5)^{\mathsf T}$. Ordinary least squares gives $(3,0.5)^{\mathsf T}$. Using $\lambda=1$ in the two objectives defined above, ridge gives $(3/2,0.5/2)^{\mathsf T}=(1.5,0.25)^{\mathsf T}$; lasso gives $(3-1,\max(0.5-1,0))^{\mathsf T}=(2,0)^{\mathsf T}$. The example shows continuous shrinkage beside an exact zero. Equal numerical values of $\lambda$ in these two different penalty formulas do not represent equal effective complexity.{{cite:tibshirani1996}} (§2.2, eqs. 3–4, pp. 269–270)

**Your turn.** With $\boldsymbol X=I_2$, $\boldsymbol y=(2,0.5)^{\mathsf T}$, and $\lambda=1$ in the same objectives, find the ridge and lasso estimates.

::: {.callout-tip collapse="true" title="Answer"}
Ridge divides both coordinates by $2$, giving $(1,0.25)^{\mathsf T}$. Lasso soft-thresholds each coordinate by $1$, giving $(1,0)^{\mathsf T}$.
:::

## Assumptions and limits
Penalties depend on parameterisation and predictor scale. A coefficient that becomes small after standardisation may not look small in the original units, and changing one input's units without refitting the penalty changes the estimator. The lasso can select one of several correlated predictors, so a zero coefficient is not evidence that its underlying measurement is scientifically irrelevant.{{cite:hoerl_kennard1970}} (§§1–2, pp. 55–58){{cite:tibshirani1996}} (§§1–2.2, pp. 267–270)

Weight decay also depends on the optimiser. A squared-weight penalty and a multiplicative decay can be matched for ordinary stochastic gradient descent after accounting for its learning rate, while an adaptive method such as Adam generally needs a separate decay step to reproduce that operation.{{cite:loshchilov_hutter2019}} (Abstract; §2, Proposition 1 and eq. 1)

## Connections
[Ridge regression](ridge-regression.qmd) is the squared-coefficient special case, while the [lasso](lasso.qmd) uses absolute coefficients and can threshold them to zero. [Weight decay](regularisation-and-weight-decay.qmd) applies a squared-weight penalty to a network under ordinary gradient descent; a [smoothing spline](cubic-smoothing-spline.qmd) instead penalises curvature of a fitted function. A [maximum a posteriori estimate](maximum-a-posteriori-estimate.qmd) connects these penalties to the modes of specified coefficient priors. [Principal components](../notes/sl-03-principal-components.qmd) reduce the input representation, and a [hypothesis test](../notes/inf-04-hypothesis-tests.qmd) addresses a different inferential question.{{cite:hoerl_kennard1970}} (§§1–2, pp. 55–58){{cite:tibshirani1996}} (§§2.1–2.2, 5, pp. 268–270, 277){{cite:krogh_hertz1992}} (§1, p. 951){{cite:reinsch1967}} (§§2–3, pp. 177–179)

## History
Reinsch's 1967 spline paper formulated smoothing as a trade-off between fit to approximate observations and a bound on curve roughness. Hoerl and Kennard's 1970 ridge paper addressed unstable coefficient estimates with correlated regression columns by adding positive values to the diagonal of the normal-equation matrix. Their examples showed how a little bias could reduce mean squared error.{{cite:reinsch1967}} (§§1–3, pp. 177–179){{cite:hoerl_kennard1970}} (§§1–3, pp. 55–60)

Krogh and Hertz analysed squared-weight decay in neural networks in work published in *Advances in Neural Information Processing Systems* volume 4. Tibshirani introduced the lasso in 1996 to combine coefficient shrinkage with variable selection and described its Laplace-prior posterior-mode interpretation. Loshchilov and Hutter's 2019 paper later separated adaptive-optimiser weight decay from an $L^2$ gradient penalty.{{cite:krogh_hertz1992}} (Abstract and §1, pp. 950–951){{cite:tibshirani1996}} (Summary, §§1, 5, pp. 267–268, 277){{cite:loshchilov_hutter2019}} (Abstract and §2, pp. 1–2)
