## Motivating example
A quality-control alarm has two ways to be wrong: interrupt a sound process or miss a faulty one. If missing a fault costs nine times as much as a false alarm, demanding a posterior fault probability above one half is unnecessarily strict under that loss model. The best action minimizes expected cost, even when it is not the most probable class.{{cite:elkan2001_costs}} (§1, eq. 1)

## Definition
Use rows for true classes and columns for predicted classes: $c_{gh}$ is the loss when truth is $g$ and action is $h$. Let $\tau_g(x)=P(Y=g\mid X=x)$. The conditional expected loss of action $h$ is $R(h\mid x)=\sum_g c_{gh}\tau_g(x)$. A Bayes action minimizes this finite sum. Some references transpose the loss matrix, so explicitly identifying true and predicted indices prevents reversed thresholds. The calculation is an expectation over possible truths after observing $x$.{{cite:grinstead_snell1997}} (§6.1, expected value as a probability-weighted sum)

## Properties — Deriving the binary cutoff
For correct decisions costing zero, let $C_{\mathrm{FN}}$ be the cost of predicting zero when truth is one, and $C_{\mathrm{FP}}$ the cost of predicting one when truth is zero. If $p=P(Y=1\mid x)$, predicting one costs $(1-p)C_{\mathrm{FP}}$, while predicting zero costs $pC_{\mathrm{FN}}$. Thus predict one precisely when
$$p>\frac{C_{\mathrm{FP}}}{C_{\mathrm{FP}}+C_{\mathrm{FN}}}.$$
At equality both actions have the same conditional risk. This derivation also clarifies the index convention used in the two-class comparison below.{{cite:elkan2001_costs}} (§1, decisions based on a cost matrix)

Multiplying every loss by a positive constant multiplies each action's risk and leaves its ordering unchanged. Adding an amount depending only on the true class also adds the same posterior average to every action. Neither transformation affects the minimizing decision. Changing deployment prevalence, however, can change posterior probabilities and therefore decisions even with fixed costs. Conditional probabilities connect class densities and prior probabilities through Bayes' rule.{{cite:grinstead_snell1997}} (§4.1, Bayes probabilities)

## Worked example — Accuracy can choose the wrong action
For posterior fault probability $p=0.2$, false-alarm cost 1 and missed-fault cost 9, the costs are $0.8$ for an alarm and $1.8$ for no alarm. The threshold is $1/10=0.1$, so raising the alarm minimizes expected loss. The ordinary maximum-posterior classifier would choose no fault because $0.2<0.5$. At $p=0.05$, an alarm costs $0.95$ and no alarm costs $0.45$, so the preferred action reverses. The cost values specify a hypothetical quality-control decision.{{cite:elkan2001_costs}} (§1, expected cost and cost units)

**Your turn.** With false-positive cost 4 and false-negative cost 1, find the probability threshold and preferred action at $p=0.7$.

::: {.callout-tip collapse="true" title="Answer"}
The threshold is $4/(4+1)=0.8$. At $p=0.7$, predicting one costs $0.3(4)=1.2$, while predicting zero costs $0.7(1)=0.7$, so predict zero.
:::

## Statistical use — Integrating local decisions
The total expected risk of a decision rule is the expectation over $X$ of its conditional risk. Choosing a minimizing action at each $x$ minimizes this integrated risk: the conditional excess loss relative to the Bayes action is nonnegative pointwise, so its expectation is nonnegative. This proves the global optimality of the conditional rule when the stated posterior probabilities and loss function are correct.{{cite:grinstead_snell1997}} (§6.1, conditional expectation)

## Assumptions and limits
Estimated probabilities require calibration in the deployment population. Changing a threshold cannot compensate for a badly estimated posterior or a loss matrix that omits relevant consequences. Costs may depend on $x$, such as the value of a transaction; the same conditional minimization then uses $c_{gh}(x)$. A capacity constraint on the number of alarms couples decisions across cases and requires an additional optimization problem.{{cite:elkan2001_costs}} (§1.2, costs versus benefits and example-dependent costs)
