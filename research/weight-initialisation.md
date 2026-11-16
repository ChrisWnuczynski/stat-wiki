# Weight initialisation

Rank 312. Lighter tier. Concept page.

## Sources read

- Hastie, Tibshirani and Friedman, ESL, Ch. 11, §11.5.1, p. 397. Near-zero random weights; exact zeros leave symmetric units unmoved; large weights often give poor solutions.
- Glorot and Bengio, AISTATS 2010, proceedings pages 249–256. Equation (12) on p. 252 sets $\operatorname{Var}(W^i)=2/(n_i+n_{i+1})$. Equation (16) on p. 253 is the uniform draw with that variance. The logistic sigmoid is reported as poorly suited to deep stacks because its mean drives saturation.
- Siegrist §5.6 for the standard normal density used to compute $2\Phi(1)-1$.

## Checked

- Fan-in with $p=3$: $\sigma=1/2$, marginal variance $4\sigma^2=1$, and conditional variance $\sigma^2(1+3)=1$.
- $2\Phi(1)-1$ rounds to $0.6827$.
- Square layer $4$: half-width $\sqrt{6/8}\approx 0.8660$, variance $0.25$.
- Your turn: $p=8$ gives $\sigma=1/3$; Glorot variance $2/16=0.125$; half-width $\sqrt{6}/4\approx 0.6124$.
- Comparison: $100^{-1/2}=0.1$ and $\sqrt{2/104}\approx 0.1387$.
- Uniform variance identity $a^2/3$ with $a^2=6/(n_j+n_{j+1})$ gives $2/(n_j+n_{j+1})$.

## Not claimed

- The fan-in rule $\sigma=(p+1)^{-1/2}$ is the marginal-variance calculation. It is not Glorot and Bengio's normalised initialisation. The article keeps the two formulas separate.
- LeCun et al. (1998) is cited in the source chapter for fan-in scaling and was not reopened.
