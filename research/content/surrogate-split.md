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
Agreement is measured on cases where the primary variable is observed. Using that agreement for cases where the primary variable is missing is a further modelling step: it is warranted when the association between the surrogate and the primary split is stable across the missingness mechanism. A surrogate estimates a binary routing decision. Distinct missing laboratory values can be sent down the same branch, because the surrogate never reconstructs the missing number. Other missing-input classifiers impute the input, model the joint distribution, or use a pattern-specific rule, and each of those procedures has its own error.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, p. 98)

## Definition — A surrogate matches a routing label
On the cases where the primary variable is present, the primary split assigns each case to a child. Call that assignment $L_i\in\{\mathrm{left},\mathrm{right}\}$. A candidate split on another variable assigns a provisional label $S_i$, and the candidate may reverse its own left and right so as to raise agreement with $L$. Raw agreement on $m$ shared cases is the proportion of matches. The majority baseline $A_0$ is the larger of the two primary-child proportions. The relative improvement $(A-A_0)/(1-A_0)$ is defined when the primary split is not constant. It equals zero when the candidate does no better than sending every case to the larger child, and it equals one when the candidate reproduces $L$ exactly.{{cite:loh2011_trees}} (§2, pp. 15–16)

The primary split itself was chosen to improve a response criterion, such as a decrease in node impurity. The surrogate is chosen to predict $L$, the routing label. A variable that separates the response well can be a poor surrogate if its partition of the cases cuts across the primary split, and a variable that is weakly related to the response can be an excellent surrogate if it tracks the primary variable.

## Interpretation — Reverse the candidate before scoring it
Suppose eight cases are sent left by the primary split on six occasions and right on two, and a candidate sends them in exactly the opposite direction on every case. After the candidate's labels are reversed, agreement is $8/8=1$ and the relative improvement is $1$. Scoring the candidate in its original orientation would have given agreement $0$ and would have discarded a perfect routing copy. The search over surrogates includes that reversal.

The worked eight-case candidate agrees on seven cases, so $A=0.875$ and $A_0=0.75$, and the relative improvement is $0.5$. A rule that always goes left matches the six left-hand cases, agrees at rate $0.75$, and has relative improvement $0$. The two numbers $0.875$ and $0.75$ differ by one case in eight. Dividing by $1-A_0=0.25$ puts that one case on the scale of the improvement still available beyond majority routing. On a balanced node of ten cases, eight matches give $A=0.8$, $A_0=0.5$ and relative improvement $0.6$, a larger improvement on a split that has no majority child.

## Intuition — Predict the question the tree already asked
At prediction time the tree wants the answer to a question: which child did the primary split intend? If the laboratory value that defines the split is missing, a second measurement can still predict that answer. The surrogate is a classifier whose target is the primary decision, trained on the cases where both measurements were observed. Once the child is chosen, the rest of the tree proceeds as it would have for a complete case. If several surrogates are ranked, the first one whose variable is observed supplies the route. If none is observed, a declared fallback, often the majority child, finishes the step.

This construction leaves the response model untouched. The outcome $Y$ enters the choice of the primary split and stays out of the agreement score $A$, which is computed entirely from $L$ and $S$.

## Statistical use — Rank surrogates on a common set of cases
Comparisons of $A$ use a shared denominator. If one candidate is missing on a different subset from another, the two agreement rates describe different collections of patients, and the ranking mixes predictive accuracy with the pattern of missingness. The relative improvement adjusts for a lopsided primary split, so a $90\%$ agreement against a $90\%$ majority child is recognised as a copy of the majority rule. In the twenty-case comparison mentioned with the worked numbers, $18/20=0.9$ against a baseline of $11/20=0.55$ is a real improvement, $(0.9-0.55)/(1-0.55)=0.777778$, because the baseline is far from one.{{cite:loh2011_trees}} (pp. 15–16, Table 1; p. 19, Table 4)

At deployment the primary variable is used whenever it is present. The surrogate is a backup route, not a second vote on the response. Publishing the primary cutoff, the surrogate cutoff, the orientation, and the agreement on the cases used to rank it makes the backup auditable.

## Common misconceptions
High agreement with the primary split is sometimes read as evidence that the surrogate is a strong predictor of the clinical outcome. The agreement calculation never sees the outcome. It sees a binary label that the primary split already computed. A surrogate with relative improvement $1$ reproduces the primary routing and therefore sends cases to the same children; the quality of those children as outcome groups was settled when the primary split was chosen.

A raw agreement of $0.75$ looks substantial until it is set beside a majority baseline of $0.75$. The relative improvement is then zero: the candidate has copied the larger child. Reporting $A$ together with $A_0$ keeps that comparison in view.{{cite:loh2011_trees}} (§2, pp. 15–16)
