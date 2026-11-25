## Lead context

Potential outcomes are the framework in which a causal question is stated
before any data are analysed. The framework attaches to each unit not one
outcome but a set of outcomes, one for each action that could in principle
be taken, and defines a causal effect as a comparison of those outcomes
for the same units. Rubin states the definition compactly: causal effects
are comparisons of potential outcomes under different treatments on a
common set of units {{cite:rubin2005}} (p. 322). Everything else in the
framework — the assumptions of consistency, exchangeability and
positivity, and the distinction between a causal contrast and an observed
association — exists to answer a single question: under what conditions
can a comparison that is defined on outcomes nobody fully observes be
recovered from the outcomes that are in fact recorded?

This article is about that framework itself: the notation, the table in
which the potential outcomes live, and the assumptions connecting the
table to observed data. The population summary most often computed from
the table, the [average treatment effect](average-treatment-effect.qmd),
has its own article, as does the broader concept of
[causality](causality.qmd) that the framework formalises.

## Definition — Units, treatments and potential outcomes

The primitive objects are units, a treatment and an outcome. A unit is
the entity to which a treatment could be applied and on which an outcome
is measured: a patient, a plot of land, a school, a job applicant. The
units together make up the population or study sample under discussion,
and a typical unit will be indexed by $i$, running from $1$ to $n$, where
$n$ is the number of units. The treatment is the action whose effect is
in question. Write $A$ for the treatment actually received by a unit,
and $a$ for a generic value that $A$ might take. For most of this article
the treatment is binary, so $a$ is either $1$ (treated) or $0$ (not
treated, the comparison condition), but nothing in the notation requires
two levels: $a$ may range over doses, durations or entirely different
interventions. Write $Y$ for the outcome actually observed for a unit.

The potential outcome notation adds a superscript that records a
hypothetical treatment value. For unit $i$, $Y_i^a$ is the outcome that
unit $i$ would have if, possibly contrary to fact, its treatment were set
to $A = a$. With a binary treatment each unit therefore carries two
potential outcomes: $Y_i^1$, the outcome under treatment, and $Y_i^0$,
the outcome under the comparison condition. When the unit is not in
focus, the subscript is dropped and $Y^a$ denotes the potential outcome
of a generic unit drawn from the population, so that
$\E[Y^a]$ is the mean outcome that would be seen if every unit in
the population received treatment value $a$, where $\E[\cdot]$
denotes expectation, that is, averaging over the population. Hernán and
Robins introduce the same objects through a clinical vignette: a patient
who dies after a transplant has $Y^{a=1} = 1$ for the outcome death, and
the causal question is the value of $Y^{a=0}$, the outcome the same
patient would have had without the transplant {{cite:hernan_robins2020}} (pp. 3–4).

Three features of the definition should be noted. First, a potential
outcome is defined by an intervention, not by an observed characteristic:
$Y_i^a$ answers "what would happen to unit $i$ if its treatment were set
to $a$?", which makes sense only for values that could in principle be
assigned. Second, both potential outcomes are attached to the unit before
treatment is assigned — attributes of the unit, like its age or baseline
measurements, except that they describe responses to actions rather than
states at a moment in time. Third, they are defined for every unit under
every treatment value, whether or not that unit could plausibly receive
it. Whether the data can say anything about a particular $Y^a$ is a
separate question, taken up under positivity below.

A causal effect, in this framework, is any comparison of potential
outcomes for a common set of units: unit by unit, as in $Y_i^1 - Y_i^0$,
or after averaging, as in $\E[Y^1] - \E[Y^0]$, or
through another summary of the two distributions. What makes it causal
is that the units, and everything about them except the superscript,
are held fixed. An associational comparison, by contrast, compares
observed outcomes between different units — those who received $A = 1$
against those who received $A = 0$ — and mixes any effect of treatment
with any prior difference between the groups. Stating exactly when the
two comparisons coincide is the work of the assumptions below.

### The science table

It is useful to lay the potential outcomes out in a table with one row
per unit and one column per treatment value. Such a table is often
called the science table: it is the full schedule of what
would happen to every unit under every treatment, the complete "science" of the problem, written down as if it were known. The table
for a binary treatment has columns $Y^0$ and $Y^1$, and it is natural to
add the columns that a study actually records: the treatment received,
$A$, and the observed outcome, $Y$.

The science table is a conceptual device, not a data set; no study
observes it. Its role is to make the target explicit before estimation
arises: every causal estimand is a function of the science table, such
as a difference of two column means, whereas every statistic is a
function of the observed columns $A$ and $Y$ alone. A causal analysis
is justified exactly when the statistic can be shown to recover, in
expectation or in the limit, the chosen function of the table. Without
that link, an analysis may describe the data accurately but does not
answer the causal question, however it is labelled.

The table also disciplines the statement of the question: to write one
down, the investigator must say which units are in the rows, which
actions are in the columns, and what outcome fills the cells. A vague
question — "does the programme work?" — has no science table. The
framework's first contribution is therefore grammatical: it forces a
causal question into a form in which it could, in principle, be answered.

## Interpretation — The fundamental problem of causal inference

The obstacle is immediate. Each unit receives exactly one treatment
value. A patient is transplanted or not; a plot is sown with one variety
or another; an applicant is trained or not. Consequently, for each unit,
at most one of its potential outcomes is ever realised and recorded: the
one corresponding to the treatment it received. The other potential
outcome describes a world that did not occur for that unit, and it
remains unobserved no matter how carefully the study is conducted or how
large it is. Holland named this the fundamental problem of causal
inference: the simultaneous observation of $Y^1$ and $Y^0$ for the same
unit is impossible, so the individual contrast between them can never be
read off the data {{cite:holland1986}} (p. 947).

This is not a problem of measurement error, sample size or technique.
The missing potential outcome is not a value recorded badly or lost; it
is a value that never existed in the observed world. A larger sample
adds rows to the science table, each still with exactly one cell
revealed. The fundamental problem is one of identification — of what
can be learned at all from the observed distribution — and it is solved,
to the extent it can be, by assumptions and design, not computation.

Holland distinguished two broad responses. The scientific response
exploits homogeneity: if units, or repeated occasions for one unit, can
be treated as interchangeable, one unit's observed outcome under
treatment can stand in for another's unobserved outcome. The statistical
response gives up on the individual contrast and targets an average over
many units, using the assignment mechanism — above all, randomisation —
to make one group a credible stand-in for what the other would have done
under the same treatment {{cite:holland1986}} (pp. 947–948). Modern
causal inference is built almost entirely on the second response, and
the assumptions below are its working parts.

## Properties — Individual effects and two null hypotheses

For unit $i$, the individual causal effect of treatment against the
comparison condition is $Y_i^1 - Y_i^0$. The definition is exact and the
quantity is, in general, unknowable: computing it requires both cells of
the unit's row, and the fundamental problem says one cell is always
missing. Hernán and Robins make the same point in their opening chapter:
individual effects cannot be identified, meaning they cannot be
expressed as a function of the observed data, because only the potential
outcome corresponding to the treatment actually received is observed for
each individual {{cite:hernan_robins2020}} (p. 4). No assumption about
the assignment mechanism changes this. Randomisation identifies
averages of potential outcomes; it does not reveal any unit's missing
cell.

Averages behave differently because averaging can be done column by
column. The mean $\E[Y^1]$ uses only the $Y^1$ column of the
science table, and $\E[Y^0]$ only the $Y^0$ column; neither
requires knowing both entries of any single row. The average treatment
effect, $\E[Y^1] - \E[Y^0]$, is the mean of the
individual effects — the two orders of operations agree for a
difference — but its identification does not require identifying any
individual effect, only the two column means separately. This is why
the framework's identifiable targets are population contrasts, a point
developed in the article on the
[average treatment effect](average-treatment-effect.qmd).

The distinction between unit-level and average statements appears again
in the two null hypotheses the framework keeps apart. The sharp null
hypothesis states that treatment has no effect on any unit:
$Y_i^1 = Y_i^0$ for every unit $i$. It is called sharp because, if it
holds, every missing potential outcome is known — it equals the observed
outcome — so the full science table can be reconstructed from the
observed data and exact randomisation tests become possible. Ding and
Li present the Fisherian randomisation test in exactly these terms: the
null is sharp because it allows all the missing potential outcomes to be
imputed {{cite:ding_li2018}} (§4.1). The average null hypothesis is
weaker: it states only that $\E[Y^1] = \E[Y^0]$, that
the two column means agree. The average null can hold while the sharp
null fails — treatment may help some units and harm others in exactly
offsetting amounts — and the sharp null implies the average null, but
not conversely. Hernán and Robins express the average null for a binary
outcome as equality of the two counterfactual risks,
$\Pr(Y^{a=1} = 1) = \Pr(Y^{a=0} = 1)$, where $\Pr(\cdot)$ denotes
probability {{cite:hernan_robins2020}} (p. 7). A report that a study
"found no effect" is ambiguous until it says which null was examined,
and a test of the sharp null and an estimate of the average effect are
answers to different questions.

### Consistency

The first assumption connects the science table to the data. Let $A$ be
the treatment a unit actually received and $Y$ its observed outcome.
Consistency states that the observed outcome is the potential outcome
under the treatment actually received:

$$Y = Y^A,$$

where $Y^A$ means $Y^a$ evaluated at the value $a$ that $A$ took for
that unit. Equivalently, for a binary treatment,
$Y = A Y^1 + (1 - A) Y^0$: a treated unit's observed outcome is its
$Y^1$, an untreated unit's observed outcome is its $Y^0$. Hernán and
Robins introduce consistency in exactly this form in their first
chapter, as the equality of the observed outcome with the counterfactual
outcome under the treatment the individual received
{{cite:hernan_robins2020}} (p. 4), and return to it at length in their
chapter on observational studies, where it is listed as one of the three
conditions on which identification rests {{cite:hernan_robins2020}} (p. 33).

Consistency looks tautological, and with a precisely specified
intervention it nearly is. Its content appears when the treatment label
conceals variation. If "treatment" is delivered at different doses, by
different routes, or with different accompanying care, then $Y^1$ does
not denote one thing, and a single $Y^1$ column already assumes the
versions away. Consistency therefore has two components, in Hernán and
Robins's account: the counterfactual outcome must be well defined,
which requires the intervention specified precisely enough that "set
$A$ to $a$" has one meaning, and the well-defined counterfactual must
be linked to the data by the equality above {{cite:hernan_robins2020}} (pp. 33, 38–39).
Where no conceivable assignment of units to $a$
exists, $Y^a$ is not well defined either. This is the substance behind
the slogan, associated with Rubin's school, that there is no causation
without manipulation: a causal effect here is an effect of a
[treatment](treatment.qmd), something that could in principle be
assigned.

### No interference and the stable unit treatment value assumption

The second assumption is already hidden in the notation. Writing
$Y_i^a$ with a single superscript asserts that unit $i$'s outcome under
treatment value $a$ depends only on unit $i$'s own treatment. If one
unit's treatment affects another unit's outcome — as when a vaccine
protects the unvaccinated contacts of the vaccinated, or when a training
programme changes the wages of workers who did not attend because the
labour market has shifted — then unit $i$'s outcome depends on the
whole allocation of treatments, and a single superscript cannot record
it. The assumption that this does not happen is no interference.

Hernán and Robins state the point in a fine point to their first
chapter: the definition of a counterfactual outcome implicitly assumes
that an individual's outcome under a treatment value does not depend on
other individuals' treatment values; the assumption of no interference
was labelled "no interaction between units" by Cox in 1958, and is
included in the stable-unit-treatment-value assumption described by
Rubin in 1980 {{cite:hernan_robins2020}} (p. 5). The stable unit
treatment value assumption, universally abbreviated SUTVA, packages no
interference together with the requirement, closely related to
consistency, that there are no hidden versions of treatment: however a
unit came to receive treatment value $a$, the outcome that would be
observed for it is $Y^a$. Rubin states the second component in those
terms in his 2005 exposition of the framework — no matter how unit $i$
received treatment $1$, the outcome that would be observed would be its
potential outcome under treatment $1$, and similarly for treatment $0$
{{cite:rubin2005}} (p. 323).

SUTVA is an assumption about the setting, not the analysis, and it can
fail in ways no analysis of the usual data can repair. Interference is
expected, not exceptional, for infectious diseases, for interventions
delivered to groups such as classrooms, and for treatments operating
through markets or social networks. When interference is present, the
notation must be enlarged: potential outcomes are indexed by other
units' treatments as well, and the estimands become effects of
allocations. The two-column science table is the special case in which
SUTVA holds, and every later result here is about that special case.

### Exchangeability

Suppose consistency and SUTVA hold, so the observed data reveal one cell
per row of a well-defined science table. The remaining problem is that
the revealed cells are not a random sample of each column. The treated
units reveal their $Y^1$ values; the untreated reveal their $Y^0$
values. To learn the column mean $\E[Y^1]$ from the treated
units' outcomes, the treated must be representative of the whole
population with respect to $Y^1$ — and similarly for the untreated and
$Y^0$. The condition that makes this legitimate is exchangeability.

Exchangeability of the treated and untreated groups means that the
distribution of the potential outcomes is the same in both groups: the
groups could be exchanged — the treated relabelled as untreated and
vice versa — without changing the distribution of $Y^1$ or of $Y^0$.
Formally, $Y^a$ is independent of $A$ for each treatment value $a$,
written $Y^a \perp\!\!\!\perp A$, where $\perp\!\!\!\perp$ denotes
statistical independence. For the identification of means, the weaker
mean version suffices: $\E[Y^a \mid A = 1] =
\E[Y^a \mid A = 0] = \E[Y^a]$ for each $a$, where
$\E[\cdot \mid \cdot]$ denotes a conditional expectation, the
mean within the group named after the conditioning bar. Hernán and
Robins develop exchangeability in their chapter on randomised
experiments, where it is the property randomisation is designed to
produce: the counterfactual outcome is independent of the treatment
actually received, so the risk observed in one group is the risk that
would have been observed in the other group under the same treatment
{{cite:hernan_robins2020}} (pp. 13–15).

Randomisation delivers exchangeability by design. If treatment is
assigned by a chance mechanism that does not depend on the units'
potential outcomes or on anything correlated with them, then the groups
formed differ only by the operation of that chance mechanism, and in
expectation — exactly, over repetitions of the assignment — the
distribution of every potential outcome, measured or unmeasured, is the
same in both groups. This is the entire logical basis of the
[randomised controlled trial](randomised-controlled-trial.qmd) and of
the [designed experiment](designed-experiment.qmd) more generally: the
design manufactures the assumption that an observational study can only
assert. Two qualifications belong with the statement. Exchangeability under
randomisation is a property of the assignment procedure over its
repetitions; a single realised allocation can be unlucky, which is
random variability, not bias. And because exchangeability concerns
potential outcomes, including unobserved ones, it can never be verified
from a single study's data — in an experiment it is warranted by the
procedure, not checked from the results.

In an observational study, treatment was chosen by patients, clinicians,
markets or circumstances, and there is no general reason for the groups
to be exchangeable. Sicker patients are given stronger treatments;
keener students choose harder courses. The groups then differ in their
potential outcomes even before treatment acts, and the observed contrast
mixes the effect with that prior difference — the phenomenon treated in
the article on a [confounding variable](confounding-variable.qmd).
Exchangeability is the precise name for the absence of that mixing.

### Conditional exchangeability

Exchangeability may fail marginally yet hold within strata of measured
pre-treatment covariates. Write $X$ for a set of variables measured
before treatment — age, severity, prior history — whose values are not
affected by treatment. Conditional exchangeability given $X$ states
that, within each stratum of units sharing the same value of $X$, the
potential outcomes are independent of treatment received:
$Y^a \perp\!\!\!\perp A \mid X$ for each $a$. Within a stratum, in other
words, treatment is as good as randomly assigned with respect to the
potential outcomes, even though across the whole population it is not.
Hernán and Robins treat this as the working assumption of observational
causal inference: the identifiability conditions are exchangeability,
in this conditional form where necessary, together with positivity and
consistency {{cite:hernan_robins2020}} (p. 28).

Conditional exchangeability is an assertion about the world and the
adequacy of $X$, not a property that adjustment machinery creates. It
holds only if $X$ captures every way in which the treated and untreated
differ that is also related to the potential outcomes; omitting an
important common cause leaves residual confounding within strata, and
no modelling of the measured variables repairs the omission. The
assumption is untestable for the same reason its marginal version is:
it is a statement about the missing cells of the science table within
each stratum. Subject-matter knowledge can argue that $X$ plausibly
exhausts the relevant differences; it cannot prove the point from the
study's own data. Choosing $X$ is a substantive task, for which
[causal diagrams](causal-diagram.qmd) provide the organising language;
the present article takes $X$ as given.

### Positivity

Conditional exchangeability within a stratum is useful only if the
stratum actually contains both treated and untreated units. Positivity
is the requirement that this is so, for every stratum that occurs in the
population and for every treatment value in the contrast: the
probability of receiving each treatment value, given the covariates,
is greater than zero. In symbols, writing $\Pr(A = a \mid X = x)$ for
the conditional probability that a unit with covariates $X = x$
receives treatment value $a$, positivity requires
$\Pr(A = a \mid X = x) > 0$ for all $a$ in the contrast and all values
$x$ that occur in the population of interest. Hernán and Robins give
the condition in this form and note that it is required only for the
covariate values in the population of interest and only for the
variables needed for exchangeability {{cite:hernan_robins2020}} (p. 32).

Positivity failures come in two kinds. A structural failure occurs when
some kind of unit cannot receive some treatment: patients with a
contraindication are never given the drug, so that stratum contains no
treated units and the drug's effect there is not identified, whatever
the sample size. A random failure occurs when a stratum could contain
both groups but, in a finite sample, contains only one. In a randomised
experiment, positivity is guaranteed by the design for the values it
assigns with positive probability. Positivity, unlike exchangeability,
can sometimes be checked, because it concerns observed treatment and
covariates only: an empty stratum is visible in the data. What the data
cannot show is whether an empty cell is structural or a sampling
accident.

### Identification

The assumptions now assemble into the framework's central result. A
quantity defined on the science table is identified when it can be
written entirely in terms of the distribution of the observed data —
of $Y$, $A$ and $X$ — so that, given unlimited data, it could be
computed without ever seeing a missing cell.

Under consistency, exchangeability and positivity, each mean potential
outcome is identified by the corresponding observed group mean:

$$\E[Y^a] = \E[Y \mid A = a].$$

The derivation has two steps, and each step is one assumption at work.
First, by exchangeability, the mean of $Y^a$ among units with $A = a$
equals the mean of $Y^a$ in the whole population:
$\E[Y^a \mid A = a] = \E[Y^a]$. Second, by consistency,
units with $A = a$ have observed outcome $Y = Y^a$, so
$\E[Y^a \mid A = a] = \E[Y \mid A = a]$. Positivity is
what guarantees that the conditioning event $A = a$ occurs, so that the
right-hand side is defined. Hernán and Robins give this argument in
their technical treatment of exchangeability, noting that mean
exchangeability is sufficient for the equality of the counterfactual
mean with the observed group mean {{cite:hernan_robins2020}} (p. 15).
The average treatment effect is then identified by the difference of
observed group means, $\E[Y \mid A = 1] - \E[Y \mid
A = 0]$, and this is the precise sense in which a randomised experiment
estimates a causal effect: randomisation warrants exchangeability, the
protocol warrants consistency and positivity, and the algebra does the
rest.

Under conditional exchangeability given $X$, the same argument works
stratum by stratum, and the stratum results are averaged over the
population distribution of $X$. Writing $\Pr(X = x)$ for the proportion
of the population with covariates $X = x$, and summing over all values
$x$ that occur, the identified form is

$$\E[Y^a] = \sum_x \E[Y \mid A = a, X = x] \, \Pr(X = x).$$

This is standardisation: the stratum-specific observed means are
reweighted to the covariate distribution of the whole population.
Hernán and Robins develop standardisation for conditionally randomised
experiments in exactly this form {{cite:hernan_robins2020}} (pp. 19–20).
The formula is stated here because it is the identification
result; the machinery for estimating it when $X$ is high-dimensional —
modelling treatment assignment through the
[propensity score](propensity-score.qmd), modelling the outcome, or
combining the two — belongs to the articles on those methods. What the
framework contributes is the statement of what those methods estimate
and the assumptions under which the estimate has a causal reading.

Identification should not be confused with estimation. Identification
says the causal quantity equals a particular function of the population
distribution of the observed data. Estimation — computing that function
from a finite sample, with sampling variability — is a further step,
and a quantity can be identified yet estimated imprecisely. Conversely,
no precision repairs a failure of identification: a narrow interval
around an observed contrast whose assumptions fail is a precise answer
to an associational question.

## Statistical use — The missing-data view

There is a second way to see the whole construction, due to Rubin, which
unifies causal inference with a familiar statistical problem. Regard
the science table as a data set with missing values. For each unit, the
treatment indicator $A$ determines which potential outcome is observed
and which is missing: a treated unit's $Y^0$ is missing, an untreated
unit's $Y^1$ is missing. Causal inference is then the problem of drawing
conclusions about a table half of whose cells are missing by design,
where the missingness mechanism is the treatment assignment mechanism
itself. Ding and Li's review is built on this observation: because for
each unit at most one of the potential outcomes is observed and the rest
are missing, causal inference is inherently a missing data problem
{{cite:ding_li2018}} (p. 214).

The analogy is exact enough to organise the assumptions. Assignment
independent of the potential outcomes, as in a completely randomised
experiment, parallels data missing completely at random; assignment
depending only on observed covariates, with conditional exchangeability
given $X$, parallels data missing at random; and assignment depending
on the missing potential outcomes themselves, as with unmeasured
confounding, parallels data missing not at random. Ding and Li draw
this parallel explicitly between the classifications of assignment and
missing data mechanisms {{cite:ding_li2018}} (pp. 214–216). The view
also explains why the framework's methods resemble missing-data
methods: standardisation is imputation by stratum means, and weighting
by the inverse probability of treatment is weighting for incomplete
data. It adds no assumptions; it shows the assumptions already made are
of a familiar kind, and that the fundamental problem is the extreme
case of missingness in which exactly one cell of every row is missing.

## Worked example — Six units, a true effect and a biased contrast

Six units have the following science table, where the outcome is binary
($1$ is the event) and the last column is the individual effect.

| Unit | $Y^0$ | $Y^1$ | $Y^1 - Y^0$ |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 0 | 1 | 1 |
| 3 | 0 | 1 | 1 |
| 4 | 0 | 0 | 0 |
| 5 | 1 | 1 | 0 |
| 6 | 0 | 0 | 0 |

The $Y^1$ column sums to $4$, so $\E[Y^1] = 4/6 = 2/3$; the
$Y^0$ column sums to $2$, so $\E[Y^0] = 2/6 = 1/3$. The true
average treatment effect is $2/3 - 1/3 = 1/3$, also the mean of the
individual effects, $(0 + 1 + 1 + 0 + 0 + 0)/6 = 1/3$. Neither null
holds: the average null fails because $2/3 \ne 1/3$, and the sharp null
fails because units 2 and 3 have $Y^1 \ne Y^0$.

Now suppose treatment is assigned, not at random, but preferentially to
units with higher $Y^0$: units 1, 2 and 5 receive treatment ($A = 1$)
and units 3, 4 and 6 do not ($A = 0$). By consistency, the observed
outcomes are $Y = 1, 1, 0, 0, 1, 0$ respectively — each unit shows the
potential outcome for the treatment it received, and the other cell of
its row is missing. The naive observed contrast is

$$\E[Y \mid A = 1] - \E[Y \mid A = 0] = \frac{1 + 1 + 1}{3} - \frac{0 + 0 + 0}{3} = 1 - 0 = 1,$$

which overstates the true effect of $1/3$ by $1 - 1/3 = 2/3$. The bias
is exactly the failure of exchangeability. Among the treated, the mean
of $Y^0$ is $(1 + 0 + 1)/3 = 2/3$; among the untreated it is
$(0 + 0 + 0)/3 = 0$; in the whole population it is $1/3$. The treated
group would have had a higher event rate than the untreated group even
if nobody had been treated, and the naive contrast credits that prior
difference to the treatment. Had the same six units been randomised,
exchangeability would hold in expectation over the randomisation, and
the difference of observed group means would be an unbiased estimate
of $1/3$ — not because randomisation reveals any missing cell, but
because it makes the groups comparable in both columns of the table.

### Your turn

Keep the science table above, but change the assignment: now only
units 3 and 4 receive treatment, and units 1, 2, 5 and 6 do not. What
is the naive observed contrast, and what is its bias relative to the
true average treatment effect of $1/3$?

::: {.callout-tip collapse="true" title="Answer"}

By consistency the observed outcomes are $1, 0, 1, 0, 1, 0$ for units
1 to 6. The treated mean is $(1 + 0)/2 = 1/2$ and the untreated mean is
$(1 + 0 + 1 + 0)/4 = 1/2$, so the naive contrast is $1/2 - 1/2 = 0$.
Its bias is $0 - 1/3 = -1/3$: this assignment makes a treatment with a
true average effect of $1/3$ appear to have no effect at all.

:::

## Connections

- [Average treatment effect](average-treatment-effect.qmd) — the
  population mean of $Y^1 - Y^0$, the summary this framework most often
  identifies.
- [Causality](causality.qmd) — the concept the potential outcome
  notation formalises: a contrast for the same units under different
  actions.
- [Confounding variable](confounding-variable.qmd) — a common cause of
  treatment and outcome, and the usual reason exchangeability fails.
- [Randomised controlled trial](randomised-controlled-trial.qmd) — the
  design that produces exchangeability, and positivity, by construction.
- [Treatment](treatment.qmd) — the intervention $A$ whose values index
  the potential outcomes.
- [Designed experiment](designed-experiment.qmd) — the broader class of
  studies in which the investigator assigns $A$.
- [Propensity score](propensity-score.qmd) — the probability of
  treatment given $X$, used to estimate the standardised mean stated
  above.
- [Causal diagram](causal-diagram.qmd) — the graphical language for
  choosing the covariates $X$ in conditional exchangeability.
- [Mediation analysis](mediation-analysis.qmd) — the extension that
  decomposes an effect into paths, using potential outcomes indexed by
  both treatment and mediator.

## Check yourself

1. A unit received $A = 0$ and its observed outcome was $Y = 1$. What
is $Y^0$ for this unit, and what can be said about $Y^1$?

::: {.callout-tip collapse="true" title="Answer"}

By consistency, $Y^0 = Y = 1$: the observed outcome is the potential
outcome under the treatment actually received. Nothing in the observed
data determines $Y^1$; it is the unit's missing potential outcome, and
the individual effect $Y^1 - Y^0$ is therefore not identified.

:::

2. In the worked example, the naive contrast was $1$ while the true
average treatment effect was $1/3$. Which identifying assumption
failed, and what numbers show the failure?

::: {.callout-tip collapse="true" title="Answer"}

Exchangeability failed. The mean of $Y^0$ was $2/3$ among the treated
and $0$ among the untreated, against $1/3$ in the whole population, so
the groups were not comparable in their potential outcomes: the treated
would have fared worse — here, had more events — even without
treatment. Consistency and positivity held; the bias of $2/3$ is the
exchangeability failure.

:::

3. In the worked example, does the sharp null hypothesis hold? Does
the average null hypothesis hold?

::: {.callout-tip collapse="true" title="Answer"}

Neither holds. The sharp null requires $Y_i^1 = Y_i^0$ for every unit,
but units 2 and 3 have $Y^1 = 1$ and $Y^0 = 0$. The average null
requires $\E[Y^1] = \E[Y^0]$, but the column means are
$2/3$ and $1/3$. The two nulls are different statements: the average
null could have held, with effects in opposite directions cancelling,
even though the sharp null does not.

:::

## History

The framework begins with Jerzy Neyman — published under the name
Jerzy Splawa-Neyman — whose 1923 Polish essay on agricultural
experiments, translated by Dabrowska and Speed for *Statistical
Science* in 1990, introduced a double-indexed array of unknown
potential yields, one index for the variety and one for the plot, of
which only one yield per plot would be observed
{{cite:splawa_neyman1990}} (p. 465). Neyman's setting was the randomised
experiment, and his problem was the variance of a difference of variety
means; the correlation between the potential yields of two varieties on
the same plot could not be estimated, because the pair is never jointly
observed — an early statement of the fundamental problem in algebraic
form {{cite:splawa_neyman1990}} (pp. 465–466).

Donald Rubin generalised the framework from 1974 onwards, extending it
to observational studies and making the assignment mechanism central;
Ding and Li's review traces it to Neyman (1923) and Rubin's papers of
1974, 1977 and 1978 {{cite:ding_li2018}} (pp. 214–215). Holland's 1986
exposition, "Statistics and Causal Inference", presented the model —
drawn from his joint work with Rubin and Rubin's 1974 paper — to a
general audience, named the fundamental problem, and presented the
framework throughout as "Rubin's model"
{{cite:holland1986}} (pp. 945, 947). Rubin's 2005 summary, "Causal
Inference Using Potential Outcomes", is a mature statement of the same
programme {{cite:rubin2005}} (p. 322).
