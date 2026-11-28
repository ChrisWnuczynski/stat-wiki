## Motivating example
A laboratory receives ten binary outcomes today and five tomorrow. It wants tomorrow's analysis to incorporate today's evidence without storing every individual outcome. Under a common Bernoulli probability and a beta prior, two running shape parameters contain everything needed for exact updating.{{cite:siegrist2022_bayes_estimators}} (§ “The Bernoulli Distribution”) An urn problem gives a small illustration of updating uncertainty: after seeing a ball's colour, infer which urn supplied it.{{cite:dodge2008}} (p. 31, urn example)

## Key results — Normalisation does not change the joint update
Bayes' formula multiplies a prior density by a likelihood and divides by its integral.{{cite:durrett2019}} (§4.1, Ex. 4.1.1, p. 216) If $L_1(\theta)$ and $L_2(\theta)$ are conditionally independent batch likelihoods, the first posterior is $\pi_1=\pi L_1/Z_1$. Updating again gives
$$
\pi_2(\theta)=\frac{\pi_1(\theta)L_2(\theta)}{\int\pi_1(u)L_2(u)\,du}
=\frac{\pi(\theta)L_1(\theta)L_2(\theta)}{\int\pi(u)L_1(u)L_2(u)\,du}.
$$
The factor $Z_1$ cancels. The identity requires finite, positive normalising integrals. It explains why coherence extends beyond conjugate families: conjugacy makes the calculation convenient, while the cancellation is an application of conditional probability.{{cite:durrett2019}} (§4.1, Ex. 4.1.1, p. 216)

For dependent batches the correct second likelihood is $p(x_2\mid x_1,\theta)$. Sequential conditioning still agrees with joint conditioning when that conditional factor is used. Multiplying two marginal binomial likelihoods instead would assert a conditional independence that the model lacks.{{cite:durrett2019}} (§4.1, Ex. 4.1.1, p. 216)

## Generalizations — Running totals and posterior prediction
For a $\operatorname{Beta}(a,b)$ prior, $s$ successes and $f$ failures give shapes $a+s,b+f$. Processing batches changes the route to these totals, not the totals themselves. The posterior mean is $(a+s)/(a+b+s+f)$; its variance is $(a+s)(b+f)/\{(a+b+s+f)^2(a+b+s+f+1)\}$.{{cite:siegrist2022_bayes_estimators}} (§ “The Bernoulli Distribution”)

The posterior also determines future uncertainty. If its shapes are $A,B$, the probability of two future successes is $\E(\theta^2)=A(A+1)/\{(A+B)(A+B+1)\}$. It generally exceeds $\{\E(\theta)\}^2$, since both future trials share the same uncertain probability. Conditional independence given $\theta$ does not imply independence after averaging over $\theta$. The beta moment identity follows by dividing the normalising integrals of the beta kernels.{{cite:siegrist2022_bayes_estimators}} (§ “The Bernoulli Distribution”, beta posterior and moments)

## Worked example
Start with $\operatorname{Beta}(2,3)$. Four successes in ten trials give $\operatorname{Beta}(6,9)$; three successes in five more give $\operatorname{Beta}(9,11)$. Pooling gives seven successes and eight failures, producing the same final shapes. The posterior mean is $0.45$, its variance is $0.0117857$, and the probability of two future successes is $3/14=0.214286$. The plug-in probability $0.45^2=0.2025$ omits uncertainty about $\theta$.

**Your turn.** Starting with $\operatorname{Beta}(2,3)$, process two batches with outcomes $(1,4)$ and $(2,3)$, where each pair is successes and trial count. Reverse their order and compare the final means.

::: {.callout-tip collapse="true" title="Answer"}
Both orders add three successes and four failures, giving $\operatorname{Beta}(5,7)$ and posterior mean $5/12=0.416667$.
:::
