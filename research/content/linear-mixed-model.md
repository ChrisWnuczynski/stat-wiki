## Motivating example

Suppose a clinic measures blood pressure repeatedly on each patient. Measurements from the same patient tend to resemble one another because the patient has a persistent baseline, even after accounting for age or treatment. Treating every reading as an independent observation understates this shared source of variation. A linear mixed model adds a patient-specific random component to a population regression, making within-patient dependence part of the probability model.{{cite:bates_lme4_2015}} (§1.1–1.2, model formulation and repeated-measure example)

## Intuition

The fixed-effect coefficients describe a population-level line. A random intercept shifts that line up or down for each patient; a random slope can also change its rate of rise with time. The shifts are not separately fixed constants for every patient: they are modelled as draws from a common distribution whose variance describes between-patient heterogeneity. This distinction lets the model estimate a population effect while allowing observed patients to depart from it. It also makes predictions for sparsely measured patients shrink toward the population pattern.{{cite:bates_lme4_2015}} (§1.1–1.2 and §2.2, fixed and random terms)

## Definition

Write the response vector as $Y=X\beta+Zb+\varepsilon$, where $X\beta$ is the fixed-effect mean, $Zb$ contains random effects, $b\sim N(0,G)$, and $\varepsilon\sim N(0,R)$ independently. In this Gaussian formulation, $G$ is a covariance matrix for group effects and $R$ is a residual covariance matrix. Conditional on $b$, the mean is $X\beta+Zb$; marginally over $b$, the mean is $X\beta$ and the covariance is $ZGZ^\top+R$. Both the mean and covariance matter. The familiar independent-error linear model is the special case without a random-effect contribution.{{cite:bates_lme4_2015}} (§1.1, equations for conditional response and random effects)

“Mixed” refers to the joint presence of fixed and random effects. It does not say that the response is a mixture of unrelated outcome types. The index of a random effect identifies the level that shares a latent shift: patient, hospital, school, batch or another grouping unit. A random intercept for patients creates dependence among a patient's observations; random slopes can make this dependence change with the observation times. The same construction can include nested or crossed grouping factors when the design warrants them. {{cite:bates_lme4_2015}} (§2.2, mixed-model formula examples)

## Interpretation — Dependence made explicit

For a random-intercept model $Y_{ij}=x_{ij}^\top\beta+b_i+\varepsilon_{ij}$, take $b_i\sim N(0,\tau^2)$ and independent $\varepsilon_{ij}\sim N(0,\sigma^2)$. Two distinct readings on one patient have covariance $\tau^2$; a single reading has variance $\tau^2+\sigma^2$. Their intraclass correlation is therefore $\tau^2/(\tau^2+\sigma^2)$. Readings from different patients have zero covariance under independent group effects. This is why the random-intercept model cannot give negative within-patient correlation, while a more general random-slope covariance may produce different correlations at different times.{{cite:bates_lme4_2015}} (§1.1 and §2.2, covariance structure of random terms)

The formula does not make all patients literally identical when $\tau^2$ is small: it says the model attributes little between-patient variance after the fixed effects. When $\tau^2=0$, the random-intercept covariance vanishes. When $\sigma^2$ is tiny compared with $\tau^2$, repeated readings on one patient are nearly alike. A variance component estimated at zero can be a genuine boundary fit, but it can also signal too few independent groups or an over-complex random-effects structure. {{cite:bates_lme4_2015}} (§4, boundary and singular covariance fits)

## Properties

The marginal covariance $ZGZ^\top+R$ is positive semidefinite when $G$ and $R$ are covariance matrices. Its form specifies which observations may share random variation. A random slope gives $b_{0i}+t b_{1i}$, so for two times $s,t$ the shared covariance is $\operatorname{Var}(b_{0i})+(s+t)\operatorname{Cov}(b_{0i},b_{1i})+st\operatorname{Var}(b_{1i})$. Its dependence on time cannot be represented by one constant intraclass correlation. These identities explain what a proposed grouping formula asserts before any fitting algorithm is used.{{cite:bates_lme4_2015}} (§1.1 and §2.2, random intercepts and slopes)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Since $\E(b)=\E(\varepsilon)=0$, $\E(Y)=X\beta$. Independence gives $\operatorname{Cov}(Y)=\operatorname{Cov}(Zb)+\operatorname{Cov}(\varepsilon)=ZGZ^\top+R$. For the random-intercept form, distinct readings $j\ne k$ on group $i$ share only $b_i$, so $\operatorname{Cov}(Y_{ij},Y_{ik})=\operatorname{Var}(b_i)=\tau^2$; each variance is $\tau^2+\sigma^2$. The ratio gives the stated correlation. With $b_{0i}+t b_{1i}$, bilinearity of covariance gives the time-dependent expression above.{{cite:bates_lme4_2015}} (§1.1 and §2.2, Gaussian mixed-model structure)
:::
:::

## Statistical use

The grouping level should follow how observations were collected. If each patient contributes several readings, the number of readings is not the number of independent patients. The fixed effects answer population questions under the specified random-effects distribution; the predicted random effects describe particular sampled patients. Maximum likelihood and restricted maximum likelihood are common ways to estimate the covariance components. Restricted likelihood accounts for the fixed-effect fit when estimating variance components; comparisons that change the fixed-effect mean structure should use a compatible likelihood criterion rather than blindly comparing restricted likelihood values.{{cite:bates_lme4_2015}} (§1.3, fitting overview; §3.4, ML and REML criteria)

A fixed effect is a population constant, while a random effect is a group-level draw from a shared distribution. The orthodontic growth-curve problem makes the distinction operational with a random intercept, random slope and fitted covariance. It uses an actual repeated-measures design, beyond the small calculation below.

## Worked example

Suppose the fitted population mean is $10+2t$ and each patient has a random intercept with variance $\tau^2=9$; measurement error has variance $\sigma^2=4$. At time $t=1$, the population mean is $12$ and the marginal variance of one reading is $9+4=13$. Two different readings on the same patient have covariance $9$ and correlation $9/13\approx0.6923$. For their difference, the shared intercept cancels: its variance is $4+4=8$. Independent-error regression would instead treat the covariance as zero and assign variance $13+13=26$ to that difference. These are different claims about the same design, not alternative ways of writing the same standard error.{{cite:bates_lme4_2015}} (§1.1 and §2.2, random-intercept covariance)

**Your turn.** A model has random-intercept variance $4$ and residual variance $6$. Find the marginal variance of one observation, the correlation of two distinct observations in the same group, and the variance of their difference.

::: {.callout-tip collapse="true" title="Answer"}
The marginal variance is $4+6=10$, the covariance is $4$, and the intraclass correlation is $4/10=0.4$. The shared intercept cancels from a difference, leaving variance $6+6=12$.
:::

## Common misconceptions

A random effect is not merely an unobserved fixed parameter with a new name: its common distribution and covariance are substantive assumptions. A fixed effect can vary in its *predicted outcome* across covariate values without becoming a random effect. Repeated readings do not provide as many independent pieces of group-level information as an equal number of unrelated patients. And a zero random-intercept estimate does not mean every patient had exactly the same observed values; residual variation remains.{{cite:bates_lme4_2015}} (§1.1–2.2, model terms and grouping)

## Assumptions and limits

The simple Gaussian model assumes independent groups, normally distributed random effects and the specified residual covariance. If measurements on one patient remain serially correlated after the random intercept is removed, $R=\sigma^2I$ misses that dependence. If each hospital treats only one kind of patient, a hospital effect and that patient characteristic may be confounded, so the model cannot identify their effects from that design alone. A random intercept also cannot represent patients whose responses change at different rates; random slopes or a different time covariance may be needed. With only two patients, a precise estimate of the between-patient variance is especially implausible, however many readings each contributes.{{cite:bates_lme4_2015}} (§1.1, covariance assumptions; §2.2, random slopes and grouping; §4, singular fits)

## Connections

The [random-intercept model](random-intercept-model.qmd) is the simplest linear mixed model, and its [intraclass correlation](intraclass-correlation.qmd) measures within-group resemblance. [Random slopes](random-slopes.qmd) let trajectories differ as well as starting levels. [Restricted maximum likelihood](restricted-maximum-likelihood.qmd) targets variance-component estimation. [Repeated measures](repeated-measures.qmd) provides a common design setting; [generalised linear mixed models](generalised-linear-mixed-model.qmd) extend the conditional-mean construction to non-Gaussian responses.{{cite:bates_lme4_2015}} (§1.1–2.2, model family and fitting)

## History

Laird and Ware's 1982 longitudinal-data work gave random-effects models a way to represent correlation among repeated measurements on one person. Henderson's mixed-model equations shaped later estimation and prediction methods. Software including `lme4` made models with nested and crossed effects comparatively accessible and developed likelihood-based fitting for large designs. These contributions connect the repeated-measurement problem, its mathematical solution and its computational implementation.{{cite:bates_lme4_2015}} (§1.1, repeated measurements and Laird–Ware attribution; §3.5, Henderson equations; §§2.2 and 3.4, model and fitting)
