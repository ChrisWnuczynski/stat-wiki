# Identifiability — rank 136 research

## Sources read

- **Checked:** Thomas J. Rothenberg (1971), “Identification in Parametric Models,” *Econometrica* 39(3), pp. 577–591, DOI `10.2307/1913267`. The original article text was opened from an NYU faculty course archive; the bibliography points to the DOI. Section 2, pp. 578–579, defines observational equivalence, global identification and local identification. Sections 3–4, pp. 580–583, relate local identification at regular points to nonsingular information and distinguish the global question.
- **Checked:** Matthew Stephens (2000), “Dealing with Label Switching in Mixture Models,” *JRSS B* 62(4), pp. 795–809, author-hosted full PDF at `https://stephenslab.uchicago.edu/assets/papers/Stephens2000b.pdf`. Sections 1–3 explain mixture permutation symmetry and why artificial ordering constraints need not yield satisfactory posterior summaries.
- **Checked:** Peter J. Green (2019), “Introduction to Finite Mixtures,” in *Handbook of Mixture Analysis*, Ch. 1, full relevant chapter in the authorized CRC Press publisher preview `https://api.pageplace.de/preview/DT0400.9780429508240_A35885599/preview-9780429508240_A35885599.pdf`. Section 1.3.1, printed pp. 13–14, explicitly credits Teicher (1963) with finite normal and gamma mixture identification, explains that the mixing distribution can be identified despite arbitrary component-number labels, and describes zero-weight or coincident-component ambiguity in labelled representations. This full source supports the page's result and history statements; proposed bibliography key `green2019_finite_mixtures`.
- **Checked:** NIST/SEMATECH e-Handbook §7.4.3.7 `https://www.itl.nist.gov/div898/handbook/prc/section4/prc437.htm` gives the two-factor intercept, main-effect and interaction model. Official R `mgcv` documentation `https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/identifiability.html` explains sum-to-zero centring of ordinary smooth terms. Both pages were opened in full.
- **Checked:** Dodge authorized local extraction, printed p. 96, “Collinearity,” explains exact design-column dependence versus near collinearity and instability. No direct “Identifiability” entry appears in its index; Dodge is orientation, while Rothenberg supplies the formal definition.
- **Checked:** Project Euclid publisher page for Teicher (1963) was opened, but its full article appeared only in an iframe, and the PDF endpoint required a security check. Its bibliographic metadata and abstract were inspected for orientation, but the page no longer cites them. The correct result and Teicher attribution are instead supported by Green's full publisher-preview chapter; the general proof remains logged.

## Baseline and calculations

- **Checked:** Baseline page has no figures. It includes label switching, positive-weight/distinct-component qualification, factor-model contrast constraints, links to mixture and two-factor ANOVA chapters, and four question backlinks. The generator retains those. Its direct backlinks primarily ask other topics, so two focused answered questions are proposed for shared bank integration.
- **Checked:** Normal-sum model $Y\sim N(\theta_1+\theta_2,1)$ has one-observation score $(Y-s)(1,1)$ and information matrix of ones with eigenvalues 2 and 0.
- **Checked:** For $Y\sim\operatorname{Bernoulli}(\theta^2)$ at $\theta=\pm1/2$, both laws have success probability $1/4$. At $\theta=1/2$, information $4/(1-\theta^2)=16/3>0$ for one observation, illustrating local versus global identification under the regular interior point.
- **Checked:** The normal-mixture worked example with weight .3, means 0 and 2, unit component variances gives density $0.1574763607$ at 0 and $0.2954568862$ at 2; both remain the same after swapping weight to .7 and reversing the means.
- **Checked:** The two-level-factor practice triple $(10,-2,3)$ gives group means $(8,13)$, as do $(15,-7,-2)$ and reference-coded $(8,0,5)$. The identified contrast is 5.
- **Checked:** New bank questions use a smooth with intercept 2 and values $(-1,0,1)$, yielding predictors $(1,2,3)$; shifting to intercept 5 and values $(-4,-3,-2)$ preserves predictions. A product model with $(a,b)=(.2,.5)$ or $(.5,.2)$ gives Bernoulli probability .1 in both cases.

## Proof scope

The collapsed box proves the normal-sum information rank, mixture label symmetry and Bernoulli-square local/global counterexample. Teicher's finite-normal-mixture result and Rothenberg's full regular-point information criterion are logged in page-local pending proof records.
