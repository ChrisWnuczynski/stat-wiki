# Modes of convergence — research record

Concept page, rank 87. Baseline 385 words, zero figures; preserve four definitions, spike and independent-copy counterexamples, links and supported source citations. Stock lead has a singular verb for a plural term; structured override in pending.

## Sources opened

- Kyle Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, “Convergence,” author-hosted https://www.randomservices.org/random/prob/Convergence.html . Read definitions, implications, subsequences and independent Bernoulli counterexample. New key `siegrist_convergence_prob`.
- Same author/book, “Convergence in Distribution,” https://www.randomservices.org/random/dist/Convergence.html . Read CDF definition, continuity points, weak-limit relationships. New key `siegrist_convergence_dist`.
- Same author/book, “Vector Spaces of Random Variables,” https://www.randomservices.org/random/expect/Spaces.html . Read convergence in mean, Markov implication, counterexamples. New key `siegrist_convergence_lp`.
- Dodge (2008) authorized index searched for convergence modes; no direct entry.
- Question bank `ex-sp-l2-markov` and `ex-sp-borel-cantelli` read with worked answers. The first exercises the $L^2$ implication; the second distinguishes infinitely many events under summable versus divergent probabilities. Neither repeats the page's embedded numerical example.

## Fact audit

- **Checked**: definitions and implication graph from the three Siegrist sections. Proof provided in one collapsed box.
- **Checked**: distributional convergence to constant implies in-probability; independent Bernoulli$(1/n)$ converge in probability and $L^2$ but not almost surely: Siegrist Convergence, Coins; Vector Spaces, Counterexamples.
- **Checked**: numerical spike probabilities and moments using exact fractions in `checks/modes-of-convergence.py`.
- **Assumed**: random variables share a probability space for almost sure, in-probability and $L^p$ comparisons; distributional convergence only compares laws.
- **Disputed/limited**: distributional convergence does not imply pointwise CDF convergence at a jump, nor does almost sure convergence alone imply convergence of expectations.
