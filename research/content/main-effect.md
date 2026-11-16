## Motivating example
An agronomist compares two crop varieties under low and high watering. A variety can do better on average yet respond differently to water; one overall variety contrast then leaves out part of the story. A main effect summarizes a factor across the levels of other factors, while the interaction tells us whether that summary represents the same contrast in every condition. This distinction guides both the design and the interpretation of factorial experiments.{{cite:nist_two_way_anova2002}} (§7.4.3.7, two-way factorial model){{cite:nist_interactions2002}} (§3.4.2.3, conditional interpretation)

## Intuition
In a balanced two-factor experiment, first average the responses for each level of factor A across the levels of B. Comparing these marginal means gives an average effect of A. Then compare A's levels separately within each B level. If those simple contrasts agree, the average is representative; if they differ, the interaction matters. In the variety-and-water example, opposite simple contrasts cancel to a zero marginal contrast.{{cite:nist_two_way_anova2002}} (§7.4.3.7, factorial layout){{cite:nist_interactions2002}} (§3.4.2.3, interactions)

## Definition
For a balanced two-factor design with cell means $\mu_{ij}$, an A main-effect contrast between levels $i$ and $i'$ is the difference of their marginal means, $b^{-1}\sum_j\mu_{ij}-b^{-1}\sum_j\mu_{i'j}$, when each B level receives equal weight. The weights must be stated in an unbalanced design; observed sample sizes, equal cell weights and a target-population distribution of B can produce different averages. In the additive model $\mu_{ij}=\mu+\alpha_i+\beta_j$, the simple contrast is $\alpha_i-\alpha_{i'}$ at every B level. With an interaction term $\gamma_{ij}$, it becomes $\alpha_i-\alpha_{i'}+\gamma_{ij}-\gamma_{i'j}$.{{cite:nist_two_way_anova2002}} (§7.4.3.7, two-way model and balanced sums of squares)

A software coefficient named for a main-effect term is coding-dependent. With reference-cell coding and an interaction, the A coefficient measures the A contrast at the reference level of B. Under sum-to-zero constraints in a balanced layout, the corresponding A coefficient can instead describe a marginal deviation. Predicted cell means and explicitly named contrasts remain the interpretable quantities across coding choices.{{cite:nist_two_way_anova2002}} (§7.4.3.7, model terms){{cite:nist_interactions2002}} (§3.4.2.3, conditional effects)

## Properties
The interaction contrast for a two-by-two table is a difference of differences: $\Delta=(\mu_{22}-\mu_{12})-(\mu_{21}-\mu_{11})$. If $\Delta=0$, A's simple effect is the same at both B levels, and the marginal A effect equals each simple effect under equal weighting. If $\Delta\ne0$, the marginal effect averages two different effects. It may be useful as a policy average, but its meaning then depends on the distribution of B over which it is averaged.{{cite:nist_interactions2002}} (§3.4.2.3, unequal simple effects){{cite:nist_two_way_anova2002}} (§7.4.3.7, marginal effects)

The usual ANOVA partition into A, B, interaction and error sums of squares is clean for a balanced design with replication. A factor with more than two levels has several independent main-effect contrasts, so a single omnibus F test does not identify which levels differ. With one observation per cell in a full interaction model there is no separate within-cell error estimate; the interaction sum of squares alone cannot be divided by an error mean square from that model.{{cite:nist_two_way_anova2002}} (§7.4.3.7, sums of squares and degrees of freedom)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
In the additive model, subtracting two cell means at the same B level cancels $\mu$ and $\beta_j$, leaving $\alpha_i-\alpha_{i'}$. Averaging this same quantity over B leaves it unchanged. With interactions, the subtraction leaves $\alpha_i-\alpha_{i'}+\gamma_{ij}-\gamma_{i'j}$; averaging over $j$ gives the marginal contrast. Subtracting the two simple contrasts in a two-by-two table cancels the A main term and leaves $\gamma_{22}-\gamma_{12}-\gamma_{21}+\gamma_{11}$, the displayed difference of differences.{{cite:nist_two_way_anova2002}} (§7.4.3.7, two-way model){{cite:nist_interactions2002}} (§3.4.2.3, interaction definition)

With reference-cell coding, set $\alpha_1=\beta_1=\gamma_{1j}=\gamma_{i1}=0$. The A level-two coefficient is $\mu_{21}-\mu_{11}$ at B level one; at B level two the contrast is $\alpha_2+\gamma_{22}$. This algebra proves why a printed “main effect” coefficient needs its coding and reference condition to be interpreted.{{cite:nist_two_way_anova2002}} (§7.4.3.7, factorial model)
:::
:::

## Statistical use — Reading a factorial comparison
Before reporting one main-effect number, inspect the cell means and their simple contrasts. If they are similar, an averaged contrast is a compact description. If they differ strongly or reverse direction, report the conditional contrasts and the averaging weights as well. Testing an A term after omitting a real A-by-B interaction can answer a different question from testing an A contrast in the full model. The design, coding constraints and order of model comparisons determine which hypothesis a software F statistic represents.{{cite:nist_two_way_anova2002}} (§7.4.3.7, ANOVA table){{cite:nist_interactions2002}} (§3.4.2.3, conditional interpretation)

## Worked example
Suppose mean yields for varieties A0 and A1 are $10$ and $16$ under low water, and $14$ and $24$ under high water. The variety simple effects are $16-10=6$ and $24-14=10$. Equal weighting over water gives variety marginal means $(10+14)/2=12$ and $(16+24)/2=20$, so the A1 main-effect contrast is $8$. The interaction contrast is $10-6=4$: the benefit of A1 is larger under high water. A statement that A1 adds eight yield units on average is accurate for equal water weighting, but it is not the contrast for either water condition.{{cite:nist_two_way_anova2002}} (§7.4.3.7, marginal means){{cite:nist_interactions2002}} (§3.4.2.3, conditional effects)

**Your turn.** In another equally weighted two-by-two experiment, A0 yields $20$ under low B and $25$ under high B; A1 yields $22$ and $35$. Find the two simple A effects, the marginal A effect and their difference of differences.

::: {.callout-tip collapse="true" title="Answer"}
The simple effects are $22-20=2$ at low B and $35-25=10$ at high B. A0's marginal mean is $22.5$, A1's is $28.5$, and their difference is $6$. The interaction contrast is $10-2=8$. The average effect of six hides a much larger benefit at high B.{{cite:nist_interactions2002}} (§3.4.2.3, conditional effects)
:::

## Common misconceptions
A main effect is not necessarily the coefficient carrying its name in a reference-coded regression with interactions; that coefficient is conditional on the reference level. A zero marginal contrast does not imply no effect at every B level, as the variety example shows. A statistically significant main-effect test does not establish a causal effect without an appropriate assignment design and assumptions. Finally, an interaction does not make all averages meaningless: it makes their weighting and conditional interpretation essential.{{cite:nist_interactions2002}} (§3.4.2.3, interaction interpretation){{cite:nist_two_way_anova2002}} (§7.4.3.7, factorial design)

## Assumptions and limits — When averaging misleads
If one water level is rare in the target population, an equal-weight average may not describe the policy population even when it accurately describes a balanced experiment. If the variety effect changes sign across water levels, reporting only the marginal contrast can conceal harm in one condition. If the experiment has no replication in each cell, the full interaction model leaves no pure-error degrees of freedom for a usual ANOVA F test. Each limitation calls for a stated target contrast and an error model suited to the design.{{cite:nist_two_way_anova2002}} (§7.4.3.7, balanced design and error degrees of freedom){{cite:nist_interactions2002}} (§3.4.2.3, conditional effects)

## Connections
An [interaction](interaction.qmd) changes a factor's simple effect across another factor's levels. A [contrast](contrast.qmd) is the explicit linear comparison of means or coefficients; choosing one avoids ambiguity about weights. [Two-factor ANOVA](../notes/inf-15-two-factor-anova.qmd) places main effects, interactions and error variation in one model.{{cite:nist_two_way_anova2002}} (§7.4.3.7)

## History
Fisher's experimental-design work helped establish factorial comparisons and analysis of variance; Dodge lists his 1935 *Design of Experiments* among the major publications. Modern NIST guidance expresses the two-factor design as main effects plus an interaction and emphasizes that a main effect must be interpreted conditionally when interactions are present.{{cite:dodge2008}} (p. 203, Fisher entry){{cite:nist_two_way_anova2002}} (§7.4.3.7){{cite:nist_interactions2002}} (§3.4.2.3)
