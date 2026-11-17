## Lead context
A sum of smooth functions lets each covariate bend on its own, and the linear predictor adds those bends instead of fitting one surface in all of the covariates at once.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## Motivating example
Suppose a log mean depends on a dose $x\in\{0,1\}$ and a setting $z\in\{0,1\}$. An additive fit gives each its own centred smooth. Take $g_1(0)=-0.3$, $g_1(1)=0.3$, $g_2(0)=-0.5$, $g_2(1)=0.5$ and intercept $1$. The four log means are $0.2$, $1.2$, $0.8$ and $1.8$. Moving $x$ from $0$ to $1$ adds $0.6$ at both values of $z$. If the corner $(1,1)$ is actually $2.4$, that common difference has failed: the dose effect is larger when $z=1$.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## Intuition
A free function of several covariates can follow every bump the sample happens to have, and it spends parameters on combinations that were barely observed. An additive model refuses those combinations. Each smooth is a function of one covariate, centred so that it does not trade a constant with the intercept, and the penalty on each smooth limits how wiggly that function may be. The default constraint makes each smooth sum to zero over the observed values of its covariate.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## Definition
`gam` fits a generalised linear model whose linear predictor is a sum of smooth functions of covariates plus an ordinary parametric piece. A Poisson illustration is $\log\mu_i=\beta_0+f_1(x_{i1})+f_2(x_{i2})$. The smooths are penalised regression splines. The basis dimension $k$ is an upper scale for the smooth; the effective degrees of freedom are then controlled by the penalty, with a usual upper limit of $k-1$.

## Interpretation
In the four-corner table the dose contrast is $0.6$ at $z=0$ and $0.6$ at $z=1$. That equality is additivity. The interaction contrast is
\[
\bigl(\eta(1,1)-\eta(1,0)\bigr)-\bigl(\eta(0,1)-\eta(0,0)\bigr)=0
\]
for the additive table, because both dose contrasts equal $0.6$. For a corner of $2.4$ instead of $1.8$ the contrast is $2.4-0.8-1.2+0.2=0.6$. Additivity is exactly the statement that this contrast is zero.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

Centring matters for the intercept. Adding $3$ to $g_1$ and subtracting $3$ from the intercept leaves every $\eta$ unchanged. The sum-to-zero constraint picks one of those representations. Without it the intercept and the smooths are not separately readable.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## Properties
The penalty is separate for each smooth. Nothing in the sum forces $g_1$ and $g_2$ to be equally wiggly. A basis with $k=4$ has a usual effective-degrees-of-freedom ceiling of $3$. A fitted smooth whose penalty drives it to a straight line uses fewer degrees of freedom than that ceiling. Setting the ceiling below the bend you need, by choosing $k$ too small, is a different failure: the penalty cannot recover a shape the basis cannot represent.

The fitting iteration is penalised iteratively reweighted least squares. Smoothing parameters may be chosen by generalised cross-validation or by REML, among other listed criteria. The choice is part of the fit. It is not a property of the additive formula alone.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $\eta(x,z)=\beta_0+g_1(x)+g_2(z)$. Then
\[
\eta(1,1)-\eta(1,0)-\eta(0,1)+\eta(0,0)
=g_1(1)-g_1(1)-g_1(0)+g_1(0)+g_2(1)-g_2(0)-g_2(1)+g_2(0)=0.
\]
The intercept cancels. Any table with a nonzero value of that contrast is not of the additive form. For the numbers $-0.3,0.3$ and $-0.5,0.5$ with intercept $1$, the four values are $0.2,1.2,0.8,1.8$ and the contrast is zero. Replacing $1.8$ by $2.4$ makes the contrast $0.6$.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

Adding a constant $c$ to $g_1$ and subtracting $c$ from $\beta_0$ does not change $\eta$. The sum-to-zero constraint $g_1(0)+g_1(1)=0$ when each corner is observed once forces $c=0$ in that trade.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)
:::
:::

## Statistical use — Read one smooth with the others held fixed
A plot of $g_1$ is the change in the linear predictor as its covariate moves, at a fixed value of the other smooths. In the table, that change is $0.6$ whether $z$ is $0$ or $1$. The sentence is conditional on $z$. It is not the change in a probability or in a mean until the link is applied. On the log link, a change of $0.6$ multiplies the mean by $e^{0.6}\approx 1.8221$ at either value of $z$. The corner $2.4$ would multiply the mean, relative to $(0,0)$, by $e^{2.4}\approx 11.0232$, whereas the additive corner $1.8$ multiplies it by $e^{1.8}\approx 6.0496$.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

The contrast calculation shows a corner of $2.4$ is not additive. Forcing additivity there leaves a residual of $0.6$ on the link scale at that corner and fits the other three corners only by compromising. A tensor-product smooth of $(x,z)$ can represent the corner and spends parameters on the interaction. That construction is distinct from a sum of one-dimensional smooths. Centring over the observed values also depends on the design: a smooth centred on a sample that never saw $x=1$ is not centred on a future population that is mostly $x=1$.

## Worked example
Intercept $1$, $g_1(0)=-0.3$, $g_1(1)=0.3$, $g_2(0)=-0.5$, $g_2(1)=0.5$.

| $x$ | $z$ | $\eta$ |
|---:|---:|---:|
| 0 | 0 | 0.2 |
| 0 | 1 | 1.2 |
| 1 | 0 | 0.8 |
| 1 | 1 | 1.8 |

The dose contrasts are $0.8-0.2=0.6$ and $1.8-1.2=0.6$. The interaction contrast is $0$. A basis ceiling $k-1=3$ for $k=4$ says a smooth in this fit cannot spend more than three effective degrees of freedom, however small its penalty. The four-corner step function above is already a very small smooth; the ceiling matters when the covariate is continuous and $k$ is set below the bend.

**Your turn.** Use the same centred smooths and change the intercept to $0$. What is $\eta(1,1)$?

::: {.callout-tip collapse="true" title="Answer"}
$0+0.3+0.5=0.8$. The interaction contrast is still zero. Only the level moved.
:::

## Common misconceptions
Additivity is not the absence of a covariate. Both covariates are in the model. What is absent is a term that depends on them jointly.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

The effective degrees of freedom are not $k$. The basis size $k$ is a ceiling. The penalty chooses a smaller value, up to the usual limit $k-1$.

A smooth plotted on the link scale is not a change in the mean. The factor $e^{0.6}\approx 1.8221$ is the mean ratio for a log link. The number $0.6$ itself is a change in $\eta$.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## Connections
A [generalised linear model](generalised-linear-model.qmd) is the case with no smooths, or with smooths reduced to linear terms. [Fisher scoring](fisher-scoring.qmd) is the unpenalised cousin of the penalised iteratively reweighted least squares used here. A [log link](log-link.qmd) turns the additive $0.6$ into the mean ratio $e^{0.6}$.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## History
`gam` fits a generalised linear model whose linear predictor is a sum of smooth functions plus a parametric component, with the smooths penalised and, by default, centred on the observed covariates. This implementation differs from Hastie's `gam` and lists tensor-product terms for smooth interactions, which are exactly the non-additive extension the corner contrast detects.
