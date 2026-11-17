## Lead context
A population is often too large, too expensive, or impossible to observe in full. Sampling is the selection of a part of it, the study of that part, and the inference back to the population. {{cite:dodge2008}} (p. 468) {{cite:openintro2019}} (p. 22)

## Motivating example
The mercury content of every swordfish in the Atlantic is not going to be measured. A research question about that average still refers to all of those fish. Measuring 60 of them, or some other number, and estimating the average from those 60, is sampling. Each fish is a case, and the 60 are the sample. {{cite:openintro2019}} (p. 22) {{cite:nist_glossary2002}} (Glossary, "sample")

## Intuition
A raffle draws names from a complete list so that the draw, rather than a person's convenience, decides who is included. That is the protection. A nutrition student asked to pick graduates by hand may over-represent health fields without meaning to. {{cite:openintro2019}} (p. 23) A telephone poll in 1936 that reached only households with telephones described those households, not the electorate. {{cite:dodge2008}} (p. 469)

## Definition
Sampling means selecting a part of a population, called the sample, studying characteristics of that sample, and making inferences about the population. It is also the set of operations that produce the sample. {{cite:dodge2008}} (p. 468) The population is the entire set of potential observations one wants to learn about. The sample is the set of units whose properties are actually observed. {{cite:nist_glossary2002}} (Glossary, "population") {{cite:nist_glossary2002}} (Glossary, "sample")

Survey sampling is this operation when the purpose is a survey: a fixed set of questions put to selected individuals, with the sample meant to stand for a wider population. {{cite:nist_glossary2002}} (Glossary, "survey") {{cite:dodge2008}} (p. 532) The methods that construct the sample are the sampling methods. {{cite:dodge2008}} (p. 532)

Simple random sampling chooses \(n\) units out of \(N\) so that every subset of size \(n\) has the same probability. There are \(\binom{N}{n}\) such subsets. {{cite:dodge2008}} (p. 497) {{cite:openintro2019}} (p. 24)

## Properties
If the probability that a given unit is selected is known, the error that comes from observing only a sample can be calculated. Random methods, including simple random sampling, stratified sampling, systematic sampling, and batch sampling, are the methods for which that probability is part of the plan. Quota sampling is a nonrandom method that tries to build a sample resembling the population by empirical rules. {{cite:dodge2008}} (p. 152)

A convenience sample selects units because they are easy to reach. Stopping people in one borough does not represent a city. {{cite:openintro2019}} (p. 24) {{cite:nist_glossary2002}} (Glossary, "convenience sample") Non-response is a second failure: if only 30 percent of a randomly drawn survey sample answers, it is unclear whether the answers represent the population that was drawn. {{cite:openintro2019}} (p. 24)

Sampling error, in the survey sense, is the error that results when the selected respondents do not represent the population about which conclusions are wanted. Coverage error is the different failure in which the frame itself does not match that population. {{cite:nist_glossary2002}} (Glossary, "sampling error") {{cite:nist_glossary2002}} (Glossary, "coverage error")

## Statistical use
Almost all of the usual estimates and their errors assume that observational data were collected in a random framework. Without that framework the formulas do not describe the uncertainty of the estimate. {{cite:openintro2019}} (p. 25) A census, observing every unit in the frame, avoids sampling error and costs more. Surveys are used because they are cheaper and faster, and the price is the sampling error, which shrinks when the sample is more representative. {{cite:dodge2008}} (p. 532) {{cite:dodge2008}} (p. 533) {{cite:nist_glossary2002}} (Glossary, "census")

Stratified and cluster designs change which subsets are equally likely. They are still sampling designs. [Systematic sampling](systematic-sampling.qmd) takes units at a fixed interval after a random start. {{cite:dodge2008}} (p. 533)

## Worked example
A population has \(N = 6\) units and a sample of size \(n = 2\) is drawn by simple random sampling. The number of possible samples is \(\binom{6}{2} = 15\). Each sample has probability \(1/15\). A census of the same population would observe all 6 units. A survey that draws 2 out of 6 has sampling fraction \(2/6 = 1/3\). {{cite:dodge2008}} (p. 497) {{cite:nist_glossary2002}} (Glossary, "census")

**Your turn.** The population grows to 10 units and the sample size stays 2. How many equally likely samples are there?

::: {.callout-tip collapse="true" title="Answer"}
The number of samples is \(\binom{10}{2} = 45\).
:::

## Common misconceptions
A larger sample is not a remedy for a frame that never listed the units of interest. The 1936 telephone poll was biased because the list was biased, not because it was small. {{cite:dodge2008}} (p. 469) {{cite:nist_glossary2002}} (Glossary, "coverage error")

An anecdotal case, one striking swordfish or one student who took seven years to graduate, is not a sample drawn to represent a population. {{cite:openintro2019}} (p. 23)

## Assumptions and limits
The probability calculation for sampling error needs a known chance of selection. Quota and convenience selections do not supply that chance. {{cite:dodge2008}} (p. 152) {{cite:nist_glossary2002}} (Glossary, "convenience sample") Even a perfect draw does not repair measurement error in the answers, or non-response that systematically removes a kind of person. {{cite:openintro2019}} (p. 24) {{cite:nist_glossary2002}} (Glossary, "nonresponse error")

## Connections
The [sample](sample.qmd) is the subset that sampling produces, and the [population](population.qmd) is the set it is meant to describe. [Sampling bias](sampling-bias.qmd) is the systematic miss that a bad draw creates. A [statistical survey](statistical-survey.qmd) is the inquiry that uses the sample. [Stratified and cluster sampling](stratified-and-cluster-sampling.qmd) are the designs that sample within strata or take whole groups. [Data collection](data-collection.qmd) is the wider activity of which sampling is one approach, beside a register and an experiment. {{cite:dodge2008}} (p. 151)

## History
Complete enumeration was the default long after the first extrapolations from counts of homes. In 1895, at the congress of the International Statistical Institute in Bern, Anders Nicolai Kiaer argued for representative samples and was opposed by participants who held that only a full count would do. Lucien March developed the idea of probabilistic sampling. The 1925 Rome congress put random sampling beside purposive selection, and the argument shifted from "sample or census" to "which sampling method". Jerzy Neyman became a founder of the theory that prefers random sampling. The 1936 telephone prediction that named Landon, and missed Roosevelt, is the usual illustration of a frame that covered only households with telephones. {{cite:dodge2008}} (p. 468) {{cite:dodge2008}} (p. 469)
