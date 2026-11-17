## Lead context

Two readers can use the word *reproducible* for different achievements. One means that a second laboratory, with new subjects, obtains the same finding. The other means that a second analyst, with the original data and the original code, obtains the same numbers. Both standards matter, and they fail for different reasons. A lost script does not by itself show that the scientific claim is false. A clean rerun does not by itself show that a new sample would agree.

## Definition — Scope

In computational science, reproducibility is the standard that the data and the computer code used to analyse them are available to others, so that the reported numerical result can be checked. It is deliberately weaker than replication. Replication has independent investigators collect new data to address the same hypothesis. Reproducibility analyses the same data again. It sits between a full repeat and a paper that cannot be checked at all, and a study can be more or less reproducible according to how much of the data, metadata, and code is shared.{{cite:peng2011}} (pp. 1226–1227)

In the psychology replication literature the same word is often used for the stronger standard. There, a direct replication tries to recreate the conditions thought sufficient for a previously observed finding, and success is assessed with new data. On that usage, a finding is reproducible when the new study recovers it, and irreproducible when random error, systematic error, or a false positive stands in the way. The two definitions should not be collapsed. Peng's standard is a check of the computation. The replication standard is a check of the phenomenon.{{cite:osc2015}} (Introduction){{cite:peng2011}} (pp. 1226–1227)

## Statistical use

A reproducible computational result has, in principle, a complete log of what the machine did. Publishing that log lets another person see choices that a prose methods section usually omits: which rows were dropped, which rows were transformed, which of several models was reported. A review of microarray analyses found studies that were not reproducible, partly reproducible, or reproducible, and the differences lined up largely with whether data and metadata were available. The practical test is modest. Someone else should be able to regenerate the tables and figures from the deposited materials.{{cite:peng2011}} (pp. 1226–1227)

A replication uses a different test. Effect sizes are placed on a common scale, [confidence intervals](confidence-interval.qmd) from the new sample are compared with the original estimate, and a [p-value](p-value.qmd) is only one of several summaries. In the Open Science Collaboration, original effects averaged about 0.40 on the correlation scale and replication effects about 0.20; 36 percent of replications were significant at 0.05, against 97 percent of the originals. Those numbers speak to new samples. They do not say whether each original script would still run.{{cite:osc2015}} (Abstract)

## History

Replication has long been described as the standard by which claims are judged: independent investigators accumulate evidence for or against a hypothesis, and spurious claims are supposed to fall away. Large computational projects made that ideal harder to reach. Repeating the Sloan Digital Sky Survey, or a long environmental cohort, costs more than most follow-up teams have. Peng argued in 2011 that sharing data and code was an attainable minimum while full replication remained rare, and that the barrier was often simply that the code no longer existed.{{cite:peng2011}} (pp. 1226–1227)

The 2015 psychology project used the other meaning in its title and then did the harder thing: new data, registered protocols, and public archives of materials. Its introduction cites the 2005 analysis of false research findings as a reason to expect that many published results would not reappear. The project therefore treats reproducibility, in its sense, as something to be estimated rather than assumed.{{cite:osc2015}} (Introduction, Abstract)

## Connections

Reproducibility in Peng's sense is a neighbour of [open science](open-science.qmd), which is the broader demand that data, code, and plans be citable and shared. Reproducibility in the replication sense is the empirical core of the [replication crisis](replication-crisis.qmd). A [randomised controlled trial](randomised-controlled-trial.qmd) can be computationally reproducible and still estimate a treatment effect that a later trial does not confirm. Conversely, a lost script can hide a correct result. Reporting both standards, and saying which one was met, is the distinction the two literatures force on the reader.{{cite:peng2011}} (pp. 1226–1227){{cite:osc2015}} (Method)
