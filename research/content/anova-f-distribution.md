## Motivating example
Three treatments produce different sample means, but their observations also vary within each treatment. ANOVA asks whether the separation between means is large relative to the within-treatment noise. A ratio is interpretable only after accounting for the different numbers of degrees of freedom in those two sources of variation.{{cite:taback2022_design}} (§§5.3.1–5.3.6)

## Intuition — Two independent estimates of one noise variance
For independent observations $Y_{ij}=\mu_i+\varepsilon_{ij}$ with $\varepsilon_{ij}\sim N(0,\sigma^2)$, write $N=\sum_i n_i$ and let $k$ be the number of nonempty groups. Define
$$
SS_B=\sum_i n_i(\bar Y_i-\bar Y)^2,\qquad
SS_E=\sum_{i,j}(Y_{ij}-\bar Y_i)^2.
$$
Under equal population means, both $SS_B/(k-1)$ and $SS_E/(N-k)$ estimate $\sigma^2$. A large ratio indicates that between-group variation exceeds the noise estimate. Different group means can enlarge the numerator without enlarging the within-group noise term.{{cite:taback2022_design}} (§§5.3.2–5.3.6)

## Proof
Let $P_G$ project onto vectors constant within groups, and let $P_1=\mathbf1\mathbf1^\top/N$. The matrices $P_G-P_1$ and $I-P_G$ are symmetric orthogonal projections of ranks $k-1$ and $N-k$, and their product is zero. Thus $SS_B=Y^\top(P_G-P_1)Y$ and $SS_E=Y^\top(I-P_G)Y$. Under the null, the common mean lies in the span of $\mathbf1$ and vanishes under both projections.{{cite:taback2022_design}} (§§5.3.2–5.3.6)

Choose orthonormal bases for these mutually orthogonal ranges and complete them to a basis of $\mathbb R^N$. Rotating $\varepsilon/\sigma\sim N_N(0,I)$ into that basis gives independent standard normal coordinates: their joint density remains proportional to $\exp(-\|z\|^2/2)$ and factors. Consequently, $SS_B/\sigma^2$ and $SS_E/\sigma^2$ are independent sums of $k-1$ and $N-k$ squared standard normals. Dividing by their degrees of freedom proves the $F_{k-1,N-k}$ law. The residual result holds also when the means differ, since group means still lie in the range of $P_G$.{{cite:pishro_nik2014}} (§6.1.5, normal random vectors){{cite:taback2022_design}} (§5.3.6)

## Statistical use — What the omnibus test answers
The exact finite-sample law requires independent normal errors with a common variance and $N>k$. Its alternative is that at least one population mean differs; rejection does not identify every differing pair. Planned contrasts and multiplicity-adjusted comparisons answer more specific questions. Unbalanced group sizes are allowed by the projection argument, while unequal error variances change its covariance structure.{{cite:openintro2019}} (§7.5, comparing many means with ANOVA)

## Worked example

### Three groups and six residual degrees of freedom
Consider groups $(1,2,3)$, $(2,3,4)$ and $(5,6,7)$. Their means are $2,3,6$, and the grand mean is $11/3$. Hence
$$
SS_B=3\{(2-11/3)^2+(3-11/3)^2+(6-11/3)^2\}=26,
\quad SS_E=2+2+2=6.
$$
The total sum of squares is $32$. With $k-1=2$ and $N-k=6$, $F=(26/2)/(6/6)=13$, and $\mathbb{P}(F_{2,6}\ge13)=0.0065918$. The evidence concerns equality of the three means under the model. It does not by itself establish a mechanism connecting treatment to outcome.{{cite:taback2022_design}} (§§5.3.6–5.3.7)

**Your turn.** Add $10$ to every observation. What happens to the sums of squares and the test?

::: {.callout-tip collapse="true" title="Answer"}
Every group mean and the grand mean increases by $10$. All centred deviations are unchanged, so $SS_B=26$, $SS_E=6$, $F=13$ and the same $p$-value follow.
:::
