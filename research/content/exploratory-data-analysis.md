## Motivating example — The same mean can hide different data
A dataset can contain a recording error, a mixture of groups, a nonlinear association or a trend that is invisible in a single summary. Exploratory data analysis begins by examining those possibilities through complementary summaries and displays. The goal is to learn what needs explanation and which assumptions deserve scrutiny before committing to a narrow model. The question, the sampling mechanism and the measurement units still guide the exploration.{{cite:dodge2008}} (p. 192, Exploratory Data Analysis)

## Definition — Exploration is a way of reasoning
Exploratory data analysis combines graphical investigation, numerical summaries, transformations and diagnostic checks to investigate a dataset's structure. It is broader than making a standard collection of plots: useful exploration follows up discrepancies and revises the questions being asked. A histogram describes a distribution, a scatterplot investigates a relationship, and a plot against observation order investigates change. Their different roles make agreement or disagreement between displays informative.{{cite:nist_eda_intro_ah}} (§1.1.1)

A practical starting point is to establish what an observation represents, which fields are missing, what units are used and whether repetitions are legitimate. A value outside a plausible range could indicate a unit mismatch, a coding convention or a scientifically interesting extreme. The response should depend on evidence about the measurement, rather than an automatic rule to delete unusual values. Validation and interpretation are distinct stages, and both are necessary.{{cite:downey2014_thinkstats2}} (Ch. 1, “Validation” and “Interpretation”)

## Interpretation — Resistance reveals sensitivity
A resistant summary changes comparatively little when a small fraction of observations is moved far away. The sample median often plays this role, whereas the mean responds directly to the magnitudes of all values. Comparing them can reveal asymmetry or sensitivity. Such disagreement is a clue, not a complete account of the data-generating process. Likewise, a transformation can make a multiplicative pattern easier to study, but it changes the scale on which differences are interpreted.{{cite:dodge2008}} (p. 192, resistance and re-expression)

The choice of a graphical resolution also matters. A histogram depends on bin boundaries and widths, and a scatterplot can obscure overlaps. Looking at several defensible resolutions helps distinguish stable structure from a display artefact. Splitting observations by a scientifically relevant group can expose a relationship hidden in the aggregate; indiscriminately splitting into many small groups can instead create unstable patterns. The analysis must keep track of which comparisons were considered.{{cite:downey2014_thinkstats2}} (Ch. 2, histograms and outliers; Ch. 7, relationships between variables)

## Worked example — One value changes the story
Consider measurements $(2,3,3,4,5)$. Their mean is $3.4$, median is $3$ and range is $3$. If the final value is recorded as $50$, the mean rises to $12.4$, while the median stays $3$ and the range becomes $48$. A sorted-value display makes the isolated high measurement immediately visible. The calculations do not decide whether $50$ is wrong; they show how strongly the mean depends on investigating that measurement. A plot against time or group may then reveal whether it belongs to a different measurement regime.{{cite:downey2014_thinkstats2}} (Ch. 2, “Outliers” and “Summarizing distributions”)

**Your turn.** If that final measurement is corrected to $8$ rather than $50$, what are the mean and median?

::: {.callout-tip collapse="true" title="Answer"}
The total is 20, so the mean is 4. The middle ordered value is still 3.
:::

## Assumptions and limits — Discovery needs a route to confirmation
An exploratory pattern can motivate a subsequent model or experiment, but a hypothesis chosen after inspecting many relationships has a different evidential status from one specified in advance. The same data can support development and diagnosis, while independent data or an explicit selection-aware procedure is useful for checking generalisation. Exploration also cannot repair a biased sample merely by improving the graph. Representativeness, missingness and dependence remain questions about how observations were obtained.{{cite:downey2014_thinkstats2}} (Ch. 1, “A statistical approach”; Ch. 9, “Replication”)

## Connections — Use several views for one question
Graphical summaries and quantitative methods can reinforce one another. A residual plot may suggest curvature, after which a fitted comparison quantifies the improvement. A robust summary may suggest a sensitivity analysis with and without a demonstrably erroneous record. The useful output is an interpretable account of structure, anomalies and limitations, together with questions that can be checked.{{cite:nist_eda_intro_ah}} (§1.1.1)
