# Joint probability density

Type: Concept/definition.

## Existing material read

- `articles/joint-probability-density.qmd` before the edit: the integral definition, the marginal formula, the transformation rule and its linear special case, and two worked question excerpts (a region probability, and the product density \(2e^{-x-2y}\) with \(\mathbb E(XY)=1/2\) and covariance \(3/4\)). Citations present: Laplace 1812, Kolmogorov 1933, Grimmett–Stirzaker 2020, Cramér 1946, Casella–Berger 2002, and Feller 1968. Seventeen linked questions. No figures. Leading body: 469 words under the `PROGRESS.md` count.
- `sources/stat2003/chapters/prob-04-joint-distributions.qmd`, the joint-density definition, the uniform-region and random-sample remarks, and the expectation paragraph.

## Sources opened and facts used

1. Rick Durrett, *Probability: Theory and Examples*, version of 11 January 2019 of the fifth edition, [author PDF](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf). Read the density language in §1.2 near p. 12, the independence definition for random variables in §2.1 on pp. 43–44, and Example 4.1.6 on p. 209, which defines a joint density by \(\mathbb P((X,Y)\in B)=\iint_B f\) and recovers the conditional mean from the marginal integral. Existing key `durrett2019`. Cambridge pagination was not compared with this author PDF.
2. Laplace 1812, Kolmogorov 1933, Grimmett–Stirzaker 2020, Cramér 1946, Casella–Berger 2002, and Feller 1968 remain because the existing definition and transformation rule cite them. Their full texts were not opened for this page. The new sentences use the opened Durrett text and the proofs written in the article. The origin of the phrase *joint density* was not found in the opened pages and is not asserted.

## Verification and decisions

- Added a formula-free lead, the triangle motivation, the integral definition with marginals and expectations, the product criterion, one collapsed proof, a uniform-triangle calculation, a check of the existing exponential answers, a hidden exercise, and a history limited to the opened pages.
- The proof covers normalisation, the marginal integral, both directions of the product criterion, the covariance identity \(\operatorname{Cov}(X+Y,X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)\), and the absolute Jacobian factor for an invertible linear map.
- `checks/joint-probability-density.py` checks the triangle moments, covariance \(1/36\), the exercise values \(3/4\) and \(1\), and the exponential mean, variance, and quadrant integral.
- The original definition, transformation rule, both worked answers, citation keys, infobox, and seventeen question links remain. No figure was present.

## Correction pass

- Corrected two mathematical statements: covariance cross terms cancel without independence, and a non-product support need not have nonuniform marginals. The triangle's marginals are the specific nonuniform example.
- Added precise locations to the opened Durrett source, rewrote editor-facing references, and removed an added History section that repeated definitions rather than recording history. The inherited transformation rule remains in the article; redundant added discussion of it was removed because this pass did not open a supporting transformation source.
- The arithmetic check now asserts the main values printed in the worked examples.
