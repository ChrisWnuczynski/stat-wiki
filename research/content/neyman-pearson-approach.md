## Motivating example

A manufacturer can tolerate at most a specified false-alarm probability when deciding whether a production change increased a defect rate.{{cite:dodge2008}} (p. 250, Hypothesis Testing) Among tests respecting that constraint, it wants the greatest chance of detecting the increase. Fixing the error budget before comparing power is the organising idea of the Neyman–Pearson approach.{{cite:siegrist2022_testing}} (§9.1, “Power”)

## Definition — A constrained decision rule

A test function $\phi(x)\in[0,1]$ gives the probability of rejecting after observing $x$. An ordinary rejection region corresponds to an indicator function; values strictly between zero and one allow randomisation. For parameter $\theta$, its power is $\beta(\theta)=E_\theta\phi(X)$. A level-$\alpha$ test satisfies
$$
\sup_{\theta\in\Theta_0}\beta(\theta)\le\alpha.
$$
The supremum matters for a composite null: checking just one convenient null parameter value can leave a larger false-alarm probability elsewhere. Type II error at an alternative is $1-\beta(\theta)$.{{cite:siegrist2022_testing}} (§9.1, Basic Theory)

## Properties — The simple-hypothesis optimisation

For two specified densities $f_0,f_1$, choose rejection where $f_1/f_0$ is large, with possible boundary randomisation. If a likelihood-ratio test $\phi_*$ has null rejection probability $\alpha$, it maximises alternative rejection probability among tests with null rejection probability at most $\alpha$.{{cite:siegrist2022_lrt}} (§9.5, The Neyman-Pearson Lemma)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a threshold $c\ge0$, take $\phi_*=1$ where $f_1>cf_0$, zero where $f_1<cf_0$, and a suitable value on equality. Then $(\phi_* -\phi)(f_1-cf_0)\ge0$ pointwise. Integrating shows $E_1\phi_*-E_1\phi\ge c(E_0\phi_*-E_0\phi)\ge0$. Thus the likelihood-ratio rule has at least as much power. Where both densities vanish the test decision affects neither probability.{{cite:siegrist2022_lrt}} (§9.5, The Neyman-Pearson Lemma)
:::
:::

For a composite alternative, the most powerful test can depend on which alternative is chosen. A uniformly most powerful test must solve every one of those pointwise problems with the same rule. Such a rule need not exist. The optimisation criterion is therefore a statement about a specified model and alternative class.{{cite:siegrist2022_lrt}} (§9.5, Composite Hypotheses)

## Worked example

Let $X_1,\ldots,X_{25}$ be independent $N(\mu,1)$ observations, with null $\mu=0$ and alternative $\mu>0$. Every fixed positive alternative makes the likelihood ratio increase with $\bar X$. The level-$0.05$ rejection rule is
$$
\bar X>\frac{1.644854}{5}\approx0.328971.
$$
At $\mu=0.4$, $\bar X$ has standard deviation $0.2$, giving power
$$
1-\Phi\left(\frac{0.328971-0.4}{0.2}\right)\approx0.63876.
$$
For a negative shift the powerful rejection tail is instead the lower tail. The one-sided rule therefore has a precisely specified direction of sensitivity. The normal likelihood-ratio construction supplies the common rejection region for all positive shifts.{{cite:siegrist2022_lrt}} (§9.5, Normal Distribution)

**Your turn.** What is the power of this upper-tail rule when $\mu=0$?

::: {.callout-tip collapse="true" title="Answer"}
It is $0.05$. Power is defined at null parameter values too; there it is the false-alarm probability.
:::

