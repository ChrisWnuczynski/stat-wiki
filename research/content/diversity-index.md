## Lead context
A woodland sample contains many oaks and one rare shrub. Counting the species says the wood is richer than a plantation of oaks alone, and it treats the shrub as equal to the oaks. A diversity index is a single number that uses both the number of classes and the way individuals are divided among those classes.

## Motivating example
Ten trees fall into three species, with counts 6, 3, and 1. Species richness is 3. That number would be the same for counts 4, 4, and 2, or for 8, 1, and 1. A visitor who cares whether the wood is mostly one species needs a summary that moves when the counts become more equal. Simpson's concentration does that: it is large when two individuals drawn at random are likely to be the same species, and small when they are likely to differ.{{cite:simpson1949}} (30 April 1949){{cite:peet1974}} (section "Simpson's Index")

## Intuition
Draw two individuals independently from a very large population. The chance they belong to the same class is high when one class dominates, and it is as small as the number of classes allows when the classes are equal. That chance is a concentration. Diversity, in the sense of evenness mixed with richness, runs in the other direction: many equal classes make the chance of a match small. The indices used in ecology are functions of this chance, or of the entropy of the same proportions.{{cite:simpson1949}} (30 April 1949){{cite:peet1974}} (section "Heterogeneity indices")

## Definition
Consider an infinite population whose individuals fall into \(Z\) classes, with proportions \(p_1,\ldots,p_Z\) that sum to 1. Simpson's concentration is
\[
\lambda=\sum_{i=1}^{Z} p_i^2.
\]
It lies between \(1/Z\) and 1. The value 1 means every individual is in a single class. The value \(1/Z\) means the classes are equal, which is the most even division possible for that number of classes. The same \(\lambda\) is the probability that two individuals drawn at random and independently are in the same class.{{cite:simpson1949}} (30 April 1949)

In a finite sample of size \(N\) with counts \(n_i\),
\[
\ell=\frac{\sum_i n_i(n_i-1)}{N(N-1)}
\]
is an unbiased estimator of \(\lambda\). The numerator counts pairs that fall inside one class, and the denominator counts all pairs. Ecologists often report a diversity form that runs the other way, \(1-\lambda\), or the reciprocal \(1/\lambda\). The reciprocal can be read as the number of equally common species that would give the same concentration.{{cite:simpson1949}} (30 April 1949){{cite:peet1974}} (section "Simpson's Index")

## Properties
Richness \(Z\) and evenness are different components. \(\lambda\) uses both, and a single number cannot be decomposed back into them without more information. For fixed \(Z\), \(\lambda\) is minimised when the \(p_i\) are equal. Adding a rare class changes \(\lambda\) only a little, because a small \(p_i\) contributes \(p_i^2\), which is smaller still. The sample estimator \(\ell\) is not the plug-in \(\sum (n_i/N)^2\); the factor \(n_i(n_i-1)\) corrects the finite-sample bias of that plug-in for \(\lambda\).{{cite:simpson1949}} (30 April 1949){{cite:peet1974}} (section "Simpson's Index")

Peet records the heterogeneity reading used in ecology: a diversity measure of this family should respond to the number of species and to the distribution of individuals among them. There is no single index that every study must use. Species richness, \(\lambda\), \(1-\lambda\), and the Shannon function answer different questions, and a paper has to say which one it computed.{{cite:peet1974}} (introduction; section "Simpson's Index")

## Statistical use
Community ecology uses the indices to compare sites, treatments, or years. The classification has to be fixed first: species, genus, or some other partition. Individuals in a class are treated as equivalent, and classes are treated as equally different, which is a modelling choice. Sampling needs to match the spatial pattern of the organisms; a sample piled into one patch estimates the patch. In genetics the reciprocal of \(\lambda\) has been used as an effective number of alleles. The same algebra appears as a concentration index in economics, where large shares play the role of abundant species.{{cite:peet1974}} (section "Assumptions and data"; section "Simpson's Index")

The income Gini coefficient is a different construction, based on the area between the Lorenz curve and the line of equality. It is also a concentration measure, and it is a different formula from Simpson's \(\lambda\). Reporting one under the other's name mixes an income inequality with a probability of a matching pair.{{cite:dodge2008}} (p. 231)

## Worked example
Counts are 6, 3, and 1, so \(N=10\) and the proportions are \(0.6\), \(0.3\), and \(0.1\). Then
\[
\lambda=0.6^2+0.3^2+0.1^2=0.36+0.09+0.01=0.46.
\]
The unbiased sample form is
\[
\ell=\frac{6\cdot 5+3\cdot 2+1\cdot 0}{10\cdot 9}=\frac{30+6}{90}=\frac{36}{90}=0.4.
\]
The plug-in \(0.46\) and the unbiased estimator \(0.4\) are not the same number. Both describe these ten individuals; \(\lambda\) is the population concentration they estimate.{{cite:simpson1949}} (30 April 1949)

**Your turn.** Ten individuals are split evenly between two classes, five and five. What is \(\lambda\)?

::: {.callout-tip collapse="true" title="Answer"}
The proportions are \(1/2\) and \(1/2\), so \(\lambda=(1/2)^2+(1/2)^2=1/2\).
:::

## Common misconceptions
Species richness is not a diversity index of the heterogeneity kind. Two communities with the same number of species can have very different \(\lambda\). A larger \(\lambda\) means more concentration, which is less diversity in the evenness sense; \(1-\lambda\) is the form that rises as the community becomes more mixed. The Gini coefficient of income is not this index. And \(\ell\) is not defined for a sample of size 0 or 1, because there are no pairs.{{cite:peet1974}} (section "Simpson's Index"){{cite:simpson1949}} (30 April 1949){{cite:dodge2008}} (p. 231)

## Assumptions and limits
The population formula assumes an infinite population and independent draws. The sample formula assumes a random sample from that population and drops samples of size 0 or 1 when the size itself is random. Every individual is assigned to one class. If the classification is arbitrary, the index inherits the arbitrariness. Spatial clustering means a convenience sample can look less diverse than the region. No index repairs a species concept that splits or lumps taxa differently in the two samples being compared.{{cite:simpson1949}} (30 April 1949){{cite:peet1974}} (section "Assumptions and data")

## Connections
The [Gini index](gini-index.qmd) used to split a classification tree is an impurity, \(1-\sum p_i^2\), which is the complement of Simpson's concentration for a discrete distribution on the classes at a node. The income Gini coefficient uses the Lorenz curve instead, and answers a question about inequality of a size variable.{{cite:dodge2008}} (p. 231){{cite:peet1974}} (section "Simpson's Index") A [multinomial distribution](multinomial-distribution.qmd) is the sampling scheme behind the counts \(n_i\) when individuals are drawn independently into a fixed set of classes.

## History
Yule and Fisher, Corbet, and Williams had already proposed sample statistics of concentration and of diversity, tied to particular frequency distributions. Simpson's 1949 letter defined a population concentration \(\lambda=\sum p_i^2\), interpretable as the probability that two randomly drawn individuals match, and gave the unbiased pair-count estimator for a sample. Ecological reviews in the following decades treated that index as the first of the heterogeneity measures, and recorded the later habits of reporting \(1-\lambda\) or \(1/\lambda\) so that the number rises as the community becomes more even.{{cite:simpson1949}} (30 April 1949){{cite:peet1974}} (section "Simpson's Index")

