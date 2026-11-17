## Motivating example
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

## Worked example
### Unequal weights inside the two groups
Let the error cases have weights $0.05$ and $0.15$, and the correct cases have weights $0.30$ and $0.50$. The total error is $0.2$, so $\alpha=\tfrac12\log4=\log2\approx0.693147$. Incorrect weights are multiplied by two and correct weights by one half. The unnormalised vector is $(0.10,0.30,0.15,0.25)$ and its total is $0.80$. After normalisation, the vector is $(0.125,0.375,0.1875,0.3125)$. The two incorrect cases sum to $0.5$, but their weights are still in the ratio one to three.

**Your turn.** Use only half of the usual coefficient for the same weights. What total mass is assigned to the incorrect group after normalisation?

::: {.callout-tip collapse="true" title="Answer"}
The multipliers are $\sqrt2$ and $1/\sqrt2$. The unnormalised group masses are $0.2\sqrt2$ and $0.8/\sqrt2$. Their ratio is $1:2$, so the new error is $1/3$.
:::

## Statistical use — An implementation identity and a diagnostic
After a finite binary update, summing the weights over the current learner's error set gives a direct numerical check. A result far from one half can indicate a sign error in the exponent, a mismatched prediction encoding, or a coefficient convention that has been mixed with a different update. The check applies before fitting the next learner. That next learner is evaluated under the new distribution, and its error need not equal that of the preceding learner.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1)

## Common misconceptions — Endpoint rounds need separate treatment
At error zero or one, the logarithm is not finite and the displayed update does not define finite normalised weights. An error of one half gives coefficient zero and leaves the distribution unchanged. For an error above one half the coefficient is negative; in binary classification, reversing the predictions supplies a rule below one half. These algebraic facts do not establish that arbitrary noisy data admit a uniformly good weak learner, which is an additional learning assumption.{{cite:freund_schapire1997}} (§5.1, weak-learner condition); {{cite:schapire2013_explaining_adaboost}} (§2)

## Key results — The normaliser is twice the balanced group mass
The identity $\varepsilon e^{\alpha}=\sqrt{\varepsilon(1-\varepsilon)}$ fixes the unnormalised mass of each group once $\alpha$ is the exact coefficient. Their sum is the normaliser $Z=2\sqrt{\varepsilon(1-\varepsilon)}$. For $\varepsilon=0.25$, $\alpha=\tfrac12\log3\approx0.549306$ and each unnormalised group mass is $\sqrt{0.25\times0.75}=0.433013$. Dividing either mass by $Z=0.866025$ returns one half. The same square-root expression is maximised at $\varepsilon=1/2$, where $Z=1$ and $\alpha=0$, and it shrinks toward zero as $\varepsilon$ approaches either endpoint. A numerical implementation can therefore check two quantities: the new weighted error, and the sum of the unnormalised weights against $2\sqrt{\varepsilon(1-\varepsilon)}$.{{cite:schapire2013_explaining_adaboost}} (§1, weight update in Fig. 1)

Halving the coefficient replaces $\alpha$ by $\alpha/2$ and replaces the multipliers $e^{\alpha}$ and $e^{-\alpha}$ by their square roots. The unnormalised incorrect mass becomes $\varepsilon\sqrt{(1-\varepsilon)/\varepsilon}=\sqrt{\varepsilon(1-\varepsilon)}$, while the correct mass becomes $(1-\varepsilon)\sqrt{\varepsilon/(1-\varepsilon)}=\sqrt{\varepsilon(1-\varepsilon)}\,(1-\varepsilon)/\varepsilon$. These are equal only in special cases. At $\varepsilon=0.2$ the ratio of incorrect mass to correct mass is $1:2$, and the normalised error is $1/3$, as in the half-coefficient exercise. The one-half identity is a property of one coefficient, not of every positive multiple of that coefficient.{{cite:freund_schapire1997}} (§5.1, Fig. 3)

## Related concepts — Equal group totals leave the hard cases heavy
After the worked update, the incorrect weights are $0.125$ and $0.375$. Their total is one half, and the second case still carries three times the weight of the first. The next weak learner is fitted to that distribution. A rule that repairs only the lighter incorrect case can leave most of the incorrect mass in place. The identity guarantees a balanced split between the two groups defined by the current classifier. It does not spread weight evenly inside the incorrect group, and it does not require the next classifier to achieve a small error.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1)

The exponential loss supplies a reason for this particular coefficient. For a fixed classifier with weighted error $\varepsilon$, the loss contribution of its coefficient is proportional to $(1-\varepsilon)e^{-\alpha}+\varepsilon e^{\alpha}$ when labels and predictions lie in $\{-1,+1\}$. Differentiating in $\alpha$ and setting the derivative to zero yields $(1-\varepsilon)e^{-\alpha}=\varepsilon e^{\alpha}$, which is the same balance used in the proof. The minimiser is $\alpha=\tfrac12\log((1-\varepsilon)/\varepsilon)$ provided $0<\varepsilon<1$. Using a different coefficient moves away from that one-dimensional minimum and, as the half-coefficient calculation shows, leaves the current classifier with weighted error different from one half.{{cite:freund_schapire1997}} (§5.1, AdaBoost.M1)

## Generalizations — The check is about one round of one classifier
The calculation uses nonnegative weights that already sum to one, binary labels, and predictions in the same coding. A multiclass mistake is not automatically an error of the same exponential form unless the algorithm states that reduction. Weights that have been rounded, truncated, or renormalised inside an earlier step can make the displayed $Z$ fail even when the coefficient formula is right. The diagnostic is applied to the classifier whose error defined $\alpha$, before a new classifier is trained. A later ensemble error on fresh observations is a different functional of the whole sequence of classifiers.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1); {{cite:freund_schapire1997}} (§5.1, weak-learner condition)

A large margin on the training weights is a separate summary from this one-round balance. Capacity arguments that turn a margin into a generalisation bound need a sampling model and a restriction on the classifiers, in addition to the algebraic update. The reweighted error of the current round can be exactly one half while those further ingredients are still missing.{{cite:schapire2013_explaining_adaboost}} (§2, “Direct Application of VC Theory”)
