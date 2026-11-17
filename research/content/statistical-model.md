## Lead context
Data are particular. A statistical model is the general description that relates them: a mathematical statement connecting the variables, with a random piece that says the relation is not exact. {{cite:nist_glossary2002}} (Glossary, "model") {{cite:dodge2008}} (p. 353)

## Motivating example
The cost of a share purchase can fall exactly on a straight line when the price per share is fixed, as with twelve simultaneous orders for one stock. Family income and the financial aid a college offers do not. Income says something about aid, and other facts say something too. A line plus a remainder is the model for the second situation. The exact line was the model for the first. {{cite:openintro2019}} (p. 305)

## Intuition
Separate what is observed from what is fixed and unknown. The variables are the observable pieces. The parameters are the fixed, generally unknown, quantities that tie the variables together. A deterministic model says the tie is exact. A stochastic model says a random error remains. {{cite:dodge2008}} (p. 353) {{cite:dodge2008}} (p. 354)

## Definition
A model is a theoretical representation of a real situation, built from mathematical symbols. Given observations and hypotheses, it aims at the best description of the phenomenon that those hypotheses allow. It contains observable variables and parameters. {{cite:dodge2008}} (p. 353)

A statistical model predicts a measured quantity. A probability model predicts the relative frequency of random outcomes. A model can have both parts. {{cite:nist_glossary2002}} (Glossary, "model")

A stochastic model for a response \(Y\) and explanatory variables \(X_1, \ldots, X_p\) has the form
\[
Y = f(X_1, \ldots, X_p \mid \beta_0, \ldots, \beta_{p-1}) + \varepsilon,
\]
where the \(\beta_j\) are parameters to be estimated and \(\varepsilon\) is an unobservable random error. Linearity refers to the coefficients. The equation \(Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \varepsilon\) is linear of the second order even though \(X\) is squared. The straight line \(Y = \beta_0 + \beta_1 X\) is the deterministic special case with no error term written. {{cite:dodge2008}} (p. 354)

In the same notation, linear regression writes \(y = \beta_0 + \beta_1 x + \varepsilon\). The point estimates of the coefficients are written \(b_0\) and \(b_1\). {{cite:openintro2019}} (p. 305)

## Properties
The response, also called the endogenous variable, is the \(Y\) being expressed. The explanatory variables are the \(X_j\). {{cite:dodge2008}} (p. 354) The error \(\varepsilon\) is what keeps the relation from being exact. A residual, after fitting, is the difference between the estimated value and the observed value. {{cite:dodge2008}} (p. 183)

Discrete models are also classed by the factors. A fixed-effect model uses factors whose levels are the finite set written into the design. A variable-effect model uses levels that were drawn at random from a larger set of possible levels. A mixed-effect model contains both. {{cite:dodge2008}} (p. 354) {{cite:dodge2008}} (p. 355)

Uncertainty about a conclusion has two contributions that the model makes explicit: the error in the observations, and the fact that the model itself is not perfect. {{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Statistical use
The model states the relation one is willing to estimate. For a line, the data produce \(b_0\) and \(b_1\), and the fitted line is used to describe or predict the average response. The error term is often dropped from the written prediction because the target is that average, not a new individual remainder. {{cite:openintro2019}} (p. 305) A residual plot then asks whether the line left a pattern behind. Curvature in the residuals means the straight line was the wrong model. {{cite:openintro2019}} (p. 310)

In a causal analysis the model is a device for estimation. It does not by itself supply the conditions under which a coefficient is an average treatment effect. {{cite:hernan_robins2020}} (p. 5) {{cite:openintro2019}} (p. 32)

## Worked example
Three points \((x, y)\) are \((1, 5)\), \((2, 8)\), and \((3, 11)\). The line \(y = 2 + 3x\) gives \(2 + 3 \times 1 = 5\), \(2 + 3 \times 2 = 8\), and \(2 + 3 \times 3 = 11\). Every residual is 0. The statistical model with an error term is \(Y = 2 + 3X + \varepsilon\) with \(\varepsilon = 0\) at these three points. A fourth point at \(x = 4\) has fitted value \(2 + 3 \times 4 = 14\). {{cite:openintro2019}} (p. 305) {{cite:dodge2008}} (p. 354)

**Your turn.** The fourth point is observed as \(y = 16\), not 14. What is the residual from the line \(y = 2 + 3x\)?

::: {.callout-tip collapse="true" title="Answer"}
The fitted value is 14. The residual is \(16 - 14 = 2\).
:::

## Common misconceptions
A fitted line is not a law the points had to obey. It is an estimate of a stated relation, and the residuals are the part the relation did not capture. {{cite:openintro2019}} (p. 305) {{cite:dodge2008}} (p. 354)

Squaring \(X\) does not make the model nonlinear. Nonlinearity is about the way the coefficients enter. \(Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \varepsilon\) is linear in \((\beta_0, \beta_1, \beta_2)\). {{cite:dodge2008}} (p. 354)

A model of an observational association is not, by being written with a coefficient, a model of a causal effect. {{cite:openintro2019}} (p. 25) {{cite:hernan_robins2020}} (p. 5)

## Assumptions and limits
The representation is only as good as the hypotheses built into \(f\) and into the behaviour of \(\varepsilon\). A straight line leaves curvature behind when the relation bends, and the residual plot is the warning. {{cite:openintro2019}} (p. 310) Parameters are features of the model, not variables of the units. {{cite:dodge2008}} (p. 353) Using an imperfect model is itself a source of uncertainty, alongside the observational error. {{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Connections
The [response variable](response-variable.qmd) is \(Y\) and the [explanatory variable](explanatory-variable.qmd) is \(X\). [Correlation](correlation.qmd) describes the linear association without writing the line. The [bias of an estimator](bias-of-an-estimator.qmd) is about the estimates \(b_0\) and \(b_1\), not about the model equation. [Measurement error](measurement-error.qmd) is one reason \(\varepsilon\) is not zero. A causal contrast such as the [average treatment effect](average-treatment-effect.qmd) is a target a model may be used to estimate, under conditions the equation does not state.

## History
The word model, for a mathematical representation fitted to observations, is traced to three eighteenth-century astronomical problems: the inequality in the motions of Jupiter and Saturn, the motion of the Moon, and the shape of the Earth. Euler treated the first in 1749, Mayer the lunar motion in 1750, and Boscovich and Maire the shape of the Earth in 1755. {{cite:dodge2008}} (p. 353) {{cite:dodge2008}} (p. 354) The split between a model that predicts a measured quantity and a model that predicts relative frequencies is the modern division into statistical and probability models. {{cite:nist_glossary2002}} (Glossary, "model")
