## Lead context
Two crossed factors separate variation due to each factor from variation in how their effects combine. Replication within every cell provides a residual variance estimate distinct from interaction.{{cite:dodge2008}} (pp. 544–545)

## Motivating example
Two treatments are applied at each of two temperatures, with two independent experimental units in every combination. A treatment difference may grow with temperature. Averaging over temperature can conceal that interaction, so a two-factor analysis starts with cell means rather than assuming that treatment differences are constant.{{cite:nist_two_way_anova2002}} (§7.4.3.7, model with interaction)

## Properties — Why balanced sums of squares add
For $a$ levels, $b$ levels and $r$ replicates per cell, use
$$
Y_{ijk}=\mu+\alpha_i+\beta_j+\gamma_{ij}+\varepsilon_{ijk},
$$
with zero sums for each main effect and for every row and column of the interaction. Decompose each centred observation into its row mean deviation, column mean deviation, interaction mean deviation, and within-cell residual. In a balanced design the cross-products vanish because the relevant row, column or within-cell sums are zero. This proves $SS_T=SS_A+SS_B+SS_{AB}+SS_E$. The component dimensions are $a-1$, $b-1$, $(a-1)(b-1)$ and $ab(r-1)$, whose sum is $abr-1$.{{cite:nist_two_way_anova2002}} (§7.4.3.7, sums-of-squares and degrees-of-freedom table)

Independent Gaussian errors with a common variance make these orthogonal sums of squares independent scaled chi-squared variables under the appropriate nulls. Dividing each effect mean square by the error mean square gives the corresponding $F$ test. Independence, equal variance and the distinction between repeated measurements and independent replicates concern the experimental units, not merely the table's shape.{{cite:dodge2008}} (p. 545)

## Worked example
Take the four cells $(8,10)$, $(12,14)$, $(11,13)$ and $(19,21)$, ordered first by the two levels of factor A and within each by the levels of B. Cell means are $9,13,12,20$, and the grand mean is $13.5$. Row means are $11,16$ and column means $10.5,16.5$. Thus
$$
SS_A=50,\quad SS_B=72,\quad SS_{AB}=8,\quad SS_E=8,\quad SS_T=138.
$$
The zero-sum interaction effects are $(1,-1,-1,1)$. Error degrees of freedom are $4$, giving $MS_E=2$. Each effect has one degree of freedom, so the three ratios are $25$, $36$ and $4$, on $F_{1,4}$. Their upper tails are approximately $0.00749$, $0.00388$ and $0.11612$. The treatment difference changes between temperatures, but the interaction test has little residual information with only two units per cell.{{cite:nist_two_way_anova2002}} (§7.4.3.7, $F$ ratios)

**Your turn.** Add $5$ to every observation. What happens to the grand mean, interaction effects and four sums of squares?

::: {.callout-tip collapse="true" title="Answer"}
The grand mean becomes $18.5$. All centred differences, interaction effects and sums of squares stay the same.
:::

## Assumptions and limits
With one observation per cell, a full interaction model fits every cell exactly and leaves no pure-error degrees of freedom. An additive model then treats the omitted interaction as part of error, an extra modelling restriction. With unequal cell counts, the balanced orthogonal decomposition does not automatically apply, and different sequential or adjusted sums of squares can answer different questions. Coding constraints identify coefficients; they do not create replication.{{cite:dodge2008}} (pp. 544–545)
