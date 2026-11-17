## Lead context
The pooled standard error estimates a common success probability under the equality null. It is a testing denominator; estimation of a difference generally uses a different standard error.{{cite:openintro2019}} (§6.2, pooled proportion)

## Motivating example
Two independently sampled groups have $60$ successes in $100$ trials and $75$ in $150$. The sample proportions differ by $0.10$. Under the null that their population proportions agree, both samples inform a single probability, estimated by $135/250=0.54$. Pooling therefore weights group proportions by their sample sizes.{{cite:openintro2019}} (§6.2, testing two proportions)

## Properties — Derive the denominator under the null
For independent binomial counts $X_i\sim\operatorname{Bin}(n_i,p_i)$, $\operatorname{Var}(\widehat p_1-\widehat p_2)=p_1(1-p_1)/n_1+p_2(1-p_2)/n_2$. Under $H_0:p_1=p_2=p$ this reduces to $p(1-p)(1/n_1+1/n_2)$. Maximising the joint null likelihood gives $\widehat p=(X_1+X_2)/(n_1+n_2)$, so substitution yields the pooled $z$ statistic. The binomial assumptions concern independent trials with a stable probability within each group.{{cite:dodge2008}} (pp. 44–45){{cite:openintro2019}} (§6.2, null standard error)

In a two-by-two table the null fitted cell counts are row total times column total divided by the grand total. Substituting those four expectations into Pearson's sum and simplifying gives exactly $X_P^2=z^2$ for the uncorrected procedures. Thus the $\chi_1^2$ upper tail and the two-sided normal tail agree. Rounding intermediate fitted counts can obscure the identity.

## Worked example
For the motivating counts,
$$
\widehat p_1-\widehat p_2=0.10,\qquad
SE_0=\sqrt{0.54(0.46)(1/100+1/150)}=0.06434.
$$
The statistic is $z=1.5542$, giving a two-sided normal probability $0.1201$. The null expected counts are $54,46,81,69$, all comfortably away from zero. This supports the large-sample approximation; it does not supply independence if trials were clustered.{{cite:openintro2019}} (§6.2, success–failure condition)

For a confidence interval for $p_1-p_2$, the unpooled estimate is $SE=\sqrt{0.6(0.4)/100+0.5(0.5)/150}=0.06377$. The approximate $95\%$ interval is $0.10\pm1.96(0.06377)=[-0.0250,0.2250]$. This interval and the pooled test need not be exact inverses because their variance estimates impose different restrictions.{{cite:openintro2019}} (§6.2, interval standard error versus pooled testing standard error)

**Your turn.** If both groups have observed proportion $0.5$, what are the pooled estimate and the equality-test statistic, for any positive sample sizes?

::: {.callout-tip collapse="true" title="Answer"}
The pooled estimate is $0.5$ and the numerator is zero, so $z=0$ and the two-sided normal probability is $1$.
:::

## Assumptions and limits
Small expected success or failure counts can make the normal approximation poor. Paired binary measurements require a paired analysis rather than the independent two-sample denominator. Choosing a one-sided direction after observing the difference changes the rejection probability. The one-sided probability is half the two-sided probability only when the observed sign agrees with a direction fixed in advance.{{cite:openintro2019}} (§6.2, conditions and alternative hypotheses)
