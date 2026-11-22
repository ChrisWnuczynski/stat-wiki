## Motivating example

Unknown mean and variance interact in a normal model: the variance determines how much a noisy sample mean is trusted, while the mean determines squared residuals. Independent priors do not remove this posterior interaction. Full conditional distributions make each parameter easy to update when the other is held fixed.{{cite:gelfand_smith1990}} (§3.5, p.405)

## Statement

Let $X_i\mid\mu,v\overset{iid}{\sim}N(\mu,v)$, with independent priors $\mu\sim N(\mu_0,v_0)$ and $v\sim\operatorname{InvGamma}(a_0,b_0)$, where $v_0,a_0,b_0>0$. The inverse-gamma convention is density proportional to $v^{-a-1}e^{-b/v}$. Then
$$\mu\mid v,x\sim N(m_v,V_v),\quad
 V_v=(n/v+1/v_0)^{-1},\quad m_v=V_v(n\bar x/v+\mu_0/v_0),$$
$$v\mid\mu,x\sim\operatorname{InvGamma}\left(a_0+\frac n2,
 b_0+\frac12\sum_i(x_i-\mu)^2\right).$$
Gaussian means and inverse-gamma variance updates arise by holding all other parameters fixed in the joint density.{{cite:gelfand_smith1990}} (§§3.4–3.5, p.405)

## Proof

The joint posterior kernel is
$$v^{-a_0-n/2-1}\exp\left[-\frac{b_0+\tfrac12\sum_i(x_i-\mu)^2}{v}
-\frac{(\mu-\mu_0)^2}{2v_0}\right].$$
For fixed $v$, use $\sum_i(x_i-\mu)^2=S+n(\mu-\bar x)^2$ and complete the square in $\mu$. The quadratic coefficient is $n/v+1/v_0$ and the linear coefficient is $n\bar x/v+\mu_0/v_0$, giving the displayed normal mean and variance. For fixed $\mu$, the normal-prior factor is constant in $v$; matching the remaining powers and reciprocal-variance exponential gives the inverse-gamma update. Gaussian precision addition is the product-of-densities identity.{{cite:deisenroth_faisal_ong2020}} (§6.5.2, p.201, Eqs.6.74–6.75; §6.6.1, p.209, Table6.2)

## Intuition — Conditioning is not marginalisation

The mean conditional uses the current value of $v$ and the variance conditional uses the current value of $\mu$. Replacing that value by an estimate is not integration. Nor is the independent-prior model the same as a joint normal–inverse-gamma prior whose conditional mean variance scales with $v$. They impose different prior dependence.{{cite:gelfand_smith1990}} (§3.5, p.405)

## Worked example

For data $(1,2,3)$, prior $\mu\sim N(0,4)$ and $v\sim\operatorname{InvGamma}(2,1)$, the mean conditional at $v=1$ is
$$\mu\mid v=1,x\sim N(24/13,4/13).$$
At $\mu=2$, the squared residual sum is two, so $v\mid\mu=2,x\sim\operatorname{InvGamma}(3.5,2)$. Its mean is $2/(3.5-1)=0.8$. The reciprocal variance has Gamma shape $3.5$ and rate two, with mean $1.75$; the reciprocal of this mean is $4/7$, which differs from the mean variance. Transforming a random parameter and transforming its expectation are different operations.{{cite:deisenroth_faisal_ong2020}} (§6.6.1, p.209, Table6.2)

**Your turn.** In the same example, what is the conditional normal law at $v=4$?

::: {.callout-tip collapse="true" title="Answer"}
The precision is $3/4+1/4=1$, hence variance one. The mean is $(3\cdot2/4)/1=1.5$, so the conditional is $N(1.5,1)$.
:::

For the same data and prior, what is the conditional law of $v$ when $\mu=0$?

::: {.callout-tip collapse="true" title="Answer"}
The residual sum of squares is $1+4+9=14$, so $v\mid\mu=0,x\sim\operatorname{InvGamma}(3.5,8)$. Its mean is $8/(3.5-1)=3.2$.
:::

## Statistical use — Alternating simulation

A systematic Gibbs sweep draws $\mu$ from its conditional using the previous variance and then draws $v$ using the new mean. Each update preserves the joint posterior when the input has that posterior law: integrating $p(\mu'\mid v,x)p(v\mid x)$ over $v$ reconstructs the joint distribution, and the same argument applies to the other update. This invariance is distinct from convergence from an arbitrary starting state. Monte Carlo error must account for dependence across sweeps.{{cite:gelfand_smith1990}} (§§2.3–2.4, pp.400–401; §3.5, p.405)
