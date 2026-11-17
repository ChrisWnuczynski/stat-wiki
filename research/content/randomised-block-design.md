## Lead context
A randomised block design assigns every treatment inside each block, so that a nuisance difference between blocks is not mistaken for a treatment effect.

## Motivating example
Four laboratory tips can look interchangeable if the coupons they measure are ignored. Coupon 4 may read high under every tip. A one-way analysis folds that coupon shift into the error and can miss a tip difference that is consistent once the coupon is held fixed. Blocking keeps the coupon in the model.{{cite:dodge2008}} (p. 447)

## Intuition — Hold the nuisance still, then randomise
A block is a group of experimental units that are similar before any treatment is applied. Every treatment appears in every block, and the assignment inside the block is random. Comparisons of treatments are then made within blocks. Differences between blocks are removed from the treatment contrast instead of inflating the residual. Randomisation inside the block is what keeps the remaining uncontrolled factors from lining up with a treatment.{{cite:dodge2008}} (p. 447){{cite:nist_randomized_block}} (§5.3.3.2, blocking)

## Definition — One observation per cell
With $b$ blocks and $t$ treatments, and one observation in every cell,
$$
Y_{ij}=\mu+\beta_i+\tau_j+\varepsilon_{ij},
$$
where $\sum_i\beta_i=0$, $\sum_j\tau_j=0$, and the errors are independent and $N(0,\sigma^2)$. The block effects $\beta_i$ and the treatment effects $\tau_j$ are fixed. The design is complete when every treatment appears in every block, and incomplete when some block–treatment pairs are absent.{{cite:dodge2008}} (p. 447){{cite:nist_randomized_block}} (§5.3.3.2, model)

The sums of squares for a complete design with one observation per cell split the total as
$$
\mathrm{SS}_{\mathrm{total}}=\mathrm{SS}_{\mathrm{blocks}}+\mathrm{SS}_{\mathrm{treatment}}+\mathrm{SS}_{\mathrm{error}},
$$
with
$$
\mathrm{SS}_{\mathrm{blocks}}=t\sum_i(\overline Y_{i\cdot}-\overline Y)^2,\qquad
\mathrm{SS}_{\mathrm{treatment}}=b\sum_j(\overline Y_{\cdot j}-\overline Y)^2.
$$
The error sum of squares has $(b-1)(t-1)$ degrees of freedom. The treatment $F$ ratio is the treatment mean square over the error mean square.

## Worked example
Three blocks and two treatments give the responses
$$
\begin{array}{c|cc}
 & A & B \\ \hline
1 & 4 & 7 \\
2 & 5 & 6 \\
3 & 6 & 8
\end{array}
$$
The grand mean is $6$. The block means are $5.5$, $5.5$ and $7$. The treatment means are $5$ and $7$. Then $\mathrm{SS}_{\mathrm{treatment}}=6$, $\mathrm{SS}_{\mathrm{blocks}}=3$ and $\mathrm{SS}_{\mathrm{error}}=1$, and $6+3+1=10=\mathrm{SS}_{\mathrm{total}}$. The treatment mean square on $1$ degree of freedom is $6$, the error mean square on $2$ degrees of freedom is $0.5$, and $F=12$. The upper tail probability of $F_{1,2}$ beyond $12$ is $0.074$. At level $0.05$ the treatment contrast is not declared, despite a two-unit gap in the treatment means, because two error degrees of freedom make the reference distribution very wide.

**Your turn.** Using the same table, compute the block $F$ ratio and its two degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
The block mean square is $3/2=1.5$ and the error mean square is $0.5$, so $F=3$ on $(2,2)$ degrees of freedom. The block sum of squares is smaller than the treatment sum of squares, and it is spread over two degrees of freedom rather than one.
:::

## Connections — Nuisance factors and the error term
[Blocks in analysis of variance](blocks-in-analysis-of-variance.qmd) are the same device in the linear model: a factor one does not want to interpret as a treatment. A [randomised controlled trial](randomised-controlled-trial.qmd) randomises without this grouping. Blocking is worthwhile when the nuisance factor is large enough to shrink the error mean square by more than the degrees of freedom it spends. If the blocks are themselves a sample from a wider population, the block term is a random effect rather than a fixed shift.{{cite:nist_randomized_block}} (§5.3.3.2, nuisance factors)

## Check yourself

### A zero residual
Two treatments in two blocks read $3,5$ in the first block and $4,6$ in the second. Find $\mathrm{SS}_{\mathrm{error}}$.

::: {.callout-tip collapse="true" title="Answer"}
Every block shows the same treatment gap of $2$, and the block shift is $1$. The additive fit reproduces every cell, so $\mathrm{SS}_{\mathrm{error}}=0$. The error still has $(2-1)(2-1)=1$ degree of freedom; the sum of squares on that degree of freedom happens to be zero because the treatment gap is the same in both blocks.
:::

### Where randomisation happens
In a complete block design, which assignments are randomised, and which grouping is fixed before the experiment?

::: {.callout-tip collapse="true" title="Answer"}
The blocks are formed from units that are already alike. Inside each block the treatments are assigned at random. The comparison of treatments is then within blocks, and the randomisation is what justifies treating the remaining within-block differences as error.
:::
