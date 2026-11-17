## Lead context
A surrogate predicts a primary split's routing decision from a different predictor. It addresses missing predictors at prediction time, rather than filling in a complete data table.{{cite:loh2011_trees}} (§2, pp. 15–16, Table 1)

## Motivating example
A tree asks whether a laboratory measurement is below a cutoff, but that measurement is unavailable for a patient. Another measurement may predict the answer to the first question well enough to choose a branch. This is a different task from asking whether the second measurement is the best predictor of the outcome. Classification with missing inputs requires a specified prediction rule.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, p. 98, “Classification with missing inputs”)

## Properties — Learn the routing label
For cases on which the primary variable is observed, define a temporary binary response $L_i$ that records left versus right. A candidate question $S_i$ is evaluated against $L_i$, allowing its orientation to reverse. For a fixed common set of $m$ complete cases, raw agreement is
$$
A=\frac1m\sum_{i=1}^m1\{S_i=L_i\}.
$$
That criterion concerns allocation agreement. The primary split instead optimises a criterion involving the actual response. CART's use of surrogates is one of several missing-value strategies among tree algorithms; results from one implementation do not determine another's behaviour.{{cite:loh2011_trees}} (pp. 15–16, Table 1; p. 19, Table 4)

A useful diagnostic compares $A$ with the majority-routing baseline $A_0=\max(m_L,m_R)/m$. Define the relative improvement $(A-A_0)/(1-A_0)$ when $A_0<1$. This comparison distinguishes genuine routing information from agreement obtained by always choosing the larger child. The diagnostic assumes candidates are assessed on the same cases; different missingness patterns otherwise change the denominator and the population being compared.

## Worked example
Suppose the primary routing on eight cases sends six left and two right. A candidate agrees on seven cases. Then $A=7/8=0.875$ and $A_0=6/8=0.75$, so its relative improvement is $(0.875-0.75)/(1-0.75)=0.5$. A constant “left” rule agrees on six cases but contributes no improvement over that baseline. In the twenty-case comparison, $18/20=0.9$ exceeds $11/20=0.55$ when both candidates use the same cases and orientation.

For a new case, the primary rule takes precedence whenever its variable is observed. When it is missing, an available surrogate supplies a routing decision. If no usable surrogate is observed, a further fallback must be specified. Surrogates therefore do not solve every missing-input case. Tree procedures differ in which alternatives they permit.{{cite:loh2011_trees}} (§2, pp. 15–16)

**Your turn.** On a balanced node of ten cases, a candidate matches the primary direction on eight. Compute its raw agreement and relative improvement over majority routing.

::: {.callout-tip collapse="true" title="Answer"}
$A=0.8$, $A_0=0.5$, and $(A-A_0)/(1-A_0)=0.6$.
:::

## Assumptions and limits
Agreement is measured where the primary value is known. Its relevance to cases with that value missing is an additional modelling concern: if missingness selects a different relationship between predictors, high training agreement may not transfer. A surrogate also does not estimate the missing laboratory value; it estimates a binary routing decision, so different missing values can lead to the same prediction. The broader missing-input classification problem can be handled by other models, each with its own assumptions.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, p. 98)
