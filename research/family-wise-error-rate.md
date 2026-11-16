# Family-wise error rate — research record

## Sources opened

- Benjamini and Hochberg (1995), full original paper, author-hosted at Tel Aviv University, pp. 289–295, especially Introduction, §2 table and §3.1. The original contrasts family-wise control with FDR and gives the $V,R$ notation and Bonferroni threshold.
- NIST/SEMATECH e-Handbook, full official §7.4.7.3, Bonferroni's method, including union inequality and simultaneous interval interpretation.
- Dodge (2008), authorized local Bonferroni biography, printed pp. 50–51, including the 1936 inequality history.
- Baseline article: 280 words, zero figures; original studentized-range paragraph and question links preserved.

## Claim ledger

- **Checked:** FWER is $P(V\ge1)$ for false rejection count $V$; strong control covers any configuration of true and false nulls (Benjamini–Hochberg 1995 pp. 289–291).
- **Checked:** Testing $m$ valid null p-values at $\alpha/m$ controls FWER at $\alpha$ by the union bound without independence (same source p. 291; NIST §7.4.7.3).
- **Checked by code:** For ten independent true nulls tested at .05, FWER is $1-.95^{10}\approx.4013$; at .005 it is $1-.995^{10}\approx.0489$. Four-test and Your turn decisions are checked in `checks/family-wise-error-rate.py`.
- **Checked:** FDR is $E[V/\max(R,1)]$, and under the complete null it equals FWER, but otherwise the criteria differ (Benjamini–Hochberg 1995 §§1–2).
- **Checked:** Dodge pp. 50–51 attributes two dependence inequalities to Bonferroni's 1936 paper. The modern multiple-testing use follows from one inequality; the article does not imply he coined FWER.
- **Assumed:** Synthetic independent-null and p-value examples illustrate operating characteristics, not observed study results.
- **Disputed/qualified:** Stock `topics.py` says FWER control with thousands of tests leaves almost no power; this is not universal. Power depends on effect sizes, dependence, procedure, and family definition. Request a qualified replacement in pending shared changes.
