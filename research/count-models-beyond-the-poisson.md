# Count models beyond the Poisson

Type: Concept. Rank 264. Tier: full.

## Material checked

- **Checked:** Baseline 741 words, 0 figures. Dodge printed pp. 425–426 states the Poisson probability function and derives E[X] = Var(X) = θ. The two-point mixture moments and the zero probabilities were recomputed from that identity.
- **Checked by code:** Equal mixture of Poisson rates 2 and 6 has mean 4, rate variance 4, count variance 8, P(Y=0)≈0.0689 against e^{-4}≈0.0183 (ratio about 3.76). The 3/4–1/4 mixture has mean 3 and variance 6. `checks/count-models-beyond-the-poisson.py`.
- **Assumed:** The law of total variance applies to a nonnegative random rate. A gamma mixing distribution is not required for the inequality Var(Y) > E(Y).
- **Not opened:** McCullagh and Nelder, Greenwood and Yule, Shmueli et al., and Huang. The page’s copied chapter already cites them. New sentences use Dodge and the mixture arithmetic.

## Sources opened

1. Dodge, *The Concise Encyclopedia of Statistics*, printed pp. 425–426. Key `dodge2008`.
