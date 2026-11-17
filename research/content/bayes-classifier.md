## Motivating example
A screening system may find a measurement more common among diseased patients than healthy ones, but disease can still be unlikely if it is rare in the population. Classification therefore combines the frequency of each class with the distribution of measurements within that class, then asks which decision has the smaller expected cost.{{cite:james_islr2013}} (§2.2.3, pp. 37–39; §4.4, pp. 138–140)

## Intuition
The Bayes classifier is an ideal decision rule defined by the *true* joint distribution of features $X$ and class $Y$. Under equal costs for all mistakes, it chooses the most probable class after observing $X=x$. That choice is made separately at each $x$: no other rule can improve its local chance of being correct there. Averaging those local chances over the feature distribution gives its population error. Since the true conditional probabilities are ordinarily unknown, a trained classifier estimates them or approximates the boundary; it is not automatically the Bayes classifier.{{cite:james_islr2013}} (§2.2.3, pp. 37–39, eqs. 2.10–2.11)

## Definition — A decision from posterior classes
Let $\tau_g(x)=P(Y=g\mid X=x)$ for classes $g=1,\ldots,G$. With zero–one loss, the rule is $B(x)\in\arg\max_g\tau_g(x)$; ties can be broken in a specified way. If class $g$ has prior probability $\pi_g$ and feature density $f_g(x)$, then $\tau_g(x)=\pi_g f_g(x)/\sum_h\pi_h f_h(x)$ wherever the denominator is positive. Thus $B(x)$ can compare $\pi_g f_g(x)$ directly. A high class-conditional *density* alone is not a high posterior probability: the prior frequency matters too.{{cite:james_islr2013}} (§2.2.3, p. 38, eq. 2.10; §4.4, pp. 138–140)

## Properties — Why the rule is optimal
Conditional on $X=x$, predicting class $a$ incurs error probability $1-\tau_a(x)$ under zero–one loss. Choosing the largest $\tau_a(x)$ minimizes this quantity. The smallest achievable population error, the *Bayes risk*, is
$$
R^*=E\!\left[1-\max_g\tau_g(X)\right].
$$
It is positive wherever classes overlap with nonzero probability: even perfect knowledge of the joint distribution cannot reveal a random class label with certainty. For two classes, the conditional error is $\min\{\tau_1(x),1-\tau_1(x)\}$, and the decision boundary lies where the two posterior probabilities tie.{{cite:james_islr2013}} (§2.2.3, pp. 38–39, eq. 2.11)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For any measurable rule $a(x)$, its zero–one risk is $R(a)=E[P\{a(X)\ne Y\mid X\}]=E[1-\tau_{a(X)}(X)]$. Pointwise, $\tau_{a(x)}(x)\le\max_g\tau_g(x)$, so $R(a)\ge E[1-\max_g\tau_g(X)]$. Taking $a=B$ attains equality. For a general loss matrix $L(a,g)$, the same conditioning gives $R(a)=E[\sum_g L(a(X),g)\tau_g(X)]$; choosing the action with the smallest sum at each $x$ attains the minimum. In two classes, if deciding class $1$ when truth is $2$ costs $c_{12}$ and deciding class $2$ when truth is $1$ costs $c_{21}$, the risks are $c_{12}\tau_2(x)$ and $c_{21}\tau_1(x)$ respectively. This establishes the unequal-cost comparison.{{cite:james_islr2013}} (§2.2.3, pp. 37–39, zero–one rule and risk)
:::
:::

## Statistical use — From an ideal rule to a fitted one
In a generative classifier, estimate class priors $\pi_g$ and class densities $f_g$, then compare their products. Linear discriminant analysis uses a Gaussian model with shared covariance; the shared covariance gives a linear decision boundary. Logistic regression instead models the posterior class probability directly. Both can approximate the Bayes rule if their assumptions and estimates are adequate. For a different target population, the prior class frequencies may change even when each class's feature distribution does not, so a boundary fitted under the old priors may no longer be best.{{cite:james_islr2013}} (§4.4, pp. 138–141; §2.2.3, pp. 38–39)

## Worked example
At a particular measurement $x$, suppose class $A$ has prior probability $0.20$ and density $f_A(x)=0.60$, while class $B$ has prior $0.80$ and density $f_B(x)=0.10$. The unnormalised posterior weights are $0.12$ and $0.08$, so $P(A\mid x)=0.12/(0.12+0.08)=0.60$ and $P(B\mid x)=0.40$. Equal mistake costs lead to class $A$, with conditional error $0.40$. If missing $B$ costs $3$ units while predicting $B$ when $A$ is true costs $1$, the expected cost of deciding $A$ is $3(0.40)=1.20$, versus $1(0.60)=0.60$ for deciding $B$. The optimal decision changes because the loss changed, not because the posterior changed.{{cite:james_islr2013}} (§2.2.3, pp. 37–39, posterior-maximizing rule)

**Your turn.** At another $x$, the posterior probability of disease is $0.20$. A missed disease costs $8$ units and a false alarm costs $1$. Decide whether to flag disease and find the probability threshold at which the decision switches.

::: {.callout-tip collapse="true" title="Answer"}
Flagging disease has expected cost $(1-0.20)\times1=0.80$; not flagging has cost $0.20\times8=1.60$, so flag. At posterior disease probability $q$, costs tie when $1-q=8q$, or $q=1/9\approx0.1111$. Above that threshold, flagging is cheaper. The $0.50$ threshold belongs to equal costs.
:::

## Common misconceptions
“Bayes” in the rule's name does not mean the class priors must have been estimated with a Bayesian parameter prior; $\pi_g$ is the population frequency of class $g$ in the joint model. A class with the largest $f_g(x)$ need not win if it has a small $\pi_g$. The rule's optimality is relative to a specified loss: the most probable class can be the wrong action when missing one class is more costly. And a low training error does not prove a fitted classifier has reached Bayes risk; the latter concerns new observations from the target population.{{cite:james_islr2013}} (§2.2.3, pp. 37–39; §4.4, pp. 138–140)

## Assumptions and limits — When the boundary moves
Suppose a test was calibrated where disease prevalence was $1\%$ but is deployed in a clinic where it is $20\%$. Even if the test's class-conditional densities are unchanged, the posterior odds and optimal boundary change with the prior odds. If the measured features are noisy or the two class densities overlap, positive Bayes error remains unavoidable. If the target penalizes false negatives much more than false positives, the zero–one classifier no longer minimizes expected cost. Finally, estimated probabilities from a misspecified Gaussian or logistic model can put the fitted boundary on the wrong side of a region; the ideal Bayes guarantee does not transfer to plug-in estimates.{{cite:james_islr2013}} (§2.2.3, pp. 38–39; §4.4, pp. 138–141)

## Connections
[A Bayes rule in one dimension](../questions/ex-sl-08-1.qmd) works out how priors shift a Gaussian boundary. [Unequal costs](../questions/ex-sl-08-2.qmd) applies the conditional-risk calculation when errors have different consequences. [The factor of two](../questions/ex-sl-11-4.qmd) compares the irreducible Bayes error with a nearest-neighbour classifier. Each question changes a different ingredient: prior frequencies, loss or the quality of an estimated rule.{{cite:james_islr2013}} (§2.2.3, pp. 37–39; §4.4, pp. 138–141)
