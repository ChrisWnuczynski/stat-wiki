## Lead context

A shop's receipts are a list of baskets, and the question is which sets of items appear together often enough to matter. The Apriori algorithm lists those sets without enumerating every subset of the catalogue. It uses one fact: adding an item to a set can only lose baskets, never gain them, so any set with an infrequent subset can be skipped.{{cite:hastie_esl2009}} (pp. 489–490, §14.2.2){{cite:agrawal_srikant1994}} (§1)

## Motivating example

Four baskets are $\{a,b\}$, $\{a,b\}$, $\{a\}$ and $\{b,c\}$. Item $a$ appears in three baskets, $b$ in three, and $c$ in one. The pair $\{a,b\}$ appears in two. If a set must appear in more than two-fifths of the baskets to be worth keeping, then $c$ is discarded at the first pass and every pair that contains $c$ is discarded with it. The pair $\{a,b\}$ survives. The listing never builds the triple $\{a,b,c\}$, because that triple contains $c$.{{cite:hastie_esl2009}} (pp. 489–490){{cite:agrawal_srikant1994}} (§2.1)

## Intuition

Support is a count of baskets. The frequent sets are closed under taking subsets: every subset of a frequent set is frequent, and equivalently a set whose support clears the threshold has no infrequent subset. Agrawal and Srikant use that fact to generate candidates. The first pass counts the single items and throws away the rare ones. Each later pass builds candidates of size $k$ only from frequent sets of size $k-1$, and it deletes any candidate that still contains an infrequent subset. The data are read once per size of set. That schedule is the point when the receipt file does not fit in memory.{{cite:agrawal_srikant1994}} (§2.1){{cite:hastie_esl2009}} (p. 490)

## Definition

Let each transaction be a subset of a catalogue of items. An item set $K$ has support $T(K)$ equal to the fraction of transactions that contain every member of $K$. Given a threshold $t$, the frequent item sets are those with $T(K)>t$, in the strict form used by Hastie, Tibshirani, and Friedman; Agrawal and Srikant state the same cut as a minimum percentage of transactions. The monotonicity is $L\subseteq K \Rightarrow T(L)\ge T(K)$.{{cite:hastie_esl2009}} (pp. 488–490, §14.2.2){{cite:agrawal_srikant1994}} (§1)

A rule $X\Rightarrow Y$, with $X$ and $Y$ disjoint, has support equal to the fraction of transactions that contain $X\cup Y$, and confidence equal to that support divided by the support of $X$. In the original shopping formulation those two quantities are stated as percentages: support $s$ means $s$ percent of transactions contain the union, and confidence $c$ means $c$ percent of the transactions that contain $X$ also contain $Y$. The mining task is to list every rule whose support and confidence clear two user thresholds. The work factors into finding the frequent item sets, and then splitting each frequent item set into a rule. From a frequent item set $K=A\cup B$, the rule $A\Rightarrow B$ has support $T(K)$ and confidence $T(K)/T(A)$. The lift is that confidence divided by $T(B)$, an estimate of $\Pr(A\text{ and }B)/(\Pr(A)\Pr(B))$.{{cite:agrawal_srikant1994}} (§1){{cite:hastie_esl2009}} (pp. 490–491, (14.7)–(14.8))

## Statistical use

In the four baskets, $T(\{a\})=3/4$, $T(\{b\})=3/4$, $T(\{c\})=1/4$ and $T(\{a,b\})=1/2$. The confidence of $a\Rightarrow b$ is $(1/2)/(3/4)=2/3$. The lift of $a\Rightarrow b$ is $(2/3)/(3/4)=8/9$, which is less than $1$: in these baskets $a$ and $b$ occur together a little less often than the product of their separate supports, because $b$ is already common. The support of $\{b,c\}$ is $1/4$. With threshold $t=2/5$, the singles $a$ and $b$ pass and $c$ fails, since $1/4$ is not greater than $2/5$. The only pair whose subsets all pass is $\{a,b\}$, and its support $1/2$ is above $2/5$. No set of size three is a candidate.{{cite:hastie_esl2009}} (p. 490){{cite:agrawal_srikant1994}} (§2.1)

There are $2^{|K|-1}-1$ nontrivial rules inside an item set of size $|K|$, one for each nonempty proper antecedent. A second threshold on confidence selects among them after the frequent item sets are known. The threshold $t$ is the computational switch. Lower it, and the number of frequent sets can grow until the passes no longer finish. A rule with high confidence and tiny support is invisible to a high threshold, because support is applied before confidence. The lists are a tool for large binary tables: which goods are bought together, which codes co-occur. A reported rule is a pair of counts. Focusing on one consequent, such as every frequent antecedent of a particular item, turns the list into a supervised question about that item.{{cite:hastie_esl2009}} (pp. 487–492)

Market-basket files of the size contemplated in the original algorithms, with catalogues large enough that a method must read the file once per item-set size, are why the monotonicity was the contribution. Sparse baskets and a high threshold are the regime in which the passes finish. The fraction $T(K)$ on a huge receipt file can be precise and still may not be the quantity a shop should act on; the algorithm returns the counts, and the decision that uses them is a further step.{{cite:agrawal_srikant1994}} (§1–§2.1){{cite:hastie_esl2009}} (pp. 489–492)

## Worked example

Baskets $\{a,b\}$, $\{a,b\}$, $\{a\}$, $\{b,c\}$. Then $T(\{a,b\})=2/4=1/2$ and $T(\{a\})=3/4$, so the confidence of $a\Rightarrow b$ is $2/3$. Since $T(\{b\})=3/4$, the lift is $8/9$. The pair $\{b,c\}$ has support $1/4$. At the strict threshold $2/5$, Apriori keeps $\{a\}$, $\{b\}$ and $\{a,b\}$, and it does not count any set that contains $c$.

**Your turn.** What is the support of $\{b,c\}$, and does that pair survive a strict threshold of $2/5$?

::: {.callout-tip collapse="true" title="Answer"}
The support is $1/4$. Because $1/4$ is not greater than $2/5$, the pair does not survive.
:::

## Common misconceptions

A high confidence is not a high support. Confidence is a conditional fraction among baskets that contain the antecedent. Support is the fraction of all baskets that contain the pair. The rule $a\Rightarrow b$ can be confident because $a$ is rare and almost always brings $b$, while the pair itself is almost absent. The threshold on support drops that rule before confidence is considered.{{cite:hastie_esl2009}} (p. 492)

Lift equal to $8/9$ compares the conditional frequency with the marginal frequency in these four baskets. A fifth basket would change it. The algorithm does not search arbitrary regions of a continuous feature space. The tractable case codes each item as present or absent, or replaces a categorical variable by indicators, and then looks only at conjunctions of those bits.{{cite:hastie_esl2009}} (pp. 488–491)

The derivation treats transactions as the units and support as a fraction of those units. It does not by itself provide a sampling error for $T(K)$. With a small file, $2/3$ and $8/9$ move when one basket is added. If too many singles pass the threshold, the pair pass is already a large counting problem.{{cite:agrawal_srikant1994}} (§1){{cite:hastie_esl2009}} (pp. 488–492)

## Connections

Apriori is an [unsupervised learning](unsupervised-learning.qmd) method for binary tables, alongside [cluster analysis](cluster-analysis.qmd) and [dimensionality reduction](dimensionality-reduction.qmd), which summarise rows and directions rather than item sets. Asking for the antecedents of one fixed item is close to [classification](classification.qmd) of that item. The procedure is one of the tools associated with [data mining](data-mining.qmd) on commercial databases. The shopping version of the association rule, with support and confidence as percentages of transactions, and the candidate generation that builds item sets from frequent subsets, are the 1994 formulation. The same monotonicity, the pass-by-size schedule, and the definitions of confidence and lift are how the algorithm is stated in the account of mining large commercial tables.{{cite:agrawal_srikant1994}} (§1–§2.1){{cite:hastie_esl2009}} (pp. 486–492)
