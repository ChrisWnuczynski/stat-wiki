# Markov's inequality

Type: Concept. Rank 240. Tier: full.

## Material checked

- **Checked:** Frozen baseline 586 body words and no figures. The page keeps the indicator comparison, the job of mean $10$ with bound $1/6$, the variance-$25$ Chebyshev bound $0.01$, and the two-point equality case.
- **Checked:** Durrett, 11 January 2019 PDF, Theorem 1.6.4 (pp. 29–30). The general inequality is stated there under Chebyshev's name, with the remark that some authors call it Markov's inequality and reserve Chebyshev for $\varphi(x)=x^2$. Display (1.6.1) is $a^2\mathrm{P}(|X|\ge a)\le\mathrm{E} X^2$.
- **Checked:** Dodge, printed p. 298, states the Bienaymé–Chebyshev inequality $\mathrm{P}(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$.
- **Checked by code:** $10/60=1/6$, $25/2500=0.01$, $4/20=0.2$, $9/256$ rounds to $0.0352$, $6/15=0.4$, $6/4=1.5$, $e^{-6}$ rounds to $0.002479$, and the Poisson($\lambda=2$) tail $\mathrm{P}(X\ge 10)$ rounds to $0.000046$.
- **Assumed:** The exponential comparison uses a rate equal to $1/10$, so the mean is $10$ and the survival at $60$ is $e^{-6}$.
- **Disputed:** None. The page's name Markov follows the remark in Durrett; his theorem label is Chebyshev.

## Sources opened and used

1. Rick Durrett, *Probability: Theory and Examples*, version 5, 11 January 2019, Theorem 1.6.4, pp. 29–30. Key `durrett2019`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 298. Key `dodge2008`.
