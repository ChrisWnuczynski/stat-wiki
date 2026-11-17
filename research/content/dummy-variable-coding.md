## Lead context
Dummy variable coding replaces a category by indicators, so a regression coefficient is a difference of means against a reference level.

## Motivating example
Three clinics record a numeric outcome, and the clinics are not ordered. Entering the clinic number $1,2,3$ as a straight line would force the step from clinic 1 to clinic 2 to equal the step from clinic 2 to clinic 3. Indicators let those two steps differ.

## Intuition — Drop one level so the columns are independent
A category with $d$ levels can be written as $d$ indicators that sum to $1$ on every row. Together with a column of ones, those $d$ indicators are linearly dependent: their sum is the intercept column, so the coefficients are not identifiable. Dropping one level, the reference, leaves $d-1$ indicators. The intercept is then the mean at the reference level, and each remaining coefficient is the difference between that level’s mean and the reference mean, when no other covariate is present.

The choice of reference changes the coefficients and does not change the fitted mean of any row. Coding level $C$ as the reference instead of level $A$ rewrites the same three means with a different intercept.

## Definition — Saturated group means
Let groups $A$, $B$, and $C$ have indicators $I_B$ and $I_C$, with $A$ as the reference. The mean model
$$
\mu=\beta_0+\beta_B I_B+\beta_C I_C
$$
gives $\mu_A=\beta_0$, $\mu_B=\beta_0+\beta_B$, and $\mu_C=\beta_0+\beta_C$. With one common variance and independent observations, least squares estimates these means by the group sample means. {{cite:nist_oneway_anova}} (§3.2.3.1, Model, ANOVA table and Assumptions)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $I_A,I_B,I_C$ are all three indicators, then $I_A+I_B+I_C$ equals the intercept column, so the four columns are dependent. Deleting $I_A$ removes that relation.

Within a group the model is a constant. The residual sum of squares for a constant fit is minimised at the group sample mean, so $\hat\beta_0=\bar y_A$, $\hat\beta_B=\bar y_B-\bar y_A$, and $\hat\beta_C=\bar y_C-\bar y_A$. {{cite:nist_oneway_anova}} (§3.2.3.1, Model, ANOVA table and Assumptions)

If the mean also contains a quantitative covariate $z$, those coefficients are differences at a fixed value of $z$. They are not, in general, the differences of the raw group means. The formulae above are the case with no other covariate.
:::
:::

## Worked example
Group $A$ has observations $10$ and $12$, group $B$ has $14$ and $16$, and group $C$ has $20$ and $22$. The sample means are $11$, $15$, and $21$. With $A$ as reference,
$$
\hat\beta_0=11,\qquad \hat\beta_B=4,\qquad \hat\beta_C=10.
$$
The fitted mean in $C$ is $11+10=21$. If $C$ is the reference instead, the intercept is $21$, the coefficient of $A$ is $11-21=-10$, and the coefficient of $B$ is $15-21=-6$. The fitted means are still $11$, $15$, and $21$.

**Your turn.** Using the same three means and reference $A$, what is the fitted mean in $B$, and what coefficient of $B$ would you report if the reference were $B$?

::: {.callout-tip collapse="true" title="Answer"}
The fitted mean in $B$ is $11+4=15$. With reference $B$ the coefficient of $B$ is omitted, and the intercept is $15$. The coefficient of $A$ is $11-15=-4$.
:::

## Connections — Factors in a linear mean
An [interaction](interaction.qmd) adds a further indicator product, so the difference between two levels of one factor can depend on the level of another. The [identity link](identity-link.qmd) reads those coefficients as differences of means. A [linear predictor](linear-predictor.qmd) that includes a full set of indicators and the intercept is not identifiable, because those indicators sum to the intercept column. {{cite:nist_oneway_anova}} (§3.2.3.1, Model, ANOVA table and Assumptions) The same reference-level arithmetic is what a two-factor model uses when level 1 of each factor is the baseline.

