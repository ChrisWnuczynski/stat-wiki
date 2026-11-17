## Lead context
A positive test for a rare condition is often a false alarm, because most of the people tested do not have the condition.

## Motivating example
A screen that detects 90% of true cases and clears 95% of people without the condition still looks strong in a laboratory report. In a population where only 2 in 100 people have the condition, only about 27 in 100 positive reports are true cases. The test has not become less sensitive. The condition is uncommon, so false positives outnumber true positives.

## Intuition — The question the patient asks
Sensitivity is the probability of a positive result when the condition is present. The positive predictive value runs the conditional the other way: it is the probability the condition is present when the result is positive. Those two probabilities agree only in special cases. When the condition is rare, the large group without it contributes many false positives, so a positive result remains weak evidence even though the test catches most true cases.{{cite:pishro_nik2014}} (§5.1, conditional probability)

## Definition — Positive predictive value
Let $D$ be the event that the condition is present and let $T+$ be a positive test. Write $p=\Pr(D)$, $s=\Pr(T+\mid D)$ and $c=\Pr(T-\mid D^c)$. The positive predictive value is
$$
\mathrm{PPV}=\Pr(D\mid T+)=\frac{ps}{ps+(1-p)(1-c)}.
$$
The numerator is the joint probability of a true positive. The second term in the denominator is the joint probability of a false positive.{{cite:pishro_nik2014}} (§5.1, conditional probability)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
By the definition of conditional probability, $\Pr(D\mid T+)=\Pr(D\cap T+)/\Pr(T+)$ whenever $\Pr(T+)>0$. The joint probability factors as $\Pr(T+\mid D)\Pr(D)=ps$. The law of total probability splits the positive results into true and false positives,
$$
\Pr(T+)=\Pr(T+\mid D)\Pr(D)+\Pr(T+\mid D^c)\Pr(D^c)=ps+(1-c)(1-p).
$$
Dividing gives the displayed ratio.{{cite:pishro_nik2014}} (§5.1, conditional probability)
:::
:::

## Worked example
Take $p=0.02$, $s=0.90$ and $c=0.95$. True positives contribute $0.02\times 0.90=0.018$ and false positives contribute $0.98\times 0.05=0.049$. The positive predictive value is $0.018/0.067=0.269$, so the proportion of positive reports that are false alarms is $0.049/0.067=0.731$.

**Your turn.** Keep the same sensitivity and specificity, and raise the prevalence to $0.10$. Find the positive predictive value and the proportion of positive reports that are false alarms.

::: {.callout-tip collapse="true" title="Answer"}
True positives now contribute $0.10\times 0.90=0.090$ and false positives contribute $0.90\times 0.05=0.045$. The positive predictive value is $0.090/0.135=0.667$, and the false-alarm share among positive reports is $0.045/0.135=0.333$. The test has not changed. The condition is less rare, so a positive result is more trustworthy.
:::

## Connections — Reversing a conditional probability
The same reversal is [Bayes' rule](bayes-rule.qmd) for two events. [Sensitivity and specificity](sensitivity-and-specificity.qmd) fix the truth and ask about the test; the [negative predictive value](negative-predictive-value.qmd) is the companion probability for a negative result. In a screening programme the prevalence is the prior probability of $D$, so a statement about a positive report is incomplete until that prior is named.

## Check yourself

### Equal sensitivity and specificity at one percent prevalence
A test has sensitivity $0.99$ and specificity $0.99$. The prevalence is $0.01$. What is the positive predictive value?

::: {.callout-tip collapse="true" title="Answer"}
True and false positives contribute the same joint probability, $0.01\times 0.99=0.0099$ and $0.99\times 0.01=0.0099$. The positive predictive value is $0.0099/0.0198=0.5$.
:::

### A prevalence of one half
Sensitivity and specificity are both $0.9$, and the prevalence is $0.5$. Show that the positive predictive value equals the sensitivity.

::: {.callout-tip collapse="true" title="Answer"}
The denominator is $0.5\times 0.9+0.5\times 0.1=0.5$, and the numerator is $0.45$, so the ratio is $0.9$. With equal prevalence of the two states and equal error rates, the reversed probability matches the sensitivity.
:::
