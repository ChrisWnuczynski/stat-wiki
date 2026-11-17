## Lead context
A confounding variable can make a treatment look harmful in the pooled table even though it looks helpful inside every group.

## Motivating example
Among men, treatment A recovers $8/10$ and B recovers $70/100$. Among women, A recovers $40/100$ and B recovers $3/10$. Inside each sex A is ahead. Pooled, B is ahead, because the sex mix is not the same in the two treatment columns.

## Intuition — The mix of groups is part of the comparison
An association between a treatment and an outcome is a comparison of rates. If a third variable changes both the chance of receiving the treatment and the chance of the outcome, the pooled rates mix unlike groups. The within-group comparisons can all run one way while the pooled comparison runs the other way, because the treatment column that looks worse overall may simply contain more of the group that does badly. The arithmetic is a property of the counts. It does not by itself name which variable is causal. {{cite:hernan_robins2020}} (Chs. 1–3)

## Definition — Associated with the treatment and with the outcome
In these counts a confounder is a variable tied to both the treatment assignment and the outcome, so that the marginal association is not the common within-group association. Holding the confounder fixed, by a stratified table or by a designed assignment that breaks the tie, is what makes the two associations separable. A variable tied to only one of them does not produce this reversal. {{cite:hernan_robins2020}} (Chs. 1–3)

## Worked example — Recovery reverses when the sexes are pooled
One hundred and ten patients of each sex are treated with A or B. Among men, A recovers \(8/10=4/5\) and B recovers \(70/100=7/10\). Among women, A recovers \(40/100=2/5\) and B recovers \(3/10\). Inside each sex, A has the higher recovery rate: \(4/5>7/10\) and \(2/5>3/10\).

Pool the sexes. A treats \(10\) men and \(100\) women, so A recovers \(48/110=24/55\approx 0.4364\). B treats \(100\) men and \(10\) women, so B recovers \(73/110\approx 0.6636\). The pooled comparison favours B. Sex is tied to treatment: \(100/110=10/11\) of A's patients are women, and \(10/11\) of B's patients are men. Sex is also tied to recovery: men recover more often under both treatments. The pooled reversal is the mixture of those two ties.

**Your turn.** Using the same within-sex rates, suppose instead that each treatment is given to \(50\) men and \(50\) women. Which treatment has the higher pooled recovery rate?

::: {.callout-tip collapse="true" title="Answer"}
A recovers \(50\cdot(4/5)+50\cdot(2/5)=60\) of \(100\) patients. B recovers \(50\cdot(7/10)+50\cdot(3/10)=50\) of \(100\). The pooled rates are \(0.60\) and \(0.50\), so A is ahead once the sex mix is the same. The reversal needed the unbalanced mix.
:::

## Connections — Design, stratification, and a causal diagram
An [observational study](observational-study.qmd) leaves the tie between treatment and the confounder intact. A [designed experiment](designed-experiment.qmd) assigns treatment by a mechanism that does not consult the confounder. {{cite:hernan_robins2020}} (Chs. 1–3) Stratifying, as in the two sex rows above, reports the association with the confounder held fixed. The figure on this page is that distinction for smoking and height. Neither the pooled rate nor a single correlation is a substitute for the stratified comparison.

