## Lead context

The propensity score is the probability that a unit receives treatment, given its observed pre-treatment covariates. It compresses a possibly long list of covariates — age, severity, prior history, setting — into one number between 0 and 1. That compression is not merely a convenience. Rosenbaum and Rubin showed that adjustment for this scalar is sufficient to remove the bias due to all the observed covariates that went into it, listing matched sampling, subclassification and covariance adjustment on the score among its applications {{cite:rosenbaum_rubin1983}} (p. 41). Austin puts the same point as study design: the score is the probability of treatment assignment conditional on observed baseline characteristics, and it lets an observational study mimic some characteristics of a [randomised controlled trial](randomised-controlled-trial.qmd) {{cite:austin2011}} (p. 399).

The score works because it is a balancing score: conditional on it, treated and untreated units have the same distribution of the observed covariates. It is not a model of the outcome, not a measure of how well treatment works, and not a probability that treatment suits a person. It summarises the assignment process — who, in these data, tended to be treated — and only for the *observed* covariates. Nothing in its construction reaches a covariate that was not measured.

## Motivating example — The problem the score is meant to solve

In a randomised experiment the investigator controls assignment, so the groups differ, in expectation, only by chance. In an observational study of a [treatment](treatment.qmd), clinicians, patients, institutions or circumstance assign treatment, usually responding to exactly the characteristics that also predict the outcome. The treated are then older, sicker or more severely affected, and a crude contrast mixes the effect of treatment with the effect of those differences. That mixing is [confounding](confounding-variable.qmd), and removing it is the central problem of [causality](causality.qmd) in observational data.

Direct adjustment is awkward in high dimensions: exact matches on many covariates are rare, strata on the full vector multiply faster than samples can fill them, and regression must extrapolate across regions where one group has no observations. Stuart makes the difficulty plain: with more than a few covariates it becomes very difficult to find matches with close or exact values of all covariates, and the propensity score, introduced in 1983, was the advance that allowed matched sets with similar covariate distributions without requiring close matches on every variable separately {{cite:stuart2010}} (§1.3). The score changes the dimension of the problem, not its logic: balance a scalar that preserves the information relevant to assignment.

## Definition

Let $A$ be a binary treatment indicator, with $A = 1$ for treatment and $A = 0$ for the comparison condition. Let $X$ be the vector of covariates measured before treatment for a unit — pre-treatment, because a variable affected by treatment cannot confound it and must not enter the score. Let $P(\cdot)$ denote probability, and $P(\cdot \mid \cdot)$ conditional probability, in the population under study. The propensity score at covariate value $X = x$ is

$$e(x) = P(A = 1 \mid X = x),$$

and $e(X)$, the score at a unit's own covariates, takes values in $[0,
1]$: the definition restricts it only as a probability restricts it, so a
covariate profile for which treatment is certain has score $1$ and one for
which treatment is impossible has score $0$. Strictly interior values — $0
< e(x) < 1$ for every $x$ that occurs — are not part of the definition;
they are the further positivity condition, stated with strong ignorability
below, and where they fail the corresponding effects are not identified.
Rosenbaum and Rubin define it in this form, as the conditional probability
of assignment to a particular treatment given a vector of observed
covariates, the propensity towards exposure to treatment 1 given the
observed covariates $x$ {{cite:rosenbaum_rubin1983}} (pp. 42–43). Hernán
and Robins write $\pi(L)$ for the same object, with $L$ in place of $X$:
close to 0 for individuals with a low probability of treatment and close
to 1 for those with a high probability {{cite:hernan_robins2020}} (p.
201).

The score belongs to an assignment process in a population, not to a unit in isolation: the same patient has one score where treatment is routine and another where it is reserved for severe cases. In a randomised experiment it is known by design — 0.5 for every unit in a trial assigning half to treatment — whereas in an observational study it must be estimated {{cite:hernan_robins2020}} (p. 201).
In the [potential outcomes](potential-outcomes.qmd) framework, let $Y$ be the observed outcome and $Y^{a=1}$ and $Y^{a=0}$ the outcomes the same unit would exhibit under treatment and under the comparison. The target is usually the [average treatment effect](average-treatment-effect.qmd), $\mathrm{E}[Y^{a=1}] - \mathrm{E}[Y^{a=0}]$, where $\mathrm{E}[\cdot]$ denotes a population mean, or the corresponding effect among the treated.

## Interpretation — The balancing property

A function $b(X)$ of the covariates is a balancing score if, conditional
on $b(X)$, the distribution of $X$ is the same for treated and untreated
units; in symbols, $X$ is independent of $A$ given $b(X)$. The vector $X$
itself is trivially a balancing score, and a useless one for dimension
reduction. Rosenbaum and Rubin defined a balancing score in just this way,
and set out to identify the coarsest such function
{{cite:rosenbaum_rubin1983}} (p. 42). Their first theorem states that the
propensity score is a balancing score: treatment assignment and the
observed covariates are conditionally independent given the propensity
score {{cite:rosenbaum_rubin1983}} (p. 44). Their second theorem states
that a function of the covariates is a balancing score if and only if it
is finer than the propensity score, in the sense that the score can be
recovered from it; the propensity score is therefore the coarsest
balancing score, and $X$ itself the finest. Note the logical shape of that
statement: the propensity score is *one* balancing score — the coarsest —
not a synonym for the class, which also contains $X$ itself and every
function of the covariates finer than the score
{{cite:rosenbaum_rubin1983}} (p. 44).

Why can conditioning on a scalar balance a vector? The covariates can be associated with treatment only through the probability of treatment they induce. Fix a value $s$ and consider all units with $e(X) = s$. Their covariates may vary widely — one unit older but less severely ill, another younger but more severely ill, arriving at the same probability of treatment by different routes. But within that set, a unit's exact covariate values give no further information about whether it was treated, because every unit in the set had the same probability $s$ of treatment. Treatment there is as if assigned by a coin with success probability $s$, independently of the covariates, and a coin does not favour one covariate profile over another. Hence the two groups within the set are drawn from the same covariate distribution. Hernán and Robins give the same argument in words: individuals with the same propensity score will generally have different values of some covariates, yet among all individuals with a given value of the score, the distribution of the covariates is the same in the treated and the untreated, so the score balances the covariates {{cite:hernan_robins2020}} (pp. 201–202). Their technical point generalises this to balancing scores generally, of which the propensity score is the simplest example {{cite:hernan_robins2020}} (p. 202).

Balance is a statement about the true score in the population. In a finite sample it is approximate — disturbed by sampling variation and by error in the estimating model — so it must be checked, not assumed. It extends only to covariates measured and included, and to functions of them.

## Properties — Strong ignorability

Balance alone does not make a causal effect; a causal interpretation also requires that the observed covariates are all that stand between assignment and the potential outcomes. Rosenbaum and Rubin call treatment assignment strongly ignorable given $X$ when two conditions hold together: the potential outcomes are independent of treatment assignment given $X$, and $0 < P(A = 1 \mid X = x) < 1$ for every covariate value $x$ that occurs {{cite:rosenbaum_rubin1983}} (pp. 43–44). The first condition is no unmeasured confounding; the second is positivity, or overlap, examined below. Austin states the same pair, with the first condition also called the no unmeasured confounders assumption — all variables affecting both assignment and outcome have been measured — and notes that Rosenbaum and Rubin showed that, under strong ignorability, conditioning on the propensity score allows unbiased estimation of average treatment effects {{cite:austin2011}} (p. 403). Stuart's statement is materially identical, with the first component also termed ignorable, no hidden bias, or unconfounded {{cite:stuart2010}} (§1.2).

The payoff is that strong ignorability is inherited by the score. Rosenbaum and Rubin's third theorem states that if assignment is strongly ignorable given $X$, it is strongly ignorable given any balancing score, hence given the propensity score {{cite:rosenbaum_rubin1983}} (p. 45). Consequently, at any value of a balancing score, the difference between treated and control means is an unbiased estimate of the average treatment effect at that value when assignment is strongly ignorable, and pair matching, subclassification and covariance adjustment on a balancing score can all produce unbiased estimates of average treatment effects {{cite:rosenbaum_rubin1983}} (pp. 43–44). Hernán and Robins state the inheritance as exchangeability: conditional exchangeability given the covariates implies conditional exchangeability given the propensity score, and positivity within levels of the score holds if and only if positivity within levels of the covariates holds {{cite:hernan_robins2020}} (p. 202). The analyst must defend ignorability given the full covariate vector — a substantive claim about what was measured — and the theorems then license work with one number instead of a vector. Neither condition is verifiable from the data — the data contain no record of an unmeasured confounder whose absence is in question — so propensity analysis repackages the identifying assumptions; it does not relax them.

## Statistical use

The true score is unknown in an observational study, so it is estimated by modelling assignment as a function of the covariates. Austin notes that in practice it is most often estimated with a logistic regression model in which treatment status is regressed on the observed baseline characteristics, the estimated score being the predicted probability from the fitted model, although bagging, boosting, tree-based methods, random forests and neural networks have also been examined {{cite:austin2011}} (p. 403). Hernán and Robins do the same in their smoking cessation example, fitting a logistic model for the probability of treatment conditional on the covariates — the model also used for inverse probability weighting in their earlier chapters {{cite:hernan_robins2020}} (p. 201).

The model's purpose is balance, not prediction. Sharp discrimination is not thereby a virtue — it usually signals poor overlap — and the model is not selected by the significance of its coefficients. What matters is whether conditioning on the estimated score leaves the groups similar on the covariates, including interactions and non-linear terms that matter for the outcome. The model is therefore fitted, checked and refitted until the balance checks below are acceptable, all without using the outcome. Variable choice matters most: covariates should be pre-treatment and related to the outcome, to assignment, or to both, with priority to genuine confounders, and variables affected by treatment must be excluded, since conditioning on a consequence of treatment can induce bias. Variables predicting assignment strongly but unrelated to the outcome also warrant caution: they push scores towards 0 and 1, worsening overlap and the variability of weighted estimates. These judgements are substantive, often organised with a [causal diagram](causal-diagram.qmd).

Once estimated, the score is used in four standard ways — Austin's introduction is organised around exactly these four: matching, stratification or subclassification, inverse probability of treatment weighting, and covariate adjustment, all using the propensity score {{cite:austin2011}} (p. 403). They rest on the same assumptions, differing in the population referred to, the handling of poor overlap, and the further modelling required.

### Matching

Matching forms sets of treated and untreated units with similar score values, discards or down-weights the rest, and compares outcomes in the matched sample as in a randomised study. Austin describes it as forming matched sets of treated and untreated subjects who share a similar value of the propensity score, with one-to-one or pair matching most common, and notes that matching in this form allows estimation of the effect among the treated {{cite:austin2011}} (p. 404). Hernán and Robins add that matching on the score is analogous to matching on a single continuous variable, each treated individual being matched with one or more untreated individuals with a close score value, and that the matched population is the population in which the effect is estimated {{cite:hernan_robins2020}} (p. 204). Exact equality of a continuous score is rare, so closeness is set by a caliper, a maximum permitted distance between scores or their logits. A narrow caliper improves balance but discards treated units with no close counterpart — and the estimate then refers to a subset defined by the matching itself, which may be hard to characterise substantively {{cite:hernan_robins2020}} (pp. 204–205).

### Stratification and subclassification

Stratification divides the sample into strata by ranges of the estimated score, estimates the contrast within each stratum, and pools the contrasts with stated weights. Within a narrow stratum the groups have similar scores and hence, approximately, similar covariate distributions, so the within-stratum contrast is approximately unconfounded. Austin describes it as a meta-analysis of a set of quasi-randomised trials: stratum-specific estimates weighted by the proportion of subjects in the stratum estimate the average effect in the whole population, while weighting by the proportion of treated subjects in each stratum estimates the effect among the treated {{cite:austin2011}} (p. 408). The number of strata is a bias–variance choice: wide strata leave residual imbalance, since the score still varies within a stratum and treated units sit at its higher end, while narrower strata reduce that bias with diminishing returns and noisier contrasts. Hernán and Robins note the same defect: the distribution of the continuous score will in general differ between treated and untreated units within some strata, such as deciles, so the groups might not be exchangeable within them, whereas methods using the numerical value of the estimated probability, rather than a categorised version, do not have that problem {{cite:hernan_robins2020}} (p. 203).

### Inverse probability weighting

Weighting constructs a pseudo-population in which treatment is independent of the measured covariates, then compares outcomes there without further adjustment. Each unit is weighted by the inverse of the probability of the treatment it actually received: $1/e(X)$ if treated, $1/(1 - e(X))$ if not. Austin defines inverse probability of treatment weighting in exactly this way — weights based on the propensity score creating a synthetic sample in which the distribution of measured baseline covariates is independent of treatment assignment, a subject's weight being the inverse of the probability of receiving the treatment actually received {{cite:austin2011}} (pp. 408–409). Hernán and Robins describe the target: a pseudo-population in which covariates and treatment are statistically independent, and in which, when conditional exchangeability given the covariates holds in the actual population, the counterfactual mean equals the corresponding pseudo-population mean, so association there is causation {{cite:hernan_robins2020}} (pp. 164–165). Intuitively, a treated unit with score $1/4$ represents four units like itself, three of whom happened not to be treated; weighting by 4 restores that representation. The price is variability: a treated unit with score near 0 receives an enormous weight, and a few such units can dominate. Stabilised weights reduce that variability without changing the target.

### Covariate adjustment with the score

The fourth use includes the estimated score as a covariate in an outcome regression, alongside the treatment indicator. Austin describes regressing the outcome on treatment status and the estimated propensity score, the model chosen by the nature of the outcome, and observes that this is the only one of the four methods requiring a model for the outcome, including a correct model of the relationship between the score and the outcome {{cite:austin2011}} (p. 409). Hernán and Robins found the same dependence in their example: the estimate from outcome regression with the score as a continuous covariate was close to the stratified and standardised ones, but its validity depends on correctly specifying the score–outcome relationship, assumed linear there, though the score's one-dimensional nature makes flexible terms such as cubic splines an easy guard {{cite:hernan_robins2020}} (p. 203). So adjustment is not assumption-free because the score appears in the model: a linear term imposed on a non-linear relationship leaves residual confounding. Its advantages are simplicity and retention of every unit; its disadvantage is that design and analysis are not separated.

### Weights for the average effect and for the effect among the treated

The weights above target the average effect in the whole population, where each group must be reweighted up to that population: treated units by $1/e(X)$, untreated by $1/(1 - e(X))$. The weighted treated mean then estimates $\mathrm{E}[Y^{a=1}]$, the weighted untreated mean estimates $\mathrm{E}[Y^{a=0}]$, and their difference is the average treatment effect. A different target requires different weights, and confusing the two is a common, consequential error.

For the average treatment effect among the treated (ATT), the target is the treated themselves. Treated units receive weight $1$ — the treated sample already represents them — while untreated units are reweighted to match the treated covariate distribution: an untreated unit with covariates $x$ receives weight $e(x)/(1 - e(x))$, the odds of treatment, so untreated units resembling treated units count for more and those unlike any treated unit count for almost nothing. Austin gives the same form: the average-effect weights are replaced by 1 for treated subjects and $e/(1 - e)$, in his notation, for untreated subjects to estimate the effect among the treated {{cite:austin2011}} (p. 409). Neither scheme corrects the other; they answer different questions, and reporting one estimand's estimate under the other's name is mislabelling. Matching and stratification make the same choice in other clothing: retaining all treated units targets the ATT, while pooling stratum contrasts by total stratum size targets the whole-population effect and pooling by treated count per stratum targets the ATT.

### Balance checking

The estimated score is not the true score, so balance is a goal to be verified, not a theorem to be invoked. Checking compares each covariate's distribution between the groups after matching, within strata, or in the weighted sample; if systematic differences remain, the score model is revised and the process repeated. Austin frames it so: assessing whether the propensity score model has been adequately specified means examining whether the distribution of measured baseline covariates is similar between treated and untreated subjects with the same estimated propensity score, and residual systematic differences indicate misspecification {{cite:austin2011}} (p. 411).

The standard summary is the standardised difference: the difference in group means, or in proportions for a binary covariate, divided by a pooled standard deviation. Austin gives both definitions and notes that it is not influenced by sample size, allows variables in different units to be compared, and that a value below 0.1 is commonly taken to indicate a negligible difference {{cite:austin2011}} (p. 412). Stuart's version standardises by the treated group's standard deviation and adds that it should be computed for each covariate and also for two-way interactions and squares, since balance on means alone does not imply balance on features a non-linear outcome model would exploit {{cite:stuart2010}} (§4.1). Means should also be supplemented with variance ratios and graphical comparisons.

Balance checking should not use hypothesis tests or p-values. Austin records the two criticisms of significance testing in matched samples: significance levels are confounded with sample size, so a smaller matched sample can appear better balanced merely through lower power, and balance is a property of the particular sample, making reference to a superpopulation inappropriate; significance testing to assess balance is therefore discouraged {{cite:austin2011}} (pp. 413–414). Stuart gives the same two reasons in the same order — balance is inherently in-sample, and tests conflate changes in balance with changes in power — and warns against using tests as a stopping rule for selecting a matched sample {{cite:stuart2010}} (§4.1). The standardised difference measures magnitude, which is the question being asked. Checks should cover every important measured pre-treatment covariate, whether or not it entered the model.

## Worked example — One confounder, two strata, an exact standardisation

Let $X$ indicate age group, $X = 1$ for older and $X = 0$ for younger patients, with $A$ as before and $Y$ a binary outcome, $Y = 1$ recording the event. The population has 80 patients, 40 younger and 40 older. Treatment, and the event under either treatment, are both more common among the older patients, so age confounds the crude comparison. Among the younger 40, 10 are treated and 30 are not, so $e = 10/40 = 1/4$; of the treated, 4 have the event, and of the untreated, 6. Among the older 40, 30 are treated and 10 are not, so $e = 30/40 = 3/4$; of the treated, 24 have the event, and of the untreated, 6.

| Age group | Score $e$ | Treated: $n$, events | Untreated: $n$, events | Treated risk | Untreated risk | Difference |
|---|---:|---:|---:|---:|---:|---:|
| Younger ($X = 0$) | $1/4$ | 10, 4 | 30, 6 | $4/10 = 2/5$ | $6/30 = 1/5$ | $1/5$ |
| Older ($X = 1$) | $3/4$ | 30, 24 | 10, 6 | $24/30 = 4/5$ | $6/10 = 3/5$ | $1/5$ |
| All patients | — | 40, 28 | 40, 12 | $28/40 = 7/10$ | $12/40 = 3/10$ | $2/5$ |

The crude contrast is $7/10 - 3/10 = 2/5$. Older patients are $30/40 =
3/4$ of the treated group but only $10/40 = 1/4$ of the untreated group.
The standardised difference for age is $(3/4 - 1/4)$ divided by the square
root of $((3/4)(1/4) + (1/4)(3/4))/2$, that is $(1/2)/\sqrt{3/16} =
2/\sqrt{3} \approx 1.155$ — far above the 0.1 level taken to indicate
negligible imbalance. The treated group's higher event rate partly records
its composition, not an effect of treatment.

Within each age group the contrast is $1/5$: $2/5 - 1/5$ among the
younger, $4/5 - 3/5$ among the older. The score takes exactly two values
here, so stratifying on the score is stratifying on age. Pooling with each
stratum's population share, $40/80 = 1/2$, gives $(1/2)(1/5) + (1/2)(1/5)
= 1/5$. That number is the standardised contrast, and it is what
adjustment on age delivers. Calling it the average treatment effect needs
one more ingredient, which the counts alone do not supply: conditional
exchangeability given age — within each age group, the treated and
untreated patients are comparable in their potential outcomes, so each
within-stratum contrast estimates that stratum's effect. Under that
assumption, $1/5$ is the ATE, and the excess of the crude contrast over
it, $2/5 - 1/5 = 1/5$, is confounding by age. Without it, the same
observed table is consistent with very different effects. Each patient
reveals only one potential outcome, so the $40$ treated patients' outcomes
under no treatment and the $40$ untreated patients' outcomes under
treatment are missing. Filling those missing binary outcomes in
arbitrarily moves the finite-population ATE across a wide range: setting
every missing $Y^{1}$ to $0$ and every missing $Y^{0}$ to $1$ gives $(28 -
(12 + 40))/80 = -24/80 = -0.30$, and the reverse filling gives $((28 + 40)
- 12)/80 = 56/80 = 0.70$. The table alone therefore identifies the
standardised contrast, and identifies the ATE only together with the
exchangeability assumption — a distinction the simple arithmetic can hide.

Weighting gives the same number, and estimates the same counterfactual
means under the same conditional-exchangeability assumption. The estimate
of $\mathrm{E}[Y^{a=1}]$ is $(1/80)\{4/(1/4) + 24/(3/4)\} = (1/80)(16 +
32) = 48/80 = 3/5$, and of $\mathrm{E}[Y^{a=0}]$ is $(1/80)\{6/(3/4) +
6/(1/4)\} = (1/80)(8 + 24) = 32/80 = 2/5$, a difference of $1/5$. For the
effect among the treated, treated patients keep weight 1 and their risk
$28/40 = 7/10$. Untreated patients are weighted by $e/(1 - e)$: $1/3$ if
younger, $3$ if older. Their weighted events are $6 \times (1/3) + 6
\times 3 = 20$ and their weighted total is $30 \times (1/3) + 10 \times 3
= 40$, a risk of $20/40 = 1/2$, giving $7/10 - 1/2 = 1/5$. The two
estimands agree only because the stratum effects were constructed equal;
the weights, not the arithmetic, decide which estimand is estimated. With
one binary confounder the score adds nothing to stratifying on the
confounder itself — the point of so simple a case is that the correction
can be verified by hand. Its value appears when $X$ has many components,
where stratification on $X$ is impossible but work on the scalar $e(X)$
remains feasible.

### Your turn

A second constructed population has one binary confounder, a risk group: $X = 1$ for high-risk and $X = 0$ for low-risk patients, with $A$ and $Y$ as in the worked example. There are 120 patients, 60 in each group. Among the 60 low-risk patients, 20 are treated and 40 are not; of the treated, 10 have the event, and of the untreated, 10. Among the 60 high-risk patients, 40 are treated and 20 are not; of the treated, 30 have the event, and of the untreated, 10.

Compute the propensity score in each group, the crude risk difference, the
within-group risk differences, the standardised contrast pooling the
within-group differences with population weights (the average treatment
effect under conditional exchangeability given risk group), the inverse
probability weighted estimate of the average treatment effect, and the
weighted estimate of the effect among the treated. State, in one sentence,
why the crude difference differs from the standardised one.

::: {.callout-tip collapse="true" title="Answer"}

The propensity scores are $20/60 = 1/3$ in the low-risk group and $40/60 =
2/3$ in the high-risk group. The crude risks are $40/60 = 2/3$ among the
treated and $20/60 = 1/3$ among the untreated, so the crude difference is
$1/3$. Within the low-risk group the difference is $10/20 - 10/40 = 1/2 -
1/4 = 1/4$, and within the high-risk group it is $30/40 - 10/20 = 3/4 -
1/2 = 1/4$. Pooling with population weights of $1/2$ gives $(1/2)(1/4) +
(1/2)(1/4) = 1/4$, the standardised contrast, which is the ATE under the
conditional exchangeability given risk group that this exercise assumes.
For the weighted estimate, $(1/120)\{10/(1/3) + 30/(2/3)\} = (1/120)(30 +
45) = 75/120 = 5/8$ estimates the mean outcome under treatment, and
$(1/120)\{10/(2/3) + 10/(1/3)\} = (1/120)(15 + 30) = 45/120 = 3/8$
estimates the mean outcome under no treatment, a difference of $1/4$. For
the effect among the treated, untreated patients receive weights
$(1/3)/(2/3) = 1/2$ in the low-risk group and $(2/3)/(1/3) = 2$ in the
high-risk group, giving a weighted untreated risk of $(10 \times 1/2 + 10
\times 2)/(40 \times 1/2 + 20 \times 2) = 25/60 = 5/12$, and an effect
among the treated of $2/3 - 5/12 = 1/4$. The crude difference is larger
because high-risk patients, who have higher event rates under either
treatment, make up a larger share of the treated group than of the
untreated group.

:::

## Assumptions and limits

### Overlap, positivity and trimming

Positivity requires both treatments to occur with positive probability at every covariate value in the population: $0 < e(x) < 1$ for all $x$, with enough data near each value to estimate rather than extrapolate. Where the score is 0 or 1, one potential outcome is never observed for such units, and no method can manufacture it. Where it is merely near 0 or 1, very few units carry the information: weighted estimates become unstable, and matched or stratified estimates rest on a handful of comparisons.

Positivity and overlap are related but distinct, and the distinction
matters for what can be checked. Positivity is structural: a property of
the assignment mechanism in the population, namely whether a unit with
covariates $x$ could receive either treatment at all. Overlap is
empirical: a property of the sample in hand, namely whether both groups
are in fact represented near each score value. A sample can display
overlap where structural positivity fails, if chance places a few unusual
units in a group they could not ordinarily join, and it can fail to
display overlap where positivity holds, if a finite sample leaves a region
empty. Overlap is therefore evidence about positivity, not a restatement
of it. Plotting the estimated score separately by group shows where the
groups share common ground. Stuart emphasises that matching methods
highlight areas of the covariate distribution with insufficient overlap,
where estimates would rely heavily on extrapolation, whereas regression
and selection models can perform poorly in exactly those situations
without their standard diagnostics revealing it {{cite:stuart2010}} (§1).
Her discussion of common support adds that subclassification and weighting
generally use all individuals regardless of overlap, so explicit
restriction to the region of common support may be beneficial, and that
common support may show the whole-population average effect to be
inestimable reliably even when the effect among the treated can be
estimated {{cite:stuart2010}} (§3.3).

Restriction — trimming, when it removes units with extreme scores — changes the estimand as well as the estimate. Discarding untreated units outside the treated range costs the ATT nothing; discarding treated units redefines the treated population, and with it the question. Hernán and Robins make the parallel point for matching: the restricted population may be hard to characterise, since individuals do not arrive with their scores visible, and a restriction in real-world variables such as age describes the target more naturally than a bound on the estimated score {{cite:hernan_robins2020}} (p. 205). Trimming must be reported as a change of target population, with the discarded units described.

### What the score does not do

The main limit is unmeasured confounding. Balancing and the inheritance of strong ignorability are statements about the covariates in $X$. An unmeasured variable influencing both assignment and outcome is not in $X$, is not balanced, and cannot be repaired by refining the score model, because the data contain nothing from which its contribution could be estimated. Hernán and Robins state it directly: the propensity score only balances the measured covariates, which does not prevent residual confounding by unmeasured factors, whereas randomisation balances both measured and unmeasured covariates and is therefore the preferred method of eliminating confounding {{cite:hernan_robins2020}} (p. 202). Excellent balance shows only that the measured covariates are balanced.

Nor does the score fix positivity — it reveals it, and the remedies change the question. It does not fix measurement error: a coarsely recorded confounder is balanced only in its recorded form. It does not address interference between units, ill-defined treatments, or time-varying confounding. And it is no substitute for an [instrumental variable](instrumental-variable.qmd) analysis when unmeasured confounding is the main concern: an instrument uses variation in treatment unrelated to the potential outcomes, a different strategy, not a refinement of adjustment. Misspecification is the limit most within the analyst's control, and weighting is its most sensitive victim, since a modest error in a small estimated score becomes a large error in its reciprocal weight. The balance checks are therefore the evidence the method has worked in the application at hand.

## Connections

- [Average treatment effect](average-treatment-effect.qmd) — the usual target; choosing it, or the effect among the treated, determines the weights and pooling.
- [Potential outcomes](potential-outcomes.qmd) — the framework in which strong ignorability, inherited by the score, is stated.
- [Causality](causality.qmd) — the general move from association to effect, of which measured confounding is the part the score addresses.
- [Confounding variable](confounding-variable.qmd) — what the score adjusts for in aggregate, summarising every measured confounder's assignment side at once.
- [Causal diagram](causal-diagram.qmd) — the tool for deciding which variables belong in $X$, a decision the score cannot make.
- [Randomised controlled trial](randomised-controlled-trial.qmd) — the design imitated in part; randomisation also balances unmeasured covariates.
- [Instrumental variable](instrumental-variable.qmd) — an alternative strategy not requiring all confounders to be measured, with different assumptions and estimand.
- [Treatment](treatment.qmd) — the intervention whose assignment probability the score describes.
- [Mediation analysis](mediation-analysis.qmd) — a neighbouring question about pathways; the score itself estimates total effects, not mediated ones.

## Check yourself

1. Two patients have the same propensity score of 0.2. One is older with mild disease; the other is younger with severe disease. A colleague objects that they cannot be compared, because their covariates are plainly different. Is the objection sound?

::: {.callout-tip collapse="true" title="Answer"}

No, not as stated. The balancing property concerns distributions, not pairs: among all patients with a score of 0.2, the covariate distribution is the same for treated and untreated patients, because each had the same probability of treatment and treatment within that group carries no further information about the covariates. Such unlike pairs are exactly what the score places together. In a finite sample, however, balance at a given score is approximate and must be checked.

:::

2. In the worked example, an analyst weights treated patients by $1/e$ and untreated patients by $1/(1 - e)$, obtains $1/5$, and reports it as the effect among the treated. What is wrong?

::: {.callout-tip collapse="true" title="Answer"}

Those are the weights for the average treatment effect in the whole population. For the effect among the treated, treated patients receive weight 1 and untreated patients weight $e/(1 - e)$, giving a weighted untreated risk of $1/2$ and an effect among the treated of $7/10 - 1/2 = 1/5$. The number coincides here only because both stratum-specific effects are $1/5$; the estimand has been mislabelled, and with unequal stratum effects the two computations would differ.

:::

3. After matching, every covariate comparison gives a non-significant p-value, but the standardised difference for disease severity is 0.35. Has balance been achieved?

::: {.callout-tip collapse="true" title="Answer"}

No. A standardised difference of 0.35 is well above the 0.1 level taken to indicate negligible imbalance, so severity remains materially imbalanced and the estimate remains confounded by it. The p-values do not override this: they conflate imbalance size with sample size, and matching shrinks the sample, so its tests have less power and can be non-significant despite substantial imbalance. The score model should be revised — for example with terms for severity or its interactions — and balance rechecked.

:::

## History

The propensity score was introduced by Paul R. Rosenbaum and Donald B. Rubin in "The central role of the propensity score in observational studies for causal effects", in *Biometrika* in 1983. The paper defined the score and balancing scores, showed the score is the coarsest balancing score, defined strongly ignorable treatment assignment, and proved that strong ignorability given the covariates implies strong ignorability given any balancing score, so matching, subclassification and covariance adjustment on a balancing score can produce unbiased estimates of average treatment effects {{cite:rosenbaum_rubin1983}} (pp. 41–45). Its summary already contained the field's programme: adjustment for the scalar score is sufficient to remove bias due to all observed covariates, with applications to matched sampling, subclassification, and the visual representation of multivariate adjustment {{cite:rosenbaum_rubin1983}} (p. 41).

The problem was older than the solution: stratification and matching on one covariate had been studied for decades, and extending them to many was the recognised difficulty. The 1983 result replaced a combinatorial problem with an estimation problem — estimate one probability well. Stuart records the same turning point: matching theory developed through the 1970s for one covariate, and the important advance in 1983 was the propensity score, facilitating matched sets with similar covariate distributions without close matches on all individual variables {{cite:stuart2010}} (§1.3). Later work added the applied machinery: subclassification, including the result reported by Austin that stratifying on the quintiles of the score removes approximately 90 per cent of the bias due to a measured confounder in estimating a linear treatment effect {{cite:austin2011}} (pp. 407–408); inverse probability weighting, connecting the score to epidemiology's weighting tradition; balance diagnostics; doubly robust estimators, which need only one of a score model and an outcome model to be correct; and sensitivity analyses for unmeasured confounding.
