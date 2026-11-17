## Motivating example
A positive screening result can be common among people with a condition while the condition remains uncommon among people with positive results. These statements count different groups. Sensitivity uses the people with the condition as its denominator; positive predictive value uses everybody with a positive result. A probability conditional on one group cannot generally be transferred to the other.{{cite:downey2020_thinkbayes2}} (Ch. 1, “Conditional Probability Is Not Commutative”)

## Definition — Conditionals refer to different reference sets
For events $A$ and $B$ of positive probability,
$$\Pr(A\mid B)=\frac{\Pr(A\cap B)}{\Pr(B)},\qquad \Pr(B\mid A)=\frac{\Pr(A\cap B)}{\Pr(A)}.$$
The numerators agree and the denominators need not. If the intersection has positive probability, equality holds precisely when $\Pr(A)=\Pr(B)$. If the intersection has probability zero, both conditionals are zero and can agree even when the marginal probabilities differ. Bayes' rule provides the conversion through the marginal probabilities, rather than permitting their omission.{{cite:grinstead_snell1997}} (§4.1, conditional probability and Bayes probabilities)

## Properties — Prior prevalence changes predictive value
Write $D$ for a condition and $+$ for a positive result. Let prevalence be $\pi=\Pr(D)$, sensitivity $s=\Pr(+\mid D)$ and false-positive probability $f=\Pr(+\mid D^c)$. Splitting positive results into disjoint groups yields
$$\Pr(D\mid +)=\frac{s\pi}{s\pi+f(1-\pi)}.$$
Provided $s>0$ and $f>0$, this tends to zero as prevalence tends to zero. The likelihood ratio $s/f$ multiplies prior odds $\pi/(1-\pi)$ to give posterior odds. A strong likelihood ratio can therefore coexist with a modest posterior probability when prior odds are small.{{cite:dodge2008}} (pp. 30–31, Bayes' Theorem)

The same bookkeeping applies to an alert system, a fault detector or evidence under competing hypotheses. It does not supply prior odds when no relevant prior model has been specified. Nor does a p-value become the probability of a null hypothesis merely by reversing the conditioning: a p-value is calculated within a sampling model, and a posterior requires a probability model over hypotheses.{{cite:grinstead_snell1997}} (§4.1, Bayes probabilities)

## Worked example — Count the people behind the percentages
Take a hypothetical population of $10{,}000$ people, prevalence $1/100$, sensitivity $9/10$ and false-positive probability $1/20$. Expected counts are $100$ with the condition, of whom $90$ test positive, and $9{,}900$ without it, of whom $495$ test positive. The positive predictive value is therefore $90/(90+495)=2/13\approx0.153846$. Sensitivity is $0.9$, but only about $15.4\%$ of positive results correspond to the condition under this model. These are an illustrative probability calculation, rather than performance claims for any actual test.{{cite:downey2020_thinkbayes2}} (Ch. 2, Bayes tables)

**Your turn.** Keep sensitivity and false-positive probability unchanged, but use prevalence $1/10$. What is the positive predictive value?

::: {.callout-tip collapse="true" title="Answer"}
The true-positive fraction is $0.9(0.1)=0.09$ and the false-positive fraction is $0.05(0.9)=0.045$. The positive predictive value is $0.09/0.135=2/3$.
:::

## Common misconceptions — Accuracy has several meanings
A test can classify most observations correctly simply because almost everybody belongs to the more common class. Its sensitivity, specificity and positive predictive value answer different questions. Reporting a single percentage without its conditioning event leaves the relevant denominator unclear. When sensitivity and specificity change between populations or testing thresholds, changing the prevalence alone is insufficient to transport predictive values. All parts of the probability model should correspond to the population and procedure under consideration.{{cite:downey2020_thinkbayes2}} (Ch. 1, conditional probability; Ch. 2, Bayes tables)

## Intuition
A conditional probability names a restricted sample space. $\Pr(A\mid B)$ restricts to the outcomes in $B$ and asks what fraction also lie in $A$. $\Pr(B\mid A)$ restricts to $A$ instead. The two restrictions are the same set only when $A$ and $B$ coincide up to null sets. The numerators $\Pr(A\cap B)$ agree. The denominators $\Pr(A)$ and $\Pr(B)$ generally do not, and the conditional probabilities differ by the ratio of those denominators:
$$\Pr(A\mid B)=\Pr(B\mid A)\frac{\Pr(A)}{\Pr(B)},$$
whenever $\Pr(B)>0$. If $\Pr(A\cap B)=0.2$, $\Pr(A)=0.4$ and $\Pr(B)=0.5$, then $\Pr(A\mid B)=0.2/0.5=0.4$ and $\Pr(B\mid A)=0.2/0.4=0.5$. The joint probability was not enough. Each conditional divides by a different margin.

Screening is this arithmetic with a rare condition in the role of $A$ and a positive test in the role of $B$. Sensitivity is $\Pr(+\mid D)$. Positive predictive value is $\Pr(D\mid +)$. In a hypothetical population of $10{,}000$ with prevalence $1/100$, sensitivity $9/10$ and false-positive probability $1/20$, ninety people with the condition test positive and $495$ people without it test positive. The predictive value is $90/(90+495)=2/13\approx 0.153846$. Most positive results are false positives because the condition is rare, not because the test is insensitive.

### Properties — Prevalence moves the predictive value in a definite direction
Write $s=\Pr(+\mid D)$ and $f=\Pr(+\mid D^c)$, and assume both are positive and $s$ does not depend on prevalence. Then
$$\Pr(D\mid +)=\frac{s\pi}{s\pi+f(1-\pi)}.$$
Differentiating with respect to $\pi$, or comparing two values directly, shows that the fraction increases with $\pi$. Lowering prevalence from $1/10$ to $1/100$, with $s=0.9$ and $f=0.05$, moves the predictive value from $2/3$ down to $2/13$. The likelihood ratio $s/f=0.9/0.05=18$ converts prior odds into posterior odds. At prevalence $1/100$ the prior odds are $1/99$. The posterior odds are $18/99=2/11$, and the posterior probability is $(2/11)/(1+2/11)=2/13$, the same count. A large likelihood ratio and a small posterior probability coexist when the prior odds are small enough.

The same identities with the labels swapped describe a negative test. Negative predictive value is $\Pr(D^c\mid -)$, and it depends on the true-negative rate and on prevalence. A rare condition makes a negative result very likely to be a true negative even when sensitivity is only moderate, because most people were negative before the test. Quoting one of these four conditional probabilities as if it were the other three collapses distinctions the formulas keep separate.{{cite:dodge2008}} (pp. 30–31, Bayes' Theorem)

### Common misconceptions
A p-value is a probability computed inside a sampling model, usually the probability of a result at least as extreme as the one observed, given a null hypothesis. It is not $\Pr(\text{null}\mid \text{data})$. Turning it into a posterior probability of the null requires a prior on the hypotheses and a model for the data under each hypothesis. The screening example is the same warning in a setting where all four ingredients can be counted. Omitting the prevalence is omitting $\Pr(D)$, and the conversion from sensitivity to predictive value cannot proceed.

Accuracy, the probability of a correct classification, can be high while predictive value is low. With prevalence $1/100$, sensitivity $0.9$ and false-positive probability $0.05$, the expected number correct in $10{,}000$ people is $90$ true positives plus $9{,}900-495=9{,}405$ true negatives, so $9{,}495/10{,}000=0.9495$. The test is accurate because almost everyone is well and most of them test negative. The positive predictive value remains $2/13$. A report of $95\%$ accuracy without a denominator does not say which of these events was counted.

Transporting a predictive value from one clinic to another requires the prevalence and the error rates of the second clinic. A different case mix changes $\pi$. A different testing threshold changes $s$ and $f$ together, often in opposite directions. Fixing $s$ and $f$ and only changing $\pi$ is the calculation above. It is the right calculation when the error rates really are stable, and the wrong one when they are not.{{cite:downey2020_thinkbayes2}} (Ch. 2, Bayes tables)

## Connections
Bayes' theorem is the identity that converts one conditional into the other. The fallacy is the habit of quoting the conversion without the marginal probabilities, or of treating the two conditionals as synonyms in ordinary language. "The test is positive in $90\%$ of cases with the condition" and "the condition is present in $90\%$ of positive tests" share the numeral and share nothing else in the worked population. Posterior odds, likelihood ratios, and base rates are the vocabulary that keeps the numeral attached to its denominator. A decision rule that acts on a positive test is a decision about $\Pr(D\mid +)$ and about the costs of the two errors. Sensitivity is one input to that rule. It is not the rule.
