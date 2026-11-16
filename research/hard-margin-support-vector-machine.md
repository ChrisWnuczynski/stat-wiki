# Hard-margin support vector machine — rank 172

Type: concept. Baseline 1,343 words, zero figures. Preserve the unit-normal and canonical margin conventions, primal and dual programmes, objective-normalisation discussion, all three-point calculations, infobox and linked questions.

## Sources opened

- Cortes and Vapnik (1995), complete publisher-hosted paper, *Machine Learning* 20, pp. 273–297, especially pp. 275–282 (§§2–3) and pp. 283–284 (§4). This original supplies the separable maximum-margin construction, quadratic dual, support-vector representation, historical relationship to Boser et al. (1992), and the soft-margin extension.
- Burges (1998), complete author-hosted tutorial at Microsoft Research, *Data Mining and Knowledge Discovery* 2, pp. 121–167, especially §3.1 pp. 128–131, §3.2 pp. 131–132, §3.4–3.5 pp. 134–136, and §4 pp. 136–139. The text gives the full-width margin, primal/dual/KKT derivation, sparse support-vector role, nonseparable case and inner-product transition.
- The local StatWiki statistical-learning source chapter was read for all original definitions, conventions and worked calculations. The authorized Dodge index has no support-vector or optimal-margin entry. The Boser et al. 1992 metadata/abstract and publisher link were inspected, but its full text was inaccessible, so no new claim cites it.

## Fact ledger

- **Checked:** Under canonical constraints, the two nearest supporting planes are separated by $2/\|w\|$; minimizing $\|w\|^2/2$ maximizes this full slab width (Cortes–Vapnik §2.1 pp. 277–279; Burges §3.1 pp. 128–129).
- **Checked:** Stationarity of the primal Lagrangian yields $w=\sum_i\alpha_i y_i x_i$ and $\sum_i\alpha_i y_i=0$; the dual is a concave quadratic and positive multipliers imply active margin constraints (Cortes–Vapnik §2.1 pp. 278–279; Burges §§3.1–3.2 pp. 129–132). An active point can have a zero multiplier in a degenerate fit (Burges §3.1 p. 130).
- **Checked:** The primal is convex and strict separability supplies a strictly feasible scaled point; Slater/KKT gives zero duality gap (Burges §§3.1–3.2 pp. 129–132; mathematical proof on page). Full general Slater duality theorem is not proved here and is separately logged for review.
- **Checked:** For $(-2,-1)$ negative and $(1,2)$ positive on the line, the closest pair $-1,+1$ gives $w=1,b=0$, full width $2$, and positive multipliers $1/2$ each. Moving the positive point $+1$ to $+1/2$ gives $w=4/3,b=1/3$, full width $3/2$, and paired multipliers $8/9$. Focused check verifies all arithmetic, the retained three-point solution and the objective factor conversion.
- **Checked:** An XOR-labelled square and one feature vector given both labels make the hard-margin constraints infeasible. The soft-margin formulation introduces violations at a price (Cortes–Vapnik §3 pp. 280–282; Burges §3.5 pp. 134–136).
- **Checked:** Cortes–Vapnik (1995) pp. 275–276 traces the kernel step to Boser, Guyon and Vapnik (1992) and presents its soft-margin extension; this supports the history paragraph without citing an unread original.
- **Assumed:** Both labels occur and the data are finite. The quoted geometric margin uses Euclidean distance in the supplied feature coordinates; feature rescaling changes that metric.
- **Disputed/qualified:** A margin of $2/\|w\|$ is the full gap, whereas $1/\|w\|$ is the distance from the decision boundary to one supporting plane. A point on the supporting plane need not have a strictly positive multiplier in degenerate configurations. The existing source chapter cites Boser (1992), Vapnik (1995) and ESL without precise locators; shared citation repairs are listed for integration rather than silently replacing those inherited facts.
