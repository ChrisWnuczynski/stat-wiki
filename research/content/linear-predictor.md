## Lead context
It is the systematic part of a model: a coefficient multiplies each chosen input column, and a link converts their sum to a mean on the response scale. This structure lets the same input design describe counts, binary outcomes, and continuous measurements while giving coefficients meanings appropriate to each link. “Linear” refers to the coefficients after columns have been built; a column may itself be a transformation or interaction of raw inputs.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Motivating example
A model for a species count can include lake distance and the logarithm of lake area. Its predictor adds the intercept, a distance term, and a log-area term. A Poisson model with log link then exponentiates that sum to obtain a positive expected count. The response count is not logarithmically transformed; the model links its *mean* to the predictor.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Intuition
The predictor is a bookkeeping device for how inputs contribute before the mean is brought back to its natural scale. A positive coefficient raises the predictor when its column rises, holding the other columns fixed. Whether that means an additive change in a mean, a multiplier of a mean, or a multiplier of odds depends on the chosen link. If an interaction column is included, the effect of one raw input can vary with another even though the sum remains linear in its coefficients.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Definition
For observation $i$, let $Y_i$ be the random response, $\mu_i=\mathbb E(Y_i\mid\mathbf x_i)$ its conditional mean, and $\mathbf x_i=(1,x_{i1},\ldots,x_{ip})^\top$ a column of specified covariate values including an intercept. With coefficient vector $\boldsymbol\beta=(\beta_0,\beta_1,\ldots,\beta_p)^\top$, the **linear predictor** is

$$
\eta_i=\mathbf x_i^\top\boldsymbol\beta
=\beta_0+\sum_{j=1}^{p}x_{ij}\beta_j,
\qquad g(\mu_i)=\eta_i.
$$

Here $\eta_i$ is the predictor on the *link scale*, $g$ is the chosen [link function](link-function.qmd), and $\mathbf x_i^\top$ is the transpose of the covariate column. The inputs may be observed measurements, indicator columns for factor levels, or predetermined transformations such as $\log A_i$ for a positive area $A_i$. Once these columns are fixed, the expression is linear in $\boldsymbol\beta$. It need not be linear in each raw measurement. An optional offset $o_i$ is added as $\eta_i=o_i+\mathbf x_i^\top\boldsymbol\beta$ with its coefficient fixed at one, rather than estimated.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

The predictor is only one part of a [generalised linear model](generalised-linear-model.qmd). The model also specifies a distribution for $Y_i$ and a link connecting its mean to $\eta_i$. The same numerical $\eta_i$ can therefore correspond to different means under different links. A conventional normal identity-link model has $\mu_i=\eta_i$; a log-link model has $\mu_i=e^{\eta_i}>0$; a Bernoulli logit model has $\mu_i=e^{\eta_i}/(1+e^{\eta_i})\in(0,1)$. None of these choices follows solely from writing the linear predictor.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Properties
Holding all other columns fixed, increasing $x_{ij}$ by $\Delta$ changes $\eta_i$ by $\beta_j\Delta$, provided the other columns really stay fixed. For a log link, the corresponding mean ratio is $e^{\beta_j\Delta}$; for a logit link, the conditional *odds* ratio is $e^{\beta_j\Delta}$. Under the identity link, the mean difference is $\beta_j\Delta$. These are exact model-based comparisons, but a logit coefficient is not itself a probability difference.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

If a binary indicator $z$ and a continuous input $x$ enter as $\eta=\beta_0+\beta_xx+\beta_zz+\beta_{xz}xz$, the change in predictor for one unit of $x$ at fixed $z$ is $\beta_x+\beta_{xz}z$. The group difference at fixed $x$ is $\beta_z+\beta_{xz}x$. These formulas give the conditional comparison: each comparison must specify what is held fixed. It also shows why a product column is compatible with a linear predictor.{{cite:nelder_wedderburn1972}} (§1.2, p. 372)

With a Poisson log link and an exposure $t_i>0$, an offset $\log t_i$ gives $\mu_i=t_i\exp(\mathbf x_i^\top\boldsymbol\beta)$. This models a count as exposure times an event rate. Treating $\log t_i$ as an ordinary column instead would estimate its coefficient and permit a different exposure dependence; the distinction is substantive.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
From $\eta_i=\beta_0+\sum_jx_{ij}\beta_j$, changing just column $j$ by $\Delta$ subtracts the old sum from the new and leaves $\beta_j\Delta$. Under the identity link $\mu=\eta$, so the mean difference is the same. Under the log link $\mu=e^\eta$, the new-to-old mean ratio is $e^{\eta+\beta_j\Delta}/e^\eta=e^{\beta_j\Delta}$. Under the logit link $\log\{\mu/(1-\mu)\}=\eta$, so the odds ratio for the same predictor change is again $e^{\beta_j\Delta}$. The inverse logit is obtained by solving $\mu/(1-\mu)=e^\eta$, giving $\mu=e^\eta/(1+e^\eta)$.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

For the interaction, substitute $x+\Delta$ for $x$: $\eta(x+\Delta,z)-\eta(x,z)=\Delta(\beta_x+\beta_{xz}z)$. Similarly $\eta(x,1)-\eta(x,0)=\beta_z+\beta_{xz}x$. These differences prove the two conditional comparisons, including the slope calculation when $\beta_x=0.2$ and $\beta_{xz}=0.1$. They also show that the predictor remains linear in the four coefficients even though $xz$ is a product of inputs.{{cite:nelder_wedderburn1972}} (§1.2, p. 372)

For an exposure offset, insert $o_i=\log t_i$ into $\log\mu_i=o_i+\mathbf x_i^\top\boldsymbol\beta$ and exponentiate: $\mu_i=\exp(\log t_i)\exp(\mathbf x_i^\top\boldsymbol\beta)=t_i\exp(\mathbf x_i^\top\boldsymbol\beta)$. The coefficient of $\log t_i$ is therefore exactly one by construction.{{cite:nelder_wedderburn1972}} (§1.2, p. 372)
:::
:::

## Statistical use
Construct the design columns before fitting, record their units and reference levels, and state the response distribution and link. For a log link, a one-unit input change must say which unit; rescaling kilometres to metres changes the numerical coefficient. For a factor, report the reference category so an indicator coefficient has a defined comparison. For an interaction, calculate contrasts at named values of the other input instead of giving one unconditional slope.{{cite:nelder_wedderburn1972}} (§1.2, p. 372)

Fitting the model estimates $\boldsymbol\beta$ under the stated response law and link. Nelder and Wedderburn derived iterative weighted linear regression for maximum-likelihood fitting. The fitted $\eta_i$ is on the link scale; applying the inverse link gives the fitted mean $\mu_i$. With a log link the mean stays positive, and with a logit link it stays between zero and one. Report the response family, link, and scale of each fitted value.{{cite:nelder_wedderburn1972}} (§§1.3–2, pp. 372–376)

## Worked example
Suppose a fitted Bernoulli logit model for a binary response uses $\eta=-2+0.5x$, where $x$ is a measured covariate. At $x=2$, $\eta=-1$, the odds are $e^{-1}\approx0.368$, and the response probability is $1/(1+e)\approx0.269$. At $x=4$, $\eta=0$, the odds are $1$ and the probability is $1/2$. The two-unit increase in $x$ multiplies odds by $e^{0.5(2)}=e\approx2.718$, while the probability rises by about $0.231$, not by a fixed amount of $e$. The interpretation is conditional on the specified covariates and logit model.{{cite:berkson1944}} (p. 358){{cite:cox1958_logistic}} (Summary; reproduced excerpt, p. 216){{cite:nelder_wedderburn1972}} (§3.3, p. 379)

**Your turn.** In the same fitted model, find the predictor and response probability at $x=0$.

::: {.callout-tip collapse="true" title="Answer"}
The predictor is $\eta=-2$. The fitted probability is $e^{-2}/(1+e^{-2})=1/(1+e^2)\approx0.119$. The intercept is a log-odds value, not a negative probability.{{cite:berkson1944}} (p. 358)
:::

## Common misconceptions
“Linear” does not forbid squared inputs, logarithms, indicators, or interactions among inputs; it describes linearity in the chosen coefficients. A coefficient's effect on the predictor scale is not automatically an effect on probability or mean. The predictor is not the random error term and does not alone specify the distribution of $Y_i$. An offset has a fixed coefficient, so using it makes a stronger modelling assumption than estimating an ordinary covariate effect. In a model with an interaction, a main-effect coefficient describes the comparison at the other variable's reference value, not at every value.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Assumptions and limits
The algebra of $\mathbf x_i^\top\boldsymbol\beta$ is valid for any fixed design columns. The interpretations above additionally assume the stated link, correctly coded inputs, and a comparison holding the other columns fixed. A comparison holding one column fixed needs care when another column is a product that changes with it. Linearly dependent columns cannot identify separate coefficients, so reference-level coding and model constraints matter. The GLM definition here assumes independent responses from the stated exponential family; a correlated-response model needs an explicit dependence structure.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Connections
A [link function](link-function.qmd) maps the mean to the predictor; the [log link](log-link.qmd) turns predictor differences into mean ratios, and the [logit link](logit-link.qmd) turns them into odds ratios. An [interaction](interaction.qmd) adds a product column so one slope changes with another input. A [generalised linear model](generalised-linear-model.qmd) combines this systematic part with a response distribution, whereas an [identity link](identity-link.qmd) makes the predictor itself the mean. The chosen columns and link together determine the meaning of each coefficient and the scale on which a fitted change is reported.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## History
Nelder and Wedderburn's 1972 paper brought together models for normal, binomial, Poisson, and gamma responses by separating a random component, a linear model for systematic effects, and a linking function. Their §1.2 restricted the linear model to systematic effects and described quantitative variables, indicator columns for qualitative factors, and mixed columns. The motivation was a unified likelihood-based fitting procedure for models that had previously been handled through several separate techniques.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–1.3, pp. 370–373)

The paper then derived an iterative weighted least-squares procedure for fitting the model coefficients. Its worked models show how the predictor and link combine for different response families: an additive mean under an identity link, a positive mean under a log link, and odds under a logit link.{{cite:nelder_wedderburn1972}} (§§2–3, pp. 373–381)
