# Newton–Raphson method

Type: concept. Rank 296. Tier: lighter.

## Facts

- **Checked by code:** For $n=4$, $y=1$, the step from $\beta=0$ lands on $-1$. At $-1$, $p=0.268941$ and the score is $-0.075766$. The next value is $-1.096339$. The root $\log(1/3)=-1.098612$. At $-1.096339$, $p=0.250426$ and the score is $-0.001706$.
- **Checked:** The Bernoulli logit Hessian equals $-np(1-p)$ and does not contain $y$ except through $p(\beta)$. A quadratic log-likelihood reaches its critical point in one Newton step.
- **Checked:** R `glm` documentation states that `glm.fit` uses iteratively reweighted least squares.
- **Assumed:** The starting value $\beta=0$ is an arbitrary interior start, not a special property of the Bernoulli model.
- **Disputed:** None. The separated-sample exercise is answered from its stated path, not from a new numerical fit.

## Sources read

1. R Core Team, `glm` documentation, `glm.fit`.
2. The logistic derivative was derived in the proof box.
