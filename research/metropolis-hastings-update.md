# Metropolis–Hastings update — rank 99

Type: Method/definition. Frozen baseline 2,572 body words and one figure. The source's update definition, two inherited properties, three worked question examples, figure, infobox and twelve question links remain generated. New prose explains the correction, a two-state asymmetric example, a proof, distinct failure cases and history.

## Sources read

- **Checked:** W. K. Hastings, “Monte Carlo sampling methods using Markov chains and their applications,” *Biometrika* 57 (1970), pp. 97–109, original author-hosted full paper at https://www.probability.ca/hastings/hastings.pdf. Read §§1–2.4, especially pp. 98–101 on normalising-constant cancellation, dependent samples, arbitrary proposals, detailed balance, rejection and scale choice, and pp. 104–105 on proposal design. The author-hosted scan is of the published journal paper; the bibliography DOI is 10.1093/biomet/57.1.97.
- **Checked:** Levin and Peres, *Markov Chains and Mixing Times*, 2nd ed. (2017), author-hosted full text, §1.6 p. 13 and §3.2 pp. 38–40 for detailed balance, the Metropolis rule and normalising-constant cancellation. The bibliography entry is pending under rank 98.
- **Checked:** The publisher DOI page for Metropolis and collaborators (1953), 10.1063/1.1699114, identifies the original molecular-simulation paper. The publisher full text was inaccessible, so the new history cites Hastings's firsthand retrospective rather than claiming to have read the original. The source chapter's supported original citation remains intact.
- **Checked:** Dodge's local index has no Metropolis or Hastings entry relevant to this update; it supplied no claim or citation here.
- **Checked by code:** Exact fractions for both asymmetric two-state examples and the inherited $9/(4e)$ acceptance result. SciPy quadrature reproduces the inherited logit-normal posterior means and intervals and prior mean. The specific R-seeded Monte Carlo outputs are retained as inherited examples and are close to independent quadrature values.
- **Assumed:** The hypothetical discrete proposal is applied exactly as specified; a target-support proposal and viable return path are needed for the balance proof. Convergence from a start is not inferred from balance alone.
- **Disputed:** None. The source explicitly warns that proposals from a small scale can have high acceptance and poor exploration, so the new text avoids an acceptance-rate target.

## Proof and bank

The one collapsed proof derives detailed balance via the minimum of forward and reverse probability flows, then stationarity by summing. Convergence and Monte Carlo limit claims are logged in pending proofs. Existing answered bank items `c-14`, `q-19` and `ex-gibbs-mh` test cancellation, diagnostic interpretation and a bivariate implementation. They differ from the inherited embedded `q-05`, `q-10`, and logit-normal examples and from the new two-state example.
