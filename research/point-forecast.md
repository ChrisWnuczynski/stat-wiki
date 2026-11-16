# Point forecast

Rank 188. Type: Concept. Frozen baseline: 475 body words, no figures; generated baseline retained the AR(1) example and the random-walk contrast. The existing forecast chapter supplies two question links and no figure on this article.

## Checked

- **Checked in full source:** Dodge (2008), printed pp. 206–207, “Forecasting”, distinguishes secular trend, cyclic, seasonal and irregular terms and discusses their use at different horizons. The extracted pages were read from `/workspace/statwiki-sources/dodge2008/pages/pdf-0209.txt` and `pdf-0210.txt`. It supports the historical and horizon passages, not the squared-error theorem.
- **Checked in the repository's original course chapter:** `sources/book/chapters/11-forecasting.qmd`, lines 1–79, supplies the existing ARIMA context, the USAccDeaths example, and the original point forecast prose. The shared forecast chapter now distinguishes information-criterion selection from autocorrelation-plot diagnosis.
- **Checked mathematically:** The conditional squared-error identity, AR(1) iterated forecast and variance, random-walk limit, and absolute-loss median property are proved in the article. Python calculation in `checks/point-forecast.py` checks all printed numerical results in the AR(1), interval, and bank exercises.
- **Assumed:** The worked autoregression has fixed known parameters and independent innovations. The 95% interval additionally assumes Gaussian innovations. The out-of-sample assessment description assumes forecasts are formed with only information available at each origin.
- **Disputed:** A point forecast is usually a conditional mean only under squared-error loss. Absolute-error or asymmetric costs change the optimal summary. The unqualified inherited statement that interval width always grows with horizon is too broad; the article gives concrete model-dependent cases.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 206–207, “Forecasting”; existing key `dodge2008`. The full entry was opened, not only an index or publisher description.
- The repository's original *Forecasting* course chapter was read to preserve existing material. Unlocated Box–Jenkins and Hyndman citations on the source lead were removed in the citation audit; the point-forecast mathematics is proved on the page.

## Changes

The page gains motivation, precise target and loss definitions, one collapsed proof, interpretation, use, a numerical worked example and hidden practice, distinct misconceptions, concrete failures, connections, and source-located history. Two fully answered point-forecast questions are pending for integration into the shared bank. The shared chapter correction was applied; the single-sentence lead amendment remains recorded separately. No figures were added or removed.
