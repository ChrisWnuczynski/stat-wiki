## Motivating example
A researcher wants to know whether a fertiliser increases wheat yield. The treatment is a specified fertiliser dose given to a plot; the comparison condition might be no fertiliser. Yield is the response measured later. If the researcher gives fertiliser to plots that already have richer soil, a higher observed mean need not come from the fertiliser. Randomly assigning plots makes the treatment comparison informative about an effect, while the outcome measurement and target population still need careful definition.{{cite:dodge2008}} (p. 541, “Treatment”){{cite:hernan_robins2020}} (Ch. 2, §2.1)

## Intuition
A treatment can be a single factor level, such as a dose, or a combination of levels, such as a particular dose plus irrigation schedule. It must be specified well enough that another investigator could say what each unit would receive. In a trial, the assignment is a deliberate action; in an observational study, the analogous variable may record an exposure people chose or happened to receive. Calling both variables $A$ does not make their comparisons equally interpretable.{{cite:dodge2008}} (p. 541, “Treatment”){{cite:hernan_robins2020}} (Ch. 1, §§1.1–1.2; Ch. 3, §3.4)

## Definition
Write $A_i=1$ when plot $i$ receives the fertiliser and $A_i=0$ for control. Let $Y_i(1)$ and $Y_i(0)$ denote its yield under those two conditions. The individual effect is $Y_i(1)-Y_i(0)$, though only one of these outcomes is observed for each plot. The average treatment effect over $N$ plots is $N^{-1}\sum_i\{Y_i(1)-Y_i(0)\}$. These expressions require the two conditions and the response time to be defined; otherwise the counterfactual outcomes are ambiguous.{{cite:hernan_robins2020}} (Ch. 1, §§1.1–1.2; Ch. 3, §§3.4–3.5)

## Interpretation
The treatment label alone does not specify what caused an outcome. A “drug” condition needs dose, timing, adherence rules and a comparison condition; a “teaching method” needs enough detail to distinguish its implementation from other versions. Under consistency, the observed outcome of a unit receiving condition $a$ is its outcome $Y_i(a)$ under that specified condition. The same treatment can have different effects on different units, so a population average does not describe every individual effect.{{cite:hernan_robins2020}} (Ch. 1, §§1.1–1.2; Ch. 3, §§3.4–3.5)

## Properties
For a complete random assignment of $n_1$ of $N$ units to treatment, with $n_0=N-n_1$ controls, the observed difference in group means is unbiased over the random assignments for the average effect in these $N$ units. This does not say the difference from any single assignment equals the effect. It requires each unit's potential outcomes to be fixed under the assignment and no unit's outcome to depend on which treatment other units receive.{{cite:hernan_robins2020}} (Ch. 2, §2.1, randomization and exchangeability)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $\widehat\tau=n_1^{-1}\sum_i A_iY_i(1)-n_0^{-1}\sum_i(1-A_i)Y_i(0)$. Every unit has assignment probability $\mathbb E_A A_i=n_1/N$ and $\mathbb E_A(1-A_i)=n_0/N$. Holding all potential outcomes fixed and taking expectation over assignments gives
$$
\mathbb E_A\widehat\tau
=\frac1N\sum_iY_i(1)-\frac1N\sum_iY_i(0)
=\frac1N\sum_i\{Y_i(1)-Y_i(0)\}.
$$
Thus unbiasedness comes from the assignment mechanism, not from observing both outcomes for a unit.{{cite:hernan_robins2020}} (Ch. 2, §2.1)
:::
:::

## Statistical use
A protocol should identify the experimental unit, the treatment levels, the assignment rule, the outcome and its measurement time. [Facial tumours in Tasmanian devils](../questions/ex-da-devil-tumours.qmd) asks which condition the investigators controlled and which response they measured. [What a randomised trial does not need to record](../questions/ex-da-blood-pressure-covariates.qmd) explores why randomized assignment balances pre-treatment predictors in expectation. A trial may still measure them to improve precision, assess subgroup effects or detect chance imbalance. In an observational comparison, measured covariates can support adjustment only under additional exchangeability, positivity and consistency assumptions.{{cite:hernan_robins2020}} (Ch. 2, §2.1; Ch. 3, §§3.2–3.5)

## Worked example
Twelve plots are randomly split into six fertiliser and six control plots. The treated yields are $12,11,15,14,10,13$ tonnes and the control yields are $9,8,11,10,7,9$. Their sums are $75$ and $54$, so their means are $12.5$ and $9$ tonnes. The observed difference is $3.5$ tonnes per plot. Under the complete random assignment described above, this difference is an unbiased estimate of the average effect across these twelve plots, although chance allocation of good soil can make this particular difference larger or smaller than that effect. No individual plot's effect can be read directly from these data.{{cite:hernan_robins2020}} (Ch. 1, §1.2; Ch. 2, §2.1)

**Your turn.** Four plots assigned a new fertiliser yield $8,9,7,10$ tonnes, and four control plots yield $6,7,5,8$. Calculate the two group means and their observed difference. Does that difference reveal the effect on every plot?

::: {.callout-tip collapse="true" title="Answer"}
The treated sum is $34$, so its mean is $34/4=8.5$ tonnes. The control sum is $26$, so its mean is $26/4=6.5$ tonnes. The observed difference is $2$ tonnes per plot. It estimates an average contrast under the assignment assumptions; it does not reveal any individual effect because each plot supplies only one of its two potential outcomes.{{cite:hernan_robins2020}} (Ch. 1, §§1.1–1.2; Ch. 2, §2.1)
:::

## Common misconceptions
A treatment is the condition applied, whereas the response is the measurement that may change. Random assignment makes treatment independent of pre-treatment traits over assignments, but a particular small trial can still have imbalanced groups. A statistically significant difference is not automatically an important effect, and a non-significant difference does not show the treatment has no effect. An exposure in observational data can be studied causally when its intervention and identification assumptions are defensible, even though its treatment was not randomized.{{cite:hernan_robins2020}} (Chs. 1–3)

## Assumptions and limits
If plots share runoff water, fertiliser on one plot could change a neighboring control plot's yield, violating the no-interference condition used in the proof. If the “treatment” combines several drug doses chosen by clinicians, the recorded binary indicator may mix different interventions and undermine consistency. If all high-risk patients receive the drug, an observational dataset has no comparable untreated high-risk patients; positivity fails there. Random assignment does not fix attrition after assignment or make a convenience sample representative of a wider population.{{cite:hernan_robins2020}} (Ch. 3, §§3.2–3.5)

## Connections
[Designed experiments](designed-experiment.qmd) specify and assign conditions; [randomised controlled trials](randomised-controlled-trial.qmd) implement that logic in a clinical setting. [Confounding](confounding-variable.qmd) explains why an observational treatment contrast can differ from an effect. [Analysis of variance](one-way-analysis-of-variance.qmd) organizes mean comparisons across several treatment levels, while a [randomised block design](randomised-block-design.qmd) restricts assignment within similar groups. The treatment question comes first: a precise effect needs precise conditions to compare.{{cite:dodge2008}} (p. 541, “Treatment”){{cite:hernan_robins2020}} (Chs. 1–3)

## History
Neyman applied counterfactual reasoning to randomized agricultural experiments in 1923. Rubin extended the potential-outcome framework to observational studies in 1974, where the assignment mechanism cannot simply be assumed to be random. These developments explain why the same treatment contrast has a direct randomization argument in a trial but needs further assumptions in observational data.{{cite:hernan_robins2020}} (Ch. 2, §2.1, historical note; Ch. 3, §3.2, historical note)
