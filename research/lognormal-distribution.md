# Lognormal distribution — rank 160

Type: distribution. Baseline 668 words and two figures. Keep both plotted curves, infobox parameters and values, source GLM context until its parent source is resegmented, the original numerical example, and all three question backlinks.

## Sources opened

- Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §5.12, full open author textbook page (Definition, Distribution Functions, Moments, Related Distributions). Read the density Jacobian, normal-log CDF and quantiles, raw moments, right-tail warning, and products of independent lognormal variables.
- Dodge (2008), printed p. 321, lognormal entry, including transformation, mean/variance and history of Galton and McAlister 1879 and Kapteyn's later work. The entry's loose claims that lognormal is an approximation to a normal distribution or that listed applications all follow it exactly are not repeated.
- Generated source chapter `03-gamma-and-quasi.qmd`, positive-response paragraph, inspected for misplaced extraction. Existing source paragraph discusses family/link selection, not the lognormal law specifically.

## Fact ledger

- **Checked:** `log X~N(μ,σ²)` implies the infobox density, CDF, median, mode, mean and variance via change of variables and normal exponential moments (Siegrist §5.12; Dodge p. 321). A single complete proof is supplied.
- **Checked:** All real power moments are finite, while `E(exp(tX))=∞` for each positive `t` (Siegrist §5.12, Moments); proof uses the exponent's large-`y` behaviour.
- **Checked:** Products of independent lognormal variables are lognormal because their logarithms add independently as normals (Siegrist §5.12, Related Distributions). Independence condition is explicit.
- **Checked:** Worked log-scale-normal model with median 100, log SD 0.4 has mean 108.33, mode 85.21, 90th percentile 166.97, and probability over 150 about 0.1554; SciPy numeric check. Your-turn model with median 50 and log SD .2 is checked similarly.
- **Checked:** Dodge p. 321 attributes early lognormal work to Galton and McAlister in 1879 and later graphical parameter estimation to Kapteyn and van Uven. The original 1879 papers were not opened, so history cites Dodge specifically and makes no technical claim about their proofs.
- **Assumed:** The lognormal model is a plausible candidate for multiplicative positive measurements; data must still be checked for log-scale normality.
- **Disputed:** Existing extracted paragraph is unrelated to the distribution's definition and has an orphan antecedent. Request a paragraph segmentation in the source chapter and keep the full paragraph on its own GLM page.

## Arithmetic

`checks/lognormal-distribution.py` checks each new and inherited printed numeric result with SciPy, lognormal infobox expressions through SymPy, figure count and question links.
