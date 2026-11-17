## Lead context
A designed experiment is a study in which the investigator chooses which condition each unit receives, so that a later difference in the response can be tied to that choice rather than to who happened to be in which group.

## Motivating example
Six field plots are available and a fertiliser is to be compared with none. If the three plots on the sunny side are given the fertiliser because they look promising, a larger yield cannot be separated from the sun. If instead three of the six plots are chosen by a fair draw, every set of three plots is equally likely. There are $\binom{6}{3}=20$ such sets, so the chance that the three sunny plots are exactly the treated ones is $1/20=0.05$. The design does not stop the sun from affecting yield. It stops the sun from being systematically lined up with the fertiliser.{{cite:dodge2008}} (p. 162, Design of Experiments)

## Intuition
An experiment names the units, the treatments, and the response before the measurements are taken. The treatment column is fixed by the plan. Repeating the measurements would change the responses, not the assignments. An observational comparison has no such column: the groups are found, not made. Random assignment is the part of the plan that balances, in expectation, every trait of the units, including traits nobody wrote down. Blinding is a different protection. It stops knowledge of the assignment from leaking into how the response is produced or recorded.{{cite:dodge2008}} (p. 162, levels of factors)

## Definition
A design is a choice of factor levels: each factor has levels, and the design states which levels, or which combinations of levels, each unit receives. The plan is fixed before the responses are recorded. A randomised design gives each unit one of a small number of treatments with equal probability. The response is what is measured afterwards. The units are the people, plants, plots, or objects that receive a treatment.{{cite:dodge2008}} (p. 162, factors and levels)

## Interpretation — Assignment, response, and what stays fixed
In Alice's caffeine comparison the units are 20 friends, the response is the change in heart rate, and the factor is caffeine with two levels. The caffeinated changes are 17, 22, 21, 16, 6, −2, 27, 15, 16 and 20, with mean $158/10=15.8$. The decaf changes are 4, 10, 7, −9, 5, 4, 5, 7, 6 and 12, with mean $51/10=5.1$. The difference is $10.7$ beats per minute. That number is a summary of this assignment. It becomes evidence about caffeine only because the drinks were allocated by the experimenter and the two drinks were otherwise matched. If the ten friends who already drank more coffee had been handed the caffeinated cola, the same $10.7$ would mix caffeine with whatever else differs between those friends.

## Properties — Balance in expectation
Let $N$ units contain a trait that $m$ of them have, and assign treatment to a simple random subset of size $n$. The number of treated units with the trait, $W$, has expectation $nm/N$. The design does not make $W$ equal $nm/N$ in every randomisation. It makes that the average over randomisations. For a trait that was never measured, the same identity applies, because the proof uses only linearity and the common inclusion probability $n/N$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Label the units $1,\ldots,N$ and let $I_j=1$ when unit $j$ is treated. A simple random subset of size $n$ gives $\Pr(I_j=1)=n/N$ for every $j$. If $A$ is the set of $m$ units with the trait, then $W=\sum_{j\in A}I_j$ and
$$
\E W=\sum_{j\in A}\E I_j=m\cdot\frac{n}{N}.
$$
The same calculation with the complementary trait gives expectation $n(N-m)/N$. Nothing in the argument requires the trait to be recorded.

For the variance, write $p=n/N$ and $\Pr(I_j=I_k=1)=n(n-1)/(N(N-1))$ for $j\neq k$. Then $\Var(I_j)=p(1-p)$ and $\Cov(I_j,I_k)=n(n-1)/(N(N-1))-p^2$. Expanding $\Var(\sum_{j\in A}I_j)$ gives
$$
\Var(W)=n\cdot\frac{m}{N}\cdot\frac{N-m}{N}\cdot\frac{N-n}{N-1}.
$$
The factor $(N-n)/(N-1)$ is the without-replacement correction. As $N$ grows with $n/N$ and $m/N$ fixed, it tends to 1 and $W$ behaves like a binomial count.
:::
:::

## Statistical use — What the plan has to state
A usable plan states the units, the factors and their levels, the response, the allocation rule, and who is blind to the assignment. With two factors the mean can be written as
$$
Y=\beta_0+\beta_1 X_1+\beta_2 X_2+\beta_{12} X_1 X_2+\text{experimental error},
$$
so that a change in $X_1$ can depend on the level of $X_2$. The interaction term is part of the plan when both factors are set by the experimenter. An analysis that ignores a factor the design actually varied is describing a different experiment from the one that was run. The aim is a conclusion that the experimental effort can support, which warns against adding factors until each cell has one observation and no estimate of error.{{cite:dodge2008}} (p. 162, efficient conclusions)

## Worked example
Twenty volunteers include 8 women. A treatment is assigned to a simple random subset of 10. The expected number of women treated is $10\times8/20=4$. The variance is
$$
10\cdot\frac{8}{20}\cdot\frac{12}{20}\cdot\frac{10}{19}=\frac{24}{19}=1.263,
$$
so the standard deviation is $\sqrt{24/19}=1.124$. A realised assignment with 6 treated women is $2/1.124=1.78$ standard deviations above the expected count. That is unusual but possible. It is not, by itself, evidence that the randomisation failed, and it is not a reason to reassign until the counts match. Reassigning until the sexes match would replace the simple random subset with a different design, and the expectation identity above would no longer be the right description of every unmeasured trait.

**Your turn.** Eight plots, four of them on a slope, receive fertiliser on a simple random subset of four plots. Find the expected number of sloping plots that are fertilised, and the probability that all four sloping plots are fertilised.

::: {.callout-tip collapse="true" title="Answer"}
The expectation is $4\times4/8=2$. The number of subsets of size 4 is $\binom{8}{4}=70$, and only one of them is exactly the four sloping plots, so the probability is $1/70=0.0143$. Balance in expectation does not make that bad draw impossible.
:::

## Common misconceptions
A designed experiment is not any study that uses a spreadsheet with a treatment column. If the column records a choice the units made themselves, the study is observational even when the analysis looks like a two-sample test. Randomisation is not a large sample. With six plots, a bad draw still has probability $0.05$, as in the opening count. And a significant difference after randomisation is not automatic evidence of a causal effect of the ingredient one hoped to study: if the caffeinated cola also contained sugar and the control did not, the design identifies the drink, not caffeine. Matching the drinks on everything but caffeine is part of the plan, not a detail to repair in the model afterwards.{{cite:dodge2008}} (p. 162, which levels are used)

## Assumptions and limits — When the assignment does not answer the question
Randomisation balances traits at the moment of assignment. It does not balance what happens next if the groups are treated differently in other ways, and it does not create a response that was poorly defined. Thirty devils split into two groups of 15, one group given a new medicine, form a designed experiment only once someone actually assigns the medicine. If the description never says whether the split was random, whether the measurer knew the assignment, or whether the untreated devils were handled in the same way, the comparison can still be confounded by those choices. Fifteen per group is also a small experiment: a modest change in tumour size can be missed even when the assignment was fair. A design supports the comparison it actually made, at the scale it actually had.{{cite:dodge2008}} (p. 162, conclusions the effort can support)

## Connections
An [observational study](observational-study.qmd) leaves the conditions unassigned. A [randomised controlled trial](randomised-controlled-trial.qmd) is the case with a control arm and a random allocation. [Blinding and placebo](blinding-and-placebo.qmd) stop knowledge of the assignment from moving the response. A [confounding variable](confounding-variable.qmd) is what randomisation is built to break. The numerical comparison of the two caffeine means, once the design is granted, is a [two-sample t test](two-sample-t-test.qmd).

## Check yourself

### Facial tumours in Tasmanian devils {#self-check-ex-da-devil-tumours}

Thirty devils are split into two groups of 15. One group is given a medicine. What must the description still say before the split can be judged as a randomised experiment, and what is the response?

[Exercise](../questions/ex-da-devil-tumours.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The split is an experiment once the investigators assign the medicine. Judging the comparison needs the allocation rule, whether measurement was blind, whether the untreated devils had the same handling, and whether the groups were comparable at the start. The response is the change in tumour size over 12 weeks, or the later size adjusted for the starting size. It is quantitative. The medicine-or-not factor is categorical with two levels.
:::

### A dose comparison for middle-of-the-night insomnia {#self-check-ex-da-motn-insomnia}

Twenty-four patients are randomly allocated to placebo, a low dose, or a high dose. What kind of study is this, and what type of variable is the dose?

[Exercise](../questions/ex-da-motn-insomnia.qmd)

::: {.callout-tip collapse="true" title="Answer"}
It is a randomised designed experiment with a placebo control. Dose takes three named levels, so it is categorical. The levels have an order, so the factor is ordinal. Total sleep time, the response, is a duration and is quantitative. The random allocation is what makes a later difference in sleep a comparison of the assigned doses.
:::

## History
Experimental designs were first used in the 1920s, mostly in agriculture, and R. A. Fisher was the first to bring mathematical statistics into the design of experiments, writing a non-mathematical outline of the principles in 1926. A design is a specification of factor levels, including the combinations used when several factors are studied together, and it is judged by whether the experimental effort can support the conclusion.{{cite:dodge2008}} (p. 162, History and domains)
