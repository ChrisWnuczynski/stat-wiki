## Motivating example
Suppose a laboratory has an uncertain calibration mean and then obtains several new readings. A variance describes the uncertainty of each source, but the algebra of combining normal information is simpler after taking reciprocals: a small variance receives a large precision. The resulting estimate moves farther toward the more precise source.{{cite:gelman_bda2013}} (§2.5, p. 40, eq. 2.10)

## Definition — What precision measures
For a random quantity with variance $v>0$, its *precision* is $\tau=1/v$. It has units inverse to the squared units of the quantity: if measurements are in metres, precision is in inverse square metres. It describes concentration under a probability model, not closeness to the truth. A very narrow distribution centred at the wrong value is precise but inaccurate. The definition applies to any finite positive variance, although the convenient addition rule below belongs to a specified normal model.{{cite:gelman_bda2013}} (§2.5, p. 40, “Precisions of the prior and posterior distributions”)

For a normal mean, distinguish three variances. The observation variance $\sigma^2$ describes variation of individual readings about an unknown mean $\mu$; the prior variance $v_0$ describes uncertainty about $\mu$ before these readings; the posterior variance $v_1$ describes uncertainty about $\mu$ afterward. Their reciprocals are not interchangeable. In particular, $1/\sigma^2$ is the precision of one observation, whereas $n/\sigma^2$ is the precision supplied about a common mean by $n$ conditionally independent observations.{{cite:gelman_bda2013}} (§2.5, pp. 39–40, normal model and eq. 2.10)

## Properties — How normal information adds
Take $X_i\mid\mu\stackrel{\mathrm{iid}}{\sim}N(\mu,\sigma^2)$ with known $\sigma^2>0$ and prior $\mu\sim N(m_0,v_0)$ with $v_0>0$. Writing $\bar x$ for the observed mean, the posterior is $N(m_1,v_1)$, where
$$
\tau_1=\frac1{v_1}=\underbrace{\frac1{v_0}}_{\tau_0}+\underbrace{\frac n{\sigma^2}}_{\tau_{\rm data}},
\qquad
m_1=\frac{\tau_0m_0+\tau_{\rm data}\bar x}{\tau_0+\tau_{\rm data}}.
$$
The posterior mean lies between $m_0$ and $\bar x$ because the two positive weights sum to one. Increasing the sample size tightens the posterior and shifts its mean toward the data, provided the observation model remains credible. The prior's *equivalent sample size* is $\sigma^2/v_0$: it is the number of observations, possibly fractional, with the same precision about $\mu$ as the prior.{{cite:gelman_bda2013}} (§2.5, p. 40, eqs. 2.9–2.10)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Conditional independence gives a likelihood proportional to $\exp\{-\sum_i(x_i-\mu)^2/(2\sigma^2)\}$. Since $\sum_i(x_i-\mu)^2=\sum_i(x_i-\bar x)^2+n(\bar x-\mu)^2$, multiplication by the prior leaves, up to factors free of $\mu$,
$$
p(\mu\mid x)\propto\exp\left[-\frac12\left\{\frac n{\sigma^2}(\mu-\bar x)^2+\frac1{v_0}(\mu-m_0)^2\right\}\right].
$$
The coefficient of $\mu^2$ is $\tau_1=\tau_0+n/\sigma^2$ and that of $-2\mu$ is $\tau_0m_0+(n/\sigma^2)\bar x$. Completing the square gives a normal density with variance $1/\tau_1$ and the stated mean. This also shows precisely why the addition rule requires the independent normal likelihood and normal prior.{{cite:gelman_bda2013}} (§2.5, p. 40, derivation around eqs. 2.9–2.10)
:::
:::

## Worked example
A prior for a calibration mean is $N(10,4)$, where the second parameter is the variance. Four independent readings have mean $12$, and each reading has known variance $9$. The prior precision is $1/4=0.25$; the data precision is $4/9\approx0.4444$. Their sum is $25/36\approx0.6944$, so the posterior variance is $36/25=1.44$. The posterior mean is
$$
m_1=\frac{(1/4)10+(4/9)12}{25/36}=\frac{282}{25}=11.28.
$$
Thus $\mu\mid x\sim N(11.28,1.44)$. The prior contributes $9/25=36\%$ of the mean's weight and the observed average contributes $16/25=64\%$. The posterior mean does not reach $12$, because the prior still carries information.{{cite:gelman_bda2013}} (§2.5, p. 40, eq. 2.10)

**Your turn.** A normal prior for a mean is $N(20,16)$. Three independent observations have mean $24$ and known individual variance $12$. Find the posterior precision, variance and mean.

::: {.callout-tip collapse="true" title="Answer"}
The prior precision is $1/16$ and the data precision is $3/12=1/4$, giving posterior precision $5/16$ and variance $16/5=3.2$. The posterior mean is $[(1/16)20+(1/4)24]/(5/16)=116/5=23.2$. The sample mean gets four times the prior's weight.
:::

## Common misconceptions — What precision does and does not tell us
The posterior precision concerns $\mu$, not a future measurement. Under the same model, a new $X_{\rm new}$ has posterior predictive variance $\sigma^2+v_1$: even if $\mu$ becomes nearly certain, individual readings still vary. Conversely, calling a prior “high precision” does not make its centre correct. If a prior $N(0,0.01)$ is used for a true mean near $10$, its initial concentration can pull a small-sample posterior badly toward zero. A normal prior permits positive and negative means; a log-normal prior requires positivity, and a bounded uniform prior permanently excludes values outside its interval. Choosing the prior therefore asks what values are possible as well as how concentrated belief should be.{{cite:gelman_bda2013}} (§2.5, pp. 39–41, normal prior and posterior weighting)

## Assumptions and limits — When addition fails
Two common shortcuts also fail. First, adding $1/v_0+1/\sigma^2$ after **four** readings ignores three of them; the data contribution is $n/\sigma^2$. Second, with shared measurement error, four readings do not provide four independent copies of the same information. For example, if all four readings equal $\mu+B+\epsilon_i$ with a common random offset $B$, averaging removes much of the $\epsilon_i$ noise but cannot remove $B$; blindly using $4/\sigma^2$ overstates precision. When $\sigma^2$ itself is unknown, treating an estimate as known also understates uncertainty. A zero variance denotes a degenerate point mass, so “infinite precision” is a limiting phrase rather than an ordinary normal model with a finite variance parameter.{{cite:gelman_bda2013}} (§2.5, pp. 39–40, stated known-variance model)

## Connections
Precision weighting is the mechanism behind normal–normal conjugacy and many Gaussian updates. Inverse-gamma or scaled inverse-chi-square priors are used when a normal variance is also unknown; the simple fixed-variance update then becomes conditional on that variance. The relation $v_1=1/\tau_1$ keeps the variance and precision descriptions equivalent, while their interpretations remain tied to the particular random quantity whose uncertainty is being described.{{cite:gelman_bda2013}} (§2.5, pp. 39–41)
