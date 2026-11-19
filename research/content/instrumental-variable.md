## Lead context

When people do not take the treatment they were assigned, or when the treatment was never assigned at all, the comparison of those who took it with those who did not mixes the effect with the reasons they took it. An instrumental variable is a third variable that moves the treatment and, under stated conditions, does not move the outcome any other way. {{cite:hernan_robins2020}} (Ch. 16, §16.1, p. 209)

## Motivating example

In a double-blind trial, $Z$ is the randomised assignment and $A$ is the treatment actually received. Some participants do not adhere. Factors $U$ that affect both adherence and the outcome confound a comparison of $A$ with the outcome. The assignment $Z$ is still associated with the treatment received. It is not expected to change the outcome except through that treatment, because the participants and their doctors do not know which pill is which. It was randomised, so it shares no causes with the outcome. Those are the three instrumental conditions, and $Z$ is an instrument for the effect of $A$ on $Y$. {{cite:hernan_robins2020}} (Ch. 16, §16.1, p. 209)

## Definition

A variable $Z$ is an instrument for the effect of treatment $A$ on outcome $Y$ when three conditions hold. First, $Z$ is associated with $A$. Second, $Z$ does not affect $Y$ except through $A$. That exclusion restriction is, at the individual level, the statement that the outcome under a given treatment does not depend on the instrument. Third, $Z$ and $Y$ share no causes. Only the first condition can be checked in the data. The other two are assumptions. In a randomised experiment they are expected from the design: assignment influences receipt, blinding blocks a direct effect of assignment, and randomisation blocks shared causes. {{cite:hernan_robins2020}} (Ch. 16, §16.1, pp. 209–211)

For a binary instrument, when a fourth condition also holds, the average causal effect on the additive scale equals the usual instrumental-variable estimand

$$
\frac{\mathrm{E}[Y\mid Z=1]-\mathrm{E}[Y\mid Z=0]}{\mathrm{E}[A\mid Z=1]-\mathrm{E}[A\mid Z=0]}.
$$


The numerator is the effect of assignment on $Y$. The denominator is the effect of assignment on $A$. If everyone adheres, the denominator is 1 and the two effects match. If few people adhere, the denominator shrinks and the treatment effect is larger than the assignment effect. The ratio inflates the assignment effect back up to the effect of the treatment. {{cite:hernan_robins2020}} (Ch. 16, §16.2, p. 213)

## Properties

In a randomised experiment the numerator and the denominator can each be estimated without adjustment, because $Z$ was assigned by a random mechanism. The ratio of the two estimates is the Wald estimator. The same number is obtained by two-stage least squares. Fit $\mathrm{E}[A\mid Z]=\alpha_0+\alpha_1 Z$, replace $A$ by its prediction, and fit the outcome on that prediction. The slope equals the ratio of the two differences. {{cite:hernan_robins2020}} (Ch. 16, §16.2, p. 213) {{cite:openintro2019}} (Ch. 1, §1.4)

A weak instrument, one for which the denominator is close to zero, produces an unstable ratio. A rule of thumb treats the instrument as weak when the first-stage $F$ statistic is under 10. In one smoking-cessation example the numerator was $2.686-2.536=0.1503$, the denominator was $0.2578-0.1951=0.0627$, and the ratio was $0.1503/0.0627=2.4$ kilograms, with a confidence interval from $-36.5$ to $41.3$ and a first-stage $F$ of $0.8$. {{cite:hernan_robins2020}} (Ch. 16, §16.2, pp. 213–214)

The three conditions alone do not make the ratio equal to the average treatment effect. A fourth condition, effect homogeneity, is required for that reading. The strongest version is a constant effect for every individual, which is scientifically implausible for most treatments and impossible for a binary outcome except under a sharp null or universal harm or benefit. Partial identification without that condition produces bounds, and the bounds are often wide enough to include the null. {{cite:hernan_robins2020}} (Ch. 16, §16.2–16.3, pp. 212–214)

## Statistical use

The instrument is the assignment indicator in a trial with non-adherence. In an observational study a candidate instrument might be a price, a distance to a facility, a physician’s preference, or a genetic variant. Cigarette price is the running example for smoking cessation and weight: it is a candidate if price affects quitting, if price affects weight only through quitting, and if price and weight share no causes. Whether the exclusion restriction and the shared-cause condition hold is a subject-matter argument. The data can check the association of $Z$ with $A$. They cannot prove the other two. {{cite:hernan_robins2020}} (Ch. 16, §16.1, pp. 210–211)

Report the first-stage association as well as the ratio. A denominator of $0.06$, an $F$ statistic of $0.8$, and an interval from $-36.5$ to $41.3$ are part of the answer, not a footnote to the point estimate $2.4$. An instrument that barely moves treatment does not identify a stable treatment effect, even when the three conditions are granted and the fourth is assumed. {{cite:hernan_robins2020}} (Ch. 16, §16.2, pp. 213–214)

## Worked example

Among people with $Z=1$, the mean outcome is 11 and the proportion treated is $0.75$. Among people with $Z=0$, the mean outcome is 7 and the proportion treated is $0.25$. The numerator is $11-7=4$. The denominator is $0.75-0.25=0.5$. The instrumental-variable estimand is $4/0.5=8$. {{cite:hernan_robins2020}} (Ch. 16, §16.2, p. 213)

**Your turn.** The treated proportion at $Z=1$ falls from $0.75$ to $0.65$. The other values stay 11, 7, and $0.25$. What is the estimand?

::: {.callout-tip collapse="true" title="Answer"}
The numerator is still $11-7=4$. The denominator is $0.65-0.25=0.4$. The estimand is $4/0.4=10$.
:::

## Common misconceptions

The ratio is not the comparison of people who took the treatment with people who did not. That comparison is confounded by $U$. The instrumental-variable calculation never contrasts those two groups directly. It contrasts levels of $Z$, and rescales by how much $Z$ moved $A$. {{cite:hernan_robins2020}} (Ch. 16, §16.1–16.2, pp. 209, 213)

A significant association between $Z$ and $A$ does not confirm that $Z$ is an instrument. It confirms condition (i). Conditions (ii) and (iii) stay assumptions. A candidate that fails condition (i), or that passes it only weakly, is not rescued by a large point estimate. The smoking example’s interval contains both large gains and large losses. {{cite:hernan_robins2020}} (Ch. 16, §16.1–16.2, pp. 211, 213–214)

The three conditions are not enough for the average causal effect. Without homogeneity the instrument identifies bounds, not the single number in the Wald formula. Reading every Wald estimate as an average treatment effect skips that fourth condition. {{cite:hernan_robins2020}} (Ch. 16, §16.3, p. 214)

## History

Wald’s 1940 estimator is the ratio of the two differences. Two-stage least squares computes the same number by substituting the prediction of treatment from the instrument. The conditions were later written in the language of potential outcomes: an exclusion restriction on the outcome, and exchangeability of the instrument with the counterfactual outcomes. Genetic variants, physician preference, and measures of access, including distance and price, became standard catalogues of candidate instruments in observational studies. The smoking-cessation calculation, with its first-stage $F$ of $0.8$, is the modern reminder that a candidate can meet the story and still be too weak to use. {{cite:hernan_robins2020}} (Ch. 16, §16.1–16.2, pp. 210–214)

## Connections

An [average treatment effect](average-treatment-effect.qmd) is the contrast the ratio is trying to recover, and it equals the ratio only with the fourth condition. A [randomised experiment](randomised-controlled-trial.qmd) supplies the instrument when adherence is incomplete and the assignment is blinded. [Ordinary least squares](ordinary-least-squares.qmd) of the outcome on the treatment received is the confounded comparison the instrument is meant to avoid. Two-stage least squares is the computational form of the Wald ratio. A [natural experiment](natural-experiment.qmd) is the observational setting in which a candidate instrument is proposed because some external change moved treatment. The exclusion restriction is the claim that has to be argued in that setting, because randomisation is no longer there to carry it. {{cite:hernan_robins2020}} (Ch. 16, §16.1–16.2, pp. 209–213)
