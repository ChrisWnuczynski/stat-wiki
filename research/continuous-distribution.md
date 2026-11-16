# Continuous distribution research notes

## Scope and baseline

- **Checked:** Rank 142 is a Concept/Definition page, not one of the 25 `distributions.json` named-family entries. Baseline has 475 words and two figures. The generated article contains a density-based definition, a three-exponential/three-normal density figure, a mass-versus-density/CDF figure, and two fully worked examples: cubic CDF and uniform unit interval. All are retained.
- **Checked:** The stock lead says a continuous law is described by a density. That is only true under the narrower absolutely continuous convention used by the copied course definition. A structured one-sentence lead override is requested in pending; the body explains both conventions for consistency.

## Sources opened

- **Checked:** Kyle Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, open licensed LibreTexts section “3.2 Continuous Distributions,” `https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/03:_Distributions/3.02:_Continuous_Distributions`. Basic Theory, Definitions and Basic Properties defines continuous as no singleton masses, defines density by integral, says some continuous laws have no density and density heights can exceed one; Constructing Probability Density Functions gives normalisation. Proposed key `siegrist2022_continuous`.
- **Checked:** Oliver Knill, *Probability and Stochastic Processes with Applications* (2009), full author-hosted book `https://abel.math.harvard.edu/~knill/books/KnillProbability.pdf`. §2.1 gives countable-additivity axioms and notes Kolmogorov’s 1933 monograph and other earlier proposals. §2.12 distinguishes absolutely continuous, pure-point and singular continuous laws and constructs the Cantor distribution with continuous CDF but no density. Proposed key `knill2009_probability`.
- **Checked:** Dodge (2008), printed p. 111 (`pdf-0117.txt`), “Continuous Distribution Function,” gives the CDF and interval identity; it also states that a continuous CDF is differentiable, which is false in general. Used as orientation only, not cited.

## Audit

- **Checked:** The collapsed proof establishes interval probabilities, zero point masses and CDF continuity from an integrable density; it constructs a Cantor counterexample to the converse. The almost-everywhere derivative result for arbitrary integrable densities invokes the standard differentiation theorem and is logged for a fuller proof in pending.
- **Checked:** The numeric checker recomputes the baseline cubic CDF’s $19/64$ interval probability and $3/4$ mean, the inherited uniform example’s $5/12$ and $7/8$, the new linear-density normalisation, interval probability and $7/6$ mean, and the mixed sensor’s atom and continuous component.
- **Checked:** Existing answered bank items `ex-prob-random-radius` (CDF/density from disc area), `ex-prob-component-five-years` (exponential tail), and `ex-prob-shifted-exp-generate` (shifted density, mean and inverse CDF simulation) genuinely exercise distinct density-law uses. Their numerical data differ from both the inherited cubic/uniform examples and the new worked/mixed examples. No direct question backlink exists for this slug, so these are selected from the answered chapter bank and connected in prose.
- **Assumed:** The constructed sensor model treats its zero reports as true atoms and its nonzero reports as exact continuous readings; a real sensor’s mechanism would need investigation.
- **Disputed:** The source chapter’s Key idea says all continuous distributions are specified by a density, while its own definition paragraph notes continuous CDFs need not have densities. Pending requests a qualifier for the Key idea and for the local density-convention definition. Dodge’s global differentiability statement is also false for a continuous CDF.
