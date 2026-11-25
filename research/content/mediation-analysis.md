## Lead context

Mediation analysis is the set of methods used to answer a question that a
total effect, on its own, cannot answer: not merely whether an exposure
changes an outcome, but how much of that change travels along a particular
pathway. The exposure is denoted $A$, the outcome $Y$, and the mediator
$M$, where a mediator is a variable that lies on a causal path from $A$ to
$Y$, so that the structure under study is $A \rightarrow M \rightarrow Y$
alongside any path from $A$ to $Y$ that does not pass through $M$.
Mediation analysis separates the total effect of $A$ on $Y$ into a part
transmitted through $M$, called an indirect effect, and a part transmitted
by every other route, called a direct effect. VanderWeele's
practitioner's guide describes the field in exactly these terms, as
analyses used to assess the relative magnitude of different pathways and
mechanisms by which an exposure may affect an outcome
{{cite:vanderweele2016}} (p. 17). The qualifier "causal" matters
throughout: the decomposition is a decomposition of a [causal](causality.qmd)
effect, defined by contrasts of potential outcomes, and it inherits causal
assumptions considerably stronger than those needed for the total effect
alone.

The distinction between a mediator and two other kinds of third variable
must be kept clear from the outset. A [confounding variable](confounding-variable.qmd)
is a common cause of $A$ and $Y$ that sits before the exposure, off the
path from $A$ to $Y$; it creates association that is not effect, and the
remedy is to adjust for it. A mediator sits after the exposure, on the
path; adjusting for it in the ordinary way does not remove bias but
changes the question, because part of the effect has been deliberately
blocked. A moderator, or effect modifier, is different again: it is a
variable across whose levels the size of an effect varies, and it need not
be caused by the exposure at all. Baron and Kenny, whose 1986 paper set
the vocabulary, defined the mediator function as that of a third variable
which "represents the generative mechanism through which the focal
independent variable is able to influence the dependent variable of
interest", in contrast to the moderator function, which partitions a
predictor into subgroups in which its effect is strongest
{{cite:baron_kenny1986}} (p. 1173).

## Motivating example — Through this pathway, or by other routes?

Consider a training programme, assigned as $A = 1$ against a comparison
condition $A = 0$, intended to improve an outcome $Y$ by first raising
participants' confidence or skill, $M$, which then improves the outcome.
Two policy conclusions hang on the split. If most of the total effect runs
through $M$, a cheaper intervention that moves $M$ directly might capture
much of the benefit, and a version of the programme that fails to move $M$
should be expected to fail overall. If most of the effect bypasses $M$,
then $M$ is a side-show, and optimising the programme should target the
other routes. A third possibility is that the two parts have opposite
signs, so the total effect can be small even though both components are
large, a configuration called inconsistent mediation.

The total effect itself is the familiar [average treatment effect](average-treatment-effect.qmd):
for binary $A$, it is $\E[Y^{1}] - \E[Y^{0}]$, where $Y^{1}$ denotes the
outcome a unit would show under $A = 1$, $Y^{0}$ the outcome under
$A = 0$, and $\E[\cdot]$ denotes expectation over the population in
question. Mediation analysis refines this single number into a pair of
numbers, defined using potential outcomes involving the mediator, that
add back to the total. Everything difficult about the subject is
contained in two observations. First, the relevant potential outcomes are
nested: they involve the outcome under one exposure level combined with
the mediator value that would have arisen under a possibly different
exposure level, and no unit is ever observed in such a crossed condition.
Second, because the mediator is not ordinarily assigned by the
investigator, the split requires assumptions about confounding of the
mediator–outcome relation that randomising $A$ does not supply. Robins
and Greenland established the second point in 1992: even in a randomised
crossover trial of the exposure, direct and indirect effects cannot be
separated without special assumptions, because randomising the exposure
does not randomise the intermediate variable
{{cite:robins_greenland1992}} (p. 143).

## Intuition — The Baron and Kenny steps, and what they do not do

For roughly two decades, the dominant applied procedure was the sequence
of regressions proposed by Baron and Kenny. In their path diagram, the
exposure affects the mediator along a path labelled $a$, the mediator
affects the outcome, with the exposure held in the equation, along a path
labelled $b$, and the exposure affects the outcome directly along a path
labelled $c'$ in the equation containing the mediator, while the total
association, from the equation without the mediator, is labelled $c$. A
variable was said to function as a mediator when three conditions held:
variations in the exposure significantly account for variations in the
mediator; variations in the mediator significantly account for variations
in the outcome; and, when the $a$ and $b$ paths are controlled, a
previously significant relation between exposure and outcome is no longer
significant, with the strongest demonstration occurring when the residual
direct path is zero {{cite:baron_kenny1986}} (pp. 1176–1177).
Operationally, the procedure estimates three regression equations: the
mediator on the exposure; the outcome on the exposure; and the outcome on
both, with separate coefficients estimated and tested in each
{{cite:baron_kenny1986}} (p. 1177). If the conditions hold in the
predicted direction, the effect of the exposure on the outcome must be
smaller in the third equation than in the second, and mediation was
declared complete when the exposure had no remaining effect with the
mediator controlled, and partial otherwise {{cite:baron_kenny1986}} (p. 1177).

The procedure's influence is not in doubt, and as a heuristic for
organising a path diagram it remains serviceable. Its defects, however,
are structural. The first defect is that the steps never estimate or test
the quantity of interest. The indirect effect is a specific number — in
linear models, the product $ab$ — yet the causal steps procedure reaches
a verdict from a sequence of significance tests on other coefficients,
without computing that number or its standard error. MacKinnon and
Fairchild note this directly: the method does not explicitly provide a
numerical value for the strength of the mediated effect
{{cite:mackinnon_fairchild2009}} (pp. 16–17).

The second defect is power. Because the verdict requires several tests to
be significant jointly, including a test of the total effect $c$, the
procedure can fail to detect mediation that is present. Simulation work
summarised by MacKinnon and Fairchild shows that the ability to detect
mediated effects with the causal-steps method can be very low, and that in
one study the approach required approximately 21,000 subjects for adequate
power when the $a$ and $b$ paths were both small and the whole effect was
mediated {{cite:mackinnon_fairchild2009}} (pp. 16–17). The requirement of
a significant total effect is also wrong in principle: mediation can exist
when the total effect is null, because a positive indirect effect and a
negative direct effect can cancel — the inconsistent-mediation
configuration, in which the sign of $ab$ differs from the sign of $c'$, so
the overall relation is zero although mediation is present
{{cite:mackinnon_fairchild2009}} (pp. 16–17).

The third defect is the deepest. The steps are stated in the language of
significance and coefficient shrinkage, but the conclusions drawn from
them were causal: that the mediator is the mechanism. Nothing in the three
regressions states the assumptions under which a coefficient attached to a
non-randomised mediator has a causal reading. Imai, Keele and Tingley
locate the problem in the linear structural equation framework itself: it
provides no general definition of causal mediation effects independent of
a particular statistical model, makes it impossible to specify the key
identification assumption cleanly, and resists extension to nonlinear
models {{cite:imai_keele_tingley2010}} (p. 309). The modern treatment
therefore begins again from potential outcomes, defines the direct and
indirect effects without reference to any regression, and only then asks
which regressions, if any, estimate them. The counterfactual definitions
come next in this article; the linear case, taken up after them, is the
special case in which the old and new approaches coincide.

## Definition — Natural direct and indirect effects

The counterfactual framework defines the components before any model is
fitted. Let $M^{a}$ denote the value the mediator would take for a unit if
the exposure were set to $A = a$, for $a$ equal to $0$ or $1$. Let
$Y^{a, m}$ denote the outcome the unit would show if the exposure were set
to $a$ and, separately, the mediator were set to the value $m$. Combining
the two notations gives the nested counterfactual $Y^{a, M^{a'}}$: the
outcome under exposure level $a$, when the mediator is held not at a fixed
number but at whatever value it would naturally have taken under exposure
level $a'$. The word "nested" is literal: the counterfactual for the
mediator under one condition is inserted inside the counterfactual for
the outcome under a possibly different condition. Imai, Keele and Tingley
build their definitions from the same ingredients, writing the potential
outcome as a function of both treatment and mediator value and defining
the unit-level mediation effect by changing the mediator from its value
under control to its value under treatment while holding the treatment
status fixed {{cite:imai_keele_tingley2010}} (pp. 311–312).

With $a = 1$ for the active exposure and $a = 0$ for the comparison, the
natural direct effect is

$$\text{NDE} = \E[Y^{1, M^{0}} - Y^{0, M^{0}}],$$

and the natural indirect effect is

$$\text{NIE} = \E[Y^{1, M^{1}} - Y^{1, M^{0}}].$$

Each definition rewards slow reading. In the natural direct effect, the
exposure changes from $0$ to $1$ in the first superscript, while the
mediator is pinned, in both terms, to $M^{0}$, the value it would have
taken under no exposure. The contrast therefore captures every route from
$A$ to $Y$ except the route that operates by changing $M$, because $M$ is
frozen at its untreated value, which differs from person to person,
rather than at a common constant. In the natural indirect effect, the
first superscript is $1$ in both terms, so the exposure itself does not
change; only the mediator moves, from $M^{0}$ to $M^{1}$. That contrast
captures exactly the part transmitted by the exposure's action on the
mediator, evaluated in the treated condition. Adding the two definitions,
the shared term $\E[Y^{1, M^{0}}]$ cancels, leaving

$$\text{NDE} + \text{NIE} = \E[Y^{1, M^{1}}] - \E[Y^{0, M^{0}}]
= \E[Y^{1}] - \E[Y^{0}],$$

where the last equality uses the composition property that the outcome
under exposure $a$ with the mediator at its natural value under $a$ is
simply the outcome under exposure $a$. On the difference scale, therefore,
the total effect is exactly the natural direct effect plus the natural
indirect effect — the counterfactual counterpart of the identity
$c = c' + ab$, and under the linear model with no interaction the two
coincide, with $\text{NDE} = c'$ and $\text{NIE} = ab$. Imai, Keele and
Tingley record the corresponding decomposition in their notation: the
total effect splits into causal mediation and direct components, and
under a no-interaction assumption the average mediation and average
direct effects sum to the average total effect
{{cite:imai_keele_tingley2010}} (p. 312). Their labels differ
slightly — the average causal mediation effect for the indirect component
and the average direct effect for the direct component — but the
quantities are the natural effects defined above.

The nested counterfactual $Y^{1, M^{0}}$ deserves emphasis because it is
the source of both the definitions' appeal and their fragility. It
describes a cross-world condition: the same unit is simultaneously under
exposure, for the purposes of the outcome, and under no exposure, for the
purposes of the mediator. No experiment on that unit observes it directly,
because observing the mediator under no exposure requires the unit to be
unexposed. Pearl, who gave the natural effects their modern formulation,
was explicit that the descriptive, natural reading asks what would happen
while holding a mediating variable at the level it would have attained
under the reference condition, in contrast to the prescriptive reading in
which the variable is fixed at a predetermined level
{{cite:pearl2001}} (§2.2, p. 413). Whether the mean of such a quantity can
be recovered from ordinary data at all is the identification question
taken up below; the definitions themselves are meaningful whether or not
a given data set can identify them.

A companion definition avoids one layer of nesting by fixing the mediator
outright. The controlled direct effect at mediator level $m$ is

$$\text{CDE}(m) = \E[Y^{1, m} - Y^{0, m}],$$

the mean effect of the exposure when every unit's mediator is set, by
intervention, to the same value $m$. Robins and Greenland's early
analysis already worked with effects defined by controlling, that is
blocking, the intermediate variable by a suitable intervention
{{cite:robins_greenland1992}} (p. 143), and Pearl's prescriptive
interpretation of direct effects — the response of the outcome to the
exposure with all other factors held fixed at a specified level — is the
controlled direct effect {{cite:pearl2001}} (§3.2, p. 415). The controlled
and natural direct effects answer different questions. The controlled
direct effect is a family of quantities, one for each $m$, corresponding
to a conceivable joint intervention: set the exposure, and set the
mediator to $m$ for everyone. The natural direct effect is a single
quantity that leaves the mediator at each person's own untreated value.
When there is no exposure–mediator interaction, the controlled direct
effect is the same at every $m$ and equals the natural direct effect, as
in the linear model above, where both are $c'$. When interaction is
present, $\text{CDE}(m)$ varies with $m$, and the two can support
different policy conclusions: a controlled direct effect speaks to a
programme that also fixes the mediator, whereas a natural direct effect
speaks to attribution of an observed total effect between pathways. There
is no controlled analogue of the natural indirect effect of the same
standing.

## Interpretation — The linear case: the product of coefficients

Suppose the mediator and outcome are each linear in their inputs, with no
interaction between exposure and mediator. Write the mediator equation as

$$M = \alpha_0 + a A + \varepsilon_M,$$

where $\alpha_0$ is an intercept, $a$ is the coefficient of the exposure in
the mediator equation, and $\varepsilon_M$ is an error term with mean zero,
and write the outcome equation as

$$Y = \beta_0 + c' A + b M + \varepsilon_Y,$$

where $\beta_0$ is an intercept, $c'$ is the coefficient of the exposure in
the outcome equation with the mediator included, $b$ is the coefficient of
the mediator in that equation, and $\varepsilon_Y$ is an error term with
mean zero. MacKinnon and Fairchild present the single-mediator model in
precisely this three-equation form, with $c$ for the total coefficient,
$c'$ for the direct coefficient, $b$ for the mediator-to-outcome
coefficient and $a$ for the exposure-to-mediator coefficient
{{cite:mackinnon_fairchild2009}} (p. 16).

Substituting the mediator equation into the outcome equation gives
$\beta_0 + c' A + b(\alpha_0 + a A + \varepsilon_M) + \varepsilon_Y$,
which collects into an equation for $Y$ in terms of $A$ alone with
coefficient $c' + ab$ on $A$. Hence, in this model, the total effect of a
one-unit change in $A$ is

$$c = c' + ab,$$

exactly, with no remainder. The indirect effect is the product of
coefficients $ab$: the exposure moves the mediator by $a$ units, each unit
of the mediator moves the outcome by $b$ units, and the composition of the
two linear steps multiplies. The direct effect is $c'$, the coefficient
that remains when the mediator is in the equation. MacKinnon and Fairchild
state the same accounting: a direct effect quantified by $c'$, a mediated
or indirect effect quantified by $ab$, equivalently by the difference in
coefficients $c - c'$, and a total effect computed by adding the two parts
{{cite:mackinnon_fairchild2009}} (p. 16). The two computations of the
indirect effect — product and difference — agree in this model because
both are algebraic rearrangements of the same substitution.

Three qualifications convert this tidy algebra into a causal claim, and
none is delivered by the algebra. First, the coefficients must have
causal interpretations, which requires the confounding assumptions set
out below, in particular for the mediator–outcome relation. Second, the
absence of an $A$-by-$M$ interaction term is load-bearing: if the outcome
equation contained a term $d A M$, the mediator's effect would be $b + d$
under exposure and $b$ under no exposure, and no single product $ab$
would describe the indirect effect. Third, linearity itself is doing
work: with a binary outcome modelled on a logit scale, coefficients do
not compose by substitution, the product and difference methods diverge,
and the decomposition must be defined at the level of potential-outcome
means. Imai, Keele and Tingley's general framework was built for exactly
this reason: to give the definition, identification, estimation and
sensitivity analysis of causal mediation effects without reference to any
specific statistical model, accommodating linear and nonlinear
relationships and continuous and discrete mediators and outcomes
{{cite:imai_keele_tingley2010}} (p. 309).

Inference for the product has one quirk: the sampling distribution of a
product of two estimated coefficients is not in general normal, so
normal-based limits for $ab$ can be inaccurate; limits based on the
distribution of the product, and resampling methods, are more accurate
{{cite:mackinnon_fairchild2009}} (p. 17).

## Properties — Identification: the four confounding assumptions

A causal reading of the natural direct and indirect effects requires,
first, that four confounding conditions hold, conditional on the measured
pre-exposure covariates, denoted $C$, being adjusted for — and, as set out
after the four conditions, three further requirements that are not
confounding conditions at all. VanderWeele's guide gives attention
throughout to the confounding assumptions required for a causal
interpretation of direct and indirect effect estimates
{{cite:vanderweele2016}} (p. 17). Stated plainly, the conditions are as
follows. There must be no unmeasured confounding of the exposure–outcome
relation: given $C$, no omitted variable may jointly cause $A$ and $Y$.
There must be no unmeasured confounding of the exposure–mediator relation:
given $C$, no omitted variable may jointly cause $A$ and $M$. There must
be no unmeasured confounding of the mediator–outcome relation: given $C$
and $A$, no omitted variable may jointly cause $M$ and $Y$. And there must
be no mediator–outcome confounder that is itself affected by the exposure:
no variable, measured or unmeasured, may be caused by $A$ and also cause
both $M$ and $Y$, or cause $Y$ in a way that entangles it with the
mediator's effect in the manner described below.

The first three conditions parallel the exchangeability condition for a
total effect, applied three times, and randomising $A$ delivers the first
two by design. The third is the one randomisation of $A$ cannot deliver,
because the mediator is a post-exposure variable that units effectively
select into. Imai, Keele and Tingley package the conditions as sequential
ignorability: given observed pre-treatment covariates, the treatment is
independent of all potential values of the outcome and the mediator; and
the observed mediator is independent of all potential outcomes given the
observed treatment and the pre-treatment covariates
{{cite:imai_keele_tingley2010}} (p. 312). Unlike the ignorability of
treatment assignment, the ignorability of the mediator may fail even in
randomised experiments, because randomising the treatment does not
randomly assign the post-treatment mediator
{{cite:imai_keele_tingley2010}} (p. 312).

The four confounding conditions, even taken together, are not a complete
identification recipe; three further requirements must hold, and each can
fail on its own. **Consistency and composition.** The observed mediator
and outcome must be the counterfactual ones generated by the exposure
actually received: for a unit with $A = a$, $M = M^{a}$ and $Y = Y^{a,
M^{a}}$, and composition must hold, $Y^{a} = Y^{a, M^{a}}$ — the outcome
under exposure $a$ is the outcome under exposure $a$ with the mediator at
the value it naturally takes under $a$. The decomposition of the total
effect into natural direct and indirect parts uses exactly this equality.
**Treatment positivity.** Each exposure level must occur with positive
probability for every covariate pattern in the population: $0 < P(A = a
\mid C = c) < 1$ for both levels $a$ and every $c$ that occurs. Failure
here does not make the contrasts undefined: the counterfactual contrast
for units of that type is a perfectly definite quantity, but it is not
identified from these data, because no unit of that type is ever observed
under the missing level, so any estimate would be extrapolation rather
than evidence. **Mediator support across
treatment levels.** The nested counterfactual $Y^{1, M^{0}}$ evaluates the
outcome under exposure $1$ at mediator values drawn from the distribution
under exposure $0$, so those values must be possible under exposure $1$ as
well. The condition is one of support, stated on the values the mediation
formula integrates over: for a discrete mediator, every value $m$ with
positive probability under the reference level, given $C$, must also have
positive probability under the evaluation level; for a continuous
mediator the probability of any single value is zero even when overlap is
perfectly adequate, and the condition is instead that every such $m$ lie
in the support of the mediator under the evaluation level — positive
density there, given $C$. This cross-level support condition can fail by
construction, and when it does the failure is fatal in a way confounding
is not. Suppose binary $A$ is randomised, so the first two confounding
conditions hold by design, but the mediator simply is the exposure, $M =
A$. The observed data then contain only the combinations $(A, M) = (0, 0)$
and $(1, 1)$; the crossed combination $(1, 0)$ that $Y^{1,
M^{0}}$ requires never occurs — and neither does $(0, 1)$, the crossed
combination the mirror-image counterfactual $Y^{0, M^{1}}$ would require.
Two outcome models fit the observed triplet
$(A, M, Y)$ identically. If $Y = M$, the natural direct effect is $\E[Y^{1,
M^{0}} - Y^{0, M^{0}}] = 0$ and the natural indirect effect is $\E[Y^{1,
M^{1}} - Y^{1, M^{0}}] = 1$: the pair $(0, 1)$. If $Y = A$, the natural
direct effect is $1$ and the natural indirect effect is $0$: the pair $(1,
0)$. The observed data cannot distinguish a wholly mediated effect from a
wholly direct one, because the off-diagonal combinations are missing — so
the natural effects are not identified, however completely the confounding
conditions are satisfied. Imai, Keele and Tingley state sequential
ignorability as their Assumption 1 together with the positivity
requirements used here {{cite:imai_keele_tingley2010}} (p. 312).

The fourth condition is the one most often omitted from applied reports.
Suppose a variable $L$ is caused by the exposure and in turn causes both
the mediator and the outcome — for instance, a side effect of treatment
that influences both adherence, the mediator, and the health outcome. Then
$L$ is a mediator–outcome confounder affected by the exposure.
Conditioning on $L$ is necessary to deconfound $M$ and $Y$, but $L$ sits
on a causal path from $A$, so conditioning on it distorts the exposure's
contribution; and the nested counterfactual $Y^{1, M^{0}}$ mixes a world
in which $L$ takes its treated value with a mediator drawn from the
untreated world. The natural direct and indirect effects are then not
identified from the observed data without further structure, even if $L$
is measured. This is the cross-world difficulty: identification requires
an assumption about the joint behaviour of quantities from two different
intervention worlds, which no data pattern can verify. Controlled direct
effects are in a stronger position here, because fixing $M$ to $m$ by
intervention defines a single-world quantity, and a measured $L$ does not
by itself block its identification. But the adjustment for $L$ has to be
the right one. Simply entering $L$ as one more regressor in a pooled
outcome regression alongside $A$ and $M$ is not itself the error — a
fitted regression averages over no distribution of $L$ at all. The error
is in how the fitted model is then used: reading the controlled effect
off its coefficients, or averaging its predictions over the sample's
pooled distribution of $L$, mixes the two arms' $L$ distributions into
one that belongs to neither arm, and blocks the part of the exposure's
effect that runs through $L$ itself. Which distribution of $L$ an
estimate averages over is decided by the prediction and standardisation
step, not by the regression. The correct adjustment is
treatment-specific standardisation, the g-formula for this setting: for
each exposure level $a$ separately, average the outcome mean $\E[Y \mid
A = a, M = m, L, C]$ over the distribution of $L$ under that same
exposure level, $P(L \mid A = a, C)$, then average the result over the
target population's distribution of the baseline covariates $C$, and
contrast the two standardised means only afterwards. Each arm keeps its
own $L$ distribution, because under the intervention that sets $A = a$
and $M = m$, $L$ would still take the values that exposure level $a$
produces. This identifies the population controlled direct effect under
assumptions stated for the controlled effect itself, rather than the
stronger natural-effect assumptions above: consistency; treatment
exchangeability given $C$, so that each arm's distribution of $L$ and
its outcomes are the ones that arm itself would produce; and
mediator–outcome exchangeability given $A$, $L$ and $C$, with $L$ among
the covariates deconfounding the mediator–outcome relation. The support
conditions are arm-specific: treatment positivity given $C$, and the
mediator value $m$ in the support of $M$ given $A = a$, $L$ and $C$ on
the histories each arm's standardisation uses — for a continuous
mediator, positive density at $m$ together with the usual regularity
there, since the fixed value $m$ itself has probability zero. The price
of the controlled effect remains that it
answers the narrower, prescriptive question.

Because the third and fourth conditions are untestable, sensitivity
analysis has a standing place in a competent mediation analysis. The
question it asks is quantitative: how strong would an unmeasured
mediator–outcome confounder have to be before the estimated indirect
effect would shrink to zero or change sign? Imai, Keele and Tingley
develop sensitivity analysis as an integral part of their framework, so
that researchers can state how severe a violation would need to be for
the original conclusions to be reversed
{{cite:imai_keele_tingley2010}} (p. 310). VanderWeele's guide likewise
introduces sensitivity analysis techniques for unmeasured confounding and
measurement error as part of the practitioner's toolkit
{{cite:vanderweele2016}} (p. 17).

## Statistical use — Interaction, and the proportion mediated

Exposure–mediator interaction means that the effect of the mediator on
the outcome differs by exposure level. In the outcome equation it appears
as a product term, $dAM$, and its presence dismantles several conveniences
at once. The product-of-coefficients formula fails, because the mediator's
coefficient is $b$ in one exposure arm and $b + d$ in the other, so the
indirect effect depends on the arm in which it is evaluated. The natural
effects remain well defined — the definitions above never assumed
interaction away — but they now come in two versions of each quantity,
depending on the reference condition. The natural and controlled direct
effects also remain different estimands: the controlled effect fixes the
mediator at a chosen $m$ for everyone, while the natural effect averages
over the mediator's own distribution under the reference condition. In
this article's linear model the two can nevertheless take the same
value: with outcome equation $Y = \beta_0 + c' A + b M + d A M +
\varepsilon_Y$, the controlled direct effect is $\text{CDE}(m) = c' +
dm$, while the natural direct effect with reference condition $0$ is
$c' + d\,\E[M^{0}]$ — the controlled direct effect evaluated at $m =
\E[M^{0}]$, whenever that value is a supported mediator level. The
estimands differ even when the values coincide. The counterfactual
definitions earn their keep precisely here. VanderWeele's guide presents
methods from the causal inference literature for conducting mediation
analysis in the presence of exposure–mediator interactions, alongside
binary outcomes, binary mediators and case-control designs
{{cite:vanderweele2016}} (p. 17). VanderWeele also developed a four-way
decomposition of the total effect, into components due to mediation
alone, interaction alone, both, and neither; it is mentioned here only to
mark that the two-way split of this article is a deliberate simplification
when interaction is present.

The proportion mediated is the ratio of the indirect effect to the total
effect, $\text{NIE} / (\text{NDE} + \text{NIE})$ on the difference scale,
equivalently $ab / c$ in the linear model. It is the number most often
quoted from a mediation analysis and the number most often misread. It is
interpretable as a proportion only when the direct and indirect effects
have the same sign and the total is not close to zero. When the signs
differ — inconsistent mediation — the ratio leaves the interval from zero
to one and stops describing a share of anything. If the direct effect is
$0.5$ and the indirect effect is $-0.3$, the total is $0.2$ and the ratio
is $-0.3 / 0.2 = -1.5$: "negative 150 per cent of the effect is mediated"
is arithmetically correct and substantively meaningless. The components,
not the ratio, carry the finding in such a case.
The proportion mediated also inherits a scale dependence: computed on a
ratio scale it need not agree with the proportion on the difference
scale. The safe practice is to report the total, direct and indirect
effects themselves, with intervals, and to add the proportion mediated
only when the signs align and the total is estimated well away from zero.

## Worked example — A linear system and its counterfactual check

A programme is evaluated with $A = 1$ for participation and $A = 0$ for
the comparison condition. The mediator $M$ is a skill score and the
outcome $Y$ is a later performance score. Suppose the structural
equations, with errors of mean zero, are

$$M = 2 + 0.5 A + \varepsilon_M, \qquad
Y = 1 + 0.3 A + 0.8 M + \varepsilon_Y.$$

In the notation of the linear section, the exposure-to-mediator
coefficient is $a = 0.5 = 1/2$, the mediator-to-outcome coefficient is
$b = 0.8 = 4/5$, and the direct coefficient is $c' = 0.3 = 3/10$. There
is no interaction term. The indirect effect is the product

$$ab = \frac{1}{2} \times \frac{4}{5} = \frac{2}{5} = 0.4,$$

the direct effect is $c' = 3/10 = 0.3$, and the total effect is

$$c = c' + ab = \frac{3}{10} + \frac{2}{5} = \frac{7}{10} = 0.7.$$

The proportion mediated is $ab / c = (2/5) / (7/10) = 4/7 \approx 0.571$,
about $57.1\%$. Both components are positive, so the proportion is a
legitimate share here. The controlled direct effect at any mediator level
$m$ is also $0.3$, because with no interaction the exposure's coefficient
does not depend on $m$.

The same numbers can be recovered, and checked, from the counterfactual
definitions. The mean mediator values under the two conditions are
$\E[M^{0}] = 2$ and $\E[M^{1}] = 2 + 1/2 = 5/2 = 2.5$. The nested
counterfactual means, computed from the outcome equation by inserting the
relevant exposure value and the relevant mean mediator value, are
$\E[Y^{0, M^{0}}] = 1 + 0.8 \times 2 = 13/5 = 2.6$,
$\E[Y^{1, M^{0}}] = 1 + 0.3 + 0.8 \times 2 = 29/10 = 2.9$, and
$\E[Y^{1, M^{1}}] = 1 + 0.3 + 0.8 \times 2.5 = 33/10 = 3.3$. Therefore

$$\text{NDE} = \frac{29}{10} - \frac{13}{5} = \frac{3}{10} = 0.3,
\qquad
\text{NIE} = \frac{33}{10} - \frac{29}{10} = \frac{2}{5} = 0.4,$$

and $\text{NDE} + \text{NIE} = 3/10 + 2/5 = 7/10 = 0.7$, matching the
total effect from the coefficient calculation and the direct contrast
$\E[Y^{1}] - \E[Y^{0}] = 33/10 - 13/5 = 7/10$. The natural direct effect
agrees with $c'$ and the natural indirect effect agrees with $ab$, as the
no-interaction linear model requires. The agreement is a property of this
model, not of mediation in general: the counterfactual quantities remain
defined when the model is enriched, while the coefficients then cease to
suffice.

### Your turn

A second programme has mediator and outcome equations with no interaction
and coefficients $a = 0.8$, $b = 0.5$ and $c' = 0.1$. Its nested
counterfactual means are $\E[Y^{0, M^{0}}] = 1.0$,
$\E[Y^{1, M^{0}}] = 1.1$ and $\E[Y^{1, M^{1}}] = 1.5$. Compute the indirect
effect as a product of coefficients, the total effect, the proportion
mediated, and the natural direct and indirect effects, and confirm that
the two routes agree.

::: {.callout-tip collapse="true" title="Answer"}

The indirect effect is $ab = 0.8 \times 0.5 = 0.4$. The total effect is
$c = c' + ab = 0.1 + 0.4 = 0.5$. The proportion mediated is
$0.4 / 0.5 = 0.8$, that is $4/5$ or $80\%$. From the counterfactual
means, the natural direct effect is $1.1 - 1.0 = 0.1$, which equals $c'$,
and the natural indirect effect is $1.5 - 1.1 = 0.4$, which equals $ab$.
Their sum is $0.1 + 0.4 = 0.5$, the total effect, so the two routes agree,
as they must in a linear model with no interaction.

:::

## Common misconceptions — Mediation is not moderation

The closing distinction is the one with which Baron and Kenny began.
Mediation concerns a variable on the causal path: the exposure causes the
mediator, and the mediator causes the outcome, so the mediator answers
the question of how or why an effect occurs. Baron and Kenny's summary is
that mediators speak to how or why effects occur, whereas moderator
variables specify when certain effects will hold
{{cite:baron_kenny1986}} (p. 1176). Moderation, in current usage effect
modification, concerns a variable across whose levels the effect itself
differs. A moderator is typically a pre-exposure characteristic — a
baseline severity, an age band, a genotype — that the exposure does not
cause; it is not on the path, and the analysis asks whether the effect of
$A$ on $Y$ is larger in one stratum than another. Statistically, mediation
in the linear case is a product of coefficients along a chain, whereas
moderation is a product term inside a single equation, an interaction.
The two can coexist, but they answer different questions. A [causal diagram](causal-diagram.qmd)
makes the distinction visual: the mediator is a node with an arrow in
from $A$ and an arrow out to $Y$, while a moderator has no arrow from $A$
into it. Methods for adjusting total effects, such as the
[propensity score](propensity-score.qmd), do not transfer automatically to
mediation: weighting that balances the exposure groups does nothing to
deconfound the mediator, which is assigned by no one. The
[potential outcomes](potential-outcomes.qmd) framing used throughout this
article is what keeps the three roles — confounder, mediator, moderator —
from collapsing into the single vague category of "third variable".

## Connections

- [Causality](causality.qmd) — mediation analysis decomposes a causal
  contrast of potential outcomes, not a merely associational one.
- [Average treatment effect](average-treatment-effect.qmd) — the total
  effect that the natural direct and indirect effects sum to on the
  difference scale.
- [Potential outcomes](potential-outcomes.qmd) — the framework in which
  $M^{a}$, $Y^{a, m}$ and the nested counterfactual $Y^{a, M^{a'}}$ are
  defined.
- [Causal diagram](causal-diagram.qmd) — the graph $A \rightarrow M
  \rightarrow Y$ displays the mediator's position.
- [Confounding variable](confounding-variable.qmd) — the four
  identification conditions are confounding conditions on the three
  relations, plus the ban on exposure-induced mediator–outcome
  confounding.
- [Propensity score](propensity-score.qmd) — a balancing method for the
  exposure contrast; it does not deconfound the mediator.

## Check yourself

1. In the worked example, the coefficients are $a = 1/2$, $b = 4/5$ and
$c' = 3/10$. What are the indirect effect, the total effect and the
proportion mediated, and why is the proportion mediated interpretable as
a share in this example?

::: {.callout-tip collapse="true" title="Answer"}

The indirect effect is $ab = (1/2)(4/5) = 2/5 = 0.4$. The total effect is
$c' + ab = 3/10 + 2/5 = 7/10 = 0.7$. The proportion mediated is
$(2/5)/(7/10) = 4/7 \approx 0.571$, about $57.1\%$. It is interpretable as
a share because the direct and indirect effects have the same sign and
the total is well away from zero.

:::

2. A colleague randomises the exposure, fits the three Baron and Kenny
regressions, finds every step significant, and reports the product $ab$
as "the causal effect through the mediator". Which assumption has the
randomisation not supplied, and which further assumption do the natural
effects need even if that one holds?

::: {.callout-tip collapse="true" title="Answer"}

Randomisation of the exposure supplies exchangeability for the
exposure–outcome and exposure–mediator relations, but it does not
randomise the mediator, so it does not supply the assumption of no
unmeasured confounding of the mediator–outcome relation given the
exposure and measured covariates. Even if that assumption holds, the
natural effects additionally require that there be no mediator–outcome
confounder affected by the exposure — the cross-world condition —
because the nested counterfactual combines the mediator from the
unexposed world with the outcome under exposure.

:::

3. An analysis reports a direct effect of $0.5$, an indirect effect of
$-0.3$ and a proportion mediated of $-150\%$. Is the arithmetic wrong,
and how should the result be reported?

::: {.callout-tip collapse="true" title="Answer"}

The arithmetic is correct: the total effect is $0.5 + (-0.3) = 0.2$, and
$-0.3 / 0.2 = -1.5$. The interpretation is the problem. This is
inconsistent mediation, in which the pathway through the mediator offsets
part of the direct effect, so the ratio is not a share of the total and
the percentage should not be reported as one. Report instead the
components — a direct effect of $0.5$, an indirect effect of $-0.3$ and a
total effect of $0.2$.

:::

## History

The vocabulary of mediation in the social sciences was fixed by Baron and
Kenny's 1986 article in the *Journal of Personality and Social
Psychology*, volume 51, issue 6, pages 1173–1182, which distinguished the
moderator and mediator functions of third variables at conceptual,
strategic and statistical levels {{cite:baron_kenny1986}} (p. 1173). The
causal-steps procedure in that article dominated applied practice for
many years, and the path-analytic tradition behind it supplied the
product-of-coefficients formula that MacKinnon and others developed into
a testing literature, including work on the non-normal distribution of
the product and on the low power of the causal steps
{{cite:mackinnon_fairchild2009}} (pp. 16–17).

The counterfactual turn came from epidemiology and computer science
independently. Robins and Greenland, in *Epidemiology* in 1992, volume 3,
issue 2, pages 143–155, asked when direct and indirect effects are
identifiable at all, and showed that adjusting for the intermediate
variable — the most common method of estimating direct effects — can be
biased, and that direct and indirect effects are not separately
identifiable when only the exposure is randomised
{{cite:robins_greenland1992}} (p. 143). Pearl's 2001 paper "Direct and
indirect effects", in the *Proceedings of the Seventeenth Conference on
Uncertainty in Artificial Intelligence*, pages 411–420, gave the natural
direct and indirect effects their structural counterfactual formulation,
distinguishing the descriptive natural effects from the prescriptive
controlled effects and establishing conditions under which the natural
effects can be estimated from experimental and non-experimental data
{{cite:pearl2001}} (pp. 411–420). Imai, Keele and Tingley then unified
definition, identification, estimation and sensitivity analysis in a
model-free framework in 2010, with sequential ignorability as the
identifying assumption {{cite:imai_keele_tingley2010}} (pp. 309–312).
VanderWeele's work, including his 2015 book and the 2016 practitioner's
guide in the *Annual Review of Public Health*, volume 37, pages 17–32,
carried the counterfactual definitions into routine epidemiological
practice, with regression-based methods for interactions, binary variables
and sensitivity analysis presented for direct implementation
{{cite:vanderweele2016}} (p. 17).
