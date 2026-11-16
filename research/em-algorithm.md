# EM algorithm — research notes

- **Checked with qualification:** Dempster, Laird and Rubin (1977), publisher DOI page and abstract, *JRSS B* 39(1), pp. 1–22, inspected for original metadata and orientation. Its full derivation was unavailable; new prose cites the full Fraley–Raftery §3 attribution and the full Ng monotonicity proof.
- **Checked:** Fraley and Raftery (2002), *JASA* §3, p. 613, full author-hosted, publisher-permitted paper at https://sites.stat.washington.edu/raftery/Research/PDF/fraley2002.pdf. Read its incomplete-data account of EM and its attribution to Dempster, Laird and Rubin (1977).
- **Checked:** Andrew Ng, Stanford CS229 original course notes, “The EM algorithm,” Part IX, pp. 2–5: Jensen lower bound, E-step conditional distribution, M-step and monotonicity argument. Opened the full eight-page Stanford-hosted PDF. The PDF is undated; bibliography year 2006 follows a 2009 scholarly citation to these CS229 notes and is an assumed edition year.
- **Checked:** scikit-learn official User Guide §2.1.1, full HTML: covariance singularities can yield unbounded Gaussian-mixture likelihoods and initialization matters.
- **Checked:** Existing StatWiki source mixture chapter and inherited article material against algebra: the two arguments of $Q$ have different roles, responsibilities remain fixed in the M step, and a normal mixture M step uses weighted means and likelihood variances.
- **Checked:** Dodge (2008), “Missing Data,” printed p. 350, provides early missing-plot history and points to Rubin 1972, but does not describe EM; it is orientation only and will not be cited for EM's 1977 history.
- **Assumed:** exact E-step conditionals and an exact or nondecreasing M step where a monotonicity claim is made; finite likelihood in the numerical example.
- **Disputed/limited:** monotone likelihood does not imply convergence of parameters or a global maximum. An unconstrained Gaussian mixture likelihood can diverge through component variance collapse.
