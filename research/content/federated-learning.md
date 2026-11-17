

## Lead context

A phone, a hospital, or a sensor can collect the records a model needs and still be a bad place to empty those records into one warehouse. Federated learning trains the shared model by moving updates, not the records.{{cite:mcmahan2017}} (p. 1) {{cite:li_sahu_talwalkar_smith2019}} (p. 1)

## Motivating example

Two clinics measure the same outcome. The first has two cases, values $1$ and $3$, so its local mean is $2$. The second has one case, value $10$, so its local mean is $10$. The mean of all three cases is $(1+3+10)/3=14/3$. The unweighted mean of the two local means is $(2+10)/2=6$. The gap is $6-14/3=4/3$. A server that averages client summaries as if the clinics were the same size has answered a different question from the pooled sample. The records never left the clinics. The arithmetic of the average still has to know how many records each clinic held.{{cite:mcmahan2017}} (pp. 1–2) {{cite:li_sahu_talwalkar_smith2019}} (p. 1)

## Intuition

Each client keeps its own sample and computes a step that would improve the current shared model on that sample. The server collects those steps, or the updated local models, and folds them into the next shared model. The communication is the scarce resource: the records are large or sensitive, and the update is smaller. The samples are not a random split of one well-mixed file. One phone's typing is not another phone's typing, and one clinic may contribute a handful of cases while another contributes thousands.{{cite:mcmahan2017}} (pp. 1–2) {{cite:li_sahu_talwalkar_smith2019}} (p. 1)

## Definition

Federated learning trains a statistical model from data that remain on the remote devices or in the separate sites that collected them. A central coordinator sends out the current model. A subset of clients updates it on local data and returns the update. The coordinator incorporates the updates and repeats. The local training sets are not uploaded.{{cite:mcmahan2017}} (p. 1) {{cite:li_sahu_talwalkar_smith2019}} (p. 1)

The setting was introduced for mobile devices coordinated by a server, under the name of a loose federation of clients. The problems for which it is aimed have three features: the real on-device data are more useful than a proxy data set sitting in a data centre; those data are private or large, so copying them for the sake of training is unattractive; and, for a supervised task, the label can be read off the user's own interaction with the device.{{cite:mcmahan2017}} (pp. 1–2)

The optimisation problem inside that protocol is not ordinary distributed optimisation on a cluster. The local samples are typically not identically distributed, the clients are unbalanced, and communication dominates the cost. The Federated Averaging procedure runs local stochastic gradient steps on each selected client and averages the resulting models at the server.{{cite:mcmahan2017}} (pp. 1–2)

The protocol is a way to fit a shared predictor, such as a next-word model on phones, when centralising the text is both a privacy risk and a heavy transfer. Each round, some devices train locally on their own, non-identical data and return an update; the server returns a new global model. [Supervised learning](supervised-learning.qmd) is still the learning problem on each device when the device can form its own labels. The federation changes where the fit is computed and how the fits are merged.{{cite:li_sahu_talwalkar_smith2019}} (p. 1) {{cite:mcmahan2017}} (pp. 1–2)

Weighting an average of local means by $n_k$ is the merge that recovers the pooled mean. The same caution applies to a model average: a client with a handful of cases should not automatically pull the shared model as hard as a client with thousands, unless the goal really is an average across clients rather than across cases.{{cite:mcmahan2017}} (pp. 1–2)

Keeping the records on the devices is not a proof that the updates reveal nothing about those records. The server still receives quantities computed from the local samples, and the formulation is explicit that some trust in the coordinator remains and that attacks on the updates are still possible. Privacy methods can be wrapped around the updates. They are an extra layer, not a consequence of the word federation.{{cite:mcmahan2017}} (pp. 1–2)

The average of client models is not automatically the fit one would have obtained by pooling the cases. The clinic calculation is the mean, the simplest fit, and already $6\neq 14/3$ when the clinics have different sizes.{{cite:mcmahan2017}} (pp. 1–2)

A simulation that randomly splits one laboratory file across imaginary clients misses the feature the method was built for. The local distributions are allowed to differ, and in the intended applications they do.{{cite:mcmahan2017}} (pp. 1–2) {{cite:li_sahu_talwalkar_smith2019}} (p. 1)

The name and the mobile-device formulation, with local stochastic gradient steps and a server that averages models, were set out for deep networks trained on decentralised data, with an emphasis on communication cost and on unbalanced, non-identical local samples.{{cite:mcmahan2017}} (pp. 1–2) A later survey places the same idea in a wider set of remote devices and silos, including phones and hospitals, and treats the departure from ordinary distributed optimisation and from privacy-preserving analysis as the research problem the protocol creates.{{cite:li_sahu_talwalkar_smith2019}} (p. 1)

## Properties

If client $k$ has $n_k$ observations with mean $\bar y_k$, the pooled mean is $\sum_k n_k\bar y_k\big/\sum_k n_k$. An unweighted mean of the $\bar y_k$ equals the pooled mean when the $n_k$ are equal, and not in general otherwise. In the clinic numbers, $n_1=2$, $\bar y_1=2$, $n_2=1$, $\bar y_2=10$. The pooled mean is $14/3$. The unweighted mean is $6$. The difference is $4/3$.

If the second clinic also has two cases equal to $10$, then $n_1=n_2=2$ and both averages equal $6$. Equal client sizes, not equal client means, are what make the unweighted average of means agree with the pooled mean.{{cite:mcmahan2017}} (pp. 1–2)

A reported empirical comparison, on deep networks and several data sets, found that this style of local updating and averaging cut the number of communication rounds by a factor of $10$ to $100$ relative to a synchronised stochastic gradient step after every small batch. That factor is a statement about those experiments. It is not an identity like $14/3$.{{cite:mcmahan2017}} (p. 1)

## Worked example

Clinic 1 contributes $1$ and $3$, hence $n_1=2$ and $\bar y_1=2$. Clinic 2 contributes $10$, hence $n_2=1$ and $\bar y_2=10$. The pooled mean is
\[
\frac{2\cdot 2+1\cdot 10}{3}=\frac{14}{3}.
\]
The unweighted mean of the clinic means is $6$. The excess is $4/3$.

**Your turn.** If clinic 2 instead contributes two observations, both equal to $10$, what is the pooled mean, and what is the unweighted mean of the two clinic means?

::: {.callout-tip collapse="true" title="Answer"}
Both means equal $6$. The pooled mean is $(1+3+10+10)/4=6$, and the unweighted mean of $2$ and $10$ is also $6$.
:::

## Assumptions and limits

The useful case assumes that a shared objective can be written as a sum of local objectives, that clients can compute a local update, and that the coordinator can form a global model from those updates. If the decision really needs one client's raw records, the protocol does not apply. If clients drop out, or if only a fraction participate in each round, the average is an average over whoever answered.{{cite:mcmahan2017}} (pp. 1–2) {{cite:li_sahu_talwalkar_smith2019}} (p. 1)

The $10$ to $100$ fold drop in communication rounds is an experimental report about particular networks and data sets. A new model can communicate more, not less, if the local steps are unstable. The identity $14/3$ does not depend on that report.{{cite:mcmahan2017}} (p. 1)

## Connections

On each client the fit is a [machine learning](machine-learning.qmd) problem, often a [supervised learning](supervised-learning.qmd) problem when the label is observed locally. [Classification](classification.qmd) of on-device examples is one such problem. The federation is orthogonal to the choice of loss: it constrains where the data sit and what may be transmitted. It is not [cluster analysis](cluster-analysis.qmd), and it is not a [dimensionality reduction](dimensionality-reduction.qmd) of a single pooled matrix, because the matrix is never pooled.{{cite:li_sahu_talwalkar_smith2019}} (p. 1) {{cite:mcmahan2017}} (pp. 1–2)
