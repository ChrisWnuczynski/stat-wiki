## Motivating example
A study that observes four successes in five trials has an observed rate of $4/5$, but that fraction is unstable. Other comparable studies can inform the prior distribution of its rate. A hierarchical beta–binomial model separates two operations: learning the common distribution of rates, and updating one study's rate while that distribution is held fixed. The second operation is a conjugate beta update.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Statement
Assume $n_j$ is a nonnegative integer, $0\le y_j\le n_j$, and $\alpha,\beta>0$. The observation model is binomial conditional on its study rate. The prior is beta conditional on the shared shapes. Conditional independence across studies is an assumption about the likelihood and the priors; it follows neither from the word *hierarchical* nor from observing separate totals. The beta density is proper for every pair of positive shapes, including shapes below one.{{cite:dodge2008}} (p. 40)

## Intuition — Conditioning removes one layer of uncertainty
Write $s=\alpha+\beta$ and $m=\alpha/s$. For a study with $n_j>0$, its conditional posterior mean is
$$
E(\theta_j\mid\alpha,\beta,y)
=\frac{y_j+sm}{n_j+s}
=\frac{n_j}{n_j+s}\frac{y_j}{n_j}
 +\frac{s}{n_j+s}m.
$$
The weights are positive and sum to one. A study with few trials receives a larger weight on the common centre. This is shrinkage of a conditional mean, with the strength determined by the current $s$. Beta–binomial updating adds successes and failures to the corresponding shapes.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

The posterior variance at fixed hyperparameters is
$$
\frac{(y_j+\alpha)(n_j-y_j+\beta)}
 {(n_j+\alpha+\beta)^2(n_j+\alpha+\beta+1)}.
$$
It describes uncertainty in a single beta distribution. A marginal posterior averages such distributions over the hyperposterior. In general that mixture has additional variance, because its conditional mean changes with the hyperparameters. A simulation that plugs in a single estimated pair of shapes cannot represent that variation.{{cite:dodge2008}} (p. 40, beta moments); {{cite:gelman2006}} (§2.1, conditional conjugacy)

## Proof
The factors depending on $\theta_j$ are $\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}$ from the likelihood and $\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}$ from the prior. Adding the exponents produces the beta kernel with shapes $a_j=y_j+\alpha$ and $b_j=n_j-y_j+\beta$. These are positive. Its integral is $B(a_j,b_j)$, so division by that integral gives a probability density. Products over different $j$ have separate integration coordinates; the joint normaliser is the product of their beta functions. That proves conditional independence as well as the marginal conditional law.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”); {{cite:dodge2008}} (p. 40)

## Worked example
### Two studies at the same hyperparameter draw
Take $(\alpha,\beta)=(2,3)$. Study A observes four successes in five trials and study B observes one success in five. Their conditional posteriors are $\operatorname{Beta}(6,4)$ and $\operatorname{Beta}(3,7)$. Their means are $0.6$ and $0.3$, and their variances are $6/275\approx0.021818$ and $21/1100\approx0.019091$. The raw rates $0.8$ and $0.2$ move towards the common prior mean $0.4$. The weight on each raw rate is $1/2$.

The probability of a success in one additional trial from A, at these hyperparameters, is $0.6$: integrate its Bernoulli success probability over the beta posterior. The conditional probability of successes in one new trial from each study is $0.6(0.3)=0.18$. With hyperparameter uncertainty, compute the average product of the two conditional means, which need not equal the product of their marginal averages.

**Your turn.** A third study has no trials. What is its conditional posterior and mean?

::: {.callout-tip collapse="true" title="Answer"}
The likelihood contributes no powers. Its conditional posterior is $\operatorname{Beta}(2,3)$ and its mean is $2/5=0.4$.
:::

## Common misconceptions — Independence depends on what is fixed
Drawing all study rates independently in one Gibbs step is compatible with marginal posterior dependence. Each draw uses the same current hyperparameters, and those hyperparameters vary between iterations. Large or small shared centres move several study means together. Conditional independence describes the coordinates within a step, rather than the collection of rates after that conditioning is removed.{{cite:gelman2006}} (§2.1, conditional conjugacy)

## Key results — The conditional mean is a weighted average of two rates
With shapes $\alpha=2$ and $\beta=3$, the prior mean is $2/5=0.4$ and the prior concentration is $5$. Study A, with four successes in five trials, has conditional posterior $\operatorname{Beta}(6,4)$, mean $0.6$ and variance $6/275=0.021818$. The weight on the raw rate $0.8$ is $5/(5+5)=1/2$, and $0.5\times0.8+0.5\times0.4=0.6$. Study B, with one success in five trials, has posterior $\operatorname{Beta}(3,7)$, mean $0.3$ and variance $21/1100=0.019091$. A study with no trials contributes a flat likelihood. Its conditional posterior stays $\operatorname{Beta}(2,3)$, and its mean stays $0.4$. The variance of that beta law is $2\cdot3/(5^2\cdot6)=0.04$, larger than either updated variance because no binomial trials have been observed.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”); {{cite:dodge2008}} (p. 40, beta moments)

Keeping the prior centre at $0.4$ and raising the concentration to $20$ uses prior shapes $(8,12)$, since $8/20=0.4$ and $12/20=0.6$. Four successes in five trials then give conditional shapes $(4+8,1+12)=(12,13)$ and conditional mean $(4+8)/(5+20)=12/25=0.48$. The raw rate $0.8$ now receives weight $5/25=0.2$. The same data moved the mean from $0.4$ only to $0.48$, whereas concentration $5$ moved study A to $0.6$. Concentration is the prior's vote count in this weighted average.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Related concepts
At the fixed shapes $(2,3)$, the probability of success on one new trial from study A is the posterior mean $0.6$. One new trial from study B has success probability $0.3$. Conditional on the hyperparameters, the probability of successes on one new trial from each study is the product $0.18$, because the two rates are independent given $(\alpha,\beta)$. Averaging that product over a posterior distribution for $(\alpha,\beta)$ is not the same as multiplying the two averaged means. A Monte Carlo step that draws $\theta_A$ and $\theta_B$ independently from their full conditionals at the current hyperparameters respects the conditional independence. The stored pairs are marginally dependent once the hyperparameters change between iterations.{{cite:gelman2006}} (§2.1, conditional conjugacy){{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Generalizations — The beta kernel needs the stated likelihood
The exponent arithmetic uses a binomial likelihood and a beta prior with positive shapes. A study that reports a continuous measurement, or a count that is not a number of successes in a known number of trials, does not have this full conditional. Shapes below one remain proper: the density may be unbounded at $0$ or $1$, and the normalising constant $B(a_j,b_j)$ is still finite. The conditional variance formula continues to apply. It describes one beta distribution at fixed hyperparameters. Replacing $(\alpha,\beta)$ by a point estimate and quoting that variance as the marginal posterior variance omits the extra spread that comes from moving the conditional mean.{{cite:dodge2008}} (p. 40, beta moments); {{cite:gelman2006}} (§2.1, conditional conjugacy)
