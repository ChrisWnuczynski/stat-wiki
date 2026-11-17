## Motivating example
After a short run of coin tosses, a forecast for several further tosses must account for uncertainty about the coin's success probability. A posterior mean gives the probability of one future success, but treating that mean as a known probability understates the variation of a future count when several trials share the same uncertain probability.{{cite:downey2020_thinkbayes2}} (§18.4, the beta distribution)

## Key results — Mixing creates dependence between future trials
If $\theta\mid x\sim\operatorname{Beta}(a,b)$, put $T=a+b$ and $p=a/T$. Conditional on $\theta$, future indicators $Y_1,\ldots,Y_m$ are independent Bernoulli variables. After integrating over $\theta$, each still has success probability $p$, but distinct indicators satisfy
$$
\operatorname{Cov}(Y_i,Y_j\mid x)=\operatorname{Var}(\theta\mid x)
=\frac{ab}{T^2(T+1)},\qquad
\operatorname{Corr}(Y_i,Y_j\mid x)=\frac1{T+1}.
$$
The sequence is exchangeable, with positive dependence from its shared random probability. Conditional independence and marginal independence are different assertions.{{cite:siegrist2022_beta_bernoulli}} (§10.7, covariance and correlation)

Summing variances and pairwise covariances gives
$$
E(\widetilde X\mid x)=mp,\qquad
\operatorname{Var}(\widetilde X\mid x)=mp(1-p)\frac{T+m}{T+1}.
$$
The multiplier is $1+(m-1)/(T+1)$: it equals one for $m=1$ and exceeds one for $m>1$. At fixed posterior mean, increasing $T$ concentrates the posterior and makes this multiplier approach one. The count law then approaches $\operatorname{Bin}(m,p)$ for fixed $m$. This follows directly from its rising-factorial probability formula.{{cite:siegrist2022_beta_bernoulli}} (§10.7, beta-binomial distribution)

## Intuition — The beta integral and sequential prediction agree
Multiplying a $\operatorname{Beta}(\alpha,\beta)$ prior by a binomial likelihood with $s$ successes in $n$ trials produces shapes $a=\alpha+s$, $b=\beta+n-s$. The predictive probability for an ordered future sequence with $k$ successes is $B(a+k,b+m-k)/B(a,b)$. There are $\binom mk$ sequences with that count, giving the beta-binomial mass.{{cite:downey2020_thinkbayes2}} (§18.4)

Alternatively, update after each future observation and multiply the successive predictive probabilities. Each success adds one to the success shape and each failure adds one to the failure shape. For any ordering with $k$ successes, the numerator is $(a)^{\overline k}(b)^{\overline{m-k}}$ and denominator $(T)^{\overline m}$. The same expression emerges independently of order.{{cite:siegrist2022_beta_bernoulli}} (§10.7, finite-dimensional distributions)

## Worked example

### Five future tosses with a shared unknown probability
A $\operatorname{Beta}(2,2)$ prior and eight successes in ten trials give $\operatorname{Beta}(10,4)$. For five future trials, probabilities for counts $0,1,2,3,4,5$ are approximately
$$
(0.006536,0.040850,0.128385,0.256769,0.333800,0.233660).
$$
They sum to one. Thus $P(\widetilde X\ge4\mid x)=0.5674603$ and $E(\widetilde X\mid x)=25/7$. The variance is $190/147=1.292517$, compared with plug-in binomial variance $50/49=1.020408$. Here the inflation factor is $19/15$, and the correlation between any two future indicators is $1/15$.{{cite:siegrist2022_beta_bernoulli}} (§10.7, beta-binomial distribution)

**Your turn.** What is the posterior predictive probability that two future tosses are both heads? Compare it with squaring the one-toss prediction.

::: {.callout-tip collapse="true" title="Answer"}
The probability is $E(\theta^2\mid x)=10(11)/(14\cdot15)=11/21\approx0.523810$. Squaring $5/7$ gives $25/49\approx0.510204$. The difference $2/147$ is the posterior variance of $\theta$.
:::
