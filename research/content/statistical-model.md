## Lead context

Data are particular. A statistical model is the general description that relates them: a mathematical statement connecting the variables, with a random piece that says the relation is not exact. A model can predict a measured quantity, or it can predict the relative frequency of random outcomes, or it can do both. Uncertainty about a conclusion then has two contributions the model makes explicit: the error in the observations, and the fact that the model itself is not perfect.{{cite:nist_glossary2002}} (Glossary, "model"){{cite:nist_glossary2002}} (Glossary, "uncertainty"){{cite:dodge2008}} (p. 353)

## Motivating example

The cost of a share purchase can fall exactly on a straight line when the price per share is fixed, as with twelve simultaneous orders for one stock. Family income and the financial aid a college offers do not. Income says something about aid, and other facts say something too. A line plus a remainder is the model for the second situation. The exact line was the model for the first. The equation written for the imperfect case is $y=\beta_0+\beta_1 x+\varepsilon$, and the point estimates of the coefficients are written $b_0$ and $b_1$.{{cite:openintro2019}} (Ch. 8, §8.1.1)

## Definition

A model is a theoretical representation of a real situation, built from mathematical symbols. Given observations and hypotheses, it aims at the best description of the phenomenon that those hypotheses allow. It contains observable variables and parameters. The variables are the observable pieces. The parameters are the fixed, generally unknown, quantities that tie the variables together. A deterministic model says the tie is exact. A stochastic model says a random error remains.{{cite:dodge2008}} (pp. 353–354)

A statistical model predicts a measured quantity. A probability model predicts the relative frequency of random outcomes.{{cite:nist_glossary2002}} (Glossary, "model")

A stochastic model for a response $Y$ and explanatory variables $X_1, \ldots, X_p$ has the form

$$
Y = f(X_1, \ldots, X_p \mid \beta_0, \ldots, \beta_{p-1}) + \varepsilon,
$$


where the $\beta_j$ are parameters to be estimated and $\varepsilon$ is an unobservable random error. Linearity refers to the coefficients. The equation $Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \varepsilon$ is linear of the second order even though $X$ is squared. The straight line $Y = \beta_0 + \beta_1 X$ is the deterministic special case with no error term written. The equation $Y = \beta_0/(X+\beta_1)+\varepsilon$ is nonlinear in the parameter $\beta_1$.{{cite:dodge2008}} (p. 354)

In the same notation, linear regression writes $y = \beta_0 + \beta_1 x + \varepsilon$. The error term is often dropped from the written prediction because the target is the average outcome, not a new individual remainder.{{cite:openintro2019}} (Ch. 8, §8.1.1)

## Properties

The response, also called the endogenous variable, is the $Y$ being expressed. The explanatory variables are the $X_j$. The error $\varepsilon$ is what keeps the relation from being exact. After a least-squares fit of $Y=X\beta+\varepsilon$, the fitted vector is $\hat Y=X\hat\beta$ and the residual vector is $e=Y-\hat Y$. A residual is the difference between the observed value and the estimated value.{{cite:dodge2008}} (pp. 354, 365)

Discrete models are also classed by the factors. A fixed-effect model uses factors whose levels are the finite set written into the design. A variable-effect model uses levels that were drawn at random from a larger set of possible levels. A mixed-effect model contains both. The design decides which of those writings is the right one, because the design says which levels were fixed and which were sampled.{{cite:dodge2008}} (pp. 354–355)

The model states the relation one is willing to estimate. For a line, the data produce $b_0$ and $b_1$, and the fitted line is used to describe or predict the average response. A residual plot then asks whether the line left a pattern behind. Curvature in the residuals means the straight line was the wrong model. In a causal analysis the equation is a device for estimation. An observational association, written with a coefficient, is not by itself a model of a causal effect.{{cite:openintro2019}} (Ch. 8, §8.1.1, §8.1.3; Ch. 1, §1.3.4)

## Worked example

Three points $(x, y)$ are $(1, 5)$, $(2, 8)$, and $(3, 11)$. The line $y = 2 + 3x$ gives $2 + 3 \times 1 = 5$, $2 + 3 \times 2 = 8$, and $2 + 3 \times 3 = 11$. Every residual is 0. The statistical model with an error term is $Y = 2 + 3X + \varepsilon$ with $\varepsilon = 0$ at these three points. A fourth point at $x = 4$ has fitted value $2 + 3 \times 4 = 14$.{{cite:openintro2019}} (Ch. 8, §8.1.1){{cite:dodge2008}} (p. 354)

**Your turn.** The fourth point is observed as $y = 16$, not 14. What is the residual from the line $y = 2 + 3x$?

::: {.callout-tip collapse="true" title="Answer"}
The fitted value is 14. The residual is $16 - 14 = 2$.
:::

## Assumptions and limits

The representation is only as good as the hypotheses built into $f$ and into the behaviour of $\varepsilon$. A straight line leaves curvature behind when the relation bends, and the residual plot is the warning. Parameters are features of the model, not variables of the units. Using an imperfect model is itself a source of uncertainty, alongside the observational error. Squaring $X$ does not make the model nonlinear. Nonlinearity is about the way the coefficients enter. A fitted line is an estimate of a stated relation, and the residuals are the part the relation did not capture. It is not a law the points had to obey.{{cite:openintro2019}} (Ch. 8, §8.1.1, §8.1.3){{cite:dodge2008}} (pp. 353–354){{cite:nist_glossary2002}} (Glossary, "uncertainty")

## History

The word model, for a mathematical representation fitted to observations, is traced to three eighteenth-century astronomical problems: the inequality in the motions of Jupiter and Saturn, the motion of the Moon, and the shape of the Earth. Euler treated the first in 1749, Mayer the lunar motion in 1750, and Boscovich and Maire the shape of the Earth in 1755. The split between a model that predicts a measured quantity and a model that predicts relative frequencies is the modern division into statistical and probability models. Least squares and $L_1$ estimation are two of the methods that estimate the parameters once the equation has been written.{{cite:dodge2008}} (pp. 353–354){{cite:nist_glossary2002}} (Glossary, "model")
