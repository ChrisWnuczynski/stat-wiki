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

## Intuition
Each observation is a deviation from the grand mean. That deviation splits into a deviation of the observation from its group mean, plus the deviation of the group mean from the grand mean. Squaring and summing would normally produce a cross-product. Within each group the deviations from the group mean add to zero, so the cross-product adds to zero as well. The two sums of squares that remain answer different descriptive questions. The within-group sum says how far the replicates sit from their own machine, treatment, or site. The between-group sum says how far those machine means sit from the overall mean, weighted by how many observations each machine contributed.

The weighting is the reason the grand mean is not the average of the group means unless the group sizes agree. Means $2$ and $5$ with sizes $2$ and $3$ have grand mean $(4+15)/5=19/5=3.8$. The unweighted average $3.5$ would be the right centre for a different identity, one that treated each group as a single observation. Using it on the five raw measurements does not make the cross-term vanish, and it does not recover $\mathrm{SST}=\mathrm{SSW}+\mathrm{SSB}$.

## Related concepts — A second numerical check of the identity
Take groups $(0,2)$ and $(6)$. The group means are $1$ and $6$, the grand mean is $(0+2+6)/3=8/3$, and
$$\mathrm{SSW}=(0-1)^2+(2-1)^2=2,$$
$$\mathrm{SSB}=2\left(1-\frac83\right)^2+1\left(6-\frac83\right)^2=\frac{50}{3}.$$
The total sum of squares about $8/3$ equals $56/3$, and $2+50/3=56/3$. The degrees of freedom are $3-2=1$ within groups, $2-1=1$ between groups, and $3-1=2$ overall. Adding ten to every observation shifts every mean by ten and leaves each of these centred sums unchanged. Multiplying every observation by a positive constant $c$ multiplies each sum of squares by $c^2$. The $F$ ratio, which is a ratio of mean squares, is unchanged by an additive shift and unchanged by a common change of units.

The normal-theory $F$ statistic in the first worked example is $10.8/(4/3)=8.1$, on $1$ and $3$ degrees of freedom. That number is a summary of the two sums. Its reference distribution requires independent normal observations, a common variance, and a null of equal population means. The identity $14.8=4+10.8$ does not use those assumptions and remains true for any five numbers with these group labels. A large ratio is a prompt to look at the design. It is not, by the algebra alone, evidence that a treatment caused the group means to differ.{{cite:nist_oneway_anova}} (§3.2.3.1, Testing and Assumptions)

## Common misconceptions
Unequal group sizes are sometimes patched by averaging the group means and then applying a balanced formula. The balanced between-group formula weights each mean by the same $n$. The identity above weights the $i$th mean by $n_i$. Substituting the unweighted mean $3.5$ into the five-observation example changes the total sum of squares and breaks the addition. Software that fits a linear model with a group factor computes the weighted version, because least squares projects onto the group-mean subspace of the actual design.

A significant $F$ ratio is also sometimes read as if every pair of groups differed. The between-group sum is one number, on $g-1$ degrees of freedom. It can be large because one group sits far from the others while the remaining groups agree. Pairwise comparisons need their own contrasts and, if several are examined, a rule for the family of tests. The decomposition still organises the bookkeeping: each contrast of group means is a direction inside the between-group subspace, and the within-group mean square remains the usual variance estimate when the equal-variance model is adopted.

## Statistical use — Residual variance in a one-way design
The same orthogonality appears in the residual vector of a linear model. The hat matrix of a group-factor design is constant on each group, with diagonal entry $1/n_i$ for an observation in group $i$. The residual variance formula $\sigma^2(1-h_{ii})$ is then $\sigma^2(1-1/n_i)$, which is exactly the variance of a deviation from a sample mean of $n_i$ independent observations. Analysis of deviance in a Gaussian model uses the drop in residual sum of squares between nested group structures. That drop is a between-group sum for the comparison being tested. Nonorthogonal factors lose the simple addition of sequential sums, because the group subspaces are no longer orthogonal after the intercept is removed. The geometry remains a sequence of projections. The arithmetic stops being a single three-term identity.
