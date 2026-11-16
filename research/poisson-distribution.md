# Poisson distribution research notes

Type: distribution. Baseline: 3,061 words and three figures (two infobox plots and one chapter plot). The original page already has the binomial rare-event limit with an inline argument, a collapsed proof of independent-sum closure, six inherited worked examples, an infobox of moments, and Gamma conjugacy. All remain. The depth text adds exposure interpretation, the distinction between a count law and a full process, a mixed-rate failure and a fresh numeric exercise.

## Sources opened

- Siegrist, “The Poisson Distribution,” §4 of the author-hosted *Probability, Mathematical Statistics, and Stochastic Processes*, https://www.randomservices.org/random/poisson/Poisson.html. Read Basic Theory, Moments, Sums, Normal Approximation and The Binomial Distribution. Checked $\lambda=rt$, mass recurrence and modes, equal mean and variance, independent sums, process interpretation and binomial rare-event limit. The source's displayed kurtosis derivation contains a typographical error; the page does not rely on it.
- NIST/SEMATECH e-Handbook §1.3.6.6.19, “Poisson Distribution,” https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm. Checked mass/CDF, mode, moments and sample-mean estimator.
- R Core Team `glm` documentation, https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html, Arguments `offset`. Checked use of an a priori known component in the linear predictor; the log-exposure formula is algebra from $\lambda_i=r_i t_i$.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, printed pp. 425–426, `/workspace/statwiki-sources/dodge2008/pages/pdf-0423.txt` and `pdf-0424.txt`. Checked the 1837 binomial-limit history and the mean/variance derivation. The printed example of two average mistakes per page and three observed has probability 0.1804.
- Poisson's 1837 *Recherches...*, Chapter III transcription, https://fr.wikisource.org/wiki/Recherches_sur_la_probabilit%C3%A9_des_jugements_en_mati%C3%A8re_criminelle_et_en_mati%C3%A8re_civile/Chapitre_III, opened to inspect the original public-domain text. The exact p. 206 rare-event passage was not located in this reading; its attribution is taken from Dodge and the original work is not newly cited for a specific formula.

## Fact ledger

- **Checked:** A Poisson count at rate $r$ over exposure $t$ has $\lambda=rt$, mean and variance $\lambda$. Siegrist §4 Basic Theory and Moments; NIST §1.3.6.6.19.
- **Checked:** The limit from $\operatorname{Bin}(n,p_n)$ requires $np_n\to\lambda$, not merely large $n$. Siegrist §4 The Binomial Distribution.
- **Checked:** Marginal Poisson counts do not imply process-level independent increments; the latter is an additional assumption. Siegrist §4 Basic Theory.
- **Checked:** For a random mean equally likely to be $1$ or $9$, $\operatorname{E}\Lambda=5$, $\operatorname{Var}\Lambda=16$, and a conditional Poisson count has pooled variance $21$ by total variance. Code check in `checks/poisson-distribution.py`.
- **Checked:** All new numeric probabilities and the existing rare-fault approximation are recomputed in the focused check.
- **Assumed:** The hypothetical help-desk rate is steady within the worked example. No empirical claim is made about a real help desk.
- **Disputed:** The original first introduction of the count law is historically nuanced; the page attributes the 1837 binomial-limit account to Dodge rather than claiming independent priority research.

## Bank selection

`ex-sp-poisson-half-hour` tests process counts and first waits with different numbers from the page exercise. `ex-inf-poisson-information` derives the score and Fisher information for iid counts. Both have worked answers and address distinct statistical uses.
