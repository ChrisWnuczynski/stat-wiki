## Lead context

A population is often too large, too expensive, or impossible to observe in full. Sampling is the selection of a part of it, the study of that part, and the inference back to the population. The mercury content of every swordfish in the Atlantic is not going to be measured, and a research question about that average still refers to all of those fish.{{cite:dodge2008}} (p. 468){{cite:openintro2019}} (Ch. 1, §1.3.1)

## Motivating example

Measuring 60 swordfish, or some other number, and estimating the average from those 60, is sampling. Each fish is a case, and the 60 are the sample. The population is every swordfish the question named. A raffle draws names from a complete list so that the draw, rather than a person's convenience, decides who is included. A nutrition student asked to pick graduates by hand may over-represent health fields without meaning to. The protection is the known chance of selection, not the size of the draw by itself.{{cite:openintro2019}} (Ch. 1, §1.3.1, §1.3.3){{cite:nist_glossary2002}} (Glossary, "sample")

## Definition

Sampling means selecting a part of a population, called the sample, studying characteristics of that sample, and making inferences about the population. It is also the set of operations that produce the sample. The population is the entire set of potential observations one wants to learn about. The sample is the set of units whose properties are actually observed.{{cite:dodge2008}} (p. 468){{cite:nist_glossary2002}} (Glossary, "population"){{cite:nist_glossary2002}} (Glossary, "sample")

Survey sampling is this operation when the purpose is a survey: a fixed set of questions put to selected individuals, with the sample meant to stand for a wider population. The methods that construct the sample are the sampling methods.{{cite:nist_glossary2002}} (Glossary, "survey"){{cite:dodge2008}} (p. 532)

Simple random sampling chooses $n$ units out of $N$ so that every subset of size $n$ has the same probability. There are $\binom{N}{n}$ such subsets. The individuals are numbered from 1 to $N$, and $n$ of those numbers are drawn, in principle without replacement.{{cite:dodge2008}} (p. 497){{cite:openintro2019}} (Ch. 1, §1.3.3)

## Properties

If the probability that a given unit is selected is known, the error that comes from observing only a sample can be calculated. Random methods, including simple random sampling, stratified sampling, systematic sampling, and batch sampling, are the methods for which that probability is part of the plan. Quota sampling is a nonrandom method that tries to build a sample resembling the population by empirical rules.{{cite:dodge2008}} (p. 152)

A convenience sample selects units because they are easy to reach. Stopping people in one borough does not represent a city. Non-response is a second failure: if only 30 percent of a randomly drawn survey sample answers, it is unclear whether the answers represent the population that was drawn.{{cite:openintro2019}} (Ch. 1, §1.3.5){{cite:nist_glossary2002}} (Glossary, "convenience sample")

Sampling error, in the survey sense, is the error that results when the selected respondents do not represent the population about which conclusions are wanted. Coverage error is the different failure in which the frame itself does not match that population. A census observes every unit in the frame and avoids sampling error. Surveys are used because they are cheaper and faster, and the price is the sampling error, which shrinks when the sample is more representative. Almost all of the usual estimates and their errors assume that observational data were collected in a random framework. Without that framework the formulas do not describe the uncertainty of the estimate.{{cite:nist_glossary2002}} (Glossary, "sampling error"){{cite:nist_glossary2002}} (Glossary, "coverage error"){{cite:nist_glossary2002}} (Glossary, "census"){{cite:openintro2019}} (Ch. 1, §1.3.5){{cite:dodge2008}} (pp. 532–533)

Stratified and cluster designs change which subsets are equally likely. They are still sampling designs. Systematic sampling takes units at a fixed interval after a random start. A telephone poll in 1936 that reached only households with telephones described those households, not the electorate. The Readers Digest prediction that named Landon, and missed Roosevelt, used a frame of telephone owners, and at that time a telephone marked a richer household. The bias was in the list, not in the arithmetic of a small sample. An anecdotal case, one striking swordfish or one student who took seven years to graduate, is not a sample drawn to represent a population.{{cite:dodge2008}} (p. 469){{cite:openintro2019}} (Ch. 1, §1.3.2)

## Worked example

A population has $N = 6$ units and a sample of size $n = 2$ is drawn by simple random sampling. The number of possible samples is $\binom{6}{2} = 15$. Each sample has probability $1/15$. A census of the same population would observe all 6 units. A survey that draws 2 out of 6 has sampling fraction $2/6 = 1/3$.{{cite:dodge2008}} (p. 497){{cite:nist_glossary2002}} (Glossary, "census")

**Your turn.** The population grows to 10 units and the sample size stays 2. How many equally likely samples are there?

::: {.callout-tip collapse="true" title="Answer"}
The number of samples is $\binom{10}{2} = 45$.
:::

## Assumptions and limits

The probability calculation for sampling error needs a known chance of selection. Quota and convenience selections do not supply that chance. A larger sample is not a remedy for a frame that never listed the units of interest. Even a perfect draw does not repair measurement error in the answers, or non-response that systematically removes a kind of person. Drawing with replacement keeps the population the same at every draw, so the included units are independent and identically distributed. Drawing without replacement from a large population, with $n$ small relative to $N$, is treated as nearly the same. The dependence is then small enough that the usual independent-sample formulas are used.{{cite:dodge2008}} (pp. 152, 497){{cite:nist_glossary2002}} (Glossary, "convenience sample"){{cite:nist_glossary2002}} (Glossary, "nonresponse error"){{cite:openintro2019}} (Ch. 1, §1.3.5)

## History

Complete enumeration was the default long after the first extrapolations from counts of homes. In 1895, at the congress of the International Statistical Institute in Bern, Anders Nicolai Kiaer argued for representative samples and was opposed by participants who held that only a full count would do. Lucien March developed the idea of probabilistic sampling. The 1925 Rome congress put random sampling beside purposive selection, and the argument shifted from whether to sample at all to which sampling method to use. Jerzy Neyman became a founder of the theory that prefers random sampling, including sampling with or without replacement, stratified sampling, and cluster sampling. The 1936 telephone prediction is the usual illustration of a frame that covered only households with telephones.{{cite:dodge2008}} (pp. 468–469)
