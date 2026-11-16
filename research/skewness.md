# Skewness

Type: Concept/topic. Rank 50.

## Material checked

- Frozen baseline: 197 body words, no figure on the article. Read its source paragraph in `sources/stat1301/chapters/da-02-descriptive-statistics.qmd` and inspected the 299-row `sources/stat1301/data/heart.csv`.
- **Checked:** NIST/SEMATECH *e-Handbook of Statistical Methods*, §1.3.5.11, gives the sample standardized third central moment, its adjusted variant, the sign interpretation, and warnings about outliers, multi-modality and transformation. NIST Dataplot Reference Manual, “Skewness”, confirms the divisor convention and several distinct coefficients.
- **Checked by code:** the source creatinine data give moment skewness 4.433610... raw, 1.576032... after the natural logarithm, and −0.008439... after reciprocation. These support the inherited rounded 4.4, 1.6 and “about zero”. The exact worked, practice and zero-skew asymmetric examples are asserted in `checks/skewness.py`.
- **Checked history:** Pearson's 1895 paper is titled *Skew Variation in Homogeneous Material* and has DOI 10.1098/rsta.1895.0010; verified against the DOI-linked Zenodo record of the original publication. The full original PDF and Royal Society DOI landing page were inaccessible, so the historical statement is limited to its subject and date.
- **Assumed:** the data file's creatinine column is measured in the unit specified by the source chapter; no external clinical interpretation is inferred.
- **Disputed:** the unqualified phrase “zero for symmetric data” lacks the requirement that the third moment and nonzero variance exist. The topic definition is narrowed accordingly.

## Sources opened and used

1. NIST/SEMATECH, [*e-Handbook of Statistical Methods*, “Measures of Skewness and Kurtosis”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm), §1.3.5.11. Opened the official page and checked the moment and adjusted formulas, sign conventions, transformation advice and heavy-tail counterexample. New key: `nist_skewness2002`.
2. National Institute of Standards and Technology, [Dataplot Reference Manual, “Skewness”](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/skewness.htm), “Description” and “Note”. Opened the official page for software conventions. New key: `nist_dataplot_skewness2023`.
3. Karl Pearson, [“Contributions to the Mathematical Theory of Evolution. II. Skew Variation in Homogeneous Material”](https://zenodo.org/records/1432104), 1895, DOI 10.1098/rsta.1895.0010. Opened the DOI-linked public-domain record; the original PDF was too large for the web reader. Existing key: `pearson1895`; used only for the narrow history statement.

## Changes and checks

- Added a numerical definition with its moment-existence condition, a collapsed proof of symmetry and affine-scale properties, two numerical examples with hidden practice, caveats and history. The inherited creatinine comparison remains and is recalculated from its data.
- Replaced three unlocated citations in the shared source paragraph with the opened, located NIST source. The Pearson citation is retained for the limited historical statement. Added an explicit shape question to the existing answered creatinine exercise, and selected the existing answered gamma-sum question whose solution interprets skewness.
- The generated article grows from 197 to 2,344 body words and from zero to one figure. The dependent Transformations of data, Normal quantile plot, Sample correlation coefficient, and Gamma distribution pages remain above their frozen word and figure baselines. The rank's one collapsed proof covers the symmetry implication and affine rule; the zero-skew and median counterexamples are calculated there. No result is left for `proofs-todo.json`.
- Verification: `checks/skewness.py` passes all displayed numerical examples and the 299-row source data; `python -m unittest discover` passes 67 tests; `python verify_citations.py --offline` verifies 439 bibliography entries; `git diff --check` passes. The source generator builds 718 articles and 557 questions. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator's Pandoc step used the local system Pandoc shim.
