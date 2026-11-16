# Exponential distribution — source check

## Sources opened
- Shortle, Thompson, Gross and Harris, *Fundamentals of Queueing Theory*, 5th ed. (Wiley, 2018), full publisher-provided Chapter 1 excerpt https://catalogimages.wiley.com/images/db/pdf/9781118943526.excerpt.pdf , p. 2. It names Erlang’s 1909 telephone-conversation paper as the queueing field’s pioneering study and distinguishes his later Poisson-arrival, exponential-holding-time telephone models. This replaces the journal metadata citation in the article.
- Kyle Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §14.2, full online chapter at https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/14:_The_Poisson_Process/14.02:_The_Exponential_Distribution. Read the distribution, moments, memorylessness, minimum, and simulation discussions.
- NIST/SEMATECH, *e-Handbook of Statistical Methods*, §8.1.6.1, full exponential reliability page at https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm. Read PDF, reliability, failure-rate and mean-life definitions.
- NIST/SEMATECH, *e-Handbook of Statistical Methods*, §8.1.6.2, full official Weibull reliability page https://itl.nist.gov/div898/handbook/apr/section1/apr162.htm. Read its PDF, hazard and Special Case sections: shape one gives the exponential law with rate the reciprocal of Weibull scale.
- NIST/SEMATECH, *e-Handbook of Statistical Methods*, §1.3.6.6.7, full exponential properties page at https://www.itl.nist.gov/div898/handbook/eda/section3/eda3667.htm. Read quantile, moments, skewness, kurtosis, and MLE summary. Its scale convention was translated to rate.
- Robert Gallager, *Discrete Stochastic Processes*, §2.2, full MIT/LibreTexts chapter at https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Discrete_Stochastic_Processes_(Gallager)/02%253A_Poisson_Processes/2.02%253A_Definition_and_Properties_of_a_Poisson_Process. Read the continuous memorylessness characterization and Poisson interarrival argument; the page proof reproduces the Cauchy-equation reasoning directly.
- Dodge, *The Concise Encyclopedia of Statistics* (2008), printed p. 194, authorized text `/workspace/statwiki-sources/dodge2008/pages/pdf-0198.txt`. Read the exponential entry for history and Gamma/geometric orientation.
- Erlang (1909), journal contents metadata at https://www.jstor.org/stable/i24528012, pp. 33–39. Checked publication, title and page span only; full paper was unavailable, so the metadata is retained only in these notes.

## Fact status
- **Checked:** rate/scale relation, density/CDF/survivor, median/quantile, mean/variance, MGF, constant hazard and memorylessness against Siegrist and NIST; algebra independently reproduced in the page proof.
- **Checked:** Gamma stage sum, exponential minimum, and Poisson arrival interpretation against Siegrist §14.2–14.3; minimum derived in the proof.
- **Checked:** censoring contributes survival rather than density; constant-hazard likelihood with failures and total exposure follows by multiplying event and survival factors.
- **Checked:** The reader-facing Erlang history against the full Wiley chapter; Erlang 1909 bibliographic metadata and Dodge p. 194 provide orientation.
- **Assumed:** service-desk calls and machine failures obey stationary independent-arrival/constant-hazard models; examples are explicitly conditional on those assumptions.
- **Disputed or unresolved:** none. The retained Bayes-factor numerical value 1.347 is stipulated by its question without a numerical lifetime sample; its posterior-odds arithmetic is checked, but that input cannot be recomputed from observations.

## Preservation
The generator supplies the original infobox values, two infobox plots, the comparison figure, memorylessness result, series-system calculation, Gamma-prior example, model-comparison example, and component-lifetime examples. The research source adds interpretation and a distinct worked call-centre calculation. Shared lead_context relocation is requested in the pending file.

- **Checked:** Siegrist, “The Pareto Distribution,” Random Services, https://www.randomservices.org/random/special/Pareto.html, “The Basic Pareto Distribution,” Related Distributions, and “The General Pareto Distribution”: the log of a unit-scale Pareto variable is exponential; scaling by $x_m$ yields the stated transformation in both directions.
