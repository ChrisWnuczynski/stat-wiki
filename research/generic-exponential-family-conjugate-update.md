# Generic exponential-family conjugate update

Type: Theorem/proposition. Rank 61.

## Material checked

- **Checked:** Frozen baseline 2,043 body words and no figures. The inherited statement, collapsed proof, Poisson, Rayleigh and Pareto examples, infobox and eleven question links are retained. The new prose adds a motivating Poisson context, interpretation of the natural sufficient statistic, a numeric update, and hidden-answer practice.
- **Checked:** Diaconis and Ylvisaker's original *Annals of Statistics* paper, Introduction and §2, eqs. 2.1–2.3 and Theorem 1 (pp. 269–272), was read and logged for the exponential-family conjugate form in `research/exponential-family.md`. The publisher DOI page was revisited. Geyer's official University of Minnesota notes, §§2.1–2.3 and eqs. 2.3–2.5, were opened and read for the coefficient update, propriety and computation limits. His exponential-family notes §9.1 were read previously for sufficiency. Raiffa and Schlaifer's publisher description was opened in the earlier hyperparameter work for historical scope.
- **Checked by code:** Prior Gamma(3,2) with Poisson data $2,0,3,3$ gives count total $8$, posterior Gamma(11,6) and mean $11/6$. Practice data $1,0,4$ give inherited coefficients $(7,5)$, posterior Gamma(8,5), mean $8/5$. `checks/generic-exponential-family-conjugate-update.py` verifies displayed values and the two answered bank questions.
- **Assumed:** The theorem's natural-parameter prior is a density with respect to $d\eta$. The later Poisson example's prior is a density with respect to $d\theta$, so the Jacobian and resulting Gamma shape differ when changing parameter scales. Observations share one natural parameter and are conditionally independent.
- **Disputed:** Matching a kernel does not establish a proper density or tractable normalizer; the article states these limits. The original copied statement did not specify a prior measure while the Poisson example used $d\theta$. The source theorem now specifies $d\eta$ and the adjacent prose explains the distinction. The generator's collapsed proof and surrounding theorem exposition were aligned to $\eta,\nu$ and given citation locators. These edits affect dependent exponential-family, natural-exponential-family, Gamma and Poisson pages and must be checked after build.

## Sources opened and used

1. Diaconis and Ylvisaker, [*Conjugate Priors for Exponential Families*](https://doi.org/10.1214/aos/1176344611), *Annals of Statistics* **7** (1979), pp. 269–281, especially §2. Existing key `diaconis_ylvisaker1979`; the original was read previously via the institutional course copy noted in `research/exponential-family.md`.
2. Charles J. Geyer, [*Proper Conjugate Priors for Exponential Families*](https://www.stat.umn.edu/geyer/5421/notes/prior.html), §§2.1–2.3 (2025), existing key `geyer2025_conjugate`.
3. Geyer, [*Exponential Families*](https://www.stat.umn.edu/geyer/f22/5421/notes/expfam.html), §9.1, previously read, key `geyer2022_exp_family`.
4. Raiffa and Schlaifer, [*Applied Statistical Decision Theory*](https://doi.org/10.4159/harvard.9780674864383), publisher description, existing key `raiffa_schlaifer1961`.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

The generated body has 4,523 words and no figures, versus 2,043 and none at baseline. One existing collapsed proof covers coefficient addition and sequential updates. Added motivating and worked examples, a hidden practice answer, two answered bank questions, concrete failures and sourced history. The source theorem also rebuilds in the exponential-family, natural-exponential-family, Gamma and Poisson articles. The changed theorem relation rebuilds in the log-partition article. Verification: 718 articles and 557 questions built; all 67 Python tests, the page check, 447-entry offline bibliography verification, and `git diff --check` pass. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator uses the system Pandoc shim.
