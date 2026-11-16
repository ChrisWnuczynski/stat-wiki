# E step — research record

Status: checked against the full original paper by Dempster, Laird and Rubin (1977), §§2–4, printed pp. 3–13, available through Brown University course archive, and the local mixture chapter §§“The E and M steps”, “An E step”, and “EM lower bound”. Dodge index has no matching entry; no historical claim is drawn from it.

- **Checked:** Dempster et al. §2 p. 6, eq. (2.17), define the conditional expected complete log likelihood with the expectation taken at the old parameter and optimization over a new candidate. The distinction between the two arguments is essential.
- **Checked:** For a finite mixture, conditioning a latent component indicator on an observation gives a posterior membership by Bayes' rule; the memberships sum to one. This specializes the original paper's general E step and matches the source chapter's E-step derivation.
- **Checked:** Dempster et al. §3 derive nondecrease of observed likelihood for exact EM updates. The E step alone is a conditional expectation, not an optimization or an assertion that any particular model fits well.
- **Checked by Python:** for two unit-variance normals with means 0 and 2 and weights 1/2, responsibilities at x=0 and x=2 are 0.88079708 and 0.11920292; their sum is one. At x=1 the responsibility is 1/2. The source chapter's pre-existing 0/3 example yields density 0.39894 and 0.004432 and membership 0.989013.
- **Assumed:** the two-component toy example uses known, equal variances and current, equal weights; it is an illustration, not a fitted dataset.
- **Disputed/limited:** A responsibility is conditional on the chosen mixture and its current parameters, so it cannot certify a true class label. A Gaussian density collapsing around one observation can make likelihood unbounded; a stable E step alone does not cure this.

Page type: Section (method step). Retain the generated definition, formula, source-chapter example, and citations; expand its reasoning, worked calculation, assumptions, proof, and practice.
