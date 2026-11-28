## Lead context
The Bonferroni correction runs each test at the family level divided by the number of tests, so that the chance of any false rejection is at most that family level.

## Motivating example
Four independent tests, each with true-null rejection probability exactly $0.05$, have family-wise error $1-(0.95)^4\approx 0.1855$ when all four nulls are true. That is more than three times the nominal $0.05$. Splitting the level into four pieces, $0.05/4=0.0125$, brings the union bound back to $0.05$. If each true-null rejection probability is exactly $0.0125$, the independent error is $1-(0.9875)^4\approx 0.0491$, just under the cap.{{cite:hastie_esl2009}} (§18.7, p. 686)

## Intuition
Let $A_j$ be the event that test $j$ falsely rejects a true null. Valid true-null $p$-values satisfy $\mathbb{P}(p_j\le t)\le t$ for every $t\in[0,1]$, so testing at level $\alpha/m$ gives $\mathbb{P}(A_j)\le\alpha/m$. The event of at least one false rejection is the union of the $A_j$. A union is no more probable than the sum of the pieces, so
$$
\mathbb{P}\Bigl(\bigcup_{j=1}^{m} A_j\Bigr)\le\sum_{j=1}^{m}\mathbb{P}(A_j)\le\alpha.
$$
The argument never asks whether the tests are independent. Under arbitrary dependence the union is at most the sum. This compares the union with a bound, not with its probability under independence.{{cite:hastie_esl2009}} (§18.7, p. 686)

## Definition
To keep the family-wise error rate at most $\alpha$ across $m$ tests, test each null at level $\alpha/m$. Equivalently, multiply each $p$-value by $m$ and compare with $\alpha$, capping the product at $1$. Hastie, Tibshirani and Friedman state the same rule as: reject $H_{0j}$ when $p_j<\alpha/M$.{{cite:hastie_esl2009}} (§18.7, p. 686)

## Interpretation — The cap is not the exact error
When all $m$ nulls are true, the error events are independent, and $\mathbb{P}(A_j)=\alpha/m$ for every $j$, the family-wise error is $1-(1-\alpha/m)^m$, which is strictly less than $\alpha$ for $m>1$ and $\alpha\in(0,1)$. A level bound $\mathbb{P}(A_j)\le\alpha/m$ alone does not give this equality: the actual marginal rejection probabilities must attain the threshold. For $m=4$ and $\alpha=0.05$ the exact value is about $0.0491$, while the union bound says $0.05$. The gap grows as $m$ increases: $1-(1-\alpha/m)^m$ tends to $1-e^{-\alpha}$, and $1-e^{-0.05}\approx 0.0488$, still under $0.05$, but each individual test has become very strict.

Pairwise positive association alone does not order the family-wise error against independence. With four true nulls and $\alpha=0.05$, assign probability $0.01234$ to each of the four singleton-rejection outcomes, $0.00016$ to the outcome where all four reject, and $0.95048$ to no rejections. All other outcomes have probability zero. Each marginal is $\mathbb{P}(A_j)=0.01234+0.00016=0.0125$, and each pair has $\mathbb{P}(A_i\cap A_j)=0.00016>0.0125^2=0.00015625$. Yet $\mathrm{FWER}=4\times0.01234+0.00016=0.04952$, above the independent value $1-(0.9875)^4\approx0.049070288$ and still below $0.05$. With valid true-null $p$-values, the union bound remains $\mathrm{FWER}\le\alpha$ under arbitrary dependence.

## Properties
The union bound and the independent formula are the two numbers a user needs.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $\mathbb{P}(A_j)\le\alpha/m$, subadditivity gives $\mathbb{P}(\cup_j A_j)\le\sum_j\mathbb{P}(A_j)\le\alpha$.{{cite:durrett2019}} (Thm. 1.1.1(ii))

If all $m$ nulls are true, the $A_j$ are independent and $\mathbb{P}(A_j)=\alpha/m$ for every $j$, then
$$
\mathbb{P}(\cup_j A_j)=1-\prod_{j=1}^{m}(1-\alpha/m)=1-(1-\alpha/m)^m.
$$
For $\alpha=0.05$ and $m=4$, $1-0.0125=0.9875$ and $0.9875^4=0.9509297119140625$, so the error is $1-0.9875^4\approx 0.04907$, which rounds to $0.0491$. Without the correction, an exact rejection probability of $0.05$ for each true null gives $1-0.95^4=0.18549375$, which rounds to $0.1855$.

The inequality $(1-\alpha/m)^m\ge e^{-\alpha m/(m-\alpha)}$ is not needed. The elementary bound $1-x\le e^{-x}$ gives $(1-\alpha/m)^m\le e^{-\alpha}$, hence $1-(1-\alpha/m)^m\ge 1-e^{-\alpha}$ is the wrong direction for an upper bound. The union bound, not the exponential, is what caps the error by $\alpha$.{{cite:hastie_esl2009}} (§18.7, p. 686)
:::
:::

## Statistical use — $p$-values and critical values
Multiplying a $p$-value by $m$ and rejecting when the product is below $\alpha$ is the same test as comparing the raw $p$-value with $\alpha/m$, except that a product above $1$ is reported as $1$. For four tests and $\alpha=0.05$, a raw $p$-value of $0.02$ becomes $0.08$ and is not rejected. A raw $p$-value of $0.01$ becomes $0.04$ and is rejected. The uncorrected tests would have rejected both.

The correction applies to any collection of tests, not only to pairwise comparisons of means. It can be conservative when the tests are highly dependent or when $m$ is large. A procedure built for one family of contrasts can be sharper. The resulting bound can be strictly loose.{{cite:hastie_esl2009}} (§18.7, p. 686)

## Worked example
Four true nulls, family-wise level $0.05$. Each Bonferroni test uses $0.0125$.

The union bound is $4\times 0.0125=0.05$. If the four error events are independent and each has probability exactly $0.0125$, the family-wise error is $1-(0.9875)^4\approx 0.0491$. If the analyst instead tests each null with rejection probability exactly $0.05$, independence gives $1-(0.95)^4\approx 0.1855$.

A raw $p$-value of $0.02$ has adjusted value $\min(1,4\times 0.02)=0.08$, which exceeds $0.05$. A raw $p$-value of $0.01$ has adjusted value $0.04$, which does not.

**Your turn.** Six tests, family-wise level $0.05$. Find the per-test level, and the adjusted value of a raw $p$-value $0.01$.

::: {.callout-tip collapse="true" title="Answer"}
The per-test level is $0.05/6=0.008333\ldots$, or $1/120$. The adjusted $p$-value is $\min(1,6\times 0.01)=0.06$, which is above $0.05$, so the test does not reject.
:::

## Common misconceptions
The correction does not require independence. Independence and the actual marginal rejection probabilities determine the exact family-wise error; level bounds alone need not be attained. With valid true-null $p$-values, the guarantee $\le\alpha$ holds whether or not the tests are independent.

Multiplying the $p$-value by $m$ does not produce a probability of the null. It produces a number to compare with $\alpha$. An adjusted value of $0.08$ is not an $8\%$ chance that the null is true.

Splitting $\alpha$ into $m$ equal pieces is not the only split that the union bound allows. Any positive levels that sum to $\alpha$ cap the family-wise error by $\alpha$. Equal splits are the usual choice, not a requirement of the inequality.

## Assumptions and limits — A valid bound can still be useless
With $m=1000$ and $\alpha=0.05$, each test uses level $0.00005$. A real signal with a raw $p$-value of $0.001$ has adjusted value $1$ and is not rejected. The family-wise guarantee still holds. The procedure has spent almost all of its level on tests that were never going to reject, which is the sense in which the method is conservative for large $m$.{{cite:hastie_esl2009}} (§18.7, p. 686)

Let $V$ count false rejections and $R$ count all rejections. The realised false-discovery proportion is $\mathrm{FDP}=V/R$ when $R>0$ and $0$ when $R=0$; the false discovery rate is its expectation, $\mathrm{FDR}=\mathbb{E}(\mathrm{FDP})$. Since $\mathrm{FDP}\le\mathbf{1}_{\{V>0\}}$, taking expectations gives $\mathrm{FDR}\le\mathbb{P}(V>0)=\mathrm{FWER}\le\alpha$ for Bonferroni with valid true-null $p$-values. FDR and FWER are different error targets, but controlling FWER also bounds FDR. Neither bound guarantees that a realised list of rejections contains no false discoveries.

If the set of tests is chosen after looking at the data, $m$ is no longer the number that entered the bound. Adding unreported comparisons, or dropping tests that did not reject, changes the family the inequality was applied to.

## Connections
The union bound used here is the same subadditivity as on a [probability space](probability-space.qmd). [Markov's inequality](markov-s-inequality.qmd) is a different bound, on a tail rather than on a union of tests. The family-wise error rate is the probability of the union. Procedures that target a false-discovery proportion answer a different question and can reject more nulls at the same nominal level.{{cite:hastie_esl2009}} (§18.7, p. 686){{cite:durrett2019}} (Thm. 1.1.1(ii))

## History
Carlo Emilio Bonferroni, born in 1892 in Bergamo, published *Teoria statistica delle classi e calcolo delle probabilità* in 1936, in which the Bonferroni inequalities for dependent events appeared.{{cite:dodge2008}} (pp. 50–51) The testing rule is the special case of a union bound that Hastie, Tibshirani and Friedman state for $M$ hypotheses: reject when $p_j<\alpha/M$, which forces the family-wise error to be at most $\alpha$.{{cite:hastie_esl2009}} (§18.7, p. 686)
