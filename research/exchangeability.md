# Exchangeability — rank 133 research

## Sources read

- **Checked:** Gelman et al., *Bayesian Data Analysis*, third edition, author-hosted electronic edition at `https://sites.stat.columbia.edu/gelman/book/BDA3.pdf`, chapter 5 §§5.1–5.2, printed pp. 102–106. The authors' book page explicitly makes the electronic edition available for non-commercial use. This supports the rat-tumour figures, latent-rate exchangeability, conditional iid mixture, finite-sequence qualification, and laboratory/time counterexamples.
- **Checked:** David A. Stephens, McGill University, *The de Finetti Representation Theorem*, MATH 559 handout, 2023, pp. 1–5, `https://www.math.mcgill.ca/dstephens/559/Handouts/Math559-Fall2023-01-DeFinetti.pdf`. The full PDF was opened. Page 1 distinguishes finite from infinite exchangeability and states the binary representation; pp. 2–4 derive it from finite hypergeometric probabilities and limits; pp. 4–5 discuss posterior prediction.
- **Checked:** The publisher archive page for de Finetti's 1937 *La prévision* at `https://www.numdam.org/item/AIHP_1937__7_1_1_0/` confirms the original publication metadata. The original article itself was not used for the representation proof; the McGill proof and Gelman discussion support that account.
- **Assumed:** The existing Lindley–Smith (1972) reference remains in the generated bibliography; no new historical claim is based on it.
- **Disputed:** A Duke course PDF found during research reverses the behaviour of the urn reinforcement parameter in its introductory example. It is not cited or used. The page uses Gelman and Stephens instead.

## Baseline preservation and calculations

- **Checked:** Baseline records 483 body words and zero figures. Existing page links to the Hierarchical Bayes definition and the rat-tumour hierarchy, including 4/14 rats, 70 historical studies, $\operatorname{Beta}(\alpha+4,\beta+10)$, and the pooling question; these are retained in the generated article. The page-local copy explains their exchangeability role and preserves the section links.
- **Checked:** A Beta(2,3) mixture has mean $2/5=0.4$, second moment $2\cdot3/(5\cdot6)=0.2$, ordered two-trial probabilities $(P_{11},P_{10},P_{01},P_{00})=(0.2,0.2,0.2,0.4)$, covariance $0.2-0.4^2=0.04$, and predictive success probabilities $3/6=0.5$ after success and $2/6=1/3$ after failure.
- **Checked:** Drawing one red and one blue ball without replacement yields $P(1,0)=P(0,1)=1/2$ and covariance $-1/4$. It is finite exchangeability with negative dependence, ruling out an iid Bernoulli mixture.
- **Assumed:** The new McGill handout is dated by its Fall 2023 filename and course path; the PDF itself does not print a date on its first page.

## Proof scope

The collapsed proof establishes permutation invariance of an iid mixture, its nonnegative cross-covariance, and the finite two-ball counterexample. The converse de Finetti representation is logged for a full proof, since its limiting-measure argument is separate.

- **Checked by code:** The additional shared-coin bank item has exchangeable joint probabilities P(1,0)=0.16 and P(1,1)=0.34 versus independent product 0.25; see the focused check.
