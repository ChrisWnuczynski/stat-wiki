# Research items to verify

Add uncertain claims here before writing them into an article.

- `questions/ex-inf-no-uniform-risk.qmd`: the stated universal “No uniform winner” claim needs a sampling-model condition. Distinct parameter values can have mutually singular laws (for example, a deterministic observation $X=\theta$), allowing a rule with zero risk at both. Repair the exercise and answer when question pages are in scope; keep its existing link in the estimator article.
- `median` history: the origin and early use of the term were not established from an opened original source. The article cites the opened 1990 absolute-deviation proof for its property, but leaves a History section out pending a checked account of the median's earlier development.
- baseline-category-logit-model: a textbook page for the model, beyond the nnet manual's baseline coding, was not opened.
- fisher-scoring: the 1972 Nelder–Wedderburn paper was not opened, so the history stays with the R manual's description of IWLS.
- simple-linear-regression: the t_{n-2} slope pivot is already in the source chapter via Fox; it was not re-derived here because that book was not opened.
- hotelling-s-t2-test: unproved result kept out of proofs-todo.json (Wishart null distribution of Hotelling's T squared). The added proof shows the one-dimensional reduction and the numerical F transform. It does not derive the normal-sample Wishart calibration.
- undirected-graph: unproved result kept out of proofs-todo.json (Hammersley–Clifford equivalence). The page proves the Gaussian path factorisation for one precision matrix. The general equivalence between a positive density's clique factorisation and its pairwise Markov property was not derived.
- Compared with probability-space (2,913 words) after this eighth article; added the Poisson tail so the numerical contrast matches the care of the first page.
- cauchy-schwarz-inequality: copied Grinstead, Pearson, Student and Casella–Berger citations were not reopened for new locators.
- designed-experiment: nist_doe_intro2002 is registered. The article still cites Dodge only; a §5.1.1 citation was not inserted.
- detailed-balance: copied citations of Kelly, Norris and Grimmett–Stirzaker have no new page locators.
- galton-watson-process: copied citations of Feller, Grimmett–Stirzaker and Ross have no new page locators.
- inverse-gaussian-distribution: open Tweedie (1957) before adding a history of the hitting-time representation. A Check yourself heading needs a self-checks entry because the distribution template rejects that research section.
- marginal-and-conditional-effects: reopen Liang and Zeger (1986) before adding a page-located citation for the generalised estimating equation.
- pearson-residual: copied citations of McCullagh–Nelder, Davison and Dunn–Smyth have no new page locators.
- pooled-variance: copied chapter citations fisher1925_smrw, casella_berger2002, and wasserman2004 still have no page locator; the books were not reopened for this pass.
- posterior-hypothesis-probability: copied citations of Gelman, Jeffreys and Kass–Raftery have no page locators in the new sense; they were not reopened.
- significance-level: the copied chapter citations of Neyman–Pearson, Lehmann–Romano and Casella–Berger have no page locators.
- stationary-and-independent-increments: copied citations of Grimmett–Stirzaker, Ross and Doob have no new page locators.
- cauchy-distribution#sample-means: unproved result kept out of proofs-todo.json (Cauchy sample averages do not settle). The article says repeated averages need not settle because the mean is undefined. The catalogue proves the mean is undefined; the strong-law implication is not proved separately.
- cubic-smoothing-spline#natural-cubic-minimiser: unproved result kept out of proofs-todo.json (The penalised residual sum of squares is minimised by a natural cubic spline). ESL states that the minimiser is a natural cubic spline with knots at the distinct inputs. The article proves only the infinite-penalty limit, the least-squares line.
- partial-correlation#gaussian-precision-block: unproved result kept out of proofs-todo.json (Conditional covariance is the inverse precision block). The article uses the Gaussian identity that the conditional covariance of two coordinates is the inverse of their precision block, then simplifies the correlation. The identity is not derived from the normal density here.
- ancillary-statistic#basu: unproved result kept out of proofs-todo.json (Basu independence). The article proves ancillarity of the centred vector for a location parameter. It does not prove independence from a complete sufficient statistic.
- benjamini-hochberg#fdr-bound: unproved result kept out of proofs-todo.json (False-discovery-rate bound). ESL states FDR at most (M0/M) alpha under independence and says the proof is complicated. The article does not prove that bound.
- chapman-kolmogorov-equations#convergence: unproved result kept out of proofs-todo.json (Convergence of transition powers). The article proves P^{m+n}=P^m P^n. It does not prove convergence of P^n.
- cramer-rao-lower-bound#multiparameter: unproved result kept out of proofs-todo.json (Multiparameter Cramér–Rao bound). The article proves the scalar inequality. A matrix bound for a vector parameter is not proved.
- fisher-neyman-factorisation#dominated-converse: unproved result kept out of proofs-todo.json (Dominated-family converse). The article proves the discrete direction. The converse on a general dominated space is not proved.
- principal-component-directions-and-scores#successive-directions: unproved result kept out of proofs-todo.json (Successive orthogonal directions). The article proves the one-direction score identity. It does not prove by induction that later directions are the remaining eigenvectors.
- soft-margin-primal#kkt-characterisation: unproved result kept out of proofs-todo.json (KKT characterisation of the soft-margin solution). The article proves the smallest feasible slack for a fixed plane. It does not prove the KKT characterisation of the minimiser.
- tukey-intervals#studentised-range-density: unproved result kept out of proofs-todo.json (Density of the studentised range). The article proves that coverage is the event R at most Q. It does not derive the density of the studentised range.
- uniformly-minimum-variance-unbiased-estimator#lehmann-scheffe-uniqueness: unproved result kept out of proofs-todo.json (Uniqueness under completeness). The article proves unbiasedness of the Poisson conditional probability. It does not prove that completeness makes that function the unique unbiased function of the sum.
- wald-test#asymptotic-null: unproved result kept out of proofs-todo.json (Asymptotic standard-normal null distribution). ESL states the normal limit of the logistic estimator. The article computes normal tail probabilities and does not prove that limit.
