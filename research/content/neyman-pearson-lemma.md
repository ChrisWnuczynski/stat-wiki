## Lead context
The likelihood ratio ranks the observations by how much power they buy for a given probability of a false rejection.

## Motivating example
A diagnostic rule must detect a change while keeping false alarms below a specified level. Two rules can have the same false-alarm probability and very different probabilities of detecting the change. The Neyman–Pearson lemma identifies the best tradeoff when the null and alternative each specify one distribution.{{cite:boyd_vandenberghe2004}} (§7.3.5, pp. 370–372)

## Definition — Tests as rejection probabilities
Let $f_0$ and $f_1$ be densities or mass functions with respect to a common measure. A test is a measurable function $\phi(x)\in[0,1]$, interpreted as the conditional probability of rejecting after observing $x$. Its size under the simple null is $\mathbb E_0\phi$, and its power is $\mathbb E_1\phi$. Deterministic tests take only values zero and one. Allowing intermediate values supplies exact sizes in discrete problems.{{cite:boyd_vandenberghe2004}} (§7.3.1–7.3.2, pp. 364–366)

For $k\ge0$, let $\phi^*$ equal one where $f_1>kf_0$, zero where $f_1<kf_0$, and a chosen rejection probability on the equality set. If $\mathbb E_0\phi^*=\alpha$, this rule maximises $\mathbb E_1\phi$ over all tests with $\mathbb E_0\phi\le\alpha$. Points with $f_0=0<f_1$ can be rejected without spending any null probability.{{cite:siegrist2022_lrt}} (§9.5, The Neyman–Pearson Lemma) The optimal tradeoff may require randomisation between deterministic decisions.{{cite:boyd_vandenberghe2004}} (§7.3.5, Fig. 7.4 and Ex. 7.4, pp. 371–372)

## Properties — The optimality inequality
For any competing test $\phi$, the product
$$
(\phi^* -\phi)(f_1-kf_0)
$$
is nonnegative pointwise: both factors have the same sign wherever the density comparison is strict. Integrating gives
$$
\mathbb E_1\phi^*-\mathbb E_1\phi
\ge k(\mathbb E_0\phi^*-\mathbb E_0\phi)\ge0.
$$
This proves optimality, including competitors of smaller size. It also shows why unused size can matter. A conservative cutoff is level $\alpha$, but it need not be most powerful among all level-$\alpha$ tests when a randomised boundary can use more of the available size.{{cite:siegrist2022_lrt}} (§9.5, proof of the Neyman–Pearson lemma)

## Worked example
Let $X\sim\operatorname{Bin}(4,p)$ and test $p=1/2$ against $p=3/4$ at level $0.1$. The ratio is increasing in $X$. Under the null, $\Pr(X=4)=1/16$ and $\Pr(X=3)=1/4$. Reject at four, and reject at three with probability $\gamma$ chosen from
$$
\frac1{16}+\gamma\frac14=\frac1{10},\qquad\gamma=0.15.
$$
At $p=3/4$, the power is
$$
\left(\frac34\right)^4+0.15\binom43\left(\frac34\right)^3\frac14=0.3796875.
$$
Rejecting only at four gives power $0.31640625$ and size $0.0625$. The extra power comes from using the remaining null probability on the next-highest likelihood ratio. This is a direct application of the discrete detector formulation.{{cite:boyd_vandenberghe2004}} (§7.3.5, pp. 370–372)

**Your turn.** For the same two laws, take level $1/16$. Is boundary randomisation necessary, and what is the power?

::: {.callout-tip collapse="true" title="Answer"}
Reject exactly when $X=4$. Its null probability is already $1/16$, so no randomisation is needed. Its power is $(3/4)^4=81/256=0.31640625$.
:::

## Assumptions and limits — Which alternatives are being compared
The lemma concerns two specified sampling laws. It supplies neither a prior probability that either hypothesis is true nor a universal ranking under every alternative. For a composite alternative, the likelihood-ratio ordering can depend on the chosen parameter value. If the same level-$\alpha$ rejection rule wins for every alternative value, it is uniformly most powerful.{{cite:siegrist2022_testing}} (§9.1, power and uniformly most powerful tests)
