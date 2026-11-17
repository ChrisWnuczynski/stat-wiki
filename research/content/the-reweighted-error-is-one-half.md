## Motivating example — Why boosting must change its attention
A classifier can make few mistakes under the weights used to fit it while performing poorly on the examples it misses. AdaBoost raises the relative weight of those missed cases. With the usual binary exponential update and the usual coefficient, the next weighting assigns equal total mass to correct and incorrect cases for that classifier. The next round must therefore find something beyond repeating the same predictions.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1)

## Statement
Let $w_i\ge0$ sum to one and let labels and predictions lie in $\{-1,+1\}$. Write $\varepsilon=\sum_{i:y_i\ne f(x_i)}w_i$ and assume $0<\varepsilon<1$. Define
$$\alpha=\frac12\log\frac{1-\varepsilon}{\varepsilon},\qquad
w_i'=\frac{w_i e^{-\alpha y_i f(x_i)}}{Z},$$
with $Z$ chosen so the new weights sum to one. The same classifier $f$ has weighted error $1/2$ under $w'$. This identity concerns its empirical weighted error. It does not state that the ensemble's error is one half, or that its error on future observations is one half.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1); {{cite:freund_schapire1997}} (§5.1, AdaBoost.M1)

## Intuition — Balancing two groups rather than every observation
All correctly classified cases are multiplied by $e^{-\alpha}$; all incorrectly classified cases are multiplied by $e^{\alpha}$. Individual weights within either group preserve their relative ratios. Only the ratio between the groups changes. Thus the procedure equalises their *total* weights, while leaving a difficult example inside the error group more influential than a low-weight example in that same group. The multiclass AdaBoost.M1 convention uses an equivalent relative multiplier for the two groups.{{cite:freund_schapire1997}} (§5.1, Fig. 3)

## Proof
Before normalisation, the incorrect group has mass $\varepsilon e^\alpha=\sqrt{\varepsilon(1-\varepsilon)}$. The correct group has mass $(1-\varepsilon)e^{-\alpha}$, which is the same square root. Hence $Z=2\sqrt{\varepsilon(1-\varepsilon)}$ and the new error is the first group's mass divided by $Z$, namely one half. This proof uses the exact logarithmic coefficient. With a smaller coefficient, the ratio generally differs from one.{{cite:schapire2013_explaining_adaboost}} (§1, weight update in Fig. 1)

## Worked example — Unequal weights inside the two groups
Let the error cases have weights $0.05$ and $0.15$, and the correct cases have weights $0.30$ and $0.50$. The total error is $0.2$, so $\alpha=\tfrac12\log4=\log2\approx0.693147$. Incorrect weights are multiplied by two and correct weights by one half. The unnormalised vector is $(0.10,0.30,0.15,0.25)$ and its total is $0.80$. After normalisation, the vector is $(0.125,0.375,0.1875,0.3125)$. The two incorrect cases sum to $0.5$, but their weights are still in the ratio one to three.

**Your turn.** Use only half of the usual coefficient for the same weights. What total mass is assigned to the incorrect group after normalisation?

::: {.callout-tip collapse="true" title="Answer"}
The multipliers are $\sqrt2$ and $1/\sqrt2$. The unnormalised group masses are $0.2\sqrt2$ and $0.8/\sqrt2$. Their ratio is $1:2$, so the new error is $1/3$.
:::

## Statistical use — An implementation identity and a diagnostic
After a finite binary update, summing the weights over the current learner's error set gives a direct numerical check. A result far from one half can indicate a sign error in the exponent, a mismatched prediction encoding, or a coefficient convention that has been mixed with a different update. The check applies before fitting the next learner. That next learner is evaluated under the new distribution, and its error need not equal that of the preceding learner.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1)

## Common misconceptions — Endpoint rounds need separate treatment
At error zero or one, the logarithm is not finite and the displayed update does not define finite normalised weights. An error of one half gives coefficient zero and leaves the distribution unchanged. For an error above one half the coefficient is negative; in binary classification, reversing the predictions supplies a rule below one half. These algebraic facts do not establish that arbitrary noisy data admit a uniformly good weak learner, which is an additional learning assumption.{{cite:freund_schapire1997}} (§5.1, weak-learner condition); {{cite:schapire2013_explaining_adaboost}} (§2)
