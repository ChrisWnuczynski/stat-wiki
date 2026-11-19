## Lead context

Several test scores, a child's background, and a later outcome are not a single regression with a long list of coefficients. Some of the scores are noisy versions of a skill that was never observed directly, and some arrows are supposed to run from background to skill to outcome. Structural equation modelling is the family of multivariate models that writes those arrows and those latent variables down, then estimates them from the covariances of the observed variables. A different tradition uses structural equations for causal interventions without requiring a latent factor. The name covers both, and a path diagram does not say which one is in force.{{cite:rosseel2012}} (p. 2){{cite:hernan_robins2020}} (Ch. 6, §6.2, Technical Point 6.2, p. 77)

## Motivating example

A development study measures industrialisation in 1960 by three indicators and political democracy in 1960 and again in 1965 by four indicators each. The scientific sentence is not "regress one score on another." It is that industrialisation is a latent level, that democracy at each date is a latent level measured with error, and that democracy in 1965 depends on industrialisation and on democracy in 1960. Seventy-five countries supply the covariances. A model with that measurement structure and those two regressions was fit by maximum likelihood. The model chi-square was 38.125 on 35 degrees of freedom, with a $p$-value of 0.329. The fit is a statement about the covariance matrix, not a statement that the arrows are the historical causes.{{cite:rosseel2012}} (p. 19)

## Definition

In the social and behavioural sciences, structural equation modelling is a class of multivariate models. The continuous-variable form that the applied literature inherited combines three older traditions. Path analysis, from Sewall Wright's genetics in 1921 and later from sociology, writes directed relations among observed variables. Simultaneous equations, from econometrics, write several outcomes that determine one another. Factor analysis, from psychology, writes observed scores as noisy measures of latent factors. The merged model has a measurement part, linking indicators to latent variables, and a structural part, linking the latent variables to each other. The continuous-variable core associated with Karl Jöreskog's LISREL is the working form of that applied field.{{cite:rosseel2012}} (p. 2)

A second use of the words is the nonparametric structural equation model attached to a causal diagram. For an ordered set of variables, each variable is a deterministic function of its parents on the graph and of an error, $V_m=f_m(\mathrm{pa}_m,\epsilon_m)$, with the first variable a function of its error alone. An intervention sets a variable to a value. The counterfactual is obtained by substituting that value and leaving the other functions as they are. The absence of an arrow means that the missing parent is not a direct cause. That definition does not require a factor-analysis measurement model, a normal distribution, or a linear equation. It is a way to state which counterfactuals a diagram is supposed to represent.{{cite:hernan_robins2020}} (Ch. 6, §6.2, Technical Point 6.2, p. 77)

In the linear social-science form the free parameters are factor loadings, regressions among latents, and variances and covariances of residuals and of exogenous factors. One loading in each factor is often fixed at 1 so that the factor's scale is the scale of a reference indicator. The remaining loadings, and the regressions, are estimated. Estimation compares the sample covariance matrix with the covariance matrix implied by those parameters. Maximum likelihood is the default. A weighted least-squares discrepancy $(s-\hat\sigma)^\top W^{-1}(s-\hat\sigma)$ is the more general form, with $s$ the non-duplicated sample covariances and $\hat\sigma$ the implied ones.{{cite:rosseel2012}} (pp. 19 and 27)

## Properties

The measurement block and the structural block answer different questions. In the industrialisation example the measurement block says that $x_1,x_2,x_3$ are indicators of one factor, `ind60`, and that the democracy items at each date are indicators of `dem60` and `dem65`. The structural block is two regressions: democracy in 1960 on industrialisation, and democracy in 1965 on industrialisation and on democracy in 1960. Residual covariances among particular items, such as the same item measured five years apart, are extra parameters. They say that two indicators share something the factors do not absorb.{{cite:rosseel2012}} (p. 19)

On the standardised scale the fitted regression of `dem60` on `ind60` is 0.447, the regression of `dem65` on `dem60` is 0.885, and the direct regression of `dem65` on `ind60` is 0.182. The chain `ind60` to `dem60` to `dem65` multiplies the two standardised coefficients:

$$
0.447\times 0.885=0.395595.
$$


Adding the direct standardised coefficient gives

$$
0.182+0.395595=0.577595.
$$


That sum is an arithmetic decomposition of the two routes drawn in the diagram, on the scale of the reported standardised solution. It is not a second estimation. The estimation has already happened, in the maximum-likelihood fit to the covariances of the 75 countries. The chi-square of 38.125 on 35 degrees of freedom, with $p=0.329$, is the test of whether the implied covariances are close to the sample covariances. A large $p$-value means the covariance discrepancies are not large relative to that reference distribution. It does not identify the arrows as interventions.{{cite:rosseel2012}} (p. 19)

The causal structural equation has a different property. The functions $f_m$ are unknown and need not be linear. What is used in practice is often the implication of the diagram: which variables must be conditioned on so that a treatment–outcome association equals an effect. The equation defines the intervention by substitution into $f_m$. A linear factor score is a different object.{{cite:hernan_robins2020}} (Ch. 6, §6.2, Technical Point 6.2, p. 77)

Under non-normal continuous data the maximum-likelihood parameter estimates can remain consistent when the model is identified and correctly specified, while the usual standard errors are too small, by as much as 25 to 50 percent in the accounts Rosseel summarises, and the chi-square tends to be too large. Asymptotically distribution-free estimation avoids the normality assumption and, in empirical checks cited there, breaks down unless the sample is very large, on the order of several thousand. A robust standard error or a rescaled chi-square is the practical alternative when the sample is the size of a typical survey rather than the size that weighted least squares wants.{{cite:rosseel2012}} (p. 27)

## Statistical use

Fit the social-science model when the scientific sentence really does have a measurement part and a structural part, and when the input you are willing to use is a covariance matrix of continuous variables. [Factor analysis](factor-analysis.qmd) is the measurement special case, with no directed regressions among the factors beyond their correlations. A path model among observed variables is the case with no latent factors. [Ordinary least squares](ordinary-least-squares.qmd) and [partial correlation](partial-correlation.qmd) recover pieces of those path models when the graph is simple enough and every variable is observed. Full estimation uses the whole covariance structure. From the mid-1970s the practical vehicle was a program an applied researcher could run. Later software, including open implementations, estimates the same class and extends it toward longitudinal and missing-data versions.{{cite:rosseel2012}} (p. 2)

Use the nonparametric structural equation when the diagram is a set of claims about interventions. [Confounding variables](confounding-variable.qmd) are the common causes the diagram says to include so that a treatment–outcome association equals the effect the intervention defines. The functions stay unspecified. Conditioning on the parents the diagram names is the operation. Estimating a loading of 2.180, which is the unstandardised loading of the second industrialisation indicator in the democracy example, is not that operation.{{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77){{cite:rosseel2012}} (p. 19)

Report the diagram, the fixed scale loadings, the estimator, the sample size, and the covariance fit together. In the democracy fit the first loading of each factor is fixed at 1, the estimator is maximum likelihood, there are 75 observations, and the chi-square test does not reject the covariance structure at conventional levels. A standardised coefficient of 0.447 without those companions is a picture. The standard error on the unstandardised industrialisation coefficient, 0.399, is part of the same table, and under non-normality that standard error is the piece most likely to be too small if the ordinary maximum-likelihood formula is trusted.{{cite:rosseel2012}} (pp. 19 and 27)

## Worked example

Take the standardised solution of the industrialisation and democracy model as given by the maximum-likelihood fit: 0.447 from industrialisation to democracy in 1960, 0.885 from democracy in 1960 to democracy in 1965, and 0.182 directly from industrialisation to democracy in 1965.

The chain product is $0.447\times 0.885=0.395595$. The sum of the chain and the direct coefficient is $0.182+0.395595=0.577595$. The chi-square comparison of implied and sample covariances is 38.125 on 35 degrees of freedom. The $p$-value is 0.329. The sample size is 75.{{cite:rosseel2012}} (p. 19)

**Your turn.** A different diagram has a single chain of two standardised coefficients, 0.5 and 0.4, and no direct arrow. What is the chain product?

::: {.callout-tip collapse="true" title="Answer"}
The product is $0.5\times 0.4=0.2$.
:::

## Common misconceptions

A model that fits the covariances is not automatically a correct causal diagram. The democracy chi-square, with $p=0.329$, says the implied second moments are close to the sample second moments under the fitted linear structure. The nonparametric structural equation asks a different question: what happens if a variable is set rather than observed. Passing one test does not answer the other.{{cite:rosseel2012}} (p. 19){{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77)

A diagram that encodes conditional exchangeability is not automatically a factor model with a nice measurement scale. The causal equation can be nonlinear and can have no latent factor at all. Reporting a path coefficient without the diagram, or a diagram without the conditional-independence claims it makes, leaves the reader with a picture instead of a model.{{cite:hernan_robins2020}} (Ch. 6, §6.2, Technical Point 6.2, p. 77)

The default standard errors are not robust to the failure of normality. If the variables are skewed, the maximum-likelihood point estimates may still be consistent, and the usual standard errors can be far too small, so that a coefficient is declared different from zero too often. The chi-square can be too large, so that a tolerable covariance fit is rejected. Those are properties of the estimator under a false distributional assumption, not properties of the arrows.{{cite:rosseel2012}} (p. 27)

Fixing a loading at 1 sets the scale of the factor. It is not a finding that the reference indicator is a perfect measure. In the democracy fit the standardised loading of the first industrialisation indicator is 0.920, not 1. The 1 is the unstandardised constraint.{{cite:rosseel2012}} (p. 19)

## History

Wright's path coefficients in the early 1920s gave genetics, and then sociology, a way to write directed relations among variables. Econometric simultaneous equations and psychological factor analysis developed in parallel. Spearman’s factor model is the early psychological source, and Haavelmo and Koopmans are the econometric sources named in the later survey of the merger. The three traditions were brought together in the early 1970s. Jöreskog's 1973 work, and the commercial distribution of LISREL from 1974, made the merged model something applied researchers could fit as a routine. Later commercial programs and, more recently, open implementations estimate the same class.{{cite:rosseel2012}} (p. 2)

The causal-diagram tradition is a later, and only partly overlapping, formalisation. Robins in 1986 set out a structural equation in which each variable is a function of its causal parents and an error, detailed enough to match the data, and Pearl later drew that model as a directed acyclic graph. An intervention is the substitution of a value into that function. The social-science program that estimates loadings from a covariance matrix and the epidemiological program that reads a diagram as a set of interventions share a name and a picture of arrows. They do not share a likelihood.{{cite:rosseel2012}} (p. 2){{cite:hernan_robins2020}} (Ch. 6, §6.2, Technical Point 6.2, p. 77)

## Connections

Structural equation models sit on top of [multivariate statistics](multivariate-statistics.qmd), because the linear form takes a covariance structure as its input, and next to [psychological statistics](psychological-statistics.qmd), which supplies many of the scales. [Factor analysis](factor-analysis.qmd) is the measurement special case. [Ordinary least squares](ordinary-least-squares.qmd) is available when every variable in a simple path is observed. A [confounding variable](confounding-variable.qmd) is what the causal diagram tells the analyst to condition on. Keeping the covariance fit, the scale constraint, and the intervention claim in separate sentences is what stops a path diagram from being asked to do all three jobs at once.{{cite:rosseel2012}} (pp. 2 and 19){{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77)
