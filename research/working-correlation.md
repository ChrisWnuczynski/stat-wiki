# Working correlation — rank 134 research

## Sources read

- **Checked:** Liang and Zeger (1986), *Longitudinal data analysis using generalized linear models*, *Biometrika* 73(1), pp. 13–22. The original paper's full PDF was opened from a university course archive at `https://www.maths.usyd.edu.au/u/jchan/GLM/Liang%26Zeger1986GEE.pdf`; the publisher DOI record is `10.1093/biomet/73.1.13`. Section 3.1 eqs. 5–6 defines the working matrix and GEE. Sections 2–3 treat mean consistency and sandwich variance; §4 lists independence, exchangeable and AR(1) examples; §5 discusses efficiency. The abstract and paper distinguish marginal regression from a fully specified joint law.
- **Checked:** The publisher record for Zeger, Liang and Albert (1988), *Models for Longitudinal Data: A Generalized Estimating Equation Approach*, and the original paper's opening/abstract in a university-hosted course copy were opened. It confirms the population-average versus subject-specific contrast. The newly written page relies on the fully read 1986 paper for its mathematical claims; the 1988 baseline citation is preserved.
- **Checked:** The existing question `ex-ur-exchangeable-bound` has a worked solution establishing the four-visit lower bound; `c-40` has a worked sandwich-robustness answer. They make two substantive bank checks.

## Baseline and calculated examples

- **Checked:** Baseline has zero figures and the inherited links to generalised estimating equations, marginal model, sandwich estimator, and the three question backlinks. The old page's four source entries are retained through generator source and bibliography files.
- **Checked:** For exchangeable $m\times m$ correlation $R=(1-\rho)I+\rho11^T$, eigenvalues are $1-\rho$ ($m-1$ times) and $1+(m-1)\rho$. For $m=4,\rho=-0.5$, they are $1.5$ three times and $-0.5$ once; the positive-semidefinite lower boundary is $-1/3$.
- **Checked:** For a two-visit cluster $(1,3)$ and singleton $(5)$ with unit variance, independence yields mean $3$. At exchangeable $\rho=0.5$, the first cluster has numerator $8/3$ and weight $4/3$, the singleton numerator $5$ and weight $1$, giving $23/7\approx3.285714$.
- **Disputed:** The inherited source chapter states that the large-sample theory requires the size of each cluster to grow, and that convergence rate depends on working-correlation error. Liang and Zeger formulate the basic asymptotics as the number of independent subjects $K\to\infty$; correlation choice affects efficiency. A specific replacement is recorded in pending shared changes.
- **Assumed:** A small sample of clusters can make the empirical sandwich unstable; the page states this as a practical limitation, not an exact finite-sample theorem.

## Proof scope

The collapsed box proves the exchangeable-matrix eigenvalue bounds and derives the intercept-only weighted GEE estimator. The page does not restate the full asymptotic sandwich-consistency theorem; its conditions and proof would need a separate rigorous treatment if promoted to a theorem page.
