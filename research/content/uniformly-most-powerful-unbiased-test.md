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

For an unknown normal variance, studentisation yields the exact one-sample $t_{n-1}$ law. At $n=42$ its two-sided $5\%$ threshold is $t_{41,0.975}=2.01954$, compared with the one-sided threshold $t_{41,0.95}=1.68288$. Choosing a direction from the observed sign and applying the latter threshold rejects in both tails: its null size is exactly $0.10$.{{cite:siegrist2022_normals}} (§6.8, “The T Variable”)

**Your turn.** A size-$0.05$ test has power $0.03$ at one alternative and $0.80$ at another. Can it be unbiased or UMPU?

::: {.callout-tip collapse="true" title="Answer"}
It is biased because $0.03<0.05$ at an alternative, so it cannot be UMPU.
:::
