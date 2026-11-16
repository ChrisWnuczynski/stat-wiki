# M step — research record

Full source: Dempster, Laird and Rubin (1977), *Maximum Likelihood from Incomplete Data via the EM Algorithm*, full original paper hosted in Brown University's course archive, §§2–4, printed pp. 3–13. Local source chapter `sources/stat3006/chapters/sl-05-mixtures-em.qmd`, §§“The E and M steps”, “The M step”, “Why the likelihood never decreases”. Dodge index has no matching entry used for historical statements.

- **Checked:** Dempster et al. §2 p. 6, eq. (2.17) define E step $Q(\phi'|\phi)$ and the M step as a maximization of $Q$ over the new parameter. Current conditioning parameter remains fixed in $Q$.
- **Checked:** The local chapter derives finite normal-mixture updates: mixing weights $N_h/n$; component means weighted by responsibilities; covariance likelihood update uses divisor $N_h$, not $N_h-1$. Dempster et al. §4 give mixture-model applications of the general update.
- **Checked:** Dempster et al. §3 prove the observed likelihood is nondecreasing after a complete exact EM update. That does not imply global optimality or even finite maximum for an unrestricted Gaussian mixture.
- **Checked by Python:** for $x=(0,2)$ and component-one memberships $(.8,.4)$, effective counts are $1.2,.8$, updated weights $.6,.4$, means $2/3,1.5$. For memberships $(.75,.25)$, weights $.5,.5$ and means $.5,1.5$.
- **Assumed:** the worked example keeps component variances fixed at one and treats supplied E-step memberships as exact. It illustrates the M calculation, not a complete fit to real data.
- **Disputed/limited:** $N_h=0$ makes the mean update undefined; unrestricted Gaussian mixture covariance can collapse at a point; a local stationary point or likelihood increase does not certify global fit.

Page type: Section (method step). Preserve baseline displayed update formulas, example and supported citations; add rationale, proof, numeric work, hidden practice and concrete limits.
