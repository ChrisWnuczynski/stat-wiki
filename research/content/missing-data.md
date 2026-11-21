## Lead context
Missing data are values the study meant to record and does not have.

## Motivating example
Four measurements were planned: $10$, a missing value, $14$ and $18$. The three observed numbers average $14$. Filling the hole with $14$ leaves that mean; filling it with $6$ moves the four-number mean to $12$.

## Intuition — An empty cell is not the same thing as a zero
A destroyed record, a plot that failed, or a coordinate that was never written down leaves a hole where a number was intended. Filling that hole by repeating the experiment is the ideal repair, and it is often impossible. A latent label in a mixture model is a different hole: the statistical story includes a component indicator that the sampler never kept. The arithmetic that replaces a dropped measurement is not the arithmetic that replaces that indicator.{{cite:dodge2008}} (p. 350, missing outcomes)

## Definition — Intended observations that are absent
Missing data occur when certain intended outcomes are not present, for example because a record was lost or a unit left the study. In a designed experiment the historical repairs estimate the missing yield rather than collect it again. Allan and Wishart treated a missing field plot in 1930, Yates in 1933, Bartlett by a covariance adjustment in 1937, and Rubin in 1972. Those dates locate early designed-experiment repairs; later missingness assumptions are a separate subject.{{cite:dodge2008}} (p. 350, definition and history)

## Worked example
Four measurements were planned: $10$, a missing value, $14$ and $18$. The mean of the three observed numbers is $(10+14+18)/3=14$. If the missing value had been $14$, the mean of all four would still be $14$. If it had been $6$, the complete mean would be $(10+6+14+18)/4=12$. The two fill-ins move the reported mean by $2$. The observed mean alone does not say which fill-in is right.{{cite:dodge2008}} (p. 350, absent outcomes)

**Your turn.** The same three numbers are observed, and the missing value is filled by $22$. What is the mean of the four numbers, and by how much does it exceed the observed mean $14$?

::: {.callout-tip collapse="true" title="Answer"}
The four-number mean is $(10+22+14+18)/4=16$. It exceeds the observed mean by $2$. A high fill-in pulls the mean up by the same amount that the fill-in $6$ pulled it down.
:::

## Connections
A mixture's missing component label is handled by the [E step](e-step.qmd) of the [EM algorithm](em-algorithm.qmd), which replaces the label by its conditional probability. That calculation needs a model for the label. A dropped measurement needs a model for why it is missing. Repeating the experiment, when it can be done, avoids both models.{{cite:dodge2008}} (p. 350, repeating the experiment)
