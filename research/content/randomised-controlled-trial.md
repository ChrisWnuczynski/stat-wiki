## Lead context
Random assignment gives treatment comparisons a probability model; the realised groups can still differ by chance.

## Motivating example
A treatment group improves more than a control group. Without knowing how treatment was assigned, that difference may reflect differences between the people who received each option. For binary treatment, random allocation with the same treatment probability across baseline covariates makes assignment marginally independent of those covariates under the allocation design. If treatment is randomised using stratum-specific probabilities, assignment is independent of potential outcomes within the design strata; marginal exchangeability is not guaranteed, so causal contrasts for the target group must account for that design.{{cite:hernan_robins2020}} (§2.2, pp. 17–18) It supplies a basis for causal comparison, provided outcomes and follow-up support that comparison.{{cite:openintro2019}} (§1.4.1, principles of experimental design)

## Definition — An assigned intervention and a comparison group
A randomised controlled trial assigns experimental units to interventions by a random procedure and compares outcomes across the assigned groups. The control can receive a placebo, usual care, or another active intervention. Randomisation, replication and control address different parts of the design; a large sample does not replace random assignment. Blinding can reduce expectations and assessment differences after assignment.{{cite:openintro2019}} (§§1.4.1–1.4.2)

The allocation procedure must be specified. Simple random assignment, a fixed-size completely randomised allocation, and blocked assignment induce different distributions over treatment groups. Allocation concealment concerns knowledge before assignment; blinding concerns knowledge after assignment. Reporting should make both mechanisms assessable.{{cite:schulz_altman_moher2010}} (p. 2, Tbl. 1, items 8–11)

## Properties — Balance is an expectation
For $n$ fixed participants, let $Y_i(1)$ and $Y_i(0)$ denote outcomes under the two assignments, with no interference between participants and a consistently defined intervention. A completely randomised design selects $n_1$ treated participants uniformly, with $0<n_1<n$. The difference in observed group means estimates
$$
\tau=\frac1n\sum_i\{Y_i(1)-Y_i(0)\}.
$$
To verify its unbiasedness, write the treated mean as $n_1^{-1}\sum_i A_iY_i(1)$. Each indicator has expectation $n_1/n$, so its expectation is the population average of the fixed $Y_i(1)$ values. The same calculation for controls gives the average of $Y_i(0)$, and subtraction gives $\E(\widehat\tau)=\tau$. This calculation averages over assignments; it does not make the two observed groups identical.{{cite:openintro2019}} (§1.4.1, randomisation)

The same argument shows that a pre-treatment covariate's difference in group means has expectation zero. A particular allocation can nevertheless produce a substantial imbalance. Recording prognostic covariates supports precision, description of participants and assessment of applicability. Reporting baseline characteristics and the numbers analysed remains informative after randomisation.{{cite:schulz_altman_moher2010}} (p. 2, Tbl. 1, items 15–17)

## Assumptions and limits — Assignment does not prevent every bias
Comparing participants by assigned treatment targets an effect of assignment, often called an intention-to-treat comparison. Nonadherence can make that differ from an effect of actually receiving treatment. Missing outcomes, unequal measurement and exclusions after allocation can undermine a simple comparison of observed means. The numbers assigned, treated and analysed, and reasons for losses, are therefore part of interpreting the result. Random sampling from a wider population is a further design question.{{cite:schulz_altman_moher2010}} (pp. 2–3, Tbl. 1, items 13, 16, 20–21)

## Worked example
Four participants have control outcomes $(1,2,3,4)$ and treatment outcomes $(3,4,5,6)$. Each participant's effect is $2$. Assign exactly two to treatment, giving $\binom42=6$ equally likely allocations. In lexicographic order of the treated pairs, the observed differences in means are
$$
0,\quad1,\quad2,\quad2,\quad3,\quad4.
$$
Their average is $2$, the finite-group average treatment effect, and their randomisation variance is $5/3$. Even with a constant treatment effect, one possible experiment observes a difference of zero. Chance imbalance is sampling variation under the allocation, rather than proof that randomisation has failed.{{cite:openintro2019}} (§1.4.1, randomisation and blocking)

**Your turn.** Instead form blocks $\{1,2\}$ and $\{3,4\}$ and independently select one treated participant per block. What are the four possible differences?

::: {.callout-tip collapse="true" title="Answer"}
The treated pairs are $\{1,3\},\{1,4\},\{2,3\},\{2,4\}$, giving differences $1,2,2,3$. Their mean is still $2$, while their variance is $1/2$. Blocking reduces assignment variation in this particular example because the blocks group similar control outcomes.
:::

## Check yourself
### What makes an experiment randomised? {#self-check-ex-da-devil-tumours}
[Facial tumours in Tasmanian devils](../questions/ex-da-devil-tumours.qmd): identify the design and what further details matter.

::: {.callout-tip collapse="true" title="Answer"}
Investigators assign medicine, so it is a designed experiment. The description does not establish random allocation, concealment, blinded tumour assessment or equal handling of controls. The response can be tumour-size change or final size adjusted for baseline; it is quantitative. Assigned medicine is a categorical explanatory variable with two levels.
:::

### A placebo-controlled allocation {#self-check-ex-da-motn-insomnia}
[A dose comparison for insomnia](../questions/ex-da-motn-insomnia.qmd): classify the intervention and outcome variables.

::: {.callout-tip collapse="true" title="Answer"}
Random allocation to placebo, low dose and high dose defines a randomised controlled experiment. Total sleep time is the quantitative response, conceptually a nonnegative continuous duration. The three named dose levels are ordered categories; actual milligram doses could also be analysed as quantitative levels under a specified model.
:::
