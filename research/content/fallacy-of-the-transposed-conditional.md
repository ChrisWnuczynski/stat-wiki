## Motivating example — Reverse the conditioning, change the denominator
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
