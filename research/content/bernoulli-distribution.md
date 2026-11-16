## Motivating example
A factory can record each inspected part as defective or sound. If the chance of a defect on a specified inspection is $p$, coding defect as $1$ and sound as $0$ makes one inspection a Bernoulli variable. The code lets probability calculations, sample proportions and binary regression use the same simple observation model. The word “success” merely names the event coded $1$; a defect can be a success in this mathematical sense.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory, Definition and Generic Examples)

## Intuition
A Bernoulli distribution assigns all its mass to two points. It has one free parameter because once $P(X=1)=p$ is set, $P(X=0)=1-p$. The mean $p$ is not a possible fractional outcome of a single trial; it is the long-run average of coded outcomes under repeated trials with the same success probability. The variance $p(1-p)$ is greatest when the two outcomes are equally likely and vanishes at $p=0$ or $p=1$. The mass and cumulative plots above show the two jumps for $p=0.35$; they depict a *discrete* law, not a continuous density between zero and one.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory, Definition and Moments)

## Definition
If $A$ is an event and $X=\mathbf1_A$, then $X\sim\operatorname{Bernoulli}(p)$ with $p=P(A)$. Equivalently, $P(X=x)=p^x(1-p)^{1-x}$ for $x\in\{0,1\}$, with the endpoint cases understood directly from the two masses. Changing which event is coded as $1$ replaces $X$ by $1-X$ and replaces $p$ by $1-p$. The two variables describe the same physical outcome with opposite labels.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory, Definition)

## Properties
Because $X^2=X$, its mean and variance are $E(X)=p$ and $\operatorname{Var}(X)=p(1-p)$, as the collapsed proof on this page shows. The probability generating function $E(z^X)=1-p+pz$ records the same two masses. It can be raised to a power for a sum of independent, identically distributed trials; without independence, generating functions do not simply multiply.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory, Moments){{cite:siegrist2022_binomial_distribution}} (§11.2, Distribution Functions)

## Related distributions
If $X_1,\ldots,X_n$ are independent Bernoulli$(p)$ variables, $S=\sum_iX_i$ counts successes and follows $\operatorname{Binomial}(n,p)$. A specified sequence containing $k$ successes has probability $p^k(1-p)^{n-k}$; there are $\binom nk$ such sequences, giving the binomial mass $P(S=k)=\binom nkp^k(1-p)^{n-k}$. Setting $n=1$ recovers the Bernoulli law. If the trials have different success probabilities, the sum is generally *Poisson binomial*, not ordinary binomial; if the draws are without replacement from a finite population, the count is hypergeometric.{{cite:siegrist2022_binomial_distribution}} (§11.2, Distribution Functions and finite-population sampling)

## Statistical inference
For independent trials with a common unknown $p$, the sample proportion $\bar X=S/n$ estimates $p$. Its variance is $p(1-p)/n$: averaging reduces sampling variation, although one observed proportion does not itself reveal whether independence and a common probability are credible. Logistic regression lets $p$ vary with measured predictors while retaining a Bernoulli response at each observation. This is why a single observation model can serve both a coin experiment and a binary disease indicator.{{cite:siegrist2022_binomial_distribution}} (§11.2, Moments and sample proportion){{cite:dodge2008}} (pp. 36–37, “Bernoulli Distribution”)

## Generating random samples — A uniform threshold
To simulate a Bernoulli$(p)$ outcome, draw $U$ uniformly from $[0,1]$ and return $1$ when $U\le p$, otherwise $0$. The interval with length $p$ has probability $p$, which proves that the result has the desired law. Use independent uniforms for independent trials; reusing the same $U$ would make the outcomes identical rather than independent.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory, uniform construction)

## Worked example
Suppose an inspection flags a part with probability $p=0.30$. One indicator has $P(X=0)=0.70$, mean $0.30$ and variance $0.30(0.70)=0.21$. For three independent inspections at the same rate, the probability of exactly two flags is $\binom32(0.30)^2(0.70)=0.189$. The probability all three are flagged is $(0.30)^3=0.027$. The first calculation counts three possible positions for the single unflagged part; the second has only one arrangement.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory){{cite:siegrist2022_binomial_distribution}} (§11.2, Distribution Functions)

**Your turn.** Four independent events each occur with probability $0.60$. Find the probability of exactly three occurrences and of at least one occurrence. State the assumption needed for both calculations.

::: {.callout-tip collapse="true" title="Answer"}
Exactly three occurrences have probability $\binom43(0.60)^3(0.40)=0.3456$. At least one has probability $1-(0.40)^4=0.9744$. Both use independence and the same success probability on every trial; otherwise the simple binomial calculation need not apply.{{cite:siegrist2022_binomial_distribution}} (§11.2, Distribution Functions)
:::

## Common misconceptions
The expectation $p$ averages coded outcomes, while an individual outcome is always $0$ or $1$. A Bernoulli variable models **one** binary outcome; a binomial variable counts successes across a specified number of independent equal-$p$ trials. Two variables may each be Bernoulli$(p)$ while being dependent: the pair $(X,X)$ has the same margins as two independent copies but always agrees. Thus knowing each trial's law does not by itself justify multiplying their probabilities.{{cite:siegrist2022_bernoulli_intro}} (§11.1, Basic Theory){{cite:siegrist2022_binomial_distribution}} (§11.2, Distribution Functions)

## Assumptions and limits — When binary does not mean Bernoulli trials
Any single coded binary event has a Bernoulli distribution, but a sequence needs stronger assumptions before its sum is binomial. Draw two tokens without replacement from a bag with one red and one blue: each draw is a binary red indicator, yet after the first red draw the second cannot be red. Their total is always one, whereas independent Bernoulli$(1/2)$ trials would sometimes total zero or two. A disease indicator may also have a different $p$ for patients of different ages; treating all patients as equal-$p$ trials erases that structure. Dichotomizing a measured blood pressure at a threshold yields a Bernoulli indicator but discards how far observations lie above or below the threshold.{{cite:siegrist2022_binomial_distribution}} (§11.2, finite-population sampling){{cite:siegrist2022_bernoulli_intro}} (§11.1, Generic Examples)

## Connections
The question [Same margins, two joints](../questions/ex-sp-bernoulli-pairs.qmd) isolates the difference between a Bernoulli marginal law and independence. [A bound for a sample proportion](../questions/ex-sp-proportion-bound.qmd) uses the Bernoulli variance to quantify how an average of independent trials concentrates around $p$. Both start with the elementary two-point law and ask what extra assumptions are needed for a statement about several observations.{{cite:siegrist2022_binomial_distribution}} (§11.2, Moments)

## History
Jakob Bernoulli's *Ars Conjectandi* was published posthumously in 1713 and studied probability in repeated trials. The modern two-point distribution bears his name; its $0$–$1$ notation and probability mass function are contemporary ways to express the success-or-failure experiment.{{cite:dodge2008}} (p. 37, “Bernoulli, Jakob” and “Bernoulli Distribution”)
