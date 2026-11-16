# Marginal model — research record

## Sources opened

- Liang and Zeger (1986), *Longitudinal data analysis using generalized linear models*, full original article, *Biometrika* 73, pp. 13–22, read in the University of Sydney university-hosted teaching archive at `https://www.maths.usyd.edu.au/u/jchan/GLM/Liang%26Zeger1986GEE.pdf`. Checked §§1–3 and §6: marginal GLM, working correlation, GEE, independent-cluster asymptotics, sandwich covariance and missingness caveat. The cited bibliography key points to the publisher DOI.
- The existing source chapter `sources/book/chapters/09-marginal-models.qmd` and generated baseline page read in full for the course's notation, schematic maternal-risk figure, burn-slope ellipse, stock definition and two linked worked answers.
- Dodge's authorized local index and text searched for “marginal model”, GEE and estimating equations. No pertinent entry was present.
- The 1988 Zeger–Liang–Albert paper's publisher abstract and an institutional PDF with unclear redistribution rights were located. Its correct baseline citation is preserved, but no new claims are attached to that paper because an unambiguously authorized full copy was not established.
- Baseline: 603 words, two figures, two worked-answer examples, no question links. Both figures and their captions, the three-part definition, infobox and examples remain in place.

## Claim ledger

- **Checked:** A marginal model targets $E(Y_{ji}\mid X_{ji})$ across the population, a mean-variance relationship, and a working within-cluster correlation; the latter need not be the true joint law (Liang–Zeger 1986 §§1,3, pp. 13–16).
- **Checked:** $U(\beta)=\sum_jD_j^TV_j^{-1}(Y_j-\mu_j)$ has expectation zero at the true mean parameter when clusters are independent and the mean is correctly specified, regardless of a fixed positive-definite working $V_j$ (Liang–Zeger §3, pp. 15–16; direct conditional expectation). This alone is not a full proof of consistency.
- **Checked:** The original paper's consistency and sandwich-covariance results are asymptotic as the number of independent subjects/clusters grows, with regularity and nuisance-parameter conditions. Changing a working correlation can change the coefficient estimate and its efficiency; a sandwich covariance estimates the resulting uncertainty rather than forcing the same answer (Liang–Zeger §§2–3, pp. 14–16).
- **Checked:** The original discussion explicitly requires missing completely at random for its broad working-correlation robustness guarantee; informative missingness can defeat a naive use of that guarantee (Liang–Zeger pp. 15–16, 20–21).
- **Checked by code:** Eight two-visit clusters, four per treatment arm, give risks $1/4$ and $3/4$, risk difference $1/2$, marginal odds ratio $9$, log odds ratio $2.1972$; treating person means as units gives descriptive SE $0.3536$ rather than the independent-observation $0.2165$. The Your turn alteration gives treated risk $5/8$, risk difference $3/8$ and odds ratio $5$.
- **Checked:** For Bernoulli margins $P(A=1)=0.2$, $P(B=1)=0.8$, $P(A=B=1)\le0.2$, so maximum covariance is $0.04$ and correlation is $0.25$; a proposed working correlation matrix must also be compatible with the margins if interpreted as a true joint law. Direct Fréchet bound; course chapter “The average, and the person”.
- **Assumed:** The eight-cluster treatment example is synthetic and for arithmetic only. Four clusters per arm are too few to justify asymptotic sandwich inference; its two SE calculations show the impact of counting independent units, not validated confidence intervals.
- **Disputed/limited:** The course source's claim that correct-mean GEE coefficients and robust standard errors “settle in the same place whatever working correlation” is too strong. Its statement that the theory requires each cluster size to grow is inconsistent with Liang–Zeger's independent-cluster asymptotics. Compatible pending shared text corrections are recorded.

## Proof debt

The article's collapsed proof establishes unbiasedness of the GEE score and the Bernoulli correlation bound. A full proof of large-sample consistency and sandwich convergence under a misspecified working correlation is logged in `research/pending/marginal-model.json` for review.
