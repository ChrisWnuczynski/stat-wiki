# Gradient descent — rank 170

Type: method. Baseline 586 words, zero figures. Preserve initialisation interval, 0.1 learning-rate illustration, epoch, gradient check, full/mini-batch and momentum/line-search/Hessian comparisons, XOR link and original network training context.

## Sources opened

- Goodfellow, Bengio and Courville (2016), full authorized *Deep Learning* online textbook, Ch. 4 §4.3 pp. 82–86: steepest direction, update and learning rate, line search and local critical points. Ch. 8 §§8.1.3, 8.2, 8.3.1–8.3.2 pp. 274–293: batch versus minibatch, stochastic gradients, stopping, local minima/saddles and momentum.
- Lemaréchal (2012), full publisher-hosted *Documenta Mathematica* historical article “Cauchy and the Gradient Method”, pp. 251–254: Cauchy's 1847 negative-gradient step for equation solving, its line-search variants and caveats about convergence.
- Stanford CS231n, full official *Neural Networks Part 3: Learning and Evaluation*, “Gradient Checks”: centred difference versus analytic derivative and floating-point choice.
- Bishop (2006), Microsoft Research-authorized full book URL inspected; browser tool rejected its 18 MB PDF before text, so no claim newly cites it.
- Dodge (2008) index checked; no gradient-descent entry.

## Fact ledger

- **Checked:** Negative gradient is steepest first-order descent in Euclidean norm; sufficiently small steps decrease a differentiable objective with nonzero gradient (Goodfellow Ch. 4 §4.3). Exact quadratic steps and stability interval verified in focused check.
- **Checked:** Random minibatch gradient of an average loss is unbiased conditional on current weights if sampled uniformly; one noisy step need not decrease the full loss (Goodfellow Ch. 8 §§8.1.3, 8.3.1).
- **Checked:** Cauchy described a negative-gradient iteration in 1847 motivated by solving simultaneous equations, not modern neural-network training (Lemaréchal pp. 251–254).
- **Assumed:** Differentiable objective for the direction argument, Lipschitz gradient for the stated finite-step descent inequality, and uniform minibatch sampling for unbiasedness.
- **Disputed:** The existing “a start in one basin stays in that basin under a small enough step” is too broad without geometric conditions. Momentum does not guarantee crossing a flat ridge. A stationary point may be a minimum, maximum or saddle. Random initialisation is useful for network symmetry but is not required by gradient descent as an optimization method.
