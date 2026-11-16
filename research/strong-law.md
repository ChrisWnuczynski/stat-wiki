# Strong law

Type: Theorem. Rank 235. Tier: full.

## Material checked

- **Checked:** Frozen baseline 378 body words and no figures. The generated page keeps the finite-mean statement and the pathwise-versus-in-probability note, including the Cauchy characteristic-function remark and the $n=400$ scale $0.025$.
- **Checked:** Durrett, 11 January 2019 PDF. Theorem 2.4.1 (p. 76) is the strong law for pairwise i.i.d. variables with a finite absolute mean, proved by Etemadi's truncation. Theorem 2.4.5 (p. 78) sends the average to infinity when the positive part has infinite mean. Theorems 2.4.7 and 2.4.9 are the renewal and Glivenko–Cantelli applications. Theorem 1.6.4 (pp. 29–30) is the inequality used for the fourth-moment tail, with the remark that some authors call the general form Markov's inequality.
- **Checked:** Dodge, printed pp. 298–299. The strong law is written as the probability-one limit of the sample average, separated from the weak law. Bernoulli (1713), Bienaymé and Chebyshev are named. The numerical display on p. 299 treats a Chebyshev upper bound as if it were a two-sided constraint on a chosen probability; that display is not used.
- **Checked by code:** Fair-coin Chebyshev bound $0.25$ at $n=100$, fourth-moment value $1862.5$, tail bound $0.18625$, and the $n=50$ bounds $0.125$ and $0.04625$.
- **Assumed:** The coin tosses are independent and fair, so the centred variable is $\pm 1/2$ with equal probability.
- **Disputed:** None. The elementary proof on the page assumes a fourth moment. The finite-mean theorem is cited from Durrett rather than reproved in full.

## Sources opened and used

1. Rick Durrett, *Probability: Theory and Examples*, version 5, 11 January 2019, §§1.6.1 and 2.4. Key `durrett2019`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 298–299. Key `dodge2008`.
