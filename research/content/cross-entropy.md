## Motivating example
If rain occurs on eight of ten comparable days, a forecast assigning only a small probability to rain should be penalized more strongly than one assigning a large probability. Cross-entropy averages the negative log probability a forecast gives to outcomes under a reference distribution. It therefore evaluates the whole predicted probability distribution, not merely whether the most likely label happened to be correct. The same logarithmic score appears in classification training and, in a special self-comparison, as the entropy impurity of a tree node.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73; Ch. 5, §5.5, p. 130){{cite:stanford_cs229_trees2018}} (§3, pp. 4–6)

## Intuition
The loss for one observed class $y$ is $-\log q_y$, where $q_y$ is the model's assigned probability. Assigning $0.9$ to what happens incurs a small loss; assigning $0.01$ incurs a much larger one. Averaging these losses under a reference law $P$ gives more weight to outcomes that $P$ expects frequently. With natural logarithms, the units are *nats*; base-two logarithms give *bits*. Changing base multiplies every score by the same positive constant and does not change which forecast has the lower score.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73)

The tree-node impurity formula uses $-\sum_g\hat p_g\log\hat p_g$. There the forecast and reference proportions are the same empirical node distribution. This is Shannon entropy $H(\hat p)$, or the special case $H(\hat p,\hat p)$ of cross-entropy. In a prediction problem the two distributions need not match: $P$ describes how outcomes occur and $Q$ is the forecast being assessed. Keeping those roles distinct prevents a node's impurity from being confused with a fitted model's loss on labelled cases.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73){{cite:stanford_cs229_trees2018}} (§3, pp. 5–6)

## Definition
For categorical probability vectors $p=(p_1,\ldots,p_K)$ and $q=(q_1,\ldots,q_K)$ on the same classes, define

$$
H(P,Q)=-\sum_{k=1}^K p_k\log q_k,
$$

with $0\log q_k=0$ when $p_k=0$. If $p_k>0$ but $q_k=0$, cross-entropy is infinite: a forecast assigned zero probability to an event the reference law can produce. The entropy of $P$ itself is $H(P)=H(P,P)=-\sum_k p_k\log p_k$, using $0\log0=0$ as a limit. This defines both the general comparison and the tree-node impurity formula.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73){{cite:stanford_cs229_trees2018}} (§3, pp. 5–6)

## Interpretation
The decomposition $H(P,Q)=H(P)+D_{\mathrm{KL}}(P\|Q)$ separates unavoidable uncertainty in outcomes from the extra cost of forecasting with $Q$ rather than $P$. Because KL divergence is nonnegative, the expected log score is smallest at the true distribution when it lies among the candidate forecasts. Cross-entropy is not symmetric: exchanging the reference and forecast changes which mistakes are weighted heavily. A large score alone does not tell whether the problem was intrinsically uncertain or the forecast was inaccurate; compare it with $H(P)$ or another forecast under the same reference law.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73)

## Properties
For a one-hot target vector $y$, only its observed class $c$ has $y_c=1$, so $-\sum_k y_k\log s_k=-\log s_c$ for a predicted softmax vector $s$. Over $n$ labelled cases, their mean cross-entropy is the negative conditional log-likelihood divided by $n$, assuming the cases' conditional probabilities multiply. This is why reducing the loss fits a probabilistic classifier. If the model uses logits $z_k$ and $s_k=e^{z_k}/\sum_l e^{z_l}$, the derivative for one case is $\partial\ell/\partial z_j=s_j-y_j$. The gradient compares predicted with observed class mass.{{cite:goodfellow_bengio_courville2016}} (Ch. 5, §5.5, p. 130, likelihood and empirical cross-entropy)

For a tree split, the parent node's empirical proportions are a weighted average of the children's proportions. Entropy is concave, so the parent entropy is at least the weighted child entropy; the difference is the split's information gain. A split can change the proportions and reduce entropy even if the majority label in each child stays the same, explaining why entropy can guide a tree where training misclassification is flat.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–6, weighted child loss and entropy impurity)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For positive $q_k$ wherever $p_k>0$, subtract $H(P)$ from $H(P,Q)$ to get $D_{\mathrm{KL}}(P\|Q)=\sum_{p_k>0}p_k\log(p_k/q_k)$. The inequality $-\log t\ge1-t$ applied to $t=q_k/p_k$ gives $D_{\mathrm{KL}}\ge\sum_{p_k>0}(p_k-q_k)\ge0$. Equality requires $q_k=p_k$ on the support of $P$ and no $Q$ mass outside it, hence $Q=P$. If a relevant $q_k$ is zero, the loss is infinite. This proves both the decomposition and the minimizing forecast.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73)

For one-hot $y$, $\ell=-\sum_k y_k\log s_k=\log\sum_l e^{z_l}-\sum_k y_k z_k$ because $\sum_k y_k=1$. Differentiating gives $\partial\ell/\partial z_j=e^{z_j}/\sum_l e^{z_l}-y_j=s_j-y_j$. For a tree node, $H(p)$ is concave because each $-p_k\log p_k$ has second derivative $-1/p_k<0$ for positive $p_k$, with continuous boundary values. Jensen's inequality applied to the parent as a weighted mixture of its two children proves nonnegative information gain. A different logarithm base multiplies the entire expression by a positive constant, preserving its ordering.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–6, weighted impurity){{cite:goodfellow_bengio_courville2016}} (Ch. 5, §5.5, p. 130)
:::
:::

## Statistical use
For probabilistic classification, average $-\log q_{i,y_i}$ on held-out labelled cases as well as on training cases. The training mean is the optimization criterion; the held-out mean assesses how well probability assignments travel to new data. A model that improves accuracy by choosing the same majority labels may still assign better or worse probabilities, which cross-entropy detects. In tree growing, use the reduction in node entropy to choose a split, weighted by child sizes; later pruning and validation control the fit of the complete tree.{{cite:goodfellow_bengio_courville2016}} (Ch. 5, §5.5, p. 130){{cite:stanford_cs229_trees2018}} (§3, pp. 4–6)

## Worked example
Suppose the reference frequencies for two outcomes are $P=(0.8,0.2)$, while a model predicts $Q=(0.6,0.4)$. With natural logarithms, $H(P,Q)=-0.8\log0.6-0.2\log0.4\approx0.5919$ nats. The reference entropy is $H(P)=-0.8\log0.8-0.2\log0.2\approx0.5004$, so the excess $D_{\mathrm{KL}}(P\|Q)\approx0.0915$. If outcome one actually occurs, this case contributes $-\log0.6\approx0.5108$; outcome two contributes $-\log0.4\approx0.9163$. Reversing the roles gives $H(Q,P)\approx0.7777$, so the two cross-entropies are not interchangeable. The model predicts the more common outcome correctly, yet its assigned probabilities still carry a measurable excess expected log loss.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73)

**Your turn.** Let $P=(0.5,0.5)$ and $Q=(0.9,0.1)$. Calculate $H(P,Q)$, $H(P)$ and their difference in nats. What happens if the second entry of $Q$ is changed to zero while $P$ remains the same?

::: {.callout-tip collapse="true" title="Answer"}
$H(P,Q)=-0.5\log0.9-0.5\log0.1\approx1.2040$ nats, while $H(P)=\log2\approx0.6931$. The difference is about $0.5108$ nats. If $q_2=0$ with $p_2=0.5$, the second outcome has positive reference probability but receives a zero forecast probability, so $H(P,Q)=\infty$. Any valid revised probability vector must also set $q_1=1$.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73)
:::

## Common misconceptions
Node entropy $H(P)$ is a self-comparison, whereas general cross-entropy $H(P,Q)$ compares two laws; calling both simply "cross-entropy" can obscure which probabilities go inside the logarithm. A low classification error does not imply a low log loss: a confidently wrong probability can incur a very large penalty. Cross-entropy is not a geometric distance, since $H(P,Q)$ need not equal $H(Q,P)$ and even $H(P,P)$ is generally positive. A zero-probability forecast for a possible outcome gives infinite loss, not a harmless zero term; the $0\log0=0$ convention applies when the *reference* probability is zero.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73)

## Assumptions and limits — When log loss misleads
If recorded labels contain systematic errors, a model that assigns high probability to the true class can be heavily penalized for the wrong recorded class; the loss assesses predictions against the labels supplied. If an application only values the most likely action under a particular cost matrix, the smallest log loss need not give the best action without using those costs. Empirical cross-entropy also depends on the evaluation distribution: a classifier tested only on common classes may look good while assigning poor probabilities to a rare but consequential class. These are failures of label quality, decision objective and sampling design, respectively.{{cite:goodfellow_bengio_courville2016}} (Ch. 5, §5.5, pp. 129–131, likelihood and data distribution)

## Connections
The KL divergence measures the excess cross-entropy above the reference entropy. Maximum likelihood minimizes empirical cross-entropy for a specified probabilistic model, and a softmax output turns the observed categorical label into a negative log probability. In a classification tree, the same logarithmic form evaluated at the node's own proportions measures impurity and guides splits. These uses share a formula but ask different questions about forecasts and sample partitions.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73; Ch. 5, §5.5, p. 130){{cite:stanford_cs229_trees2018}} (§3, pp. 4–6)

## History
Shannon's information-theoretic entropy describes the average information in outcomes from one distribution. Later comparisons of a reference distribution with another coding or predictive distribution lead to cross-entropy and KL divergence, now standard tools in statistical learning. The tree-impurity usage keeps Shannon's self-entropy formula, while classifier training uses the two-distribution log score.{{cite:goodfellow_bengio_courville2016}} (Ch. 3, §3.13, pp. 71–73; Ch. 5, §5.5, p. 130){{cite:stanford_cs229_trees2018}} (§3, pp. 5–6)
