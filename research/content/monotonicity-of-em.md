## Motivating example
When latent labels make a likelihood difficult to optimise, EM replaces direct optimisation with an expectation step and an easier parameter step. A useful guarantee is that the observed-data log-likelihood cannot decrease under an exact EM update. The guarantee concerns the objective being fitted, rather than predictive error, distance to a global optimum or monotone motion of each parameter coordinate.{{cite:dempster_laird_rubin1977}} (§3, Theorem 1, p. 7)

## Key results — A nondecreasing Q function is sufficient
Fix the observed data $y$ and current parameter $\theta_0$. Let $q_0(z)=p_{\theta_0}(z\mid y)$ and $Q(\theta\mid\theta_0)=\mathbb E_{q_0}\log p_\theta(y,Z)$. If the required conditional expectations are finite and the conditional distributions have suitable common support, then every candidate $\theta_1$ satisfying $Q(\theta_1\mid\theta_0)\ge Q(\theta_0\mid\theta_0)$ also satisfies $\ell(\theta_1)\ge\ell(\theta_0)$. Thus an exact M step is sufficient, while a generalised EM step can improve $Q$ without fully maximising it.{{cite:dempster_laird_rubin1977}} (§3, GEM definition and Theorem 1, pp. 6–7)

## Proof
The factorisation $p_\theta(y,z)=p_\theta(y)p_\theta(z\mid y)$ gives $Q(\theta\mid\theta_0)=\ell(\theta)+\mathbb E_{q_0}\log p_\theta(Z\mid y)$. Subtracting the identity at $\theta_0$ and rearranging yields
$$\ell(\theta_1)-\ell(\theta_0)=Q(\theta_1\mid\theta_0)-Q(\theta_0\mid\theta_0)+D_{\mathrm{KL}}(q_0\Vert q_1),$$
where $q_1(z)=p_{\theta_1}(z\mid y)$. Nonnegativity of KL divergence proves the implication. For completeness, Jensen's inequality gives $\mathbb E_{q_0}\log(q_1/q_0)\le\log\mathbb E_{q_0}(q_1/q_0)\le0$, so its negative is nonnegative. Equality requires the two conditional laws to agree almost everywhere, along with zero improvement in $Q$.{{cite:dempster_laird_rubin1977}} (§3, Lemma 1, Theorem 1 and eq. 3.10, pp. 6–7)

The E step makes a likelihood lower bound tight at the current parameter, while the M step raises that bound with its conditional distribution held fixed. The next E step tightens the bound again. This is an equivalent variational interpretation of the same inequality and makes clear why updating the conditional distribution and the parameter solve different optimisation problems.{{cite:wainwright_jordan2008}} (§6.2, pp. 153–156, eqs. 6.9–6.16)

## Worked example
### One noisy binary observation
Let a latent variable satisfy $Z\sim\operatorname{Bernoulli}(\theta)$, with $\Pr(Y=1\mid Z=1)=4/5$ and $\Pr(Y=1\mid Z=0)=1/5$. Observe $Y=1$. Its likelihood is $1/5+3\theta/5$. At $\theta_0=1/2$, the E step gives $q_0=\Pr(Z=1\mid Y=1)=4/5$. Maximising the Bernoulli complete-data expectation gives $\theta_1=4/5$. The observed probability rises from $1/2$ to $17/25$, and the log-likelihood rises by $\log(34/25)\approx0.307485$.

The $Q$ improvement is $(4/5)\log(8/5)+(1/5)\log(2/5)\approx0.192745$. At the new parameter the latent success probability is $16/17$, and $D_{\mathrm{KL}}(\operatorname{Bernoulli}(4/5)\Vert\operatorname{Bernoulli}(16/17))\approx0.114740$. Their sum reproduces the observed improvement. This verifies the complete identity rather than checking only the direction of one update.

**Your turn.** What parameter follows after another exact EM update from $\theta_1=4/5$?

::: {.callout-tip collapse="true" title="Answer"}
The next E step gives $16/17$, which is also the next M-step estimate. The observed success probability becomes $1/5+(3/5)(16/17)=13/17$.
:::

## Common misconceptions — Monotone values do not imply a global solution
A monotone log-likelihood sequence converges to a finite value if it is bounded above. That statement alone does not imply convergence of the parameter sequence or global optimality of a limit. Mixture likelihoods can have several stationary points and can be unbounded when a component variance collapses onto an observation. Convergence assertions therefore need additional conditions on the parameter domain and update mapping.{{cite:wainwright_jordan2008}} (§6.2, incomplete-data likelihood and EM)

Monte Carlo approximation in an E step or an inexact numerical optimisation can also violate the exact inequality. A constrained M step preserves the argument if the current parameter is feasible and the step does not decrease $Q$ within that same feasible set. Imposing a new constraint that excludes the current fit is a different optimisation problem. A meaningful implementation diagnostic compares the observed likelihood after each iteration while also checking that the intended conditional expectation and parameter constraints were used.{{cite:dempster_laird_rubin1977}} (§3, GEM condition, pp. 6–7)

## Related concepts — The likelihood gap splits into two nonnegative pieces

The change in the observed log-likelihood equals the change in $Q$, with the conditional law of the latent variables held at the current parameter, plus the Kullback–Leibler divergence from that conditional law to the conditional law at the new parameter. The divergence is nonnegative. Any step that does not decrease $Q$ therefore cannot decrease the observed log-likelihood. Equality needs both a zero change in $Q$ and agreement of the two conditional laws. An exact M step maximises $Q$. A generalised step only has to avoid decreasing it. Both sit under the same identity. [EM algorithm](em-algorithm.qmd) is the iteration that alternates the conditional expectation with a parameter update.

The identity does not say that the parameter sequence converges, that a limit maximises the likelihood globally, or that the likelihood is bounded above. A mixture in which a component variance may collapse onto one observation is a standard unbounded likelihood: the observed log-likelihood can increase at every step and still have no finite maximiser. A numerical check that prints only the observed likelihood can miss an update that raises the likelihood while lowering $Q$, or that refreshes the conditional distribution in the middle of the parameter step. Comparing $Q$ at the new parameter with $Q$ at the old one, under a fixed conditional law, is the comparison the theorem assumes. Monte Carlo error in the expectation step can make that comparison noisy enough to leave the exact inequality.{{cite:dempster_laird_rubin1977}} (§3, Theorem 1, p. 7){{cite:dempster_laird_rubin1977}} (§3, GEM condition, pp. 6–7){{cite:wainwright_jordan2008}} (§6.2, pp. 153–156, eqs. 6.9–6.16)
