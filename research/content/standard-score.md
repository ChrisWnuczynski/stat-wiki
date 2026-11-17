## Lead context
A measurement is easier to compare after it is expressed in units of its own spread. A standard score, often called a z-score, subtracts a centre and divides by a scale. {{cite:dodge2008}} (p. 325) {{cite:nist_glossary2002}} (Glossary, "standard deviation")

## Motivating example
Four package weights, in the same units, are 2, 4, 4, and 6. Their mean is 4. The squared deviations from 4 sum to 8, so the population-style root-mean-square is $\sqrt{8/4}=\sqrt{2}$. The weight 6 sits $\sqrt{2}$ above the mean, which is one root-mean-square unit. The same weight is not "large" until that unit is named. {{cite:openintro2019}} (Ch. 2, §2.1)

## Definition
Given values $x_1,\ldots,x_n$ with mean $\bar x$ and a positive scale $s$, the standard score of $x_i$ is $(x_i-\bar x)/s$. When $s$ is the standard deviation of the same list, the scores have mean 0. When $s$ is a population standard deviation known before the list is seen, the score compares the observation with that external scale. The [normal distribution](normal-distribution.qmd) uses this score when a measurement is compared with a normal curve of mean $\mu$ and standard deviation $\sigma$: the score is $(x-\mu)/\sigma$. {{cite:dodge2008}} (p. 325) {{cite:nist_glossary2002}} (Glossary, "standard deviation")

## Properties
For the four weights and the root-mean-square $\sqrt{2}$, the scores are $(2-4)/\sqrt{2}=-\sqrt{2}$, $0$, $0$, and $\sqrt{2}$. Their sum is 0, so their mean is 0. The sum of their squares is $2+0+0+2=4$, and $4/4=1$, so these scores have root-mean-square 1. That identity is the point of dividing by the list's own scale: the scores are centred and then measured in a unit that the list itself defines. {{cite:openintro2019}} (Ch. 2, §2.1) {{cite:dodge2008}} (p. 325)

## Worked example
The mean of 2, 4, 4, and 6 is $(2+4+4+6)/4=4$. Using the divisor $n=4$ inside the second moment, the second moment is $8/4=2$ and the scale is $\sqrt{2}$. The score of 6 is $(6-4)/\sqrt{2}=\sqrt{2}\approx 1.414$. The score of 2 is $-\sqrt{2}$.

**Your turn.** Using the same centre and the same scale, what is the score of a new weight 4?

::: {.callout-tip collapse="true" title="Answer"}
The score is $(4-4)/\sqrt{2}=0$.
:::

## Assumptions and limits
The division requires a positive scale. A list whose values are all equal has scale 0, and the score is undefined. Replacing the root-mean-square that uses divisor $n$ by the sample standard deviation that uses divisor $n-1$ changes the scores: for these four weights the sum of squared deviations is still 8, the sample variance is $8/3$, and the score of 6 becomes $2/\sqrt{8/3}=\sqrt{1.5}\approx 1.225$. The comparison with a normal curve is a further step. A score of 2 is an unusual normal outcome only when the normal model is the one being used. {{cite:nist_glossary2002}} (Glossary, "standard deviation") {{cite:openintro2019}} (Ch. 2, §2.1)

## History
Standardising a measurement by its spread is the step that lets a normal approximation be tabled once and then reused. The [normal distribution](normal-distribution.qmd) is the curve those tables describe. The score itself is only the change of unit. {{cite:dodge2008}} (p. 325) {{cite:openintro2019}} (Ch. 2, §2.1)
