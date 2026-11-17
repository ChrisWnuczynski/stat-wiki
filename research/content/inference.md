## Lead context

A poll, a clinical series, or a production sample is a fragment of a larger collection. The fragment is in hand; the collection is not. Inference is the step that treats the fragment as evidence about a quantity defined on the collection: a proportion, a mean, a treatment contrast, a future observation. The step is inductive. It does not follow from the arithmetic of the sample alone, and it is not a description of the sample for its own sake.{{cite:dodge2008}} (p. 263){{cite:gelman_bda2013}} (Ch. 1, §1.2, p. 7)

## Definition — From a sample to an unobserved quantity

Inference is reasoning by induction from information collected on a sample, with the aim of saying something about the population tied to that sample. The population quantity may be a parameter that organises the sampling distribution, or a further observation that has not yet been recorded. Either way, the target is not one of the numbers already on the page.{{cite:dodge2008}} (p. 263){{cite:gelman_bda2013}} (Ch. 1, §1.2, p. 7)

The same move appears in two neighbouring descriptions. Inferential statistics estimates parameters that characterise a population and tests hypotheses about those parameters, using a sample that stands in for the population. A textbook account of the same task says that inference is concerned with the uncertainty of those parameter estimates, and that the working tools are a point estimate, an interval of plausible values, and a test of a claim. The equations change with the parameter. The job does not.{{cite:dodge2008}} (pp. 263–264){{cite:openintro2019}} (Ch. 5, p. 169)

Descriptive summary stays inside the observed records. Inference leaves them, and therefore has to say under what sampling story the departure is allowed. A [confidence interval](confidence-interval.qmd) reports a range from a method with a long-run coverage rate. A test compares the sample with what a stated hypothesis would tend to produce. An [estimator](estimator.qmd) is the rule that turns the sample into a number aimed at the parameter.{{cite:openintro2019}} (Ch. 5, p. 169){{cite:dodge2008}} (p. 264)

## Statistical use

The ordinary sequence is to name the target, name the sampling model, compute a summary that does not depend on the unknown parameter, and then attach a statement about error. For a proportion, the sample proportion is the point estimate, and the gap between that proportion and the population proportion is the error of the estimate. Part of the gap is sampling variability, which shrinks as the sample grows when the draws are comparable. Part of it is bias from the way the sample was obtained or the question was worded, which a larger sample does not erase.{{cite:openintro2019}} (Ch. 5, §5.1.1, pp. 170–171)

Hypothesis tests and intervals are the two public forms of the same calculation. An interval lists parameter values the method would not find surprising at a stated rate. A test asks whether a particular value, often a null claim of no difference or of a legally required level, sits so far in the tail of the sampling distribution that the method rejects it. Both forms need the model that connects the sample to the population. Without that model the arithmetic is a description, not an inference.{{cite:openintro2019}} (Ch. 5, p. 169){{cite:dodge2008}} (pp. 263–264)

Prediction of a new case is inference as well when the new case is not in the sample. The uncertainty then includes both uncertainty about the fitted parameter and the fresh noise of the new case. A probability statement about the parameter itself, rather than about the behaviour of a procedure, is a different reading of the same data and is developed as Bayesian updating.{{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3; §1.2, p. 7)

## History

The early history of inferential statistics is the early history of probability used on data. Bayes’s essay on the doctrine of chances, de Moivre’s work on the probability of events in play, Gauss’s theory of errors, and Laplace’s analytic theory of probabilities supplied ways to pass between observations and an unknown quantity. Later in the nineteenth century Galton’s treatment of correlation, and Pearson’s criterion for whether a system of deviations could reasonably have arisen from random sampling, made the sample-to-population step a standard scientific calculation.{{cite:dodge2008}} (pp. 263–264)

Gosset’s 1908 paper on the probable error of a mean gave small samples a reference distribution of their own. Neyman and Pearson’s 1928 papers set out how test criteria were to be used and interpreted. Fisher’s later writing on statistical methods and scientific inference tied estimation, likelihood, and experimental design into one programme. Modern introductions still organise the subject as point estimation, intervals, and tests, with a separate development for probability statements about the parameter.{{cite:dodge2008}} (p. 264){{cite:openintro2019}} (Ch. 5, p. 169){{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3)

## Connections

[Estimation theory](estimation-theory.qmd) is the part of the subject that produces a number or an interval for a parameter. [Frequentist inference](frequentist-inference.qmd) judges procedures by their behaviour in repeated samples. [Mathematical statistics](mathematical-statistics.qmd) is the body of proofs that makes those judgements precise. [Asymptotic analysis](asymptotic-analysis.qmd) replaces an exact sampling distribution, when one is unavailable, by a limit as the sample size grows. A [decision problem](decision-problem.qmd) asks what action the inference should support, once losses are named.
