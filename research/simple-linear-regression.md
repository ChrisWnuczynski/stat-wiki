# Simple linear regression

Type: Concept/definition. Rank 219. Tier: full.

## Material checked

- **Checked:** Baseline 1,101 words and 2 figures (the father–son scatter and the heart–oxygen figure). The source definition, advertising table, melanoma table and sampling statements stay in the generated page. The added prose uses a separate five-seedling calculation.
- **Checked:** NIST/SEMATECH Handbook 151, §4.1.4.1, defines a model that is linear in its parameters, names the least-squares criterion, records Gauss, Legendre and possibly Adrain, and warns about extrapolation and outliers. §4.4.3.1 minimises $Q$, derives the straight-line estimators, notes that the intercept estimator depends on the slope estimator unless $\bar x=0$, and estimates the error standard deviation by $\sqrt{Q/(n-p)}$.
- **Checked:** Dodge printed p. 304 states the least-squares criterion and attributes the method's introduction to Legendre (1805). Printed p. 305 writes the straight-line model, the two partial derivatives, and the normal equations.
- **Checked by code:** seedling means $6$ and $7$, $S_{xx}=40$, $S_{xy}=42$, slope $1.05$, intercept $0.70$, residual sum $1.90$, $\sqrt{19/30}\approx 0.7958$, $\sqrt{19/1200}\approx 0.1258$, fitted value $8.05$ at $7$ hours. Changing the last response to $20$ gives slope $1.95$ and intercept $-2.90$. The three-point practice line has slope $0.5$, intercept $1.5$ and residual sum $1.5$.
- **Assumed:** Unbiasedness uses a correct straight mean and fixed inputs. The variance $\sigma^2/S_{xx}$ adds uncorrelated, equal-variance errors. A $t_{n-2}$ law is not claimed in the added proof; it needs normality as well.
- **Disputed:** Dodge names Legendre (1805) as introducing least squares. NIST records independent work by Gauss, Legendre and possibly Adrain. The article reports both and does not pick a single inventor.

## Sources opened and used

1. NIST/SEMATECH e-Handbook of Statistical Methods, §4.1.4.1, `https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm`. New pending key `nist_linear_model2002`.
2. NIST/SEMATECH e-Handbook of Statistical Methods, §4.4.3.1, `https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm`. New pending key `nist_ls_straight2002`.
3. Yadolah Dodge, *The Concise Encyclopedia of Statistics*, 2008, printed pp. 304–305. Existing key `dodge2008`.

## Skipped

No new claim about the $t_{n-2}$ law was added, because Fox's regression chapter was not opened in this pass. The normal-equation algebra on Dodge p. 305 was readable and is cited; the later numerical ANOVA fragment on the facing page was not used.
