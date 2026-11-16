# Minimal sufficiency

Type: Concept. Rank 241. Tier: full.

## Material checked

- **Checked:** Frozen baseline 412 body words and no figures. The page keeps the ratio criterion, the known-variance normal calculation, and the uniform-shift remark that $(\min,\max)$ is minimal sufficient while the range is ancillary.
- **Checked by code:** Poisson samples $(2,0,5)$ and $(1,3,3)$ have likelihood ratio $36/240=0.15$. Against $(4,0,0)$ the ratio is $0.1\lambda^3$, equal to $0.1$ at $\lambda=1$ and $0.8$ at $\lambda=2$. The normal samples $(1,3)$ and $(2,2)$ have ratio $e^{-1}\approx 0.3679$. The uniform sample $0.2,0.9,1.1$ has likelihood support $[0.1,0.2]$ and range $0.9$.
- **Assumed:** The Poisson observations are independent with a common rate, and the normal observations are independent with variance $1$. The uniform likelihood is $1$ on the parameter interval of length at most $1$ that covers the sample, and $0$ elsewhere.
- **Disputed:** None.
- **Not opened:** Lehmann and Scheffé (1950), Lehmann and Casella (1998), and Casella and Berger (2002) are the citations on the copied definition. They were not reopened, so the new calculations do not cite them. Dodge has no sufficiency entry.

## Sources opened and used

The new numerical arguments are direct expansions of the Poisson, normal, and uniform likelihoods. No additional bibliography key is used.
