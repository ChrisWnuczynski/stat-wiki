# Precision matrix research notes

Type: concept. Baseline: 483 words, no figures. Preserve the inherited three-variable chain, its partial-correlation calculation, infobox, links and three original citations. Add a two-variable worked inverse, a collapsed Gaussian proof, a non-Gaussian counterexample and a measured account of sparse estimation.

## Sources opened

- Friedman, Hastie and Tibshirani (2008), “Sparse inverse covariance estimation with the graphical lasso,” *Biostatistics* 9(3):432–441, DOI 10.1093/biostatistics/kxm045. Read the full author-hosted preprint at https://arxiv.org/pdf/0708.3517, especially §1–2: Gaussian inverse-covariance graph, penalised log determinant objective and high-dimensional motivation. Existing bibliography key `friedman_glasso2008`; preprint title is “with the lasso,” publication title is “with the graphical lasso.”
- Speed and Kiiveri (1986), “Gaussian Markov Distributions over Finite Graphs,” *Annals of Statistics* 14(1):138–150, DOI 10.1214/aos/1176349846. Opened publisher/DOI search record and abstract. Checked the description of Gaussian Markov laws through inverse-covariance zeros; full paper was not newly read. Existing key `speed_kiiveri1986`.
- Dempster (1972), “Covariance Selection,” *Biometrics* 28(1):157–175, DOI 10.2307/2528966. Opened the original JSTOR DOI landing record for orientation; full article and abstract were inaccessible. New historical prose cites Evans's full account. Existing key `dempster1972_cov` is preserved in inherited material.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, “Partial Correlation,” printed pp. 412–413, `/workspace/statwiki-sources/dodge2008/pages/pdf-0410.txt` and `pdf-0411.txt`. Checked the distinction between marginal and controlled correlation and the motivating third-variable example. The Gaussian precision formula is supported by Evans's full chapter and the algebraic proof.
- Lauritzen (1996), *Graphical Models*, publisher/DOI page inspected, https://doi.org/10.1093/oso/9780198522195.001.0001; full relevant section unavailable. Inherited citation preserved, no new claim rests solely on that book.
- Robin J. Evans (2025), full Oxford author-hosted *Graphical Models* Ch. 5 at https://www.stats.ox.ac.uk/~evans/gms/_book/gauss.html, read §5.1 and Bibliographic Notes. It proves the Gaussian inverse-covariance zero condition and explicitly attributes covariance selection to Dempster (1972); new prose cites this full source for both claims.

## Fact ledger

- **Checked:** For a nonsingular Gaussian law, $K_{ij}=0$ is equivalent to conditional independence of coordinates $i,j$ given the rest, and the partial correlation is $-K_{ij}/\sqrt{K_{ii}K_{jj}}$. Friedman et al. §1; algebra in one collapsed proof.
- **Checked:** The new $\Sigma=\begin{pmatrix}4&2\\2&3\end{pmatrix}$ has determinant 8, inverse $\frac18\begin{pmatrix}3&-2\\-2&4\end{pmatrix}$, conditional variance $8/3$, regression coefficient $2/3$ and correlation $2/\sqrt{12}=0.57735$. The Your turn matrix has determinant 3, conditional variance $3/2$ and correlation $1/2$.
- **Checked:** For $Z\sim N(0,1)$, $\operatorname{Cov}(Z,Z^2)=E Z^3=0$, $\operatorname{Var}(Z^2)=2$, and the inverse covariance is diagonal although the coordinates are dependent. This is a deliberate non-Gaussian failure case, verified symbolically and numerically in `checks/precision-matrix.py`.
- **Checked:** The inherited chain matrix is positive definite, with precision $K_{13}=0$, positive marginal $\Sigma_{13}$ and partial correlation $1/2$ on adjacent pairs.
- **Assumed:** The health-measurement motivation is hypothetical. No causal claim follows from a precision edge.
- **Disputed:** Historical priority in covariance selection involves several contributors; the page names specific documented publications without claiming sole invention of all Gaussian graph methods.

## Bank selection

Answered `ex-sl-19-2` computes a different three-node precision inverse and graph. Answered `ex-sl-19-8` tests conditional association, penalised graph estimation and the limits of causal interpretation. Both extend the page's own two-variable arithmetic.
