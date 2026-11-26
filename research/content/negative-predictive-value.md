## Lead context
Negative predictive value conditions on the test result: it is the probability of absence of the target condition among negative results.

## Motivating example
A patient receives a negative screening result. Sensitivity describes how often affected people test positive, so it does not directly answer the patient's conditional question. The answer also depends on how common the condition was in the population to which the test was applied.{{cite:openintro2019}} (§3.2.7, Bayes' theorem)

## Definition — The denominator is all negative results
Using a reference classification, let $TN$ count true negatives and $FN$ false negatives. The empirical negative predictive value is
$$
\widehat{\mathrm{NPV}}=\frac{TN}{TN+FN},
$$
provided at least one result is negative. Its complement $FN/(TN+FN)$ is the false omission proportion. Specificity instead divides $TN$ by all actual negatives, including false positive tests; changing that denominator changes the conditional question.{{cite:lindholm2022_ml}} (§4.5, p. 87, Tbl. 4.1)

Write $D$ for presence of the condition and $-$ for a negative result. At population prevalence $\pi=\mathbb{P}(D)$, sensitivity $s=\mathbb{P}(+\mid D)$ and specificity $c=\mathbb{P}(-\mid D^c)$, Bayes' formula gives
$$
\mathrm{NPV}=\mathbb{P}(D^c\mid-)=\frac{c(1-\pi)}{c(1-\pi)+(1-s)\pi}.
$$
The denominator is the total negative-result probability and must be positive. This calculation treats $s,c,\pi$ as specified probabilities; estimates introduce sampling uncertainty.{{cite:openintro2019}} (§3.2.3, conditional probability; §3.2.7, Bayes' theorem)

## Interpretation — Reassurance and evidence have different baselines
The posterior odds of the condition after a negative result are
$$
\frac{\mathbb{P}(D\mid-)}{\mathbb{P}(D^c\mid-)}=\frac{\pi}{1-\pi}\frac{1-s}{c}.
$$
When $c>0$, the negative likelihood ratio $(1-s)/c$ describes the multiplication of prior odds. A high NPV can partly reflect a low prior prevalence, even when the likelihood ratio provides little additional evidence. An uninformative test with $\mathbb{P}(-\mid D)=\mathbb{P}(-\mid D^c)>0$ leaves NPV equal to $1-\pi$.{{cite:openintro2019}} (§3.2.7, Bayes' theorem)

For fixed $0<s<1$ and $c>0$, increasing prevalence decreases NPV. Direct differentiation of the displayed fraction gives
$$
\frac{d\,\mathrm{NPV}}{d\pi}=-\frac{c(1-s)}{[c(1-\pi)+(1-s)\pi]^2}<0.
$$
Applying a predictive value in a new population therefore requires a suitable prevalence and applicability of the conditional test rates. A differently selected sample can change the mix of cases and test performance as well as prevalence.{{cite:lindholm2022_ml}} (§4.5, pp. 86–89)

## Worked example
In a population of $1000$ with prevalence $0.1$, sensitivity $0.9$ and specificity $0.8$, the expected classification counts are

| Actual state | Positive test | Negative test |
|:--|--:|--:|
| Condition present | 90 | 10 |
| Condition absent | 180 | 720 |

There are $730$ negative results, yielding $\mathrm{NPV}=720/730=72/73\approx0.986301$. The positive predictive value is only $90/270=1/3$. The two values condition on different groups of results and need not be similar.{{cite:lindholm2022_ml}} (§4.5, p. 87, Tbl. 4.1)

If prevalence rises to $0.5$ while sensitivity and specificity stay fixed, NPV becomes $0.8/(0.8+0.1)=8/9\approx0.888889$. The negative likelihood ratio stays $(1-0.9)/0.8=1/8$; the prior odds have changed.{{cite:openintro2019}} (§3.2.7, Bayes' theorem)

**Your turn.** What proportion of negative results in the displayed table are false negatives?

::: {.callout-tip collapse="true" title="Answer"}
The false omission proportion is $10/730=1/73\approx0.013699$, the complement of NPV. It is not the false negative rate $10/100=0.1$, which conditions on the actual condition.
:::

## Check yourself
### A negative screening result {#self-check-ex-inf-npv-same}
[Negative predictive value](../questions/ex-inf-npv-same.qmd): use sensitivity $0.98$, specificity $0.90$ and prevalence $0.02$.

::: {.callout-tip collapse="true" title="Answer"}
The joint probability of absence and a negative result is $0.90(0.98)=0.882$. False negative probability is $0.02(0.02)=0.0004$. Therefore NPV is $0.882/0.8824\approx0.999547$. Quote NPV with a negative result and positive predictive value with a positive result.
:::

### A positive screening result {#self-check-ex-inf-ppv-screen}
[The same screening test](../questions/ex-inf-ppv-screen.qmd): compare its positive predictive value.

::: {.callout-tip collapse="true" title="Answer"}
True positive probability is $0.98(0.02)=0.0196$ and false positive probability is $0.10(0.98)=0.098$. Positive predictive value is $0.0196/0.1176=1/6$, and five sixths of positive results are false alarms. A high NPV can coexist with a low positive predictive value.
:::
