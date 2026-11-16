# Null deviance

Rank 350. Lighter tier. Concept page.

## Facts checked

- R documentation for `glm`, the `null.deviance` and `df.null` entries: null deviance is the deviance of the null model, and `df.null` is that model's residual degrees of freedom. The null model includes an intercept when the fitted model does.
- Bernoulli saturated contribution is \(0\) for \(y\in\{0,1\}\) under \(0\log 0=0\).
- Observations \(1,1,0,1\): \(\hat p=3/4\), \(D_0=-2(3\log(3/4)+\log(1/4))\approx 4.498681\), printed \(4.4987\). Null degrees of freedom \(3\).
- The illustrative residual deviance \(1.4987\) was chosen so the drop is exactly \(3\) on \(1\) degree of freedom. It is not a fit to an external data set.
- Label swap \(1,0,0,0\) gives the same deviance. Five observations with four ones: \(\hat p=4/5\), `df.null` \(=4\).

## Assumed

- The deviance definition \(2(\ell_{\mathrm{sat}}-\ell_{\mathrm{model}})\) is the one used by the binomial calculations. R's value is that number for the null model.

## Disputed

- None.

## Not opened

- McCullagh and Nelder was not opened. The cholesterol `glm` printout on the page was not refit, because `data/cholest.csv` is not in the tree. No new claim uses those printed deviances.
