## Lead context
Sampling distributions, posterior distributions and simulation transitions condition on different things. Writing those conditioning statements explicitly separates three normal-model calculations that can otherwise look interchangeable.{{cite:siegrist2022_normals}} (§6.8, “The T Variable”)

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
Posterior propriety here needs full column rank, $n>p$ and SSE $>0$. The frequentist Student pivot additionally uses Gaussian iid errors and independence of the coefficient estimate and residual sum of squares. A posterior statement conditions on observed $y$; a sampling statement varies $Y$ under fixed parameters. Agreement of some formulas does not identify these experiments.{{cite:siegrist2022_normals}} (§6.8, “The Sample Variance” and “The T Variable”)
