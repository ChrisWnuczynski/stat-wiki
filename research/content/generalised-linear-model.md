## Lead context
One regression specifies a response distribution, a linear predictor and a link. The same columns can then describe a count, a binary outcome or a continuous measurement, because the distribution, not a transformation of the data, determines which values are possible. The link is applied to the conditional mean, so the recorded responses stay on their original scale.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–1.3, pp. 370–373) {{cite:sas2012_glm}} (Ch. 3, “Generalized Linear Models”)

## Motivating example — A count and a presence can share the same columns
For a lake's species count, distance from the coast and log area can be columns in a predictor. A Poisson response with a log link turns that predictor into a positive expected count. A binary question about whether a lake has a particular species could use the same input columns with a Bernoulli response and logit link; its fitted mean would then be a probability. The response type and link change the meaning of a coefficient.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, 3.2–3.3, pp. 372–373, 377–380)

## Definition — Response law, predictor, and link
Write $\mathbf x_i=(1,x_{i1},\ldots,x_{id})^\top$ for the chosen covariate column of observation $i$, including an intercept, and $\boldsymbol\beta=(\beta_0,\ldots,\beta_d)^\top$ for its coefficients. Let $Y_i$ be the random response and $y_i$ a realised value. Its conditional mean is $\mu_i=\mathbb E(Y_i\mid\mathbf x_i)$, and the linear predictor is $\eta_i=\mathbf x_i^\top\boldsymbol\beta$. A monotone, invertible link $g$ satisfies $g(\mu_i)=\eta_i$. Conditional on the specified covariates, the responses have independent exponential-family distributions; their means can differ. The distribution, design columns and link together specify the model.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–373) {{cite:sas2012_glm}} (Ch. 3, “Generalized Linear Models”)

The exponential-family convention used for the mean and variance is

$$
f(y_i;\theta_i,\phi)=\exp\left\{\frac{y_i\theta_i+c(\theta_i)}{e(\phi)}+d(y_i;\phi)\right\}.
$$


Here $f$ is a density or mass function, $\theta_i$ is its natural parameter, $\phi$ is a common dispersion parameter, $e(\phi)>0$ is its scale, $c$ contains the parameter-only part, and $d$ contains terms not involving $\theta_i$. In this sign convention, $\mu_i=-c'(\theta_i)$ and $\operatorname{Var}(Y_i\mid\mathbf x_i)=-c''(\theta_i)e(\phi)$ when differentiation under the integral or sum is valid. The more usual convention writes $y_i\theta_i-b(\theta_i)$; it is equivalent on setting $b=-c$. The link is *canonical* when $\eta_i$ equals the natural parameter after that parameter has been expressed as a function of the mean.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–373)

## Interpretation — What “linear” and the link each control
The distribution describes which response values are possible and how they vary around $\mu_i$; the design columns say which inputs enter; and the link states the scale on which their effects add. For a normal identity-link model, $\mu_i=\eta_i$. For a Poisson log-link model, $\mu_i=e^{\eta_i}>0$. For a Bernoulli logit model, $\mu_i=e^{\eta_i}/(1+e^{\eta_i})$ is a probability. Thus the same number on the predictor scale can represent different fitted means.{{cite:nelder_wedderburn1972}} (§§3.1–3.3, pp. 376–380)

“Linear” describes the coefficient sum after the columns are chosen. A column may contain a logarithm, indicator or interaction of raw measurements. In the lake example, $\log A_i$ is a transformed input for positive area $A_i$; it is distinct from the log link on the mean. A covariate transformation and a link answer different modelling questions.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, pp. 372–373)

## Properties — Mean–variance ties and coefficient scales
Under the canonical form above, the mean is $-c'(\theta_i)$ and the conditional variance is $-c''(\theta_i)e(\phi)$. This ties a response family's variance to its mean. A Poisson member has equal conditional mean and variance, while a Bernoulli member with success probability $p_i$ has mean $p_i$ and variance $p_i(1-p_i)$. A normal member with common variance $\sigma^2$ has variance $\sigma^2$ at every mean. These are model assumptions to assess against the data, not consequences of writing a linear predictor alone.{{cite:nelder_wedderburn1972}} (§§1.1, 3.1–3.3, pp. 371, 376–380)

For a log link with a one-unit change in a column $x_{ij}$ while all other columns are fixed, the fitted mean is multiplied by $e^{\beta_j}$. For a logit link on a Bernoulli mean, the fitted *odds* are multiplied by $e^{\beta_j}$ instead. The probability change in the second case depends on the starting probability. A link need not be canonical: the binomial family, for example, permits a probit link as well as a logit link.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, 3.3, pp. 372–373, 379–380)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Because $f$ integrates or sums to one, differentiating its normalisation with respect to $\theta$ gives $0=\mathbb E[(Y+c'(\theta))/e(\phi)]$. Therefore $\mathbb EY=-c'(\theta)$. Differentiating again gives $0=c''(\theta)+\mathbb E[(Y+c'(\theta))^2]/e(\phi)$, so $\operatorname{Var}(Y)=-c''(\theta)e(\phi)$. These steps require the differentiation and integration or summation to be interchanged.{{cite:nelder_wedderburn1972}} (§1.1, p. 371)

For a normal mean, use $c(\theta)=-\theta^2/2$ and $e(\phi)=\sigma^2$; the formulas give mean $\theta$ and variance $\sigma^2$. For Poisson, $c(\theta)=-e^\theta$ and $e(\phi)=1$, giving mean and variance $e^\theta$. For Bernoulli, $c(\theta)=-\log(1+e^\theta)$ and $e(\phi)=1$. Its mean is $p=e^\theta/(1+e^\theta)$, and differentiating again gives variance $p(1-p)$. These substitutions prove the three family examples.{{cite:nelder_wedderburn1972}} (§§1.1, 3.1–3.3, pp. 371, 376–380)

Under a log link, $\mu=e^\eta$; replacing $\eta$ by $\eta+\beta_j$ gives the mean ratio $e^{\eta+\beta_j}/e^\eta=e^{\beta_j}$. Under a logit link, $\mu/(1-\mu)=e^\eta$, so the same replacement gives an odds ratio $e^{\beta_j}$. This proves the two coefficient interpretations under the stated fixed-column comparison.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, 3.3, pp. 372–373, 379–380)
:::
:::

## Statistical use — Fit on the link scale, report on the response scale
Begin with the unit and support of the response. A count can motivate a Poisson model; a zero-or-one response can motivate Bernoulli regression; a roughly symmetric continuous measurement can motivate a normal model. State the link and any input transformations separately. Fit the coefficients by maximum likelihood when the specified distribution supplies a likelihood; Nelder and Wedderburn showed that the score equations can be solved by iterative weighted least squares.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374) {{cite:sas2012_glm}} (Ch. 3, “Generalized Linear Models”)

After fitting, report fitted means on the response scale as well as coefficients on the link scale. Compare the observed response pattern with what the chosen variance function predicts. The deviance compares a fitted model's likelihood with a more flexible benchmark, but its interpretation depends on the sampling model and dispersion; a small coefficient standard error alone cannot establish a good fit. The lake example below contrasts a linear latitude term with a smoother one to examine structure left in the fitted mean.{{cite:nelder_wedderburn1972}} (§§2.3–2.4, pp. 375–376)

## Worked example — The same predictor under Poisson and Bernoulli
Consider two possible models using the predictor $\eta=\log 2+x\log 3$, where $x=0$ or $1$ is a realised input. If the response is Poisson with a log link, the expected count is $e^\eta$: it is $2$ at $x=0$ and $6$ at $x=1$. The mean ratio is $6/2=3$. If the response instead records a zero-or-one outcome with a Bernoulli logit link, the odds are $e^\eta$, equal to $2$ and $6$, while the probabilities are $2/(1+2)=2/3$ and $6/(1+6)=6/7$. The odds ratio is $6/2=3$, but the probability difference is $6/7-2/3=4/21\approx0.1905$. The two models share a predictor and differ in their response law and link.{{cite:nelder_wedderburn1972}} (§§3.2–3.3, pp. 377–380)

At $x=2$, the same predictor is $\log18$. The Poisson expected count is $18$; the Bernoulli probability is $18/19\approx0.9474$. Each additional unit of $x$ multiplies the Poisson mean or the Bernoulli odds by $3$, with different consequences on the response scales.{{cite:nelder_wedderburn1972}} (§§3.2–3.3, pp. 377–380)

**Your turn.** For the same predictor $\eta=\log2+x\log3$, find the Poisson mean and Bernoulli success probability when $x=-1$.

::: {.callout-tip collapse="true" title="Answer"}
Now $e^\eta=2/3$. The Poisson mean is $2/3$, while the Bernoulli odds are $2/3$ and its success probability is $(2/3)/(1+2/3)=2/5$.
:::

## Common misconceptions — The link transforms the mean, not the raw response
A link transforms the *mean*, not each observed response. Logging a predictor such as lake area is also separate from choosing a log link. The word “linear” permits transformed columns and interactions while requiring an additive coefficient sum in the chosen columns. A canonical link is a mathematical match to the exponential-family parameter; another permitted link may suit the response question better.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, 3.3, pp. 372–373, 379–380) {{cite:sas2012_glm}} (Ch. 3, “Generalized Linear Models”)

## Assumptions and limits — Independence and the family’s variance claim
The independence assumption concerns responses conditional on their specified covariates. A Poisson GLM's equality of mean and variance, or a Bernoulli GLM's mean–variance relation, is part of its chosen response model. Dependence among observations, unmodelled heterogeneity or an unsuitable mean function can make model-based standard errors and comparisons unreliable. Examine whether the fitted relation and spread are credible for the population and measurement process.{{cite:nelder_wedderburn1972}} (§§1.1, 2.3, pp. 371, 375–376) {{cite:sas2012_glm}} (Ch. 3, “Generalized Linear Models”)

## Connections — The link sets the scale of a coefficient
A coefficient is a change in the [linear predictor](linear-predictor.qmd). The [link function](link-function.qmd) decides what that change means for the conditional mean: an additive shift under the identity, a multiplicative shift under the log, and a shift in log odds under the logit. [Binary logistic regression](binary-logistic-regression.qmd) and [Poisson regression](poisson-regression.qmd) are the Bernoulli and count cases of that construction. [Deviance](deviance.qmd) then compares the likelihood of a fitted model with the likelihood of a saturated benchmark, on the scale fixed by the chosen distribution.{{cite:nelder_wedderburn1972}} (§§1.2–2.4, pp. 372–376)

## History — Nelder and Wedderburn, 1972
Nelder and Wedderburn's 1972 paper put normal, binomial, Poisson and gamma models into a common exponential-family and link-function framework. Their aim was a unified likelihood-based fitting method for responses whose distributions and systematic effects had previously been handled with separate techniques. They derived an iterative weighted regression algorithm and extended analysis of variance through differences in deviance.{{cite:nelder_wedderburn1972}} (Summary; Introduction; §§2.1–2.4, pp. 370–376)

The 2012 *SAS/STAT User's Guide* presents generalised linear models as a standard approach to nonnormal responses and contrasts linking the mean with transforming the observed data. It places normal linear, logistic and other response models under the same three-part construction, reflecting the framework's later use in statistical software.{{cite:sas2012_glm}} (Ch. 3, “Generalized Linear Models”)
