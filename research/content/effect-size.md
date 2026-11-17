## Lead context

A test can reject a null hypothesis because the sample is large, even when the departure from the null is tiny. Effect size is the magnitude of that departure, kept separate from the probability of detecting it. In a comparison of means it is the difference one cares about, in the units of the measurement. In a compatibility reading of an interval it is the set of magnitudes the data do not rule out.{{cite:openintro2019}} (Ch. 5, p. 204; Ch. 7, §7.4.2, pp. 279–280){{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)

## Motivating example

A trial compares a new drug with a standard drug on blood pressure. The investigators decide, before looking at $p$-values, that a further reduction of 3 mmHg would matter clinically. That 3 mmHg is the minimum effect size of interest. With 100 patients per arm and a standard error of 1.7 mmHg for the difference of means, a two-sided 5% test rejects only if the observed difference falls outside $\pm 1.96\times 1.7=\pm 3.332$ mmHg. An effect of exactly $-3$ mmHg therefore sits mostly inside the non-rejection region. The probability of rejecting, if that effect is real, is only about 0.42. The effect can be real and still be missed, and a different effect, of 0.2 mmHg, could be declared significant in a much larger trial without being the effect anyone set out to find.{{cite:openintro2019}} (Ch. 7, §7.4.2–§7.4.3, pp. 279–281)

## Intuition

Statistical significance answers “would a procedure this sensitive often produce a result this far from the null, if the null were true?” Effect size answers “how far from the null is the result, or how far would we need it to be?” The first question depends on the sample size. The second is a feature of the scientific scale. Multiplying the sample size shrinks the standard error and can make a fixed effect size significant. It does not change the effect size.{{cite:openintro2019}} (Ch. 5, p. 204; Ch. 7, §7.4.2, p. 279)

An interval makes the same separation. A confidence interval that excludes only very large effects is reporting compatibility with a wide range of magnitudes. Calling the interval a compatibility interval is a reminder that the magnitudes inside it are the effect sizes the data, under the model, do not conflict with. The name does not add a new number. It refuses to collapse the number to a yes or no.{{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)

## Definition

In a test of a point null, the effect size is the difference between the true parameter and the null value, or, in the observed sample, the difference between the point estimate and the null value. With large samples, even a small difference of that kind is identified as statistically significant. In a sample-size calculation the effect size is the specific difference the study is being asked to detect, such as a drop of 3 mmHg in blood pressure.{{cite:openintro2019}} (Ch. 5, p. 204; Ch. 7, §7.4.2, pp. 279–280)

The difference is kept in the units of the response unless a later, separate standardisation is defined. A difference of 3 mmHg is not a probability and not a $p$-value. Power is the probability of rejecting the null when a stated effect size is true. Power depends on the effect size, the standard error, and the significance level. It is not itself the effect size.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280)

A confidence or compatibility interval is a set of effect sizes. Under the model and the adjustment that produced the interval, the values inside it are the magnitudes highly compatible with the data. Systematic bias that the interval does not account for can move the whole set. The effect size being discussed is then the effect size of the estimator’s target, which may not be the effect size of the scientific contrast.{{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)

## Properties

For a difference of means with standard error $s$, a two-sided level-$\alpha$ test based on a normal approximation rejects when the observed difference $\bar d$ satisfies $|\bar d|>z_{1-\alpha/2}\,s$. If the true difference is $\delta$, the power is the probability that a draw from the sampling distribution centred at $\delta$ falls outside that threshold. Shifting $\delta$ from 0 to the minimum interesting value, while holding $s$ fixed, moves power. Holding $\delta$ fixed and decreasing $s$, by a larger sample, also moves power. The two knobs are different.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280)

In the blood-pressure sketch, $z_{0.975}\times 1.70=3.332$, and the $z$-score of the lower critical point under a true difference of $-3$ is

$$
\frac{-3.332-(-3)}{1.7}=\frac{-0.332}{1.7}\approx -0.20.
$$

The lower-tail probability at $-0.20$ is about 0.42, which is the approximate power once the far tail in the wrong direction is ignored. The arithmetic shows a 3 mmHg effect detected with probability well below one half at this sample size. It does not show that 3 mmHg is small or large in any absolute sense. That judgement is the investigators’ choice of the minimum effect size of interest.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280)

## Statistical use

State the effect size in the units of the measurement, beside any $p$-value. When planning a study, name the smallest difference that would change a decision, compute the standard error the design will produce, and only then compute power. When reporting a completed study, give the estimate and the interval. A confidence interval that runs from a trivial difference to a large one is a finding about precision, not a finding that the effect size is the point estimate alone.{{cite:openintro2019}} (Ch. 7, §7.4.2–§7.4.3, pp. 279–281){{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)

A [Kruskal–Wallis test](kruskal-wallis-test.qmd) or a $t$ test can establish that a difference is detectable. Neither replaces the effect size. An [interval for a difference of means](interval-for-a-difference-of-means.qmd) is the effect-size summary that already carries the statistical uncertainty of the comparison, under the model used to form it.

## Worked example

Take the normal approximation above, with standard error $1.7$ mmHg. The two-sided 5% critical difference is $1.96\times 1.7=3.332$ mmHg. Under a true effect size of $-3$ mmHg, the lower critical point has

$$
z=\frac{-3.332-(-3)}{1.7}=-0.1953,
$$

which rounds to the $-0.20$ used to read a tail probability of about $0.42$. The power against this effect size is about $0.42$. Against an effect size of $0$, the same critical value has tail probability $0.05$ by construction of the test, not because the effect size changed the critical value.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280)

**Your turn.** The standard error of a difference is $2$ mmHg, and the minimum effect size of interest is $5$ mmHg in the negative direction. Using the critical value $1.96\times 2$, compute the $z$-score of the lower critical point when the true difference is $-5$.

::: {.callout-tip collapse="true" title="Answer"}
The lower critical point is $-3.92$. Then $z=(-3.92-(-5))/2=1.08/2=0.54$. The true effect size of $5$ mmHg now sits past the critical value, so more than half of the sampling distribution falls in the rejection region on that side. The $z$-score is $0.54$, not a $p$-value and not the effect size itself.
:::

## Common misconceptions

A small $p$-value is not a large effect size. A large effect size is not automatically significant: the blood-pressure calculation has a pre-specified effect of 3 mmHg and power about 0.42. Standardising a difference by a standard deviation produces a different number, useful for comparing unlike scales, and is not required for the definition used in a power calculation on a single scale. The width of a confidence interval is not an effect size. The location of the interval is a range of effect sizes.{{cite:openintro2019}} (Ch. 5, p. 204; Ch. 7, §7.4.2, p. 280){{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)

## Assumptions and limits

Power calculations of the normal kind assume the standard error used in the plan, independence, and a sampling distribution close enough to normal that a $z$ critical value is honest. They describe detection of a stated effect size, not the truth of that effect size. An interval’s list of compatible effect sizes is conditional on the model and on whatever adjustment for confounding or selection was built into the estimator. Bias that the interval ignores does not shrink when $n$ grows, so a narrow interval around the wrong contrast is a precise statement about the wrong effect size.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280){{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)

## Connections

A [p-value](p-value.qmd) measures surprise under a null, not magnitude. Power, in the sample-size calculation above, is the probability of rejecting at a stated effect size. An [interval for a difference of means](interval-for-a-difference-of-means.qmd) displays a range of effect sizes. [Type I and type II errors](type-i-and-type-ii-errors.qmd) are the two ways the yes-or-no decision can fail; the effect size is what the type II error is being computed against.

## History

The separation of a detectable difference from a meaningful difference is part of the ordinary teaching of tests once sample size is allowed to vary. Exercises on hypothesis tests name the difference between the null value and the point estimate an effect size, and warn that large samples flag small differences as significant. Power calculations then take a minimum effect size of interest as an input chosen on scientific grounds, as in the 3 mmHg blood-pressure plan, and return a probability of detection. Later discussions of confidence intervals press the same distinction from the other side: an interval exhibits which effect sizes remain compatible with the data under the assumptions of the fit, and a narrow interval is not by itself a complete account of uncertainty when systematic bias is still in play.{{cite:openintro2019}} (Ch. 5, p. 204; Ch. 7, §7.4.2, pp. 279–280){{cite:hernan_robins2020}} (Ch. 10, Fine Point 10.2, p. 142)
