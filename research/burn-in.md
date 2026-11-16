# Burn-in: research notes

## Sources opened

- **Checked:** C. J. Geyer, “Practical Markov Chain Monte Carlo” (1992), original *Statistical Science* article, §3.7, printed p. 480, via the Duke-hosted journal PDF. Defines burn-in or warm-up as the initial part thrown away because equilibrium may not yet have been reached. Its 1–2% discussion is conditional on a sufficiently long, well-mixing run; it is not a universal prescription. §3.6 distinguishes spacing (thinning) from warm-up.
- **Checked:** A. Gelman and D. B. Rubin, “Inference from Iterative Simulation Using Multiple Sequences” (1992), original *Statistical Science* article, §§1.2–1.3, printed pp. 458–459, via the Duke-hosted journal PDF and author-hosted PDF. One sequence can seem settled while staying in a restricted region; dispersed starts and multiple sequences offer a diagnostic comparison. The paper does not claim a finite diagnostic proves convergence.
- **Checked:** Stan Reference Manual 2.40, “MCMC Sampling,” “Automatic parameter tuning” and “Warmup times and estimating the metric,” official documentation. Warmup estimates step size and mass matrix, so the initial phase also tunes an adaptive sampler. Documentation read 2026-11-16.
- **Checked for history and orientation only:** Dodge, *The Concise Encyclopedia of Statistics*, “Monte Carlo Method,” printed pp. 359–360. It traces the name and broad simulation method, but has no separate burn-in discussion. Cite it for that history, not for warm-up practice.
- **Checked:** inherited `sources/book/chapters/bayes-04-mcmc.qmd`, section “Warm-up is not a convergence proof,” to preserve the existing distinction among initialisation, convergence assessment, and serial dependence. The generated page also pulls an iid-pairs sentence from `sources/book/chapters/bayes-09-linear-regression.qmd` p. 556, where it describes direct posterior factorisation; the new Definition paragraph supplies that missing context.

## Mathematical checks

- **Checked:** For row-stochastic $P=((.9,.1),(.2,.8))$, the stationary law is $(2/3,1/3)$ and the non-unit eigenvalue is $0.7$. If $X_0=A$, $\Pr(X_t=B)=(1-0.7^t)/3$. At $t=5$ this is $0.27731$ with total-variation distance $0.0560233333$ from stationarity; at $t=10$ it is $0.3239174917$ with distance $0.0094158416$.
- **Checked:** If $X_0=B$, $\Pr(X_t=B)=1/3+(2/3)0.7^t$; at $t=5$ this is $0.44538$ and the distance is $0.1120466667$. These are exact finite-state calculations, not a general way to choose burn-in.
- **Checked:** The transition recursion is $p_{t+1}=0.1+0.7p_t$; subtracting its fixed point $1/3$ proves exponential decay for this chain.

## Scope decisions

- **Assumed:** The two-state chain is hypothetical, used to expose starting-state bias explicitly.
- **Disputed:** No fixed burn-in percentage or visual trace-plot criterion guarantees equilibrium for arbitrary MCMC. Exclude such a claim.
- **Disputed:** Treating retained draws as independent after burn-in is false for this chain; retain a separate discussion of autocorrelation and Monte Carlo error.
