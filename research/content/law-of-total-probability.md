## Motivating example
A manufacturer's overall defect rate combines the defect rates of its factories with their production shares. Equal production shares make the unweighted average valid automatically; unequal shares call for weighting by production share, even though the two averages can coincide. Total probability supplies the weights by dividing the experiment into mutually exclusive possibilities.{{cite:pishro_nik2014}} (§1.4.2)

## Statement
Let $(B_i)$ be a finite or countable measurable partition of the sample space. For every event $A$,
$$
\mathbb P(A)=\sum_i\mathbb P(A\cap B_i)
=\sum_{i:\mathbb P(B_i)>0}\mathbb P(A\mid B_i)\mathbb P(B_i).
$$
Cells of probability zero contribute zero through their intersections and require no conditional-probability ratio. The same formula holds if the union of the disjoint cells has probability one.{{cite:pishro_nik2014}} (§1.4.2)

## Intuition — Conditional probabilities need their mixing weights
Each conditional probability describes the frequency within one cell. Multiplying by that cell's probability converts it to the joint probability of falling in the cell and satisfying $A$. These joint contributions can then be added without overlap. Independence between $A$ and the partition cells is unnecessary; conditional rates are useful precisely when they vary across the cells.{{cite:grinstead_snell1997}} (§4.1, Bayes' formula)

## Proof
Distributivity gives $A=A\cap\bigcup_iB_i=\bigcup_i(A\cap B_i)$. The sets in the final union are disjoint, so countable additivity gives the first equality. For a positive-probability cell, the definition of conditional probability gives $\mathbb P(A\cap B_i)=\mathbb P(A\mid B_i)\mathbb P(B_i)$. A zero-probability cell has an intersection of probability zero. Substituting proves the second equality.{{cite:pishro_nik2014}} (§1.4.2, proof)

## Worked example

### Production shares and defective chips
Suppose three factories produce shares $(0.15,0.35,0.50)$ with defect rates $(0.01,0.05,0.02)$. Their contributions to the overall defect probability are $(0.0015,0.0175,0.0100)$, summing to $0.029$. An unweighted average of the three rates would answer a different sampling question.{{cite:pishro_nik2014}} (§1.4.2, weighted conditional probabilities)

For a defective chip, Bayes' rule divides each contribution by $0.029$. The factory probabilities are approximately $(0.05172,0.60345,0.34483)$. They sum to one. Total probability determines the denominator, while Bayes' rule reverses the direction of conditioning.{{cite:grinstead_snell1997}} (§4.1, Bayes' formula)

**Your turn.** Factory 1 supplies 20% of production and factory 2 supplies 80%. Their defect rates are 1% and 4%. Find the overall rate.

::: {.callout-tip collapse="true" title="Answer"}
The weighted rate is $0.2(0.01)+0.8(0.04)=0.034$, or $3.4\%$.
:::

## Generalizations — Updating the partition probabilities
For a cell with $\mathbb P(B_j)>0$, whenever $\mathbb P(A)>0$ the posterior weight is
$$
\mathbb P(B_j\mid A)=
\frac{\mathbb P(A\mid B_j)\mathbb P(B_j)}{
\sum_{i:\mathbb P(B_i)>0}\mathbb P(A\mid B_i)\mathbb P(B_i)}.
$$
A zero-probability cell also has zero posterior probability. Small prior weights can offset high conditional event rates. A rare cause is therefore not automatically probable after an associated event is observed: its joint contribution must be compared with all the alternatives.{{cite:pishro_nik2014}} (§1.4.3)
