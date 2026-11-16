# Cramér–Rao lower bound

Type: Concept. Rank 282. Tier: lighter.

## Facts

- **Checked:** The scalar bound is the Cauchy–Schwarz argument on the score, under differentiation under the integral and a support free of \(\theta\). Equality holds when the score is linear in \(T-g(\theta)\).
- **Checked by code:** Bernoulli information \(n/\{\theta(1-\theta)\}\) gives bound \(0.009375\) at \(\theta=1/4\), \(n=20\), and \(0.025\) at \(\theta=1/2\), \(n=10\). One Bernoulli score has variance \(1/\{\theta(1-\theta)\}\). One Poisson score \(X/\lambda-1\) has variance \(1/\lambda\).
- **Assumed:** A scalar parameter and a density or mass function whose support does not depend on \(\theta\).
- **Disputed:** Nothing numerical. Cramér (1946) and Rao (1945) were not opened, so the article does not attribute a page in those works. The uniform\((0,\theta)\) model is excluded because the support depends on \(\theta\); the order of its maximum's variance was not re-derived here.

## Sources opened

The inequality is proved from Cauchy–Schwarz. Dodge's entry for Harald Cramér (printed p. 140) is biographical and does not state the bound.

## Proofs

The scalar regular bound and the Bernoulli and Poisson information calculations are proved. A multiparameter bound is not.
