# Beta–Binomial conjugacy — rank 159

Type: theorem/proposition. Baseline 1,304 words and one figure. Preserved the displayed prior-sensitivity figure, the stock statement, source proof, two embedded exercises with worked answers, infobox and all question links.

## Sources opened

- MIT OpenCourseWare, 18.05 Class 15, *Conjugate priors: Beta and normal* (Spring 2022), full 7-page PDF. Read pp. 1–5, especially §4 and §5.1–5.2. It derives the beta–binomial update and sequential Bernoulli form, explaining why positive shapes and the support matter. The existing source proof is replaced by a more complete single normalised derivation.
- Dodge (2008), printed pp. 30, 32 and 40. Read the Bayes entry for the Price publication history and the beta entry for its density and mean. The source does not attribute beta–binomial conjugacy's modern terminology to Bayes.
- Read the generated source statement and embedded practice q-06/q-17; compared against baseline. The new example uses different numbers from the preserved prior-sensitivity figure.

## Fact ledger

- **Checked:** Beta prior times binomial likelihood gives Beta with success and failure increments (MIT §5.1, p. 5). Proof normalises by the beta integral.
- **Checked:** With shapes 2 and 3 and 7 successes among 20, posterior is Beta(9,16), mean 9/25=.36, variance 144/16250≈.0088615, and probability of two future successes is 9/65≈.13846. Checked by SymPy and SciPy.
- **Checked:** Sequential batches commute because their counts add; a future Bernoulli success has posterior predictive probability equal to the beta mean. Derived from the same integral.
- **Checked:** A prior with zero density outside its support keeps zero posterior density there for positive finite marginal likelihood. This is also in preserved exercise q-06.
- **Checked:** Bayes's essay appeared after his death through Price in 1763 (Dodge p. 32). This is historical background, not a claim that he named the beta family.
- **Assumed:** The trial model is independent Bernoulli with one common rate, as in the statement. Counterexamples use changing rates and dependence.
- **Disputed:** Treating shapes themselves as literal observed counts is only an analogy; the exponents are shape minus one and a `Beta(1,1)` prior has total concentration two but no actual past trials. The article distinguishes this.

## Shared source requests

The theorem depth `context` currently puts a second sentence in the lead. Move its substantive thought to the body and retain a citation-only marker in context. Source setup/intuition/use/proof and article history contain unlocated citations to books that were not read for this pass; replace or locate those using the opened MIT note or retain only original citations whose locations can be checked. The figure remains unchanged.
