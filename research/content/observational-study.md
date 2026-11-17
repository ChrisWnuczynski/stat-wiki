## Motivating example
A hospital observes a higher complication rate among patients receiving treatment A than among patients receiving treatment B. The clinicians chose treatment rather than assigning it by a random device. If A was preferentially prescribed to patients with more severe illness, the crude difference mixes treatment choice with the severity of the cases. An observational design describes how that comparison arose; the word observational does not specify a particular regression model.{{cite:openintro2019}} (§1.3.4, “Observational studies”)

## Definition — Record an exposure without assigning it
An observational study measures exposures and outcomes whose allocation is outside the investigator's intervention. Records may be collected prospectively as events unfold or retrospectively from records of events that have occurred. A study can contain measurements collected in both ways. In an experiment, investigators deliberately vary a factor; random assignment is a further design feature, rather than part of every intervention's definition.{{cite:openintro2019}} (§§1.2.5, 1.3.4){{cite:nist_doe_intro2002}} (§5.1.1, experimental design)

The observational unit and the target population should be specified before describing an association. Repeated measurements of one person are several records but one person. A hospital convenience sample describes its observed patients directly; generalising to every patient in a region needs a sampling or transport argument. Random sampling concerns who enters the study. Random treatment allocation concerns which condition each enrolled unit receives. Those are separate operations.{{cite:openintro2019}} (§§1.3.1, 1.3.3–1.3.5)

## Interpretation — Conditioning changes the comparison
For binary exposure $A$, outcome $Y$ and risk stratum $Z$, the crude risk is
$$P(Y=1\mid A=a)=\sum_z P(Y=1\mid A=a,Z=z)P(Z=z\mid A=a).$$
The weights can differ by exposure group. Consequently a crude risk difference need not have the same sign as every stratum-specific risk difference. This follows from summing over the observed strata, without requiring a causal model. Confounding is a reason to investigate the difference in weights and the process that produced it; a regression coefficient alone cannot establish that the relevant confounders have been measured.{{cite:openintro2019}} (§1.3.4, confounding)

A standardised descriptive risk uses a common specified set of non-negative weights $w_z$ summing to one: $R_a^{\mathrm{std}}=\sum_z w_zP(Y=1\mid A=a,Z=z)$. The interpretation is the model's comparison at that common stratum mix. Calling it a treatment effect additionally requires that the within-stratum comparison identifies what treatment assignment would change. In particular, recording a covariate does not ensure adequate overlap between treatment groups or remove measurement error in that covariate.

## Worked example — Opposite crude and standardised signs
Consider a hypothetical set of 200 records. A has 80 high-risk patients with 40 complications and 20 low-risk patients with 2 complications. B has 20 high-risk patients with 12 complications and 80 low-risk patients with 16 complications. The crude rates are $42/100=0.420$ and $28/100=0.280$, so A's crude excess is $0.140$.

Within the high-risk stratum the rates are $0.500$ for A and $0.600$ for B; within the low-risk stratum they are $0.100$ and $0.200$. A's rate is smaller in both strata. Giving each stratum weight $1/2$ produces $R_A^{\mathrm{std}}=0.300$ and $R_B^{\mathrm{std}}=0.400$, a difference of $-0.100$. The sign reversal arises because A contains many more high-risk patients, not because arithmetic within either stratum has changed. This numerical construction illustrates the confounding mechanism described for observational comparisons.{{cite:openintro2019}} (§1.3.4)

**Your turn.** Give the high-risk stratum weight $1/4$ and the low-risk stratum weight $3/4$. Calculate both standardised risks.

::: {.callout-tip collapse="true" title="Answer"}
The risks are $0.25(0.5)+0.75(0.1)=0.200$ for A and $0.25(0.6)+0.75(0.2)=0.300$ for B. Their difference remains $-0.100$ because the stratum-specific differences are equal.
:::

## Assumptions and limits — A design description precedes a causal claim
Comparability has to be argued using the subject matter and the data-collection process. Relevant questions include why the exposure was chosen, whether outcomes were measured in the same way in both groups, which units were missing, and whether follow-up depended on exposure or outcome. Prospective collection can improve temporal ordering and measurement, but does not itself randomise the exposure. Retrospective collection is similarly a timing description, rather than a proof that a result is biased.{{cite:openintro2019}} (§1.3.4, prospective and retrospective studies)

Deliberately varying a process input answers a different design question from observing inputs that operators selected in routine production. Uncontrolled factors still require attention in an experiment, and deliberate manipulation alone should not be confused with random allocation. Reporting the allocation and observation mechanisms makes the scope of the comparison assessable.{{cite:nist_doe_intro2002}} (§5.1.1, controlled inputs and uncontrolled factors)
