# Repeated measures — rank 167

Type: concept. Baseline 181 words, zero figures. Preserve the same-unit definition, mixed/marginal links, tree competition example, and the toenail application link.

## Sources opened

- Schober and Vetter (2018), full open-access article *Repeated Measures Designs and Analysis of Longitudinal Data*, *Anesthesia & Analgesia* 127:569–575, pp. 569–573: repeated observations, subject as cluster, paired test, summary statistics, repeated-measures ANOVA, GEE and mixed models, working covariance, missing-data caution and history of approaches.
- Bates, Mächler, Bolker and Walker (2015), full author-hosted published-paper manuscript *Fitting Linear Mixed-Effects Models Using lme4*, pp. 1–4 §§1–1.2: conditional/marginal covariance, fixed/random terms, longitudinal sleepstudy example. Original article DOI 10.18637/jss.v067.i01.
- Bell, Kenward, Fairclough and Horton (2013), full open-access *BMJ* article *Differential dropout and bias in randomised controlled trials*, section “Statistical analysis: what works and what does not work”: mixed-model inference under missing at random versus nonignorable dropout.
- Dodge (2008) index checked for “Repeated Measures”; no dedicated entry. No Dodge claim is cited.

## Fact ledger

- **Checked:** Same-subject measurements share a sampling unit; treating all occasions as independent distorts uncertainty (Schober & Vetter pp. 569–570). Repeated-measures ANOVA, summary statistics, GEE and mixed models answer related but different questions (pp. 570–573).
- **Checked:** Random-intercept covariance and equicorrelation lower bound follow from direct covariance/eigenvalue calculation in the page proof. All example numbers checked by focused script.
- **Checked:** The existing example of two trees in the same soil may exhibit positive dependence from shared conditions or negative dependence through competition; the page distinguishes that from the nonnegative random-intercept covariance restriction.
- **Assumed:** Different subjects are independent, and random intercepts and occasion errors are mutually independent with constant variances in the illustrative model.
- **Disputed:** Positive within-unit correlation is common but not universal. Negative equicorrelation requires $\rho\ge-1/(m-1)$ for a valid $m$-occasion covariance, so the random-intercept model cannot represent every pattern. Dropout depending on unobserved outcomes is not solved automatically by a mixed model.
