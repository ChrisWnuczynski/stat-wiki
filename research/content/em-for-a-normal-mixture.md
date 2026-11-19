## Motivating example

A set of measurements may contain two overlapping populations without a recorded label for each observation. Assigning every point permanently to its closest mean loses uncertainty about those labels. A normal mixture instead treats component membership as latent and alternates between fractional memberships and parameter estimation.{{cite:deisenroth_faisal_ong2020}} (§11.3, pp.360–361)

## Definition — One complete iteration

For $p(x)=\sum_{k=1}^K\pi_k\phi(x;\mu_k,\sigma_k^2)$, the E-step computes
$$r_{ik}=\frac{\pi_k\phi(x_i;\mu_k,\sigma_k^2)}{\sum_j\pi_j\phi(x_i;\mu_j,\sigma_j^2)}.$$
All parameters on this right-hand side are from the current iterate. Put $N_k=\sum_i r_{ik}$. For a component with $N_k>0$, the unconstrained M-step is
$$\pi_k^{\rm new}=N_k/n,\quad
\mu_k^{\rm new}=\frac{\sum_i r_{ik}x_i}{N_k},\quad
(\sigma_k^2)^{\rm new}=\frac{\sum_i r_{ik}(x_i-\mu_k^{\rm new})^2}{N_k}.$$
The residuals use the updated mean and the same responsibilities throughout this M-step. These unconstrained updates require positive updated variances. Fixed variances, shared variances, or covariance constraints require the corresponding constrained maximisation.{{cite:deisenroth_faisal_ong2020}} (§11.3, p.361, Eqs.11.53–11.56)

## Properties — Why the likelihood increases

The E-step forms the conditional expectation of the complete-data log likelihood. The M-step increases that expected log likelihood while holding the conditional distribution fixed. This is the $Q(\theta\mid\theta^{\rm old})$ construction.{{cite:dempster_laird_rubin1977}} (§2, p.6, Eq.2.17)

With zero-weight terms interpreted by their continuous limits, Jensen's inequality bounds the observed log likelihood below by
$$\sum_{i,k}r_{ik}\{\log\pi_k+\log\phi(x_i;\mu_k,\sigma_k^2)-\log r_{ik}\}.$$
At the E-step responsibilities, the bound touches the current likelihood. Increasing the bound therefore cannot decrease the likelihood. This statement concerns exact E-steps and an M-step that increases $Q$; it does not guarantee a global maximum or convergence of the parameter sequence.{{cite:dempster_laird_rubin1977}} (§3, pp.6–8, Lem.1 and Thm.1)

## Worked example — A two-point update

Take $x=(0,4)$, initial weights $(0.5,0.5)$, means $(1,2)$ and variances $(1,1)$. The first-component responsibilities are $(0.817574,0.075858)$, giving effective counts $(0.893433,1.106567)$. The updated weights, means and variances are
$$\pi^{\rm new}=(0.446716,0.553284),\quad
\mu^{\rm new}=(0.339626,3.340571),$$
$$ (\sigma^2)^{\rm new}=(1.243157,2.202868).$$
The observed log likelihood increases from $-5.443868$ to $-3.804429$. Both points still contribute to both components. Effective counts can be fractional: they are sums of conditional probabilities, rather than observed membership counts.{{cite:deisenroth_faisal_ong2020}} (§11.3, p.361, Eqs.11.53–11.56)

**Your turn.** With $x=(0,2)$ and responsibilities $(0.75,0.25)$ for component one, find both updated weights, means and unconstrained variances.

::: {.callout-tip collapse="true" title="Answer"}
Both effective counts are one, hence both weights are $1/2$. The means are $0.5$ and $1.5$. The weighted squared residual sums are $0.75$ for each component, so both variances are $0.75$.
:::

## Assumptions and limits — Degeneracy and stopping

A freely varying normal-mixture likelihood can become unbounded: centre one component on an observation and let its variance tend to zero while another component gives positive density to the other observations. The density at the chosen observation diverges. A variance lower bound or an explicit prior changes the estimation problem and can prevent that collapse. Random starts can explore different local solutions but cannot by themselves remove a likelihood singularity.{{cite:deisenroth_faisal_ong2020}} (§11.5, p.368)

A small likelihood increment can be useful as a stopping rule, but it measures improvement in the objective rather than distance between parameters or distance to a global optimum. Components with similar distributions can exchange labels without changing the mixture density.{{cite:dempster_laird_rubin1977}} (§3, pp.7–10)
