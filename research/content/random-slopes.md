## Lead context
A random slope lets the effect of a covariate differ by group, with the group-specific slopes drawn from a common distribution.{{cite:bates_lme4_2015}} (§1.1, eq. 2–3, p. 3)

## Motivating example
Eighteen drivers are each observed across several days of sleep restriction, and reaction time is expected to worsen as the days accumulate. A single slope would say that every driver slows by the same number of milliseconds per day. The plots of these studies usually show some drivers slowing sharply and at least one hardly changing. A random slope gives each driver a deviation from the average daily change, and a variance component says how large those deviations are in the population of drivers, not merely in the eighteen who were measured.{{cite:bates_lme4_2015}} (§1.2, p. 3)

## Intuition — The slope is a draw, the mean slope is the fixed effect
Write the observation on occasion $t$ in group $j$ as a fixed line plus a group-specific intercept and a group-specific slope,
$$
Y_{jt}=\beta_0+\beta_1 t+a_j+b_j t+\varepsilon_{jt}.
$$
The pair $(a_j,b_j)$ is a draw, not a constant to be re-estimated as if the same groups would reappear. Repeat the study and a new set of groups arrives with new draws. The fixed coefficients $\beta_0$ and $\beta_1$ are the mean intercept and the mean slope of that population. The covariance matrix of $(a_j,b_j)$ describes the spread of intercepts, the spread of slopes, and whether groups with high intercepts tend to have steep or flat slopes. The residual $\varepsilon_{jt}$ is what is left after that group line.{{cite:bates_lme4_2015}} (§1.1, eq. 2–3, p. 3)

Dropping $b_j$ returns a random-intercept model: parallel lines, shifted up or down. Keeping $b_j$ lets the lines fan out. The fanning is visible in the marginal covariance, which grows with $t^{2}$ when the slope variance is positive.

## Definition
In the linear mixed model the conditional distribution of the response, given the random effects, is normal with mean $X\beta+Zb$ and covariance $\sigma^{2}$ times a known weight matrix. The random-effects vector itself is normal with mean zero and covariance $\Sigma$. A random intercept and a random slope for one grouping factor are the case in which the rows of $Z$ that belong to a group are $(1,\ t)$, and the corresponding $2\times 2$ block of $\Sigma$ is
$$
\begin{pmatrix}\sigma_a^{2}&\sigma_{ab}\\\sigma_{ab}&\sigma_b^{2}\end{pmatrix}.
$$
The block must be positive semidefinite, so $\sigma_a^{2}\ge 0$, $\sigma_b^{2}\ge 0$ and $\sigma_{ab}^{2}\le\sigma_a^{2}\sigma_b^{2}$. Bates, Mächler, Bolker and Walker parameterise $\Sigma$ as $\sigma^{2}\Lambda\Lambda^{\top}$, which enforces that semidefinite constraint by construction and makes the residual scale $\sigma$ explicit.{{cite:bates_lme4_2015}} (§1.1, eq. 2–4, p. 3)

## Properties — The marginal covariance carries the slope variance
Integrating out the random effects gives a covariance that depends on the occasion times.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Given $(a_j,b_j)$, the observations in group $j$ are independent with variance $\sigma^{2}$, so the conditional covariance of $Y_{jt}$ and $Y_{js}$ is $\sigma^{2}$ on the diagonal and $0$ off it. The law of total covariance adds the covariance of the conditional means. Those means differ from the fixed line by $a_j+b_j t$ and $a_j+b_j s$, and
$$
\operatorname{Cov}(a_j+b_j t,\ a_j+b_j s)=\sigma_a^{2}+(t+s)\sigma_{ab}+ts\sigma_b^{2}.
$$
Therefore, for $t\ne s$,
$$
\operatorname{Cov}(Y_{jt},Y_{js})=\sigma_a^{2}+(t+s)\sigma_{ab}+ts\sigma_b^{2},
$$
and the marginal variance at occasion $t$ is that expression at $s=t$, plus $\sigma^{2}$. If $\sigma_b^{2}>0$, the variance grows like $t^{2}\sigma_b^{2}$ as the occasion moves away from the origin of $t$. Setting $\sigma_b^{2}=\sigma_{ab}=0$ removes every term that involves $t$, and the covariance between occasions becomes the constant $\sigma_a^{2}$.{{cite:bates_lme4_2015}} (§1.1, eq. 2–3, p. 3)
:::
:::

A comparison that removes the random slope sets $\sigma_b^{2}$ and $\sigma_{ab}$ to $0$. That point is on the boundary of the positive-semidefinite set Bates requires of $\Sigma$.{{cite:bates_lme4_2015}} (§1.1, eq. 3–4, p. 3)

## Statistical use — Quote the mean slope, and the spread of slopes, separately
The estimate of $\beta_1$ is the average change per unit of $t$. The estimate of $\sigma_b$ is the typical size of a group’s departure from that average. They answer different questions. A large $\sigma_b$ means the average slope is a poor description of a single group, even when $\beta_1$ itself is precisely estimated. The correlation $\sigma_{ab}/(\sigma_a\sigma_b)$ says whether groups that start high tend to rise faster or slower. Predicting the realised $(a_j,b_j)$ for the groups in the sample is a third task: with the variances treated as known it is a best linear predictor of a random vector, and with the variances estimated it is the empirical version of that predictor. Those predictions change if the study is repeated. The fixed coefficients are the quantities the repetition is supposed to estimate.{{cite:bates_lme4_2015}} (§1.1–1.2, eq. 2–3, p. 3)

Software such as `lmer` encodes the random slope by a term `(t | group)` in the model formula. The same formula with `(1 | group)` drops the slope and the intercept–slope covariance together. The fit minimises a profiled residual maximum-likelihood criterion, or a profiled likelihood, in the variance parameters.{{cite:bates_lme4_2015}} (§1, pp. 1–3)

## Worked example
Take $\sigma_a^{2}=4$, $\sigma_b^{2}=1$, $\sigma_{ab}=-1/2$ and $\sigma^{2}=1$. At occasion $t=2$,
$$
\operatorname{Var}(Y_{j2})=4+2\cdot 2\cdot\bigl(-\tfrac12\bigr)+2^{2}\cdot 1+1=4-2+4+1=7.
$$
The covariance between occasion $0$ and occasion $2$ is
$$
4+(0+2)\bigl(-\tfrac12\bigr)+0=3.
$$
The negative covariance $\sigma_{ab}$ lowers the variance at $t=2$ relative to a model with the same marginal variances and no intercept–slope correlation: without it the variance would be $4+4+1=9$ rather than $7$. The correlation of the random intercept and slope is $(-1/2)/\sqrt{4\cdot 1}=-1/4$. Groups with a high intercept tend to have a slightly flatter slope, and by $t=2$ that negative association has pulled the marginal variance down by $2$.

**Your turn.** Use the same variances and set $\sigma_{ab}=0$. Find $\operatorname{Var}(Y_{j2})$ and $\operatorname{Cov}(Y_{j0},Y_{j2})$.

::: {.callout-tip collapse="true" title="Answer"}
The variance is $4+0+4+1=9$. The covariance is $4+(0+2)\cdot 0+0\cdot 2=4$. Removing the intercept–slope correlation raises the marginal variance at $t=2$ from $7$ to $9$ and raises the covariance with the baseline from $3$ to $4$.
:::

## Common misconceptions
The random slope is not a fixed interaction with a set of named groups. A fixed interaction estimates a separate constant for each group that was observed and does not by itself say what a new group would do. The variance $\sigma_b^{2}$ is not a standard error of $\beta_1$. One describes the spread of group slopes; the other describes the precision of the mean slope. A correlation near zero between intercept and slope is not a statement that the slope is unnecessary. The slope variance can be large while the intercept and the slope are nearly uncorrelated.

Setting $\sigma_b^{2}=0$ is a boundary point of the covariance parameter, not an interior point of the positive-semidefinite set.

## Assumptions and limits — The origin of $t$, and a slope variance of zero
The term $t^{2}\sigma_b^{2}$ depends on where $t=0$ is placed. Shifting the time origin moves variation between the intercept, the slope, and their covariance, while the fitted lines for the observed occasions stay the same. A large intercept variance and a small slope variance after centring $t$ are not the same scientific claim as the same numbers before centring. Report the origin with the variance components.

A second limit is the boundary. If the slope deviations are negligible, a fit can place $\sigma_b^{2}$ at zero, on the edge of the covariance set. An interior normal approximation to that variance estimate is then the wrong local picture, because the parameter cannot move below zero.

The normal assumption on $(a_j,b_j)$ is a model for the population of groups. A few groups with slopes far beyond that normal spread will pull $\sigma_b^{2}$ up. The marginal covariance formula remains the second-moment calculation whenever the stated variances exist; the normal likelihood used to estimate them does not.

## Connections
A model with only a random intercept is the special case $\sigma_b^{2}=\sigma_{ab}=0$. [Fixed and random effects](fixed-and-random-effects.qmd) names the distinction between $\beta_1$ and the draws $(a_j,b_j)$, and the [linear mixed model](linear-mixed-model.qmd) is the joint specification. The fixed part $\beta_0+\beta_1 t$ is an ordinary linear mean; the random part changes the covariance, not the interpretation of $\beta_1$ as a population-average slope. A [generalised linear mixed model](generalised-linear-mixed-model.qmd) keeps the same linear predictor and replaces the normal residual by a non-normal conditional distribution, so the marginal covariance formula in the proof is then no longer the whole sampling story.{{cite:bates_lme4_2015}} (§1.1, eq. 2–3, p. 3)

## History
Random-effects models for repeated measurements were already in wide use when Bates, Mächler, Bolker and Walker set out the form fitted by `lmer`: a normal conditional mean $X\beta+Zb$, a normal random-effects vector with covariance factorised as $\sigma^{2}\Lambda\Lambda^{\top}$, and a profiled criterion in the variance parameters. Their running example is the sleep-deprivation reaction-time study, in which each subject’s day slope is a draw around a population slope. The marginal covariance calculation above is the second-moment consequence of that conditional normal model.{{cite:bates_lme4_2015}} (§1, pp. 1–3)
