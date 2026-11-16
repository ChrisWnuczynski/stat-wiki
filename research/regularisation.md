# Regularisation

Type: Concept/topic. Rank 36.

## Material checked

- Before this edit, the generated article had 587 body words in the frozen baseline, no figures, a short definition, excerpts on high-dimensional regression, neural-network weight decay and normal-prior MAP estimation, and eleven distinct question links.
- The source passages in `sl-18-high-dimensional.qmd`, `sl-16-networks-in-practice.qmd` and `bayes-09-linear-regression.qmd`; the ridge, lasso, weight-decay and MAP pages; and the existing question links.

## Sources opened and used

1. Arthur E. Hoerl and Robert W. Kennard, [“Ridge Regression: Biased Estimation for Nonorthogonal Problems”](https://homepages.math.uic.edu/~lreyzin/papers/ridge.pdf), *Technometrics* **12** (1970), pp. 55–67. Read the Introduction and §§1–3, pp. 55–60, including the ridge normal equations and spectral argument. Existing key `hoerl_kennard1970`.
2. Robert Tibshirani, [“Regression Shrinkage and Selection via the Lasso”](https://www2.stat.duke.edu/courses/Spring06/sta395/tibshirani.pdf), *JRSS B* **58** (1996), pp. 267–288. Read the Summary, §§1–2.2, 4, 5 and 7.1, including soft thresholding, cross-validation and the Laplace-prior MAP account. Existing key `tibshirani1996`.
3. Christian H. Reinsch, [“Smoothing by Spline Functions”](https://tlakoba.w3.uvm.edu/AppliedUGMath/auxpaper_Reinsch_1967.pdf), *Numerische Mathematik* **10** (1967), pp. 177–183. Read §§1–3, pp. 177–179. Existing key `reinsch1967`.
4. Anders Krogh and John A. Hertz, [“A Simple Weight Decay Can Improve Generalization”](https://proceedings.neurips.cc/paper/1991/file/8eefcfdf5990e441f0fb6f3fad709e21-Paper.pdf), *Advances in Neural Information Processing Systems* **4** (1992), pp. 950–957. Read the Abstract, §1, eqs. 1–2, and the conclusion. Existing key `krogh_hertz1992`.
5. Ilya Loshchilov and Frank Hutter, [“Decoupled Weight Decay Regularization”](https://openreview.net/pdf?id=Bkg6RiCqY7), *ICLR* (2019). Read the Abstract and §2, including Proposition 1 and eq. 1. New key `loshchilov_hutter2019`.
6. Gavin C. Cawley and Nicola L. C. Talbot, [“On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation”](https://www.jmlr.org/papers/volume11/cawley10a/cawley10a.pdf), *JMLR* **11** (2010), pp. 2079–2107. §5.3, p. 2102, was opened in the cross-validation pass and supports the held-out assessment advice. Existing key `cawley_talbot2010`.

## Changes and checks

- Added a specific lead, motivating comparison, precise penalised-least-squares definition, interpretation, solution properties, statistical use, worked numbers, limitations, relationships and two History paragraphs. The definition distinguishes ridge, lasso, spline roughness and weight decay; every newly stated symbol is explained. Each new factual paragraph has located citations to opened sources.
- One collapsed Proof box derives ridge uniqueness, lasso fitted-value uniqueness, orthonormal soft thresholding, the normal and Laplace MAP correspondences, and the ordinary versus adaptive weight-decay distinction. No result on this page was added to `proofs-todo.json`.
- Replaced the copied high-dimensional chapter overview with a specific ridge/lasso comparison and corrected its source pointer. Rewrote the copied weight-decay paragraph and the normal-prior paragraph, supplying the likelihood and variance definitions. Those rewrites remove editor-facing wording and unlocated citations to unopened books; the definitions, prior-mode formula and eleven question links remain.
- `checks/regularisation.py` asserts the actual printed $X=I_2$, $y=(3,0.5)^T$, ridge $(1.5,0.25)^T$ and lasso $(2,0)^T$ values, source keys, locations, one proof box and all eleven question links.

## Verification

Generated article: 2,433 body words versus 587 before; zero figures versus zero before; eleven distinct question links; one collapsed Proof box. The generator produced 718 articles and 557 question pages. All 36 page checks, 67 Python tests and offline validation of 421 bibliography entries pass. `git diff --check` is clean. The temporary Quarto-to-Pandoc shim handled the generator's `quarto pandoc` call; a full rendered HTML build was not run.
