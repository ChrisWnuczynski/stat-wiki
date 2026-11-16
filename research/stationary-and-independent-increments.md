# Stationary and independent increments

Type: Definition. Rank 262. Tier: full.

## Material checked

- **Checked:** Durrett (2019), pp. 353–354: Brownian motion has independent increments, and $B(s+t)-B(s)$ is normal with mean 0 and variance $t$. The covariance $\E B_s B_t=\min(s,t)$ is the calculation on p. 355 from those two properties.
- **Checked by code:** $e^{-1}=0.3679$ and $e^{-2}=0.1353$. The inhomogeneous window means 1, 4 and 5 add.
- **Assumed:** A homogeneous Poisson process has Poisson increments of mean $\lambda h$ and independent increments on disjoint intervals. The inhomogeneous example is the same construction with a deterministic non-constant intensity.
- **Disputed:** Grimmett and Stirzaker, Ross, and Doob are cited in the copied definition and were not reopened.

## Comparison with the first article

The pooled-variance article and this one both open with a numerical story, prove the main identity, give a hidden prompt and two checked questions, and separate a real limitation (heteroscedasticity there, a random rate here) from the definition.

## Sources opened

Durrett (2019), pp. 353–355. Key `durrett2019`.
