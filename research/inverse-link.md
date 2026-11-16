# Inverse link research notes

## Scope and baseline

- **Checked:** Rank 139 is a Concept page. `research/baseline.json` records 522 words and zero figures; the generated page has a reciprocal-gamma definition, a three-link equation (log, reciprocal and inverse-square), a clotting-time example at predictors 0.25 and 0.05, and a zero-crossing example at intercept 0.5 and slope -0.1. The new content retains those facts and all existing question links, infobox values and references.
- **Checked:** The stock lead describes an arbitrary inverse *of* a link, but this page's definition and gamma material describe the particular reciprocal link. A one-sentence description override is requested in the pending record.

## Sources opened

- **Checked:** Nelder and Wedderburn (1972), full original journal scan hosted for a University of Sydney statistics course, `https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf`, especially §1.3 p. 372 and §3.4 pp. 380–381. The authors set out an exponential-family component, linear systematic component and linking function, and identify the gamma inverse transformation. The journal article’s publisher/DOI record is `https://doi.org/10.2307/2344614` (existing bibliography key `nelder_wedderburn1972`).
- **Checked:** R Core Team, official `family` documentation, `https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html`, Usage, Arguments and Value. It explicitly gives `Gamma(link = "inverse")`, the inverse Gaussian default `1/mu^2`, alternative links, and the separate `linkfun`, `linkinv`, `variance`, `valideta` functions. Existing key `rstats_family2026`.
- **Checked:** Dodge (2008), printed p. 219 (`pdf-0222.txt`), has an entry “Generalized Linear Regression” about heterogeneous errors in a linear model. It is not the Nelder–Wedderburn GLM definition, so it was used only for orientation and is not cited on the page. The Dodge index has no direct inverse-link entry.

## Mathematical and interpretive audit

- **Checked:** For reciprocal link, $\mu=1/\eta$, $d\mu/dx=-\beta_1/\eta^2$, and $\mu(x+\Delta)/\mu(x)=\eta(x)/(\eta(x)+\beta_1\Delta)$ on the positive predictor domain. The collapsed proof derives these and the gamma natural-parameter sign explicitly.
- **Checked:** With gamma shape $k$ and mean $\mu$, natural parameter is $-k/\mu$ in a unit-dispersion canonical form, or $-1/\mu$ with dispersion $1/k$. Thus R's positive reciprocal link is canonical only *up to sign*. The older baseline's wording already carries this qualification.
- **Checked:** A gamma mean and variance function are distinct from its link; an inverse-Gaussian model can also use the reciprocal link. The official R documentation supplies the software claims.
- **Checked:** All printed worked, practice, baseline and domain-crossing values are recomputed in `checks/inverse-link.py`.
- **Assumed:** Dose in the constructed worked example is a generic nonnegative study-scale unit; the example does not claim to reproduce the historical clotting dataset.
- **Disputed:** Dodge's “Generalized Linear Regression” is not a source for the reciprocal GLM link. The course-book claim that the family chiefly changes standard errors is too broad for unrestricted likelihood or AIC comparisons; this page gives the separate variance and likelihood roles without repeating that claim.

## Question bank

- **Checked:** `q-38` has a full worked answer identifying the general inverse-link map when changing logit to probit. It tests the distinction from this page's named reciprocal link.
- **Checked:** `q-57` has a full worked answer deriving the negative-binomial canonical link and its inverse mean map, another instance of the general link direction. Neither duplicates the page's dose calculation.
