## Motivating example
A hardness tester's tip should be compared with other tips on comparable metal. If one coupon is harder under every tip, treating coupon-to-coupon variation as measurement noise can conceal a stable difference between tips. Blocking compares treatments within a common coupon before combining those comparisons.{{cite:taback2022_design}} (§5.8, randomized block designs)

## Properties — Orthogonal treatment, block and residual variation
In a complete balanced design with $b$ blocks and $t$ treatments, each cell contributes once. Let $r_i=\bar Y_{i\cdot}-\bar Y$, $c_j=\bar Y_{\cdot j}-\bar Y$ and $e_{ij}=Y_{ij}-\bar Y_{i\cdot}-\bar Y_{\cdot j}+\bar Y$. Then $Y_{ij}-\bar Y=r_i+c_j+e_{ij}$. The block and treatment deviations each sum to zero, while every row and column of $e$ sums to zero. Summing cross-products therefore gives
$$
SS_T=t\sum_i r_i^2+b\sum_j c_j^2+\sum_{i,j}e_{ij}^2.
$$
The component dimensions are $b-1,t-1,(b-1)(t-1)$, whose sum is $bt-1$. This is an algebraic decomposition for any complete rectangular data table.{{cite:taback2022_design}} (§5.8.1)

Normal additive modelling adds a distributional interpretation. Under independent $N(0,\sigma^2)$ errors, orthogonal coordinates in the treatment, block and residual subspaces are independent normals. The treatment component is centred under equal treatment effects, giving the exact treatment $F_{t-1,(b-1)(t-1)}$ null law. A block effect may be nonzero without invalidating that treatment test: it lies in an orthogonal subspace.{{cite:taback2022_design}} (§§5.8–5.9){{cite:pishro_nik2014}} (§6.1.5, normal random vectors)

## Assumptions and limits — Additivity is a substantive restriction
With only one observation per cell, a separate unrestricted block-by-treatment interaction and a residual error term cannot both be estimated. The additive model assumes a common treatment contrast across blocks. Crossed lines or systematic patterns in residuals can signal departures. Blocking also consumes $b-1$ residual degrees of freedom, so a smaller residual sum of squares does not guarantee a smaller residual mean square or greater power in every dataset.{{cite:taback2022_design}} (§5.9)

Fixed block effects describe these particular blocks. A random-effects model describes a sampled block population and introduces variance components. Random allocation within a block protects the treatment comparison in the experimental design; introducing block labels after observing outcomes does not create that randomisation.{{cite:taback2022_design}} (§§5.2 and 5.8–5.9)

## Worked example — A contrast after accounting for coupons
For the four-coupon hardness table, $SS_{\rm coupon}=0.825$, $SS_{\rm tip}=0.385$ and $SS_E=0.080$. The residual mean square is $0.080/9=0.00888889$, giving treatment $F=(0.385/3)/(0.080/9)=14.4375$, with $p=0.00087127$. Without blocks, the same treatment sum of squares is compared with $(0.825+0.080)/12=0.0754167$, giving $F=1.70166$. The gain comes from explaining substantial coupon variation.{{cite:taback2022_design}} (§§5.8.1 and 5.9)

The mean difference of tip 4 minus tip 3 is $9.875-9.450=0.425$. Under the additive independent-error model its standard error is $\sqrt{2MS_E/b}=0.0666667$. A single pre-specified 95% interval is $0.425\pm t_{9;0.975}(0.0666667)=(0.27419,0.57581)$. Simultaneously examining many pairwise intervals requires a multiple-comparison procedure.{{cite:taback2022_design}} (§§5.6 and 5.9)

**Your turn.** Add $5$ to every reading on coupon 4. Which sums of squares for the treatment test change?

::: {.callout-tip collapse="true" title="Answer"}
The treatment and residual sums of squares are unchanged: row shifts cancel from column contrasts and the double-centred residuals. The block sum of squares changes. The treatment $F$ statistic stays $14.4375$.
:::

## Check yourself
### Reconstruct the hardness table {#self-check-ex-inf-hardness}
[Tips and coupons](../questions/ex-inf-hardness.qmd) compares the blocked and unblocked analyses.

::: {.callout-tip collapse="true" title="Answer"}
The blocked residual sum of squares is $1.290-0.825-0.385=0.080$ on nine degrees of freedom. Dividing the tip mean square by $0.080/9$ gives $14.4375$. Omitting coupon effects gives error $0.905$ on twelve degrees of freedom and $F\approx1.70$.
:::

### Two treatments reduce to paired differences {#self-check-ex-inf-paired-f}
[Two treatments in blocks](../questions/ex-inf-paired-f.qmd) connects the tests.

::: {.callout-tip collapse="true" title="Answer"}
If $D_i=Y_{i1}-Y_{i2}$, then $SS_{\rm treatment}=b\bar D^2/2$ and $MS_E=s_D^2/2$. Their ratio is $b\bar D^2/s_D^2=T^2$. The upper-tail $F_{1,b-1}$ critical value is the square of the two-sided paired-$t$ critical value.
:::
