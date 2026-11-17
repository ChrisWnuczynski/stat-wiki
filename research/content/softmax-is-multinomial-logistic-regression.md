## Motivating example
A classifier with three possible labels must return a coherent probability vector rather than three unrelated scores. Softmax normalises one real score per class into positive probabilities summing to one. When those scores are affine functions of the observed predictors, the resulting family is multinomial logistic regression. Hidden layers change the feature representation supplied to this final probability model.{{cite:zhang_d2l2023}} (“Softmax Regression”, softmax operation and probabilistic interpretation)

## Statement
Include an intercept in $x$ if required and write $z_k=\beta_k^Tx$. Then
$$p_k(x)=\frac{e^{z_k}}{\sum_{h=1}^K e^{z_h}},\qquad \log\frac{p_k(x)}{p_1(x)}=(\beta_k-\beta_1)^Tx.$$
Thus the log odds relative to a reference class are linear, exactly the baseline-category multinomial logistic model. The scores themselves need not sum to zero and their exponentials need not be probabilities before normalisation. Any finite scores give strictly positive probabilities; boundary probability vectors are approached as limits of score differences.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.3, softmax units, equations 6.28–6.29)

## Proof
Dividing $p_k$ by $p_1$ cancels the shared denominator and gives $e^{z_k-z_1}$. Taking the logarithm yields the linear log-odds expression. Conversely, exponentiating baseline-category log odds and using $\sum_kp_k=1$ reconstructs the softmax formula with reference score zero. If the same vector $c$ is added to every coefficient vector, each exponential is multiplied by $e^{c^Tx}$, which cancels. Setting $\beta_1=0$ or imposing an equivalent constraint removes this shared non-identifiability.

For one-hot class indicators $y_{ik}$, the log likelihood is $\sum_{i,k}y_{ik}\log p_k(x_i)$. Its negative is cross-entropy, so minimising cross-entropy and maximising that likelihood are identical optimisation objectives. This identity concerns the probability model and loss, regardless of whether its features were recorded directly or learned by earlier network layers.{{cite:zhang_d2l2023}} (“Softmax Regression”, log-likelihood and cross-entropy)

## Intuition — Only score differences carry class information
For two classes,
$$p_1=\frac{1}{1+e^{-(z_1-z_2)}}.$$
The binary logistic model therefore depends on one score difference. With $K$ classes there are $K-1$ independent log-odds contrasts, not $K$ separately identified score levels. A coefficient interpretation should identify its reference category and feature units. Adding a common intercept to every score cannot make any category more likely.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.3, overparameterisation of softmax)

The derivative with respect to scores is $\partial p_k/\partial z_j=p_k(1\{k=j\}-p_j)$. For a realised category $g$, differentiating negative log probability gives $\partial[-\log p_g]/\partial z_j=p_j-1\{j=g\}$. The gradient compares the predicted probability vector with the observed one-hot vector. Its components sum to zero, matching the invariance to a common score shift.{{cite:zhang_d2l2023}} (“Softmax Regression”, gradients of cross-entropy)

## Worked example — Three odds with simple values
Take scores $z=(0,\log2,\log3)$. Their exponentials are $(1,2,3)$ and their sum is 6, giving probabilities $(1/6,1/3,1/2)$. If the third category occurs, the loss is $-\log(1/2)=\log2=0.693147$. The score gradient is $(1/6,1/3,-1/2)$ and sums to zero.

For a stable numerical calculation, subtract the largest score before exponentiating. Here the shifted scores are $(-\log3,\log(2/3),0)$, with exponentials $(1/3,2/3,1)$ and the same probabilities after normalisation. A common shift leaves the mathematics unchanged while avoiding excessively large exponentials in computation.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.3, numerical stabilisation)

**Your turn.** Add 1000 to each of the three scores. What happens to the probabilities and the loss for category three?

::: {.callout-tip collapse="true" title="Answer"}
They stay (1/6,1/3,1/2), and the loss stays log(2). The common score shift cancels, so a stable computation need not exponentiate 1000.
:::

## Statistical use — Linear in features does not mean linear in raw inputs
A network can produce features $h(x;\theta)$ and use scores $\beta_k^Th(x;\theta)$. Conditional on those features, the final layer is still multinomial logistic regression. If the features are learned jointly, the full model is generally nonlinear in the recorded inputs and its optimisation need not be convex in all parameters together. The equivalence of the output layer does not erase the role of the hidden representation.{{cite:goodfellow_bengio_courville2016}} (Chapter 6, pp. 164–166; §6.2.2.3)

## Common misconceptions — Normalisation alone does not establish calibration
Softmax gives a coherent probability vector, but that algebraic property does not establish agreement between reported probabilities and observed frequencies in the target population. Class imbalance, model misspecification and overfitting can all matter. Likewise, an arbitrarily selected decision threshold changes the rule used to act on probabilities, rather than changing their underlying meaning.{{cite:zhang_d2l2023}} (“Softmax Regression”, probability model and assessment)
