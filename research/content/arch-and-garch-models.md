## Motivating example
Daily returns may alternate in sign while unusually large magnitudes persist for several days. A model for the conditional mean can miss this pattern. ARCH and GARCH model the conditional variance, allowing yesterday's squared shock to change today's uncertainty even when returns themselves have little linear correlation.{{cite:engle2001_garch101}} (§ “ARCH/GARCH Models”)

## Definition — A predictable variance and a new shock
Write $r_t=\sqrt{h_t}Z_t$, where $h_t$ is determined by information available before time $t$, and the innovations have conditional mean zero and variance one. Then $\E(r_t\mid\mathcal F_{t-1})=0$ and $\operatorname{Var}(r_t\mid\mathcal F_{t-1})=h_t$. A conditional mean model may be subtracted before applying this construction to its residuals.{{cite:engle2001_garch101}} (§ “ARCH/GARCH Models”)

An ARCH(1) recursion is $h_t=\omega+\alpha r_{t-1}^2$. GARCH(1,1) adds persistence in the variance itself:
$$
h_t=\omega+\alpha r_{t-1}^2+\beta h_{t-1},\qquad
\omega>0,\quad\alpha,\beta\ge0.
$$
These sign conditions ensure positive conditional variances from positive starting values. A normal conditional distribution is a further assumption; the recursion alone specifies a conditional second moment rather than a full return distribution.{{cite:bollerslev1986}} (§2, eqs. 1–2, pp. 308–309)

## Properties — Constant unconditional variance, changing conditional variance
For a weakly stationary GARCH(1,1) solution with finite second moment, taking expectations gives $v=\omega+(\alpha+\beta)v$. Thus
$$
v=\frac{\omega}{1-\alpha-\beta},\qquad \alpha+\beta<1.
$$
The condition concerns a stationary finite-variance solution. A process initialised at a finite variance can still have finite moments at each finite time when the coefficient sum is at least one; its variance will not settle at this positive finite fixed point. Weak stationarity and the stronger distributional notion of strict stationarity are different requirements.{{cite:bollerslev1986}} (§2, Thm. 1, p. 310)

The returns form a martingale-difference sequence under the conditional-mean assumptions, so distinct returns have zero covariance when their second moments exist. Their squares can remain dependent through $h_t$. This is how conditional heteroscedasticity can coexist with a flat linear autocorrelation pattern in the returns.{{cite:bollerslev1986}} (§2, Thm. 1, p. 310)

## Worked example — Forecasting the fading effect of a shock
Let $\omega=0.02$, $\alpha=0.10$ and $\beta=0.85$. The stationary variance is $0.4$. If today's variance is $0.4$ and today's return is two, tomorrow's variance is $0.02+0.10(4)+0.85(0.4)=0.76$.

Put $m_j=\E_t(h_{t+j})$. The first forecast is known at time $t$, and for $j\ge1$ the tower property gives $m_{j+1}=\omega+(\alpha+\beta)m_j$. Subtracting $v$ and iterating proves
$$
m_j=v+(\alpha+\beta)^{j-1}(m_1-v).
$$
The tenth-day forecast is $0.626890$. The excess over $0.4$ halves after $\log(1/2)/\log(0.95)=13.5134$ forecast steps, measured from the first forecast. This describes a conditional variance forecast; a realised squared return need not decline smoothly.{{cite:engle2001_garch101}} (§ “ARCH/GARCH Models”, multistep variance forecasts)

**Your turn.** Keep $\omega=0.02$ and use $\alpha=0.10,\beta=0.80$. Find the stationary variance and the one-step forecast after return two when today's variance equals that level.

::: {.callout-tip collapse="true" title="Answer"}
The stationary variance is $0.02/(1-0.9)=0.2$. The next variance is $0.02+0.1(4)+0.8(0.2)=0.58$.
:::

## Check yourself

### Which part of a series changes? {#self-check-c-50}

[Practice question](../questions/c-50.qmd)

What do ARCH and GARCH model, and what does the GARCH term add?

::: {.callout-tip collapse="true" title="Answer"}
They model changing conditional variance. ARCH uses past squared shocks, while GARCH also uses past conditional variances, allowing a shock to affect uncertainty through a persistent recursion.
:::

### Compare a mean recursion {#self-check-depth-weak-stationarity-ar}

[Practice question](../questions/depth-weak-stationarity-ar.qmd)

For an AR(1) coefficient $0.4$ and innovation variance nine, compute its stationary variance, lag-one covariance and lag-two correlation.

::: {.callout-tip collapse="true" title="Answer"}
They are $9/(1-0.4^2)=75/7$, $(0.4)(75/7)=30/7$, and $0.4^2=0.16$. This recursion governs linear dependence in the series level; the GARCH recursion instead governs its conditional variance.
:::
