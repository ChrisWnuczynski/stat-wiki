## Lead context
Sampling distributions, posterior distributions and simulation transitions condition on different things. Writing those conditioning statements explicitly separates three normal-model calculations that can otherwise look interchangeable.

## Motivating example
A normal regression has $n=12$ observations, $p=3$ full-rank coefficients and residual sum of squares $18$. Its residual estimate is $s^2=2$. A frequentist coefficient pivot uses $9$ degrees of freedom; a posterior variance calculation uses an inverse-gamma shape; a sampler must choose either a marginal or a full conditional variance law. The same fitted residuals enter all three, but the probability statements differ.

## Properties — Integrate the coefficient scale correctly
Set $v=\sigma^2$, $Q=X^\top X$ and $\widehat\beta=Q^{-1}X^\top y$. Completing the square gives
$$
\|y-X\beta\|^2=\mathrm{SSE}+(\beta-\widehat\beta)^\top Q(\beta-\widehat\beta).
$$
Under the specified prior $\pi(\beta,v)\propto v^{-1}$ relative to $d\beta\,dv$, the joint kernel is $v^{-n/2-1}\exp\{-[\mathrm{SSE}+(\beta-\widehat\beta)^\top Q(\beta-\widehat\beta)]/(2v)\}$. The integral of the Gaussian coefficient kernel contributes $(2\pi v)^{p/2}|Q|^{-1/2}$, so
$$
v\mid y\sim\operatorname{IG}((n-p)/2,\mathrm{SSE}/2),\qquad
\beta\mid v,y\sim N_p(\widehat\beta,vQ^{-1}).
$$
This calculation is a direct normal integral. The one-mean normal reference analysis is the $p=1$ instance, with the equivalent prior $1/\sigma$ relative to $d\mu\,d\sigma$.{{cite:bernardo2005_reference}} (§3.8, ex. 16)

The full conditional fixes $\beta$, so it does not integrate that Gaussian kernel. Consequently $v\mid\beta,y\sim\operatorname{IG}(n/2,\|y-X\beta\|^2/2)$. The determinant factor in a normal density is essential whenever its covariance depends on the conditioning parameter.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78)

## Worked example
For these summaries, $v\mid y\sim\operatorname{IG}(4.5,9)$. Its mean is $9/(4.5-1)=18/7=2.5714$, which differs from $s^2=2$. At a coefficient value with residual sum of squares $24$, the full conditional is instead $\operatorname{IG}(6,12)$. If $c_{jj}=1/4$, a conditional coefficient standard deviation at $v=2$ is $\sqrt{1/2}$; integrating $v$ yields a marginal $t_9$ coefficient distribution with scale $\sqrt{1/2}$. A $t$ scale is not its standard deviation, whose square here is $(1/2)\,9/7$.{{cite:bernardo2005_reference}} (§3.8, ex. 16; §3.11, ex. 21)

Independent repetitions of “draw $v$ from its marginal, then $\beta$ from its conditional” have density $p(v\mid y)p(\beta\mid v,y)=p(\beta,v\mid y)$ each time. Gibbs updates instead use the coefficient from the preceding step in the variance conditional. Their joint posterior can be stationary while successive pairs remain dependent. This follows from the factorisation itself, rather than from the visual appearance of a simulation trace.

**Your turn.** With $n=10$, $p=2$ and SSE $=16$, find the marginal inverse-gamma shape and rate, and its mean.

::: {.callout-tip collapse="true" title="Answer"}
The shape is $4$, the rate is $8$, and the mean is $8/(4-1)=8/3$.
:::

## Assumptions and limits
Posterior propriety for this reference prior uses full column rank, $n>p$ and $\mathrm{SSE}>0$. The frequentist Student pivot uses Gaussian iid errors and independence of the coefficient estimate and the residual sum of squares, and it describes the distribution of a function of $Y$ at a fixed parameter. A posterior statement conditions on the observed $y$ and a prior. The two calculations can share an algebraic skeleton, the completed square $\mathrm{SSE}+(\beta-\widehat\beta)^\top Q(\beta-\widehat\beta)$, and still describe different experiments.

## Definition — Three different conditional distributions
Hold the observed response fixed and write $v=\sigma^2$. The joint posterior under $\pi(\beta,v)\propto v^{-1}$ has two conditionals that answer different questions.

The marginal posterior of the variance integrates the coefficients:
$$
v\mid y\sim\operatorname{IG}\bigl((n-p)/2,\,\mathrm{SSE}/2\bigr).
$$
The conditional posterior of the coefficient given the variance is
$$
\beta\mid v,y\sim N_p(\widehat\beta,\,vQ^{-1}).
$$
The full conditional of the variance given a coefficient value keeps that coefficient in the residual sum of squares:
$$
v\mid\beta,y\sim\operatorname{IG}\bigl(n/2,\,\|y-X\beta\|^2/2\bigr).
$$
The marginal inverse-gamma shape is $(n-p)/2$ because the Gaussian integral over $p$ coefficients contributes a factor $v^{p/2}$. The full conditional shape is $n/2$ because that integral has not been taken. With $n=12$ and $p=3$, the marginal shape is $4.5$ and the full-conditional shape is $6$.{{cite:bernardo2005_reference}} (§3.8, ex. 16)

A sampling statement fixes $(\beta,v)$ and moves $Y$. Under Gaussian iid errors the pivot $(\widehat\beta_j-\beta_j)/(s\sqrt{c_{jj}})$ then has a $t_{n-p}$ law. The symbol $t_{n-p}$ also appears as the marginal posterior of a coefficient under this prior. The shared name records a shared integral, and the conditioning event differs: the sampling pivot treats $\beta_j$ as fixed and $\widehat\beta_j$ as random, while the marginal posterior treats $\widehat\beta_j$ and $\mathrm{SSE}$ as fixed and $\beta_j$ as random.

## Interpretation — A marginal variance is an average of conditional variances
For the worked summaries, $v\mid y\sim\operatorname{IG}(4.5,9)$ has mean $9/(4.5-1)=18/7=2.571429$. With $c_{jj}=1/4$, the conditional variance of the coefficient at a fixed $v$ is $v/4$. Averaging over the marginal posterior of $v$ gives
$$
\operatorname{Var}(\beta_j\mid y)=\E(v\mid y)\,c_{jj}=\frac{18}{7}\cdot\frac14=\frac{9}{14}=0.642857.
$$
The same number comes from the marginal $t_9$ description. The scale of that $t$ law satisfies $\mathrm{scale}^2=(1/2)$, because $(\mathrm{SSE}/9)c_{jj}=(18/9)(1/4)=1/2$, and a $t$ random variable on $9$ degrees of freedom has variance $\mathrm{scale}^2\cdot9/(9-2)=(1/2)\cdot9/7=9/14$. The scale and the standard deviation answer different questions. At the posterior mean of $v$ the conditional standard deviation is $\sqrt{(18/7)/4}=\sqrt{9/14}=0.801784$. The standard deviation of the marginal posterior is the same number here only because $\E(v)c_{jj}$ equals the $t$ variance; the scale $\sqrt{1/2}=0.707107$ is smaller.{{cite:bernardo2005_reference}} (§3.8, ex. 16; §3.11, ex. 21)

The plug-in that freezes $v$ at the residual estimate $s^2=2$ gives conditional standard deviation $\sqrt{2/4}=\sqrt{1/2}=0.707107$. That calculation reports the spread of $\beta_j$ given a fixed variance. It omits the posterior uncertainty in $v$, which is exactly the gap between $0.707107$ and $0.801784$ in this example.

## Intuition — What each sampler conditions on
An independent posterior draw can be made in two steps that follow the factorisation $p(\beta,v\mid y)=p(v\mid y)\,p(\beta\mid v,y)$. Draw $v$ from the marginal inverse-gamma, then draw $\beta$ from the normal distribution centred at $\widehat\beta$ with covariance $vQ^{-1}$. Each pair is an exact draw from the joint posterior, and successive pairs are independent if the generator's draws are independent.

A Gibbs sampler uses a different pair of conditionals: $v\mid\beta,y$ and $\beta\mid v,y$. After a coefficient vector has been drawn, the next variance draw sees $\|y-X\beta\|^2$, which exceeds $\mathrm{SSE}$ whenever $\beta\neq\widehat\beta$. The chain can have the joint posterior as its stationary distribution while consecutive pairs remain dependent. The dependence is the point of a Markov update. Monitoring a trace estimates that dependence; it does not change the stationary conditional distributions.

For the worked numbers, a coefficient with $\|y-X\beta\|^2=24$ produces the full conditional $\operatorname{IG}(6,12)$, whose mean is $12/(6-1)=2.4$. The marginal mean is $2.571429$. The two means differ because one of them has integrated $\beta$ and the other has pinned $\beta$ at a point whose residual sum of squares is $24$.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78)

## Common misconceptions
The residual estimate $s^2=\mathrm{SSE}/(n-p)=2$ and the posterior mean $18/7$ are both functions of $\mathrm{SSE}$. They use different divisors. The sampling unbiased estimator divides by $n-p=9$. The inverse-gamma mean with shape $(n-p)/2$ and rate $\mathrm{SSE}/2$ divides by $(n-p)/2-1=(n-p-2)/2$, which is $3.5$ in this example, giving $9/3.5=18/7$. Using $s^2$ as a posterior summary is a plug-in choice, and the posterior mean is the average of $v$ under the stated prior.

Drawing $v$ from the full conditional at the current $\beta$, and then drawing a new $\beta$, is a Gibbs transition. Drawing $v$ from the marginal and then drawing $\beta$ is an independent posterior sample. The two algorithms use different distributions for $v$. Only the second one produces independent pairs from the joint posterior on every iteration.{{cite:bernardo2005_reference}} (§3.8, ex. 16)

## Connections
The completed-square identity is also the source of the frequentist residual sum of squares: $\|Y-X\beta\|^2=\mathrm{SSE}+(\widehat\beta-\beta)^\top Q(\widehat\beta-\beta)$ holds as an algebraic decomposition of the observed vector. In the sampling experiment $\mathrm{SSE}$ and $\widehat\beta$ are random and independent under Gaussian errors, and $\mathrm{SSE}/v\sim\chi^2_{n-p}$. In the posterior experiment $\mathrm{SSE}$ is a fixed number and $v$ is random. The chi-squared tail and the inverse-gamma tail are integral transforms of the same quadratic, taken in opposite directions. Keeping the random element explicit is what separates the three calculations.
