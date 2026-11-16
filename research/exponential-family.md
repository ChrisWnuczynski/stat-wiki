# Exponential family

Type: Concept/definition. Rank 35.

## Material checked

- Before this edit, the generated article had 2,993 body words, no figures, the five-function GLM definition, normal, Poisson and binomial derivations, four linked properties, the Gamma-regression exercise, the short concept answer, and seven distinct question links (six in the further-reading list plus the worked Gamma question).
- The source passages in `01-introduction-to-glms.qmd`, `bayes-07-exponential-families.qmd`, and the practice answers; the normal, Poisson, binomial, GLM, natural-parameter and conjugacy pages; the old depth baselines and citation keys.

## Sources opened and used

1. J. A. Nelder and R. W. M. Wedderburn, [“Generalized Linear Models”](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), *JRSS A* **135** (1972), pp. 370–384. Read the Summary, Introduction, §§1.1–2.4 (pp. 370–376), and §§3.1–3.4 (pp. 376–381). Key `nelder_wedderburn1972`.
2. Persi Diaconis and Donald Ylvisaker, [“Conjugate Priors for Exponential Families”](https://www.cs.columbia.edu/~blei/fogm/2020F/readings/DiaconisYlvisaker1979.pdf), *Annals of Statistics* **7** (1979), pp. 269–281. Read the Introduction and §2, including eqs. 2.1–2.3 and Theorem 1 (pp. 269–272). Existing key `diaconis_ylvisaker1979`.
3. Charles J. Geyer, [“Exponential Families”](https://www.stat.umn.edu/geyer/f22/5421/notes/expfam.html), dated 24 August 2022. Read §§3.1–3.7, 4, 7.1–7.5, 8.3, 9.1, 9.4 and 10. New key `geyer2022_exp_family`.
4. Geyer, [“Proper Conjugate Priors for Exponential Families”](https://www.stat.umn.edu/geyer/5421/notes/prior.html), dated 29 October 2025. Read §§2.1–2.4, particularly eqs. 2.3–2.5 and the propriety conditions. New key `geyer2025_conjugate`.
5. Kyle Siegrist, [“Introduction to the Poisson Process”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/14:_The_Poisson_Process/14.01:_Introduction_to_the_Poisson_Process), last modified 10 August 2020. Read §14.1, “The Poisson Model” and “The Basic Assumption,” to separate a Poisson count from a full Poisson process. New key `siegrist2020_poisson_process`.
6. [R `family` documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html), “Details,” opened 16 November 2026, for the quasi-Poisson variance specification. New key `rstats_family2026` uses the access year explicitly because the rolling documentation has no fixed publication year.
7. [*SAS/STAT 12.1 User's Guide*, Ch. 3, “Generalized Linear Models”](https://support.sas.com/documentation/cdl/en/statug/65328/HTML/default/statug_intromod_sect011.htm), reopened for the distinction between linking the mean and transforming a response. Existing key `sas2012_glm`.

## Changes and checks

- Added lead context, a motivating comparison, a precise bridge between the dispersion-scaled GLM form and the unscaled natural form, interpretation, moment and conjugacy properties, statistical use, a numeric Poisson–Gamma example, limits, cross-links and two History paragraphs. Every new factual paragraph has a citation to an opened, located passage.
- Aligned the inherited Bayesian properties and concept answer to $h(x)\exp\{\eta^{\mathsf T}T(x)-A(\eta)\}$, leaving $a,b,c,d,e$ for the GLM form. The Gamma exercise now uses lowercase fixed covariates and located citations. Replaced the original normal density's second notation formula as genuine duplication; its sign-convention relationship remains in prose. Replaced broad model-choice anecdotes with a sourced comparison. Corrected the inherited statement that Poisson counts themselves imply independent increments; that condition belongs to a Poisson process. All definitions, worked derivations, practice questions, cross-links and infobox facts remain.
- One collapsed Proof box derives the moment and Fisher-information identities, the scalar mean–variance formulas, sufficiency of the summed statistic and the conjugate update. It does **not** prove the Pitman–Koopman–Darmois converse; `research/proofs-todo-overrides.json` keeps that exact property in the generated proofs todo despite the page's other proofs. The generator change is needed because its old todo logic treated one Proof box as covering every property on a concept page.
- Source corrections affect dependent articles. The measurement-error excerpt was expanded to 431 words from its 410-word baseline, preserving its topic content. The distribution and Bayesian-result retention tests now accept the newly opened citations in place of inherited unlocated ones. The natural-parameter page's two-citation status is documented in `citations-todo.md` pending a checked source for its separate completeness claim.

## Verification

Generated article: 4,894 body words versus 2,993 before; zero figures versus zero before; seven distinct question links; one collapsed Proof box and one specifically listed converse todo item. The page-specific check asserts its printed Poisson–Gamma values and inherited numerical examples, symbols, citations and preserved links. All 35 completed pages' exact-value checks, 67 Python tests, and offline validation of 420 bibliography entries pass. `git diff --check` is clean. The temporary Quarto-to-Pandoc shim was used for the generator's Pandoc call; no HTML render was attempted.
