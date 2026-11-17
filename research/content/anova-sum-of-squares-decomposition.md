## Motivating example
Measurements from several machines can vary because machine means differ and because repeated measurements on one machine differ. ANOVA separates these two kinds of sample variation. The sum-of-squares decomposition is an exact identity about the recorded values; probability assumptions enter when its components are used to estimate variances or calibrate a test.{{cite:nist_oneway_anova}} (§3.2.3.1, one-way layout)

## Statement
Let group $i$ contain $n_i$ observations, with mean $\bar y_i$, and let $N=\sum_i n_i$ and $\bar y=\sum_i n_i\bar y_i/N$. Then
$$\underbrace{\sum_i\sum_j(y_{ij}-\bar y)^2}_{\mathrm{SST}}=\underbrace{\sum_i\sum_j(y_{ij}-\bar y_i)^2}_{\mathrm{SSW}}+\underbrace{\sum_i n_i(\bar y_i-\bar y)^2}_{\mathrm{SSB}}.$$
The grand mean is a weighted mean of group means when group sizes differ. The corrected total has $N-1$ degrees of freedom, split into $N-g$ within groups and $g-1$ between $g$ groups.{{cite:dodge2008}} (pp. 399–400, One-Way Analysis of Variance)

## Proof
Write $y_{ij}-\bar y=(y_{ij}-\bar y_i)+(\bar y_i-\bar y)$. Squaring and summing gives a within-group sum, a between-group sum and cross-term
$$2\sum_i(\bar y_i-\bar y)\sum_j(y_{ij}-\bar y_i).$$
Each inner sum is zero by the definition of the group mean. The cross-term therefore vanishes and gives the identity. The between-group term repeats the constant $(\bar y_i-\bar y)^2$ exactly $n_i$ times. This proof applies to unequal group sizes and does not assume normal errors, equal variances or random sampling.{{cite:nist_oneway_anova}} (§3.2.3.1, total, within-level and across-level variation)

## Key results — The F law requires a probability model
Under independent normal observations with a common variance and equal population means, between- and within-group sums of squares, divided by that variance, have independent chi-squared laws. Their mean-square ratio has the one-way ANOVA $F$ reference distribution. Equal-variance and independence assumptions are substantive here: the arithmetic identity alone cannot justify that reference law. A treatment interpretation also needs a suitable design or causal assumptions beyond the identity.{{cite:nist_oneway_anova}} (§3.2.3.1, Testing and Assumptions)

## Worked example
### Unequal groups
Take group one as $(1,3)$ and group two as $(4,5,6)$. The group means are $2$ and $5$, and the grand mean is $19/5=3.8$. Within-group sums are $2$ and $2$, giving $\mathrm{SSW}=4$. The between-group sum is $2(2-3.8)^2+3(5-3.8)^2=10.8$. Directly centring all five measurements at $3.8$ gives $\mathrm{SST}=14.8=4+10.8$. An unweighted average of group means would be $3.5$ and would not yield the corrected-total identity.{{cite:dodge2008}} (pp. 399–400)

The degrees of freedom are $3$ within, $1$ between and $4$ total. If the normal equal-variance model is appropriate, the observed mean-square ratio is $10.8/(4/3)=8.1$. The example computes a statistic; its inferential interpretation depends on the stated model and design.{{cite:nist_oneway_anova}} (§3.2.3.1, ANOVA table)

**Your turn.** Add ten to every observation in the two groups. What are the new sums of squares?

::: {.callout-tip collapse="true" title="Answer"}
All means rise by ten, so every centred deviation stays the same. The within, between and total sums remain 4, 10.8 and 14.8.
:::

## Generalizations — Projection explains the zero cross-term
The fitted vector of group means is the least-squares projection onto vectors constant within each group. Residual deviations are orthogonal to that space. Removing the intercept leaves a between-group contrast space orthogonal to the constant vector. This geometric view explains the additive sums of squares and why the dimensions add to $N-1$. For nonorthogonal multi-factor designs, individual sequential term sums can depend on the order in which models are enlarged.{{cite:nist_ls_straight2002}} (§4.4.3.1, least squares)
