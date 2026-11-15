# Standard error

Type: Concept/topic.

## Existing material read

- `articles/standard-error.qmd` before the edit: the definition and formulas for one and two means, a retained lost-hours example, exact normal one-standard-error coverage calculation, and GLM coefficient standard error. Leading body: 478 words; no figures; 25 linked questions.
- `sources/stat2004/chapters/inf-03-confidence-intervals.qmd`, especially “From a standard error to an interval,” and `sources/stat2004/chapters/inf-02-estimation.qmd` for the normal mean and nuisance variance.
- `questions/ex-inf-safety-interval.qmd` and `questions/ex-inf-green-voters.qmd`, including their answers.

## Sources opened and facts used

1. Student [W. S. Gosset], [“The Probable Error of a Mean”](https://en.wikisource.org/wiki/The_Probable_Error_of_a_Mean), *Biometrika* 6 (1908), pp. 1–25, original text. Read the introduction and the paper’s stated aims, the small-sample variability problem, and the normal-sample assumption. The [publisher record](https://academic.oup.com/biomet/article-abstract/6/1/1/225634) confirms year, volume, and pages. Citation key `student1908`, already present.
2. NIST/SEMATECH, [e-Handbook glossary](https://www.itl.nist.gov/div898/handbook/glossary.htm), standard error entry. Read the repeated-sample definition. Key `nist_glossary2002`, already present.
3. NIST/SEMATECH, [e-Handbook §1.3.5.2, “Confidence Limits for the Mean”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm). Read the $t$ interval and explanation of sample size and spread. Key `nist_mean_limits2002`, added here.
4. NIST/SEMATECH, [e-Handbook §4.1.2](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd12.htm) and [§4.4.4](https://itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm), opened during the preceding page’s research. Used for model assumptions and interpretation of fitted coefficients. Keys `nist_process_model2002` and `nist_model_fit2002`, already present.

## Verification and decisions

- The preexisting definition, lost-hours calculations, normal coverage calculation, GLM formula, Try it callout, and 25 question links remain. No figure, citation, or original worked example was removed.
- The single collapsed proof covers the stated independent and dependent difference rules, affine rule, sample-size relation, and exact normal-sample $t$ interval. The new worked example gives the units and a follow-up two-sample calculation.
- `checks/standard-error.py` recomputes the new values and the old safety-programme calculation and normal coverages. The quoted $t_{24,0.975}=2.064$ is rounded, so its endpoints are approximate.
- History confines itself to what the 1908 paper and modern NIST pages directly show. No date or attribution was inferred for the invention of the phrase “standard error.”

## Correction pass

- The added Casella–Berger citation had no opened supporting text. The variance identities now cite the opened Grinstead–Snell chapter 6 exercise, and the exact normal-sample $t$ claim cites the opened Siegrist §6.08 and NIST §1.3.5.2 passages. Student's original paper is cited only for the small-sample problem read in pp. 1–5. New citations identify a section, glossary entry, chapter exercise, or page.
- The inherited confidence-interval excerpt now cites the opened sources for its variance and coverage calculations. Removed new GLM commentary that the opened NIST pages did not support. The arithmetic check asserts the displayed numbers in the worked example, follow-up answer, and safety-programme excerpt.
