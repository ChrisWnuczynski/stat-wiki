# Support vectors and their multipliers research notes

## Scope and baseline

- **Checked:** Rank 140 is a Concept/Section page. Baseline has 168 words and zero figures. Its three-case multiplier table, examples of $C=0.03$, $1$ and $100$, infobox and five question backlinks are kept. The new page explains why the table follows from KKT conditions.
- **Checked:** The baseline table’s $\alpha=0$ row correctly allows a point *on* the margin, as well as outside it. Thus “all margin contacts have positive multiplier” is false when constraints are redundant.

## Sources opened

- **Checked:** Cortes and Vapnik (1995), original paper via university faculty-hosted scan `https://homepages.math.uic.edu/~lreyzin/papers/cortes95.pdf`, publisher record `https://doi.org/10.1007/BF00994018`. §2.1 pp. 278–280 gives hard-margin geometry, dual multipliers and support vectors; Appendix A.1 pp. 291–292 derives stationarity and complementary slackness. Existing key `cortes_vapnik1995`. The 1995 paper’s particular soft-margin penalty includes squared slack, so the page uses Burges for the standard linear-slack $C$-box formulation.
- **Checked:** Burges (1998), author’s full tutorial hosted by Microsoft Research at `https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/svmtutorial.pdf`, publisher record `https://doi.org/10.1023/A:1009715923555`. §3.1 gives the hard-margin dual; §3.2 gives KKT; §3.5 gives the linear-slack soft-margin dual, $0\le\alpha_i\le C$, and intercept recovery; §3.7 discusses nonunique multipliers; §4 kernels and §5 solver checks. Existing key `burges1998`.
- **Checked:** Dodge index has a printed p. 292 “Lagrange Multiplier” entry but no support-vector-machine entry. The general multiplier entry was orientation only and is not cited for SVM-specific claims.

## Audit

- **Checked:** The collapsed proof derives the hard-margin dual expansion and the soft-margin $C$ box and three KKT cases under the stated linear slack objective. It avoids attributing that exact soft-margin form to Cortes and Vapnik (1995).
- **Checked:** The three-point worked example and changed nearest point in Your turn are recomputed in `checks/support-vectors-and-their-multipliers.py`, including margins, dual balance and full slab width. These data differ from the bank’s two-point $(3,3)$ versus $(1,1)$ example.
- **Checked:** `ex-sl-17-2` has a full answer for a two-point hard-margin dual; `ex-sl-17-6` has a full answer interpreting three multipliers in a soft-margin fit. They exercise distinct aspects of this page and use different numbers from its embedded example.
- **Assumed:** The drawn $C=0.03,1,100$ comparison in the baseline describes an illustrative overlapping sample; the page does not infer exact support-vector counts from it.
- **Disputed:** “Only points on or inside the margin influence the fit” needs the qualifier that a zero-multiplier margin contact may be redundant. The page explicitly adds it without removing the baseline claim.
