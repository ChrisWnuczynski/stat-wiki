## Lead context

Pupils share a classroom, classrooms share a school, and schools share a district. Measurements inside one of those groups resemble each other more than measurements from different groups. A multilevel model gives the coefficients of a regression permission to vary from group to group, and it can do so at more than one grouping at once. The groups may be nested, one inside another, or crossed, so that a unit belongs to two groupings neither of which contains the other.{{cite:gelman2005_anova}} (pp. 1–2){{cite:bates_lme4_2015}} (p. 3, equations 2 and 3)

## Motivating example

Two clinics each record a blood pressure for three patients, once. The six numbers are not six independent draws from one population: the three patients in a clinic share a staff, a protocol, and a local case-mix. A single regression line ignores that sharing and treats the clinic as invisible. A separate line for every clinic, with no link between the lines, fits the six numbers and says nothing about a clinic that was not in the file. A multilevel model puts a clinic shift around a common line and gives that shift a variance, so that both the common line and the size of the clinic differences are part of the fit.{{cite:gelman2005_anova}} (pp. 1–2){{cite:bates_lme4_2015}} (p. 1, §1)

## Definition

A multilevel model is a regression in which some coefficients are constant across groups and others vary, with the varying coefficients given a distribution, and in which the groups may be nested or crossed. Nested groups sit inside one another: patients in clinics in districts. Crossed groups cut across one another: pupils taught by a teacher and also belonging to a neighbourhood, with teachers not confined to one neighbourhood. Classical analysis of variance already batched effects this way, and it became awkward once nesting, crossing, and unequal group sizes appeared together. The hierarchical version keeps the batches and estimates a variance for each batch.{{cite:gelman2005_anova}} (pp. 1–2 and 20–21)

For a Gaussian response the conditional model is

$$
(Y\mid B=b)\sim N(X\beta+Zb,\ \sigma^2 W^{-1}), \qquad B\sim N(0,\Sigma),
$$


with $\Sigma$ a positive semidefinite covariance. The term $X\beta$ holds the constant coefficients. The term $Zb$ holds the varying coefficients, and the pattern of $Z$ says which observations share a group. A random intercept for clinic $i$ is the special case $Y_{ij}=x_{ij}^\top\beta+b_i+\varepsilon_{ij}$ with $b_i\sim N(0,\tau^2)$ and $\varepsilon_{ij}\sim N(0,\sigma^2)$, independent across clinics and independent of the clinic effects.{{cite:bates_lme4_2015}} (p. 3, equations 2 and 3)

A generalised linear mixed model keeps a linear predictor of the same shape, $x^\top\beta+z^\top b$, and replaces the normal conditional distribution by a distribution suited to the response, through a link function. A binary outcome is not made normal by the normal distribution on $b$. The normal law is the law of the group coefficient. Counts and binary outcomes are the cases in which ecology and medicine usually meet the model.{{cite:bolker2009_glmm}} (p. 127)

## Interpretation

Under the random-intercept model, two distinct patients in clinic $i$ have covariance $\tau^2$, and one patient has variance $\tau^2+\sigma^2$. Their correlation is

$$
\frac{\tau^2}{\tau^2+\sigma^2}.
$$


Patients in different clinics have covariance $0$ when the clinic effects are independent. The correlation cannot be negative in this one-parameter form, because $\tau^2$ and $\sigma^2$ are variances. A model with varying slopes can produce a correlation that changes with the covariate. The correlation is a description of the population of patients, marginal over the clinic effect. It is not the residual correlation after the clinic effect has been conditioned on. Conditional on $b_i$, the patients in a clinic are independent in this model.{{cite:bates_lme4_2015}} (p. 3, equations 2 and 3)

With $\tau^2=9$ and $\sigma^2=3$, the marginal variance of one observation is $12$ and the within-clinic correlation is $9/12=3/4$. The difference of two observations in the same clinic cancels $b_i$, so its variance is $3+3=6$, not $12+12=24$. The shared level is a feature of the level, not extra noise in the contrast inside the clinic. The ratio of those two difference-variances is $24/6=4$. The within-clinic contrast is the more precise one because the clinic level cancels.

Nesting adds a variance at each level that is shared by every observation under that level. If clinics sit inside districts, two patients in the same clinic share the district effect and the clinic effect. Two patients in the same district but different clinics share only the district effect. Crossing does not create that inclusion. A teacher effect and a neighbourhood effect can both touch a pupil without either group containing the other.{{cite:gelman2005_anova}} (p. 2){{cite:bates_lme4_2015}} (p. 2)

The constant coefficients describe the population pattern. The varying coefficients describe how far groups depart from it, and they support a prediction for a group that was sparsely measured, pulled toward the pattern of the other groups. One of the incompatible vocabularies for this split says that fixed effects are constant across individuals and random effects vary. Another says that fixed effects are estimated by least squares and random effects are estimated with shrinkage. The fitted model has to say which coefficients are constant and which are varying, because the two words do not pick out one definition.{{cite:gelman2005_anova}} (pp. 20–21)

For a non-Gaussian response the coefficients are conditional on the group effect. An odds ratio from a logistic multilevel model is an odds ratio given the group effect. Averaging the probability over groups is not the same operation as transforming the averaged predictor. Reporting the conditional odds ratio as the population-average odds ratio changes the question.{{cite:bolker2009_glmm}} (p. 127)

## Worked example

Take $\tau^2=9$ and $\sigma^2=3$ in a random-intercept model. One reading has variance $9+3=12$. Two readings in the same clinic have correlation $9/12=0.75$ and covariance $9$. Their difference has variance $6$. Two readings in different clinics have correlation $0$ and a difference with variance $12+12=24$. The within-clinic difference is the more precise contrast, by a factor of $24/6=4$ in variance, because the clinic level cancels.{{cite:bates_lme4_2015}} (p. 3, equations 2 and 3)

**Your turn.** A random-intercept model has $\tau^2=4$ and $\sigma^2=12$. Find the marginal variance of one observation, the within-group correlation, and the variance of the difference of two observations in the same group.

::: {.callout-tip collapse="true" title="Answer"}
The marginal variance is $4+12=16$. The within-group correlation is $4/16=0.25$. The shared intercept cancels in a difference, leaving variance $12+12=24$.
:::

## Connections

The Gaussian specification is a [linear mixed model](linear-mixed-model.qmd), and its one-group case is a [random-intercept model](random-intercept-model.qmd) whose within-group resemblance is an [intraclass correlation](intraclass-correlation.qmd). The non-Gaussian specification is a [generalised linear mixed model](generalised-linear-mixed-model.qmd). [Fixed and random effects](fixed-and-random-effects.qmd) is the older vocabulary for constant and varying terms, and the five definitions in the analysis-of-variance literature do not agree. A Bayesian treatment with a prior on the group distribution is a [hierarchical Bayesian model](hierarchical-bayesian-model.qmd). The data layouts that most often need the grouping are [panel data](panel-data.qmd), [repeated measures](repeated-measures.qmd), and a [cross-sectional data](cross-sectional-data.qmd) set whose units sit inside regions.{{cite:gelman2005_anova}} (pp. 20–21){{cite:bates_lme4_2015}} (pp. 1–3){{cite:bolker2009_glmm}} (p. 127)

## History

Analysis of variance organised effects into batches and compared the variance of each batch, but the classical calculations became awkward once nesting, crossing, and unequal group sizes appeared together. Recasting those batches as varying coefficients in a hierarchical model made the same comparisons available in unbalanced designs, and it made the fixed-or-random question a question about how a batch of coefficients would be used.{{cite:gelman2005_anova}} (pp. 1–2 and 20–21)

Software for linear mixed models then made nested and crossed group factors ordinary specifications, with the conditional normal model written as $X\beta+Zb$ and the group covariance left as a parameter. Maximum likelihood and restricted maximum likelihood are the fitting criteria for the Gaussian case. Generalised linear mixed models extended the same predictor to binary and count data. That is the form in which ecology, medicine, and the social sciences usually meet a multilevel model when the outcome is not a normal measurement.{{cite:bates_lme4_2015}} (pp. 1–3){{cite:bolker2009_glmm}} (p. 127)
