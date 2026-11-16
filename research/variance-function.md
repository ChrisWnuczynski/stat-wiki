# Variance function research notes

Type: concept. Baseline: 286 words, zero figures. The existing definition lists normal, Poisson, Bernoulli, Gamma and inverse Gaussian forms and contrasts a fully specified family with quasi-likelihood. The generator's original definition and citation remain; the depth text adds derivation, diagnosis and numerical comparisons.

## Sources opened

- Hua Zhou, *Generalized Linear Models* (UCLA Biostat 200C, 2020), full online chapter, https://ucla-biostat-200c-2020spring.github.io/slides/09-glm/glm.html, especially “Exponential family distribution,” “Moments,” “Link function,” “Fisher scoring algorithm and IRWLS,” and “Diagnostics.” Checked all five standard variance shapes, exponential-family moment identities, GLM weights and Gamma parameterization.
- R Core Team, `family` documentation, https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html, full page, especially Arguments, Details and Value. Checked that each family object supplies `variance`, `quasi` accepts user-specified variance functions, quasi-Poisson and quasi-binomial free dispersion, and link and variance are separate components.
- Dodge 2008 index searched for “Variance function” and generalized linear models; no direct entry was found. No Dodge fact is cited for this page.

## Fact ledger

- **Checked:** With unit weights, GLM conditional variance is $\phi V(\mu)$, with the listed forms for Gaussian, Poisson, Bernoulli, Gamma and inverse Gaussian responses. Zhou, family table; R `family` Arguments.
- **Checked:** For an exponential-family density in the stated form, $\mu=b'(\theta)$ and variance is $\phi b''(\theta)$, derived in the collapsed proof; Zhou, Moments.
- **Checked:** Gamma shape $1/\phi$ and rate $1/(\phi\mu)$ yields variance $\phi\mu^2$; Zhou, Gamma example. All page numbers checked in `checks/variance-function.py`.
- **Checked:** A quasi-family models a mean–variance relation without a complete likelihood; R `family` Details. This does not imply every variance function comes from a regular exponential family.
- **Assumed:** The two-temperature reaction-time groups are hypothetical and used only for arithmetic.
- **Disputed:** Historical priority for variance-function terminology is not asserted. The history paragraph describes development of the documented GLM and R `quasi` framework without attributing an unverified first use.

## Bank selection

`q-55` directly tests Gamma $V(\mu)=\mu^2$ and how its variance changes with the mean. `c-41` tests why different response components in vector-response regression need their own variance functions. Both have worked answers and are distinct from the embedded numeric exercise.
