

## Lead context

Several test scores, a child's background, and a later outcome are not a single regression with a long list of coefficients. Some of the scores are noisy versions of a skill that was never observed directly, and some arrows are supposed to run from background to skill to outcome. Structural equation modelling is the family of multivariate models that writes those arrows and those latent variables down, then estimates them from the covariances. A different tradition uses structural equations for causal interventions without requiring a latent factor. The name covers both, and they should not be silently identified.

## Motivating example

Three observed scores are x = 1, 2, 3 and y = 2, 3, 5, and a treatment indicator z = 0, 0, 1. The least-squares slope of y on z alone uses the two untreated responses with mean 2.5 and the treated response 5, so the crude difference is 2.5. The same y regressed on x has a slope, because y rises with x. A structural equation that says z affects y only through a path that is not confounded by x is a different equation from the crude difference. The number 2.5 is the difference in means. It equals an effect of z only under a diagram that says x is not a common cause. Writing the diagram is part of the model. The subtraction is not.

## Definition

In the social and behavioural sciences, structural equation modelling is a class of multivariate models for continuous observed variables, later extended to other kinds of variables. The models combine three older traditions. Path analysis, from Sewall Wright's genetics and later from sociology, writes directed relations among observed variables. Simultaneous equations, from econometrics, write several outcomes that determine one another. Factor analysis, from psychology, writes observed scores as noisy measures of latent factors. The merged model has a measurement part, linking indicators to latent variables, and a structural part, linking the latent variables to each other. The continuous-variable form associated with Karl Jöreskog's LISREL is the working core of that applied field.{{cite:rosseel2012}} (pp. 1–2)

A second use of the words is the nonparametric structural equation model attached to a causal diagram. There each variable is a function of its parents on the graph and of an error, and interventions set a variable to a value rather than observing it. That definition does not require a factor-analysis measurement model. It is a way to state which counterfactuals a diagram is supposed to represent.{{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77)

## Statistical use

The social-science model is fit to a covariance matrix. [Factor analysis](factor-analysis.qmd) is the measurement special case, with no directed relations among the factors beyond their correlations. A path model among observed variables is the case with no latent factors. [Ordinary least squares](ordinary-least-squares.qmd) and [partial correlation](partial-correlation.qmd) recover pieces of those path models when the graph is simple enough. Full estimation, in the LISREL line, uses the whole covariance structure, and the practical vehicle from the 1970s onward was a program that applied researchers could run. Later software, including open implementations, estimates the same class of models and extends it toward longitudinal and missing-data versions.{{cite:rosseel2012}} (pp. 1–2)

The causal structural equation is used differently. The functions $f_m$ are unknown and nonparametric. What is used in practice is the implication of the diagram: which variables must be conditioned on so that a treatment–outcome association equals an effect. [Confounding variables](confounding-variable.qmd) are the common causes the diagram says to include. The equation defines the intervention. A linear factor-score formula is a further modelling choice, used only when it is written down.{{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77)


## Worked example

Three observed scores are x = 1, 2, 3 and y = 2, 3, 5, and a treatment indicator z = 0, 0, 1. The least-squares slope of y on z alone uses the two untreated responses with mean 2.5 and the treated response 5, so the crude difference is 2.5. The same y regressed on x has a slope, because y rises with x. A structural equation that says z affects y only through a path that is not confounded by x is a different equation from the crude difference. The number 2.5 is the difference in means. It equals an effect of z only under a diagram that says x is not a common cause. Writing the diagram is part of the model. The subtraction is not.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::



The integer list used above is a device for keeping the target fixed. With 20 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.

That integer list used above is a device for keeping the target fixed. With 20 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Wright's path coefficients in the early 1920s gave genetics, and then sociology, a way to decompose a correlation along directed paths. Econometric simultaneous equations and psychological factor analysis developed in parallel. The three traditions merged in the early 1970s. Jöreskog's 1973 work, and the commercial distribution of LISREL from 1974, made the merged model something applied researchers could fit as a routine. The causal-diagram tradition is a later, and only partly overlapping, formalisation: a structural equation for each node, errors, and a rule for what happens when a node is set rather than observed.{{cite:rosseel2012}} (pp. 1–2){{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 20. Their total is 210, so their mean is 10.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 8.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Structural equation modelling has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 10.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Factor analysis](factor-analysis.qmd), [Ordinary least squares](ordinary-least-squares.qmd), [partial correlation](partial-correlation.qmd), [Confounding variables](confounding-variable.qmd).

Two further limits are algebraic. The sum of deviations from the mean 10.5 is zero, so the mean is the least-squares centre of these 20 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 10.5.

## Connections

Structural equation models sit on top of [multivariate statistics](multivariate-statistics.qmd), because their input is a covariance structure, and next to [psychological statistics](psychological-statistics.qmd) and social statistics, which supply the scales. A model that fits the covariances is not automatically a correct causal diagram. A diagram that encodes conditional exchangeability is not automatically a factor model with a nice measurement scale. Reporting a path coefficient without the diagram, or a diagram without the conditional-independence claims it makes, leaves the reader with a picture instead of a model.{{cite:rosseel2012}} (pp. 1–2){{cite:hernan_robins2020}} (Ch. 6, §6.2, p. 77)
