# Logit, probit and complementary log-log links

Type: Concept. Rank 284. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, p. 296, Eq. 9.2, defines the logit link, and the same page defines the probit as \(\Phi^{-1}\). The log link for Poisson counts is on that page and is not one of these three probability links.
- **Checked by code:** At \(\eta=1/2\), the three inverses round to \(0.6225\), \(0.6915\) and \(0.8077\). The logit odds equal \(e^{1/2}=1.6487\) to four decimals. At \(\eta=-1/2\) the inverses round to \(0.3775\), \(0.3085\) and \(0.4548\). At \(0\), complementary log-log rounds to \(0.6321\), while logit and probit equal \(1/2\). And \(1-0.8077=0.1923\).
- **Assumed:** \(\Phi\) is the standard normal distribution function.
- **Disputed:** Nothing numerical. Complementary log-log is not stated on the ESL page that was opened. Its formula is the standard inverse of \(\log(-\log(1-p))\), and the range and asymmetry are proved from that formula. McCullagh and Nelder was not opened, so no page of that book is cited.

## Sources opened

Hastie, Tibshirani and Friedman (2009), p. 296. Key `hastie_esl2009`.

## Proofs

Range of all three inverses, symmetry of logit and probit, and failure of that symmetry for complementary log-log are proved.
