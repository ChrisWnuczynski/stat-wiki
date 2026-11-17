## Motivating example
For the points $0,1,4,5$, one cluster has within-cluster sum of squares $17$, while splitting into $\{0,1\}$ and $\{4,5\}$ reduces it to one. More clusters can always improve an optimised training dispersion, even for unstructured data. The gap statistic asks whether that improvement exceeds the improvement expected under a specified reference geometry.{{cite:dai_shen_liu2026_cluster_significance}} (§4.2, eq. 12)

## Definition — Compare logarithmic dispersions
For candidate count $k$, let $W_k>0$ be the observed within-cluster dispersion and let $W^*_{kb}>0$ come from applying the same clustering procedure to reference dataset $b$. With $B$ independent reference datasets,
$$
\widehat{\operatorname{Gap}}(k)=\frac1B\sum_{b=1}^B\log W^*_{kb}-\log W_k.
$$
A larger value means that the observed clustering is tighter than its reference comparison on the logarithmic scale. The definition averages logs, rather than taking the log of an arithmetic mean. Equivalently it is the log ratio of the reference geometric mean to $W_k$.{{cite:vans_patil_sharma2021_feats}} (§ “Gap Statistic”, eqs. 2–3)

The reference is commonly uniform over a box in the input coordinates or over a box after a principal-component rotation. These choices encode different notions of unstructured data. Scaling features and changing the reference box can therefore change the selected count. A geometric criterion does not identify a unique scientifically meaningful population partition without further modelling choices.{{cite:dai_shen_liu2026_cluster_significance}} (§4.2){{cite:merigo_anfossi_chicco2026_gap}} (§2, Methods)

## Properties — The uncertainty allowance and stopping rule
Write $\overline\ell_k=B^{-1}\sum_b\log W^*_{kb}$ and
$$
\operatorname{sd}(k)=\left\{B^{-1}\sum_b(\log W^*_{kb}-\overline\ell_k)^2\right\}^{1/2},\qquad
s_k=\sqrt{1+1/B}\operatorname{sd}(k).
$$
Choose the smallest candidate $k$ for which $\widehat{\operatorname{Gap}}(k)\ge\widehat{\operatorname{Gap}}(k+1)-s_{k+1}$. This rule can select a smaller count than the maximiser of the gap. The displayed dispersion uses denominator $B$; replacing it by $B-1$ is a different finite-simulation convention.{{cite:vans_patil_sharma2021_feats}} (§ “Gap Statistic”, eqs. 4–5)

The allowance is not a conventional significance threshold at a chosen Type I error level. It measures variability under the chosen reference construction and enters a comparison across candidate counts. More simulation reduces uncertainty in the estimated reference mean but does not eliminate variability of an individual reference dispersion.{{cite:dai_shen_liu2026_cluster_significance}} (§4.2)

## Worked example — A maximum need not be selected
Suppose the gaps for counts one through five are $(0.30,0.70,1.10,1.15,1.00)$ and their allowances are $(0.05,0.05,0.06,0.06,0.07)$. At one, $0.30<0.70-0.05$; at two, $0.70<1.10-0.06$; at three, $1.10\ge1.15-0.06$. The rule selects three, although the largest gap occurs at four.

For a separate fixed-count calculation, take four reference log dispersions $2.2,2.3,2.4,2.5$ and observed log dispersion $1.5$. Their mean is $2.35$, giving gap $0.85$. Their denominator-four standard deviation is $0.111803$, and the adjusted allowance is $0.125$. These calculations isolate the arithmetic from the choice of clustering algorithm and reference distribution.{{cite:vans_patil_sharma2021_feats}} (§ “Gap Statistic”)

**Your turn.** Keep these four reference values and increase the observed log dispersion from $1.5$ to $1.8$. What changes?

::: {.callout-tip collapse="true" title="Answer"}
The gap falls from $0.85$ to $0.55$. The reference standard deviation and allowance remain $0.111803$ and $0.125$, since the reference replicates have not changed.
:::

## Assumptions and limits — Optimisation and the candidate range
For globally minimised within-cluster sum of squares, splitting a cluster cannot increase the optimum: the finer partition can use the same centre in both pieces. Separate local optimisation runs need not achieve this monotonicity. At $k=n$, singleton clusters have zero dispersion, so its logarithm is undefined. The candidate range and numerical handling must keep every logged dispersion positive. These restrictions follow from the objective and logarithm, rather than from a guarantee that a selected count equals a true number of groups.{{cite:dai_shen_liu2026_cluster_significance}} (§1, clustering optimisation; §4.2)

