## Motivating example

An experiment estimates a failure rate, but an engineer needs median lifetime. Once the rate likelihood has been maximised, invariance supplies the median estimate by transforming the maximiser. The principle concerns a change of parameter, rather than a transformation of the observations.{{cite:siegrist_mle2022}} (§ “Extending the Method and the Invariance Property”)

## Statement

Let $L(\theta;x)$ have a finite global maximum attained at $\widehat\theta$. For a parameter of interest $\eta=g(\theta)$, define its profile likelihood by
$$
L_g(\eta;x)=\sup_{\theta:g(\theta)=\eta}L(\theta;x).
$$
Then $g(\widehat\theta)$ maximises $L_g$. A one-to-one transformation simply relabels the parameter space. A many-to-one transformation groups parameter values and takes the best fit within each group. This definition makes the claim precise even when $g$ discards nuisance information.{{cite:siegrist_mle2022}} (§ “Extending the Method and the Invariance Property”)

The hypothesis that a maximiser is attained matters. A likelihood can have a supremum at an excluded endpoint, and a solution of its score equation can be a local maximum or a minimum. Invariance carries a global maximiser to the transformed problem; it supplies no general repair for a likelihood with no maximiser. Maximum likelihood estimates can also be nonunique or biased.{{cite:dodge2008}} (p. 334)

## Proof

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $M=L(\widehat\theta;x)$. Every value of $L$ is at most $M$, so every fibre supremum $L_g(\eta;x)$ is at most $M$. The fibre through $g(\widehat\theta)$ contains $\widehat\theta$ itself and therefore has supremum at least $M$. Its supremum equals $M$, which proves maximality. If several parameter values maximise $L$, each of their images maximises the profile likelihood.{{cite:siegrist_mle2022}} (§ “Extending the Method and the Invariance Property”)
:::
:::

## Worked example

Four exponential lifetimes are $1,2,3,4$ hours. Their sum is ten hours and their mean is $2.5$ hours. For a positive rate,
$$
\ell(\lambda)=4\log\lambda-10\lambda,
\quad \ell'(\lambda)=4/\lambda-10,
\quad \ell''(\lambda)=-4/\lambda^2<0.
$$
The global maximiser is $\widehat\lambda=0.4$ per hour. The fitted mean lifetime is $1/0.4=2.5$ hours, the fitted median is $(\log2)/0.4\approx1.73287$ hours, and fitted survival through two hours is $e^{-0.8}\approx0.44933$. Each is a different function of the same maximiser.{{cite:siegrist_mle2022}} (§ “The Gamma Distribution”, shape one; § “Extending the Method and the Invariance Property”)

For a many-to-one example, suppose a normal model with known variance has mean estimate $\widehat\mu=-2$, and the target is $\eta=\mu^2$. For $\eta>0$ its fibre contains $\pm\sqrt\eta$. Profiling compares both signs; $\widehat\eta=4$ follows even though the inverse parameterisation has two branches. It would be incorrect to restrict to the positive branch while still claiming to optimise over the full model.{{cite:siegrist_mle2022}} (§ “Extending the Method and the Invariance Property”)

**Your turn.** What is the maximum likelihood estimate of the exponential rate expressed per minute rather than per hour?

::: {.callout-tip collapse="true" title="Answer"}
It is $0.4/60=1/150$ per minute. Invariance respects the units of the transformation.
:::

## Related concepts — Maximisation and expectation

Invariance does not say $E[g(\widehat\theta)]=g(E\widehat\theta)$, and it does not preserve unbiasedness. The proof is an ordering argument about the observed likelihood, containing no averaging over repeated samples. Nor does a parameter transformation add a Jacobian to an ordinary likelihood: the probability model for the observed data is unchanged. Jacobians arise when transforming a density with respect to the variable being integrated.{{cite:siegrist_mle2022}} (§ “Extending the Method and the Invariance Property”)

## History

Maximum likelihood is associated with Ronald Fisher, who used the method in his first statistical publications in 1912. Its precursors include eighteenth-century work by Johann Heinrich Lambert and Daniel Bernoulli. The parameter-estimation principle provided a framework in which estimates of several scientifically meaningful quantities could be obtained from the same fitted model.{{cite:dodge2008}} (p. 334)
