# Canonical link research notes

- **Checked:** Nelder and Wedderburn (1972), original full paper https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf . Read §§1.1–1.3 pp. 371–372, §2.1–2.2 pp. 373–374, and §§3.2–3.4 pp. 377–381. These support the exponential-family form, canonical-parameter case, score/Hessian/sufficient statistics, and Poisson, binomial and gamma examples.
- **Checked:** Dodge (2008) authorized index has no canonical-link entry. Its "Generalized Linear Regression" entry, p. 219, concerns generalized least-squares regression rather than the Nelder–Wedderburn GLM; it is not cited for this page.
- **Checked by code:** logistic and Poisson mean/odds arithmetic in `checks/canonical-link.py`.
- **Assumed:** Independent observations, fixed design and dispersion for the displayed score, Hessian and sufficiency argument; explicitly stated in the page.
- **Disputed:** The gamma natural parameter is $-1/\mu$ in the chosen exponential-family form, while positive inverse links are often called canonical up to sign convention. Text specifies the convention and domain.
