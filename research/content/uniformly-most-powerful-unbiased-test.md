## Lead context
Unbiasedness restricts a test's entire power function: every alternative must be rejected at least as often as the null size. It is distinct from unbiased estimation.{{cite:draxler_kurz2026_exact}} (§3.2, definition and Cases 3–4)

## Motivating example
For $Z\sim N(\delta,1)$, a right-tail test detects positive shifts efficiently, but a negative shift makes rejection less likely than under $\delta=0$. When departures in either direction matter, that right-tail rule is biased. Restricting attention to unbiased tests makes a uniform optimality result possible.{{cite:draxler_kurz2026_exact}} (§3.2, definition and Cases 3–4)

## Properties — Why equal tails solve the normal problem
Let $\phi(Z)\in[0,1]$ be a size-$\alpha$ test. If its differentiable power is minimised at $\delta=0$, then $E_0\{Z\phi(Z)\}=0$. For $c=z_{1-\alpha/2}$, the equal-tail rule $\phi_*(z)=1\{|z|>c\}$ satisfies both this moment constraint and $E_0\phi_* =\alpha$. The analogous scalar exponential-family construction imposes a size condition and a first-moment condition.{{cite:draxler_kurz2026_exact}} (§3.2, definition and Cases 3–4)

A direct argument proves optimality. For any fixed $\delta\ne0$, draw the straight line $a z+b$ joining $e^{\delta z}$ at $z=-c$ and $c$. Strict convexity puts the exponential below this line inside $(-c,c)$ and above it outside. Therefore $(\phi_* -\phi)(e^{\delta z}-az-b)\ge0$ pointwise. Integrating against the null normal density, the constant and linear terms cancel by the two constraints. Multiplying by $e^{-\delta^2/2}$ shows $E_\delta\phi_*\ge E_\delta\phi$. Its power is symmetric in $\delta$ and its derivative for $\delta>0$ is $\varphi(c-\delta)-\varphi(c+\delta)>0$, where $\varphi$ is the standard normal density. Thus it is itself unbiased. Thus it dominates every unbiased size-$\alpha$ competitor at every alternative. This proof is specific to the normal shift problem. In a general scalar exponential family, the two critical boundaries are determined by size and first-moment conditions rather than equal numerical tail probabilities.{{cite:draxler_kurz2026_exact}} (§3.2, eqs. 10–11)

## Worked example
At $\alpha=0.05$, $c=1.95996$. Under $\delta=1$, the two-sided power is
$$
P_1(Z>c)+P_1(Z<-c)=1-\Phi(c-1)+\Phi(-c-1)=0.17008.
$$
A right-tail rule uses $z_{0.95}=1.64485$ and has power $0.25951$ at $\delta=1$, but only $0.00409$ at $\delta=-1$. Its higher power in one direction comes with failure of the unbiasedness requirement in the other.

For an unknown normal variance, studentisation yields the exact one-sample $t_{n-1}$ law. At $n=42$ its two-sided $5\%$ threshold is $t_{41,0.975}=2.01954$, compared with the one-sided threshold $t_{41,0.95}=1.68288$. Choosing a direction from the observed sign and applying the latter threshold rejects in both tails: its null size is exactly $0.10$.

**Your turn.** A size-$0.05$ test has power $0.03$ at one alternative and $0.80$ at another. Can it be unbiased or UMPU?

::: {.callout-tip collapse="true" title="Answer"}
It is biased because $0.03<0.05$ at an alternative, so it cannot be UMPU.
:::

## Intuition
Unbiasedness is a requirement on the whole power curve. A test of size $\alpha$ is unbiased when its power is at least $\alpha$ at every alternative. A one-sided normal test is excellent against shifts in its chosen direction and poor against shifts in the other direction. At a standard normal observation, the right-tail $5\%$ rule uses the threshold $1.64485$. Its power at a shift of $+1$ is about $0.260$, but its power at a shift of $-1$ is about $0.004$, below the null size. That rule is biased. Restricting the competition to unbiased tests removes it, and within the remaining class the equal-tail rule is optimal for a normal shift.{{cite:draxler_kurz2026_exact}} (§3.2, definition and Cases 3–4)

## Definition
Let $\phi(z)$ be the probability of rejecting when the observation is $z$, taking values in $[0,1]$. For $Z\sim N(\delta,1)$, the power is $\beta(\delta)=E_\delta\phi(Z)$. Size $\alpha$ means $\beta(0)=\alpha$. Unbiasedness means $\beta(\delta)\ge\alpha$ for every $\delta$. If the power is differentiable and minimized at the null, its derivative there is zero, which is the moment constraint $E_0\{Z\phi(Z)\}=0$. The equal-tail test $\phi_*(z)=1\{|z|>z_{1-\alpha/2}\}$ meets both constraints. At $\alpha=0.05$ the threshold is $1.95996$, and the power at $\delta=0.5$ is about $0.079$, above the size. The same two constraints, size and a first-moment condition, determine the critical points in a regular one-parameter exponential family. Those points need not be equal numerical tail probabilities once the family is no longer a normal shift.{{cite:draxler_kurz2026_exact}} (§3.2, eqs. 10–11)

## Statistical use
The normal-shift result is the template for two-sided tests that must detect departures of either sign. When the variance is unknown, the same symmetry is carried by the Student statistic. At $n=42$, the two-sided $5\%$ point of $t_{41}$ is $2.01954$ and the one-sided point is $1.68288$. Using the one-sided point on whichever side the sample happens to fall rejects under the null with probability $0.10$, twice the advertised level. The two-sided critical value is the one that keeps the size at $5\%$ without choosing the direction from the data. In a scalar exponential family the analogous unbiased test still has two boundaries, but they are solved from the size equation and the moment equation together. Reporting only one tail after seeing the sign is a different procedure.

## Common misconceptions
Uniform optimality among unbiased tests does not say that the two-sided rule beats every rival, including biased ones. The right-tail rule has higher power against positive shifts. It is excluded because it falls below size against negative shifts. A second confusion is to treat unbiasedness of a test as unbiasedness of an estimator. An unbiased estimator has the right expectation. An unbiased test has a power function that does not dip below its size. A third confusion is to expect equal tail areas in every two-sided problem. Equal tails solve the normal-shift moment constraint because the null density is symmetric. In an asymmetric exponential family the two critical values are generally unequal.{{cite:draxler_kurz2026_exact}} (§3.2, definition and Cases 3–4)

## Assumptions and limits
The dominance argument uses the normal likelihood ratio and a straight chord across the two critical points. Strict convexity of the exponential puts the likelihood ratio on the correct side of that chord, and the size and moment constraints cancel the intercept and slope. The argument does not extend unchanged to several parameters, to a boundary null, or to a discrete distribution whose attainable sizes jump. A randomized test may be needed to achieve size exactly $\alpha$ on a lattice. The numerical power curve for the normal shift can be checked directly: it is symmetric, it equals $\alpha$ at zero, and it increases as the shift moves away from zero.{{cite:draxler_kurz2026_exact}} (§3.2, eqs. 10–11)
