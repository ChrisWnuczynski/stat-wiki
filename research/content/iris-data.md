## Motivating example
An iris flower has four recorded dimensions, and its species is known for this collection. The table is small enough to inspect yet rich enough to show why a pooled covariance, a cluster found without labels and a supervised species classifier answer different questions. A clean pattern in these rows is an invitation to test a method, not evidence that every new flower will follow the same rule.{{cite:r_iris_doc2026}} (Description, Format and Examples)

## Intuition
The unit of observation is a flower. Sepal length, sepal width, petal length and petal width are measured in centimetres; `Species` is a categorical label with three values. The familiar rectangular `iris` data frame has $150$ rows and five columns, with $50$ flowers in each species. Because the classes are balanced *in this table*, a naive overall accuracy can conceal which species were confused. The companion `iris3` object rearranges the same measurements as a $50\times4\times3$ array, retaining the species grouping rather than adding new observations.{{cite:r_iris_doc2026}} (Description and Format)

## Interpretation — What the measurements separate
The covariance and mean calculations show two forms of structure. Setosa has mean petal length $1.462$ cm, while versicolor and virginica have means $4.260$ and $5.552$ cm. Yet a large pooled covariance can be created by differences between species means, even when within-species covariance is small. Thus an overall association between two flower measurements need not describe the relation among flowers of a single species. The decomposition makes that distinction mathematical.{{cite:r_iris_doc2026}} (Format and Examples)

## Properties — A pooled covariance has two parts
If $G$ is species and $X$ is a vector of flower measurements, the pooled covariance equals the mean within-species covariance plus the covariance of species mean vectors. The second term can be large when species centres are far apart. A PCA of all $150$ measurements therefore describes variation in this assembled table, including between-species differences; a PCA within setosa describes a different population of rows. This is why the group definition belongs before a covariance interpretation.{{cite:r_iris_doc2026}} (Description and Examples)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $m=E(X)$ and $m_G=E(X\mid G)$. Since $X-m=(X-m_G)+(m_G-m)$, expand $(X-m)(X-m)^\top$. Conditional on $G$, the cross terms vanish because $E(X-m_G\mid G)=0$. Taking expectations leaves $E\{\operatorname{Cov}(X\mid G)\}+E\{(m_G-m)(m_G-m)^\top\}$, and the final term is $\operatorname{Cov}\{E(X\mid G)\}$. The identity requires finite second moments but no Gaussian assumption.
:::
:::

## Statistical use — Labels and evaluation
When fitting a supervised classifier, `Species` is the response and the four dimensions are predictors. A train/test split must keep the test labels outside every fitting and tuning step, including scaling and dimension reduction. When fitting an unsupervised cluster or mixture, the labels should likewise stay out of the fit if agreement with species is to be an external description. The clustering table does that and finds a clean setosa cluster but mixes versicolor with virginica. Relabelling clusters to match species after fitting helps describe the table; it does not convert the fitted groups into a validated prediction rule.{{cite:r_iris_doc2026}} (Format and Examples)

The data represent measured flowers associated with Anderson's collection, with no documented probability sampling design for all irises. They are useful for seeing methods disagree, but a random split of these $150$ rows estimates performance only for data resembling this collection. If a new survey has different locations, instruments or species frequencies, a classifier can fail even when it classifies all recorded setosa flowers correctly. A method that assumes a single Gaussian distribution for the pooled rows also treats three species centres as one cloud, contrary to the observed grouping.{{cite:r_iris_doc2026}} (Source and Description)

## Worked example
In the recorded table, setosa petal lengths range from $1.0$ to $1.9$ cm; the smallest versicolor petal length is $3.0$ cm and the smallest virginica length is $4.5$ cm. A rule that calls a flower setosa when petal length is below $2.0$ cm labels all $50$ setosa rows and none of the other $100$ rows as setosa. Its *apparent* binary accuracy on this table is therefore $150/150=100\%$. The gap is striking, but choosing the threshold after inspecting these same rows makes the apparent accuracy a poor estimate of future error.{{cite:r_iris_doc2026}} (Description and Format)

**Your turn.** Using the species means printed above, find the versicolor-minus-setosa and virginica-minus-versicolor differences in mean petal length. Which gap is larger?

::: {.callout-tip collapse="true" title="Answer"}
The first gap is $4.260-1.462=2.798$ cm. The second is $5.552-4.260=1.292$ cm. The setosa-to-versicolor gap is larger; neither difference alone determines how much the species distributions overlap.
:::

## Common misconceptions
An unsupervised fit that later agrees with species labels did not predict those labels: the comparison is made on the same flowers. A high apparent separation does not imply zero error on a new collection, especially after a cutoff was selected using the full data. Equal numbers of the three species in `iris` are a feature of this teaching table, not evidence of equal prevalence in nature. Finally, clustering components need not carry stable species names: exchanging numeric cluster labels leaves the partition unchanged.{{cite:r_iris_doc2026}} (Format and Examples)

## Connections
[Principal components as a modelling step](../questions/ex-sl-03-7.qmd) asks what scaling does before classifying irises. [The fitted LDA model](../questions/ex-sl-08-7.qmd) makes the species labels part of a supervised fit. [A label that was not in the fit](../questions/ex-ur-held-out-label.qmd) asks what an unlabeled mixture's agreement with species can and cannot establish. These are three distinct roles for the same table.{{cite:r_iris_doc2026}} (Format and Examples)

## History
The R documentation credits Edgar Anderson with collecting the data and names his 1935 account of the Gaspé Peninsula irises. Fisher's 1936 paper then used multiple flower measurements to study species discrimination. The common phrase “Fisher's iris data” reflects the later analysis; “Anderson's iris data” records who collected the measurements.{{cite:fisher1936}} (§§I–II, p. 179)
