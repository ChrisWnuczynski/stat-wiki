## Motivating example
A neural network's training loss can change very little over many iterations. That observation alone does not identify a local minimum. A gradient can be small near a saddle, a saturated activation can transmit almost no derivative, and a poorly conditioned direction can force tiny stable steps even when the full gradient is substantial. Diagnosis needs information about derivatives and parameterization as well as a plot of the loss.{{cite:goodfellow_bengio_courville2016}} (§§8.2.1–8.2.3, pp. 278–284)

A second difficulty is that different parameter vectors can describe exactly the same prediction function. Interchanging two hidden units and their associated output weights changes their labels inside the computation but not the output. This symmetry creates repeated representations of one fitted function, rather than evidence for distinct predictive explanations.{{cite:zhang_d2l2023}} (§“Numerical Stability and Initialization”, “Breaking the Symmetry”)

## Statement
For a differentiable loss $L(\theta)$, a stationary point satisfies $\nabla L(\theta)=0$. An interior local minimum must be stationary. If the Hessian is positive definite at a stationary point, that point is a strict local minimum; a Hessian with both positive and negative eigenvalues identifies a saddle. A zero Hessian eigenvalue requires further analysis because second-order curvature alone is inconclusive. These are local criteria and do not compare separated regions of a nonconvex loss.{{cite:goodfellow_bengio_courville2016}} (§4.3.1, §§8.2.2–8.2.3)

A plateau is a region in which changes in the loss, or in selected directional derivatives, are small on the scale relevant to the optimization. It need not consist of stationary points. Its practical effect therefore depends on learning-rate scale and finite numerical precision, as well as on the exact mathematical function.{{cite:goodfellow_bengio_courville2016}} (§8.2.3, pp. 282–284)

## Intuition — Equivalent units and ineffective directions
Write a one-hidden-layer scalar network as $f(x)=\sum_{j=1}^m a_jh(w_j^\top x+b_j)$. Applying the same permutation to the triples $(a_j,w_j,b_j)$ leaves the sum unchanged. If all hidden units have distinct parameter triples, up to $m!$ arrangements represent the same function. Repeated triples reduce that count. A count of parameter-space minima therefore overstates the number of different fitted functions.{{cite:goodfellow_bengio_courville2016}} (§8.2.2, pp. 280–281)

With ReLU activation, $h(cz)=ch(z)$ for $c>0$. Replacing $(w_j,b_j,a_j)$ by $(cw_j,cb_j,a_j/c)$ also leaves the function unchanged. This is a continuous rescaling symmetry. A regularization penalty that depends directly on parameter magnitudes can break it, even though the unpenalized prediction remains identical. Symmetries of a prediction function and symmetries of a penalized objective must be distinguished.{{cite:goodfellow_bengio_courville2016}} (§8.2.2, p. 281)

## Proof
For the permutation identity, substitute a permutation $\pi$ of $\{1,\ldots,m\}$ into the sum. Relabeling the finite index gives $\sum_j a_{\pi(j)}h(w_{\pi(j)}^\top x+b_{\pi(j)})=\sum_k a_kh(w_k^\top x+b_k)$. For positive ReLU rescaling, $(a_j/c)h(cw_j^\top x+cb_j)=a_jh(w_j^\top x+b_j)$ by positive homogeneity. These calculations prove the stated prediction symmetries directly.

For equal units, the gradients also agree when the objective and optimizer treat their coordinates identically. If incoming weights, hidden biases and outgoing weights begin in equal pairs, a deterministic gradient update preserves their equality by induction. Common minibatches do not break that equality: both units receive the same inputs and paired derivatives at every step. Independent random initializations supply distinct starting coordinates. Randomness that is itself identical for the paired units would not help.{{cite:zhang_d2l2023}} (§“Numerical Stability and Initialization”, “Breaking the Symmetry”)

## Worked example
### A saddle with zero gradient
Consider $L(u,v)=u^2-v^2$. Its gradient is $(2u,-2v)$, so the origin is stationary. Its Hessian is $\operatorname{diag}(2,-2)$, with one eigenvalue of each sign. Along $(u,0)$ the loss is positive for nonzero $u$; along $(0,v)$ it is negative. The origin is therefore a saddle, even though its gradient is exactly zero. With gradient descent step size $0.1$, the update is $(u,v)\mapsto(0.8u,1.2v)$. A small nonzero $v$ grows rather than returning toward the saddle. This illustrates the local curvature diagnostic.{{cite:goodfellow_bengio_courville2016}} (§8.2.3, pp. 282–284)

For a separate symmetry calculation, take $f(x)=2\operatorname{ReLU}(x)+3\operatorname{ReLU}(-x)$. Swapping the two hidden triples leaves $f(2)=4$ and $f(-2)=6$. Rescaling the first hidden weight from $1$ to $4$ and its output weight from $2$ to $1/2$ also preserves those outputs. A function can be identifiable in prediction at these inputs while its parameter representation is not unique.

**Your turn.** Starting at $(u,v)=(1,0.1)$ in the saddle example, perform one step with step size $0.1$ and evaluate the loss before and after.

::: {.callout-tip collapse="true" title="Answer"}
The next point is $(0.8,0.12)$. The loss falls from $1-0.01=0.99$ to $0.64-0.0144=0.6256$, even though the second coordinate moves away from zero.
:::

## Common misconceptions — Small gradients require interpretation
A flat direction caused by a symmetry need not degrade the fitted predictions. Conversely, a tiny loss change need not mean that the optimization has found a good function: a saturated unit may transmit a tiny derivative while the fit remains poor. The sigmoid derivative $s(z)(1-s(z))$ tends to zero as $|z|$ grows, giving a concrete mechanism for such saturation.{{cite:zhang_d2l2023}} (§“Numerical Stability and Initialization”, “Vanishing Gradients”)

Nonconvexity permits poor local minima but does not establish that they dominate the difficulty of every trained network. A useful diagnostic examines gradient size, curvature, activation ranges and sensitivity to initialization. Each observation answers a different question about the current optimization trajectory.{{cite:goodfellow_bengio_courville2016}} (§§8.2.1–8.2.3)
