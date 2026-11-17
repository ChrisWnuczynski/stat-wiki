## Lead context

Pupils share a classroom, classrooms share a school, and schools share a district. Measurements inside one of those groups resemble each other more than measurements from different groups. A multilevel model gives the coefficients of a regression permission to vary from group to group, and it can do so at more than one grouping at once.

## Motivating example

Two clinics each record a blood pressure for three patients, once. The six numbers are not six independent draws from one population: the three patients in a clinic share a staff, a protocol, and a local case-mix. A single regression line ignores that sharing and treats the clinic as invisible. A separate line for every clinic, with no link between the lines, fits the six numbers and says nothing about a clinic that was not in the file. A multilevel model puts a clinic shift around a common line and gives that shift a variance, so that both the common line and the size of the clinic differences are part of the fit.{{cite:gelman2005_anova}} (pp. 1–2){{cite:bates_lme4_2015}} (eqs. 2–3, p. 3)

## Intuition

Coefficients come in batches. The overall intercept is one number. The clinic adjustments are a batch of numbers, one per clinic, regarded as varying. A further batch, if the data have one, adjusts schools or districts. Calling an effect constant means it is the same for every group. Calling it varying means groups are allowed to differ. The varying effects are not a second copy of the data. They are tied together by a distribution whose spread is estimated from the groups that were seen.{{cite:gelman2005_anova}} (pp. 2, 21)

The Gaussian linear version of this idea is a [linear mixed model](linear-mixed-model.qmd). Counts, binary outcomes, and other non-normal responses use a [generalised linear mixed model](generalised-linear-mixed-model.qmd), with the group shifts still on the scale of the linear predictor. The grouping structure, not the name of the software, is what makes the model multilevel.{{cite:bolker2009_glmm}} (p. 127){{cite:bates_lme4_2015}} (p. 1)

## Definition

A multilevel model is a regression in which some coefficients are constant across groups and others vary, with the varying coefficients given a distribution, and in which the groups may be nested or crossed. Nested groups sit inside one another: patients in clinics in districts. Crossed groups cut across one another: pupils taught by a teacher and also belonging to a neighbourhood, with teachers not confined to one neighbourhood.{{cite:gelman2005_anova}} (pp. 1–2, 21)

For a Gaussian response the conditional model is
\[
(Y\mid B=b)\sim N(X\beta+Zb,\ \sigma^2 W^{-1}), \qquad B\sim N(0,\Sigma),
\]
with \(\Sigma\) a positive semidefinite covariance. The term \(X\beta\) holds the constant coefficients. The term \(Zb\) holds the varying coefficients, and the pattern of \(Z\) says which observations share a group. A random intercept for clinic \(i\) is the special case \(Y_{ij}=x_{ij}^\top\beta+b_i+\varepsilon_{ij}\) with \(b_i\sim N(0,\tau^2)\) and \(\varepsilon_{ij}\sim N(0,\sigma^2)\), independent across clinics.{{cite:bates_lme4_2015}} (eqs. 2–3, p. 3)

A generalised linear mixed model keeps the linear predictor \(x^\top\beta+z^\top b\) and replaces the normal conditional distribution by a distribution suited to the response, through a link function. A binary outcome is not made normal by the normal distribution on \(b\). The normal law is the law of the group coefficient.{{cite:bolker2009_glmm}} (p. 127)

## Properties

Under the random-intercept model, two distinct patients in clinic \(i\) have covariance \(\tau^2\), and one patient has variance \(\tau^2+\sigma^2\). Their correlation is
\[
\frac{\tau^2}{\tau^2+\sigma^2}.
\]
Patients in different clinics have covariance \(0\) when the clinic effects are independent. The correlation cannot be negative in this one-parameter form. A model with varying slopes can produce a correlation that changes with the covariate.{{cite:bates_lme4_2015}} (eqs. 2–3, p. 3)

With \(\tau^2=9\) and \(\sigma^2=3\), the marginal variance of one observation is \(12\) and the within-clinic correlation is \(9/12=0.75\). The difference of two observations in the same clinic cancels \(b_i\), so its variance is \(3+3=6\), not \(12+12=24\). The shared level is a feature of the level, not extra noise in the contrast inside the clinic.

Nesting adds a variance at each level that is shared by every observation under that level. If clinics sit inside districts, two patients in the same clinic share the district effect and the clinic effect. Two patients in the same district but different clinics share only the district effect. Crossing does not create that inclusion. A teacher effect and a neighbourhood effect can both touch a pupil without either group containing the other.{{cite:gelman2005_anova}} (p. 2){{cite:bates_lme4_2015}} (p. 2)

## Statistical use

Use a multilevel model when the sampling or the treatment really is grouped and the target involves that grouping. The constant coefficients describe the population pattern. The varying coefficients describe how far groups depart from it, and they support a prediction for a group that was sparsely measured, pulled toward the pattern of the other groups. A [fixed and random effects](fixed-and-random-effects.qmd) distinction is one vocabulary for constant and varying coefficients; the fitted model should say which coefficients are which.{{cite:gelman2005_anova}} (pp. 20–21)

The Gaussian linear case is estimated by maximum likelihood or by restricted maximum likelihood, as in a [linear mixed model](linear-mixed-model.qmd). A binary or count response uses a [generalised linear mixed model](generalised-linear-mixed-model.qmd). A [panel data](panel-data.qmd) file is the case in which the inner group is the person and the occasions are the repeated rows. A single [cross-sectional data](cross-sectional-data.qmd) set still has a multilevel structure when the rows sit inside regions. [Repeated measures](repeated-measures.qmd) are the experimental form of the same grouping.{{cite:bates_lme4_2015}} (pp. 1–3){{cite:bolker2009_glmm}} (p. 127)

If the scientific target is only the average association across groups, and the group shifts are a nuisance, a marginal model can avoid specifying \(B\). That analysis is not a multilevel model. It does not produce a clinic-specific adjustment.{{cite:bolker2009_glmm}} (p. 127)

## Worked example

Take \(\tau^2=9\) and \(\sigma^2=3\) in a random-intercept model. One reading has variance \(9+3=12\). Two readings in the same clinic have correlation \(9/12=0.75\) and covariance \(9\). Their difference has variance \(6\). Two readings in different clinics have correlation \(0\) and a difference with variance \(12+12=24\). The within-clinic difference is the more precise contrast, by a factor of \(24/6=4\) in variance, because the clinic level cancels.{{cite:bates_lme4_2015}} (eqs. 2–3, p. 3)

**Your turn.** A random-intercept model has \(\tau^2=4\) and \(\sigma^2=12\). Find the marginal variance of one observation, the within-group correlation, and the variance of the difference of two observations in the same group.

::: {.callout-tip collapse="true" title="Answer"}
The marginal variance is \(4+12=16\). The within-group correlation is \(4/16=0.25\). The shared intercept cancels in a difference, leaving variance \(12+12=24\).
:::

## Common misconceptions

A multilevel model is not a [linear mixed model](linear-mixed-model.qmd) under another name, and it is not only a [generalised linear mixed model](generalised-linear-mixed-model.qmd). Each of those pages is one conditional distribution inside the same grouping idea. Using only the Gaussian page misses binary and count responses. Using only the non-Gaussian page misses the linear case in which the marginal covariance is \(\tau^2+\sigma^2\).{{cite:bates_lme4_2015}} (p. 1){{cite:bolker2009_glmm}} (p. 127)

It is not hierarchical clustering. Clustering builds a tree of observations from a distance. A multilevel model is a probability model for a response, with groups that are given in the design or in the sampling. It is also not, by itself, a [hierarchical Bayesian model](hierarchical-bayesian-model.qmd). That model is the case in which the group distribution is a prior and the answers are posterior. The grouping can be estimated by likelihood as well.{{cite:gelman2005_anova}} (pp. 1–2)

Varying coefficients are not the same thing as a regression surface that changes with a covariate. A slope on age can be constant across clinics and still make the fitted mean change with age. It becomes a varying effect when each clinic is allowed its own slope.{{cite:gelman2005_anova}} (p. 21)

## Assumptions and limits

The simple random-intercept model assumes independent groups, a common variance \(\tau^2\), and residuals that are independent once the group effect is in the model. Serial correlation inside a patient who is measured several times is not absorbed by a single clinic intercept. Too few groups makes \(\tau^2\) weakly identified: two clinics do not determine a variance of clinic effects, however many patients each clinic has.{{cite:bates_lme4_2015}} (eqs. 2–3, p. 3)

Nesting that is entangled with a treatment is a design limit, not a computational one. If every clinic offers only one treatment, the clinic effect and the treatment effect are the same contrast. A multilevel model does not separate them. Crossed factors need the design to have actually crossed them; a formula that writes two grouping factors does not create combinations the study never observed.{{cite:gelman2005_anova}} (p. 2)

For a non-Gaussian response the coefficients are conditional on the group effect. An odds ratio from a logistic multilevel model is not the odds ratio in the population average, because averaging the probability is not the same operation as transforming the averaged predictor. Reporting one as the other changes the question.{{cite:bolker2009_glmm}} (p. 127)

## Connections

The Gaussian specification is a [linear mixed model](linear-mixed-model.qmd), and its one-group case is a [random-intercept model](random-intercept-model.qmd) whose within-group resemblance is an [intraclass correlation](intraclass-correlation.qmd). The non-Gaussian specification is a [generalised linear mixed model](generalised-linear-mixed-model.qmd). [Fixed and random effects](fixed-and-random-effects.qmd) is the older vocabulary for constant and varying terms. A Bayesian treatment with a prior on the group distribution is a [hierarchical Bayesian model](hierarchical-bayesian-model.qmd). The data layouts that most often need the grouping are [panel data](panel-data.qmd), [repeated measures](repeated-measures.qmd), and a [cross-sectional data](cross-sectional-data.qmd) set whose units sit inside regions.

## History

Analysis of variance already organised effects into batches and compared the variance of each batch, but the classical calculations became awkward once nesting, crossing, and unequal group sizes appeared together. Recasting those batches as varying coefficients in a hierarchical model made the same comparisons available in unbalanced designs, and it made "fixed or random" a question about how a batch of coefficients would be used rather than a question with a single textbook answer.{{cite:gelman2005_anova}} (pp. 1–2, 20–21)

Software for linear mixed models then made nested and crossed group factors ordinary specifications, with the conditional normal model written as \(X\beta+Zb\) and the group covariance left as a parameter. Generalised linear mixed models extended the same predictor to binary and count data, which is the form in which ecology, medicine, and the social sciences usually meet a multilevel model when the outcome is not a normal measurement.{{cite:bates_lme4_2015}} (pp. 1–3){{cite:bolker2009_glmm}} (p. 127)
