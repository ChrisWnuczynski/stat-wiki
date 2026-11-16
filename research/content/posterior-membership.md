## Lead context
Posterior membership is the conditional probability that a point came from one component of a mixture, computed after the point has been seen.{{cite:grinstead_snell1997}} (p. 164, conditional probability)

## Motivating example — A point between two clusters
Two clusters have prior weights $0.6$ and $0.4$. At a particular $x$ the component densities are $0.2$ and $0.8$. The second cluster is less common and more concentrated at this $x$. The unnormalised products are $0.6\times 0.2=0.12$ and $0.4\times 0.8=0.32$. The point is more probably from the second cluster, even though that cluster has the smaller weight. The memberships are $0.12/0.44=3/11\approx 0.2727$ and $0.32/0.44=8/11\approx 0.7273$.{{cite:grinstead_snell1997}} (p. 164, weighting by a conditional probability)

## Intuition
The component label is not observed. The density says how typical the point is of each component. The weight says how common the component was before the point was seen. Multiplying and normalising is Bayes' rule for a finite set of labels. The results are nonnegative and sum to one. A hard assignment would replace them by $0$ or $1$. The soft values are what a weighted update uses.{{cite:grinstead_snell1997}} (p. 164)

## Definition
For a mixture with weights $\pi_h>0$ summing to one and component densities $f_h$, the posterior membership of component $h$ at $x$ is
\[
\tau_h(x)=\frac{\pi_h f_h(x)}{\sum_{m}\pi_m f_m(x)},
\]
provided the denominator is positive. If the denominator is zero, every component density is zero at $x$ and the conditional probability of the label is not defined by this ratio.{{cite:grinstead_snell1997}} (p. 164, conditional probability when the conditioning event has positive probability)

## Interpretation
In the example the prior odds of component $1$ against component $2$ are $0.6/0.4=1.5$. The density ratio is $0.2/0.8=0.25$. The posterior odds are $1.5\times 0.25=0.375$, and $0.375/(1+0.375)=0.375/1.375=3/11$, the same membership. A large density can overturn a moderate prior weight. It does not overturn a prior weight of zero: if $\pi_2=0$ the second product is zero whenever the density is finite.{{cite:grinstead_snell1997}} (p. 164)

## Properties
The memberships sum to one by construction of the denominator. They are the weights in an update that holds them fixed while estimating a component mean. With one observation at $x=4$ and memberships $3/11$ and $8/11$, the weighted means of a one-point sample are both $4$, and the component counts are $3/11$ and $8/11$. With a second point at $0$ that has membership $1$ on component $1$, the updated component-$1$ mean is
\[
\frac{(3/11)\cdot 4+1\cdot 0}{3/11+1}=\frac{12/11}{14/11}=\frac{12}{14}=\frac{6}{7}\approx 0.8571.
\]
Component $2$ still has only the point at $4$, so its mean stays $4$. Recomputing the memberships from these means is a new conditional probability, not a part of this weighted average.{{cite:grinstead_snell1997}} (p. 164)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $H$ be the component label and $X$ the observation. Then $\Pr(H=h)=\pi_h$ and the conditional density of $X$ given $H=h$ is $f_h$. The joint probability element for $(H=h, X\in dx)$ is $\pi_h f_h(x)\,dx$. Dividing by the marginal element $\sum_m\pi_m f_m(x)\,dx$, when that sum is positive, gives $\tau_h(x)$. The terms sum to one over $h$. Posterior odds equal prior odds times the density ratio because the marginal density cancels:
\[
\frac{\tau_1}{\tau_2}=\frac{\pi_1 f_1}{\pi_2 f_2}.
\]
In the example that ratio is $0.12/0.32=0.375$.{{cite:grinstead_snell1997}} (p. 164, conditional probability)
:::
:::

## Statistical use — Hold the memberships fixed, then refresh them
A weighted mean uses the current memberships as weights and does not differentiate through them. The one-point update above treats $3/11$ and $8/11$ as fixed numbers. After the means move, the densities at the data change, and the memberships are recomputed. Mixing those two stages, by letting the weight depend on the mean inside the same derivative, is a different algorithm. If a component density becomes arbitrarily peaked at a single point, that point's membership on the component tends to one and the other points' memberships on it tend to zero. That is a numerical failure of an unconstrained Gaussian component, visible in the same ratio.{{cite:grinstead_snell1997}} (p. 164)

## Worked example
Weights $0.6$ and $0.4$, densities $0.2$ and $0.8$. Products $0.12$ and $0.32$. Memberships $3/11\approx 0.2727$ and $8/11\approx 0.7273$. Posterior odds $0.375$.

Now two points, $x=4$ with those memberships and $x=0$ with membership $1$ on component $1$. Component counts are $3/11+1=14/11$ and $8/11$. The component-$1$ mean is $6/7\approx 0.8571$. The component-$2$ mean is $4$. The weight $\pi$ update, if it were the normalised counts, would be $(14/11)/2=7/11\approx 0.6364$ for component $1$, because the two points together have total membership $2$.{{cite:grinstead_snell1997}} (p. 164)

**Your turn.** Keep the weights $0.6$ and $0.4$. Suppose the densities at a new point are equal, both $0.5$. What are the memberships?

::: {.callout-tip collapse="true" title="Answer"}
The products are $0.3$ and $0.2$. The memberships are $0.3/0.5=0.6$ and $0.2/0.5=0.4$, the prior weights. Equal densities do not move the weights.{{cite:grinstead_snell1997}} (p. 164)
:::

## Common misconceptions
The membership is not the prior weight. Here the prior weight $0.6$ became $3/11\approx 0.2727$ because the density ratio was $1/4$.{{cite:grinstead_snell1997}} (p. 164)

The membership is not a hard label. A point with $\tau_1=3/11$ contributes $3/11$ of a count to component $1$, not a full count and not zero.{{cite:grinstead_snell1997}} (p. 164)

A zero denominator is not a membership of $1/2$. If both densities vanish, the ratio does not define a conditional probability. The formula requires a positive marginal density.{{cite:grinstead_snell1997}} (p. 164, positive conditioning probability)

## Assumptions and limits — When the component densities are the wrong ones
The calculation treats $\pi_h$ and $f_h$ as the current numerical inputs. If those densities are not the densities that generated the point, $\tau_h$ is the conditional probability in the wrong mixture. Equal covariance Gaussian components that differ only by a mean will assign memberships that a heavy-tailed component would not. And a prior weight estimated from a sample that fixed the number of points per component is not the population weight; the formula will still multiply whatever weight it is given.{{cite:grinstead_snell1997}} (p. 164)

## Connections
[Bayes' rule](bayes-rule.qmd) is the same ratio for a finite label. A [finite mixture](finite-mixture-model.qmd) is the joint distribution of the label and the observation. The weighted mean that holds $\tau_h$ fixed is one step of an alternating fit; refreshing $\tau_h$ is the conditional probability at the new parameters.{{cite:grinstead_snell1997}} (p. 164)

## Check yourself

1. In the example, what is $\tau_1+\tau_2$?

::: {.callout-tip collapse="true" title="Answer"}
$1$. The memberships are $3/11$ and $8/11$.{{cite:grinstead_snell1997}} (p. 164)
:::

2. If the densities are equal, do the memberships equal the prior weights?

::: {.callout-tip collapse="true" title="Answer"}
Yes. The density ratio is $1$, so the posterior odds equal the prior odds, and the memberships are $0.6$ and $0.4$ in the practice problem.{{cite:grinstead_snell1997}} (p. 164)
:::

3. With points at $4$ and $0$ as in the worked update, what is the component-$2$ mean?

::: {.callout-tip collapse="true" title="Answer"}
$4$. Only the first point has positive membership on component $2$, and that point sits at $4$.{{cite:grinstead_snell1997}} (p. 164)
:::

## History
Conditional probability is the ratio of a joint probability to a marginal probability when the marginal is positive. Mixture membership is that ratio for a latent component label. The numerical products $0.12$ and $0.32$ are a finite case: two labels, two densities, one observation. The same ratio is what a later weighted update treats as a fixed weight.{{cite:grinstead_snell1997}} (p. 164, conditional probability)
