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
With one observation per cell, a full interaction model has a parameter for every cell mean. The fitted values match the observations and the residual sum of squares is zero, so there is no pure-error mean square to put in the denominator of an $F$ ratio. An additive model, which drops the interaction, then uses the interaction sum of squares as its residual. That is a modelling restriction: the error variance and the interaction are tied together. Unequal cell counts remove the balance that made the row, column and interaction contrasts orthogonal, and sequential sums of squares then depend on the order of the factors. Coding constraints choose one basis for the same column space; they leave the residual degrees of freedom unchanged.{{cite:dodge2008}} (pp. 544–545)

## Definition — Cell means, main effects and interaction
With $a$ levels of factor A, $b$ levels of factor B and $r$ independent replicates in every cell, the saturated cell-mean model gives each pair $(i,j)$ its own mean $\mu_{ij}$. The two-factor decomposition writes
$$
\mu_{ij}=\mu+\alpha_i+\beta_j+\gamma_{ij},
$$
with $\sum_i\alpha_i=0$, $\sum_j\beta_j=0$, and zero row and column sums for $\gamma_{ij}$. These constraints pick one set of coefficients for a description that, before the constraints, is unchanged by moving a constant between $\mu$, $\alpha$, $\beta$ and $\gamma$. The interaction term $\gamma_{ij}$ is the part of the cell mean that remains after the row and column structure has been removed. In the worked $2\times2$ table the cell means are $9,13,12,20$, the grand mean is $13.5$, and the interaction effects are $(1,-1,-1,1)$. The within-row differences for factor B are $13-9=4$ and $20-12=8$. The difference of those differences is $4$. Under the zero-sum constraints the interaction effect in each cell is that contrast divided by $4$, hence $\pm1$, with signs that alternate.{{cite:nist_two_way_anova2002}} (§7.4.3.7, model with interaction)

The error term $\varepsilon_{ijk}$ is the deviation of replicate $k$ from its cell mean. Its sum of squares uses the $r-1$ free deviations in each of the $ab$ cells, hence $ab(r-1)$ degrees of freedom. In the worked table $r=2$ and $ab=4$, so the error degrees of freedom are $4$ and $MS_E=8/4=2$.

## Interpretation — Orthogonal pieces in a balanced table
Balance makes the four sums of squares add to the total sum of squares about the grand mean. For the worked observations the pieces are $50$, $72$, $8$ and $8$, and $50+72+8+8=138$. Each main-effect piece has one degree of freedom in a $2\times2$ layout, and the interaction has $(2-1)(2-1)=1$. Dividing by $MS_E=2$ produces the ratios $25$, $36$ and $4$. Under independent Gaussian errors with a common variance, and under the corresponding null that a given effect is zero, each ratio has an $F_{1,4}$ law, with upper tails $0.00749$, $0.00388$ and $0.11612$. The interaction tail is the largest of the three because the interaction sum of squares is the smallest effect piece and the residual information is only four degrees of freedom.{{cite:nist_two_way_anova2002}} (§7.4.3.7, $F$ ratios)

Adding $5$ to every observation moves the grand mean from $13.5$ to $18.5$ and leaves every centred deviation unchanged. Row effects, column effects, interaction effects and all four sums of squares are invariant under that shift. A change of measurement origin is absorbed by $\mu$.

The interaction contrast has a direct cell-mean reading. The difference of the within-row B differences is $8-4=4$, and dividing by $4$ recovers the zero-sum effect $1$. Squaring the alternating effects $(1,-1,-1,1)$, weighting by the two replicates, and summing gives $SS_{AB}=2(1^2+1^2+1^2+1^2)=8$, which matches the worked decomposition.

## Intuition — Replication is what estimates pure error
Two units in the same cell see the same factor combination. Their difference estimates noise, on the modelling assumption that the units are independent and share a variance. A second temperature changes the treatment difference from $4$ to $8$ in the cell means. That change is the interaction, and it is estimated from the pattern of cell means. With only one unit in each cell the within-cell difference is unavailable, and the interaction pattern has nothing left to be compared with. Replication and the interaction are different uses of the table: replication fills the error line, and a second factor level is what makes an interaction estimable at all.

## Statistical use — Name the comparison before reading an $F$ ratio
The A ratio $25$ compares row means after the balanced column structure has been removed. The B ratio $36$ does the same for columns. The interaction ratio $4$ asks whether the B difference changes between the rows. A scientific report that quotes one of these ratios names the factor coding, the cell counts, and the residual degrees of freedom. In a balanced table the three numerators are orthogonal, so the order in which the factors are written does not change the sums of squares. In an unbalanced table that invariance fails, and a sequential sum of squares for A after B answers a different question from a sequential sum of squares for A before B.{{cite:nist_two_way_anova2002}} (§7.4.3.7, sums-of-squares and degrees-of-freedom table)

The Gaussian common-variance model supplies the $F$ reference. A large interaction ratio is evidence, under that model, that a single treatment difference is a poor summary of the two temperatures. The worked interaction ratio has tail $0.11612$, so these eight observations leave the interaction compatible with a wide range of $F_{1,4}$ outcomes. More replicates would change $MS_E$ and its degrees of freedom together.

## Common misconceptions
The constraints $\sum_i\alpha_i=0$ and $\sum_j\beta_j=0$ are a coordinate choice. They force the coefficients to describe deviations from a grand mean. A different coding, such as a reference cell, represents the same fitted cell means with different numerical coefficients. The fitted values, the residual sum of squares and the $F$ test of a given subspace are properties of the column space, and they survive a change of basis.

An interaction sum of squares of $8$, equal to the error sum of squares, is sometimes described as “no interaction.” The two sums of squares happen to be equal, and they are estimates of different quantities. The interaction mean square is $8/1=8$ and the error mean square is $2$, so the ratio is $4$. Equality of the raw sums of squares is an accident of the degrees of freedom.{{cite:dodge2008}} (p. 545)
