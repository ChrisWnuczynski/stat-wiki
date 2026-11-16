# Outlier research notes

Page type: concept. Baseline: 471 words, zero figures. Generated baseline also includes a Tukey fence example for $2,3,3,4,5,6,7,8,20$, the 1.5 IQR rule, and distinctions among erroneous records, genuine tails and influence. Those are retained by the generator; the depth text extends them with calculations, a proof and diagnostic context.

## Sources opened

- NIST/SEMATECH e-Handbook, §1.3.5.17, “Detection of Outliers,” full online section, https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm. Checked: bad data versus genuine extremes; labeling, accommodation and identification; normality requirement for named tests; masking and swamping; bound on ordinary sample z-scores; graph-based diagnosis. The mean/std bound was rederived below.
- NIST/SEMATECH e-Handbook, §1.3.3.7, “Box Plot,” full online section, https://www.itl.nist.gov/div898/handbook/eda/section3/boxplot.htm. Checked: inner fences at 1.5 IQR and outer fences at 3 IQR, possible-outlier marking.
- Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 404, “Outlier,” local authorized page `/workspace/statwiki-sources/dodge2008/pages/pdf-0403.txt`. Checked: model-relative definition, historical account of Legendre and Peirce, controversy over deletion, and robust accommodation. Dodge's compressed historical summary is used as such; no original nineteenth-century paper was cited.

## Fact ledger

- **Checked:** Fences classify a point for further investigation; they do not establish measurement error. NIST §1.3.5.17; Dodge p. 404.
- **Checked:** For the baseline sample, hinges including the centre are 3 and 7, IQR 4, upper inner fence 13. Python arithmetic check in `checks/outlier.py`.
- **Checked:** With the usual sample standard deviation, the largest possible sample z-score magnitude is $(n-1)/\sqrt n$; the proof in the page shows why. NIST §1.3.5.17.
- **Checked:** The five-value example has $s=\sqrt{20}$ and maximum score $8/\sqrt{20}$. Python check.
- **Checked:** A normal-theory outlier test can misinterpret a nonnormal tail; NIST §1.3.5.17.
- **Assumed:** The illustrative delivery times are hypothetical; no empirical population claim is made.
- **Disputed:** The exact attribution of early rejection rules across nineteenth-century authors is historical and summarized by Dodge. The page attributes the account explicitly to Dodge rather than asserting independent archival verification.

## Question-bank gap

The existing bank has no outlier-specific answered item. `ex-inf-milk-summaries` computes quartiles but does not ask for a fence or assess a flagged observation; `ex-da-correlation-reading` asks about skewness and normality but not outlier diagnosis. Neither substantively tests this page. The embedded Your turn task covers a fence calculation. A pending shared change requests two bank questions with checked answers.

- **Checked:** NIST/SEMATECH e-Handbook §1.3.3.7, https://www.itl.nist.gov/div898/handbook/eda/section3/boxplot.htm, “Box plots with fences,” gives the 1.5 IQR outlier flag.
