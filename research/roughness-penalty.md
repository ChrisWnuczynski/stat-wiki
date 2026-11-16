# Roughness penalty

Type: Concept/section. Rank 234. Tier: full.

## Material checked

- **Checked:** Frozen baseline 661 body words and one figure, the roughness-penalty plot. The generated page keeps the penalised exponential-family criterion, the cubic-spline description, the knot and degrees-of-freedom paragraphs, and that figure.
- **Checked:** Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, corrected 12th printing, §5.4. Equation (5.9) on p. 151 is the squared-error criterion with penalty $\lambda\int(f'')^2$. The limits $\lambda=0$ and $\lambda=\infty$ are stated there. Equations (5.11)–(5.13) on p. 152 reduce the fit to a ridge regression in a natural-spline basis. Figure 5.6 uses $\lambda\approx 0.00022$, about 12 degrees of freedom.
- **Checked by code:** The three-point slope is $0$, the residual sum of squares is $2/3$, the quadratic penalty on $[0,2]$ is $8$, the scores meet at $\lambda=1/12$, $8\times 0.1=0.8$, $\int(6x)^2=12$, and $8\pi^4$ rounds to $779.27$.
- **Assumed:** The squared-error penalty and the penalised normal log-likelihood differ by the cosmetic factor $1/2$ once $\lambda$ is rescaled. That factor is the one named in the copied normal-likelihood sentence.
- **Disputed:** None. Dodge has no roughness-penalty entry. Reinsch (1967) and Green and Silverman (1994) remain the citations already attached to the copied criterion; those books were not reopened for new page numbers, so the new prose cites the ESL pages that were read.

## Sources opened and used

1. Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning*, 2nd ed., 12th printing, §§5.4, pp. 151–152. Existing key `hastie_esl2009`. Author-posted PDF from `https://hastie.su.domains/ElemStatLearn/download.html`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), page search. No roughness entry. Not cited.
