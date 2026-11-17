## Lead context

Counting a sample and naming a population still leaves a mathematical question: which functions of the sample are entitled to stand for which parameters, and what can be proved about those functions before any particular sample arrives. Mathematical statistics is that question, pursued with the language of probability. It is where bias, efficiency, sufficiency, and the distribution of a test statistic are defined and compared.{{cite:dodge2008}} (pp. 184–185, 263–264)

## Definition — A mathematical theory of estimation and testing

Mathematical statistics is the mathematical development of methods that pass from a sample to statements about a population. Its early line runs through the probability calculations that made such a passage possible, and its modern core is the theory of estimation: how an estimator is defined, when it is biased or efficient or sufficient, and how an interval or a test is calibrated from the sampling distribution. Fisher’s 1922 paper on the mathematical foundations of theoretical statistics is the document later summaries credit with saying clearly what estimation is. The 1925 paper on the theory of statistical estimation then fixed a vocabulary — bias, efficiency, sufficiency — that the subject still uses.{{cite:dodge2008}} (pp. 184–185)

The scope is wider than a single formula. Point estimation produces a number. Interval estimation produces a set. Hypothesis testing produces a decision to reject or not, with an error probability computed from the model. Descriptive statistics can stop at indicators computed on the sample that was seen. Mathematical statistics asks what those indicators do when the sample is regarded as random and the population parameter is fixed but unknown.{{cite:dodge2008}} (pp. 184–185, 263–264)

The same scope includes the probability theorems that justify large-sample approximations, the algebra of least squares, and the exact distributions available in normal models. A first course meets the subject as the central limit theorem, a standard error, and a reference distribution. A second course meets it as theorems about estimators. Both are the same project at different depths.{{cite:openintro2019}} (Ch. 5, §5.1.3, p. 172; Ch. 5, p. 169){{cite:hansen2010}} (Ch. 5, §5.1, p. 65)

## Statistical use

The working products are the procedures other pages define one by one. An [estimator](estimator.qmd) is a statistic aimed at a parameter. Its [bias](bias-of-an-estimator.qmd) is the gap between its expectation and the target. A [confidence interval](confidence-interval.qmd) is a set-valued procedure with a coverage probability. A test uses a [critical region](critical-region.qmd) whose probability under the null is the type I error. [Maximum likelihood](maximum-likelihood.qmd) and the [method of moments](method-of-moments.qmd) are two constructions whose properties the theory then studies.{{cite:dodge2008}} (pp. 184–185){{cite:openintro2019}} (Ch. 5, p. 169)

When an exact sampling distribution is unavailable, the theory supplies limit theorems. The weak law of large numbers, the central limit theorem, and the continuous mapping theorem are the usual tools for showing that an estimator concentrates and that a suitably scaled error is approximately normal. Those approximations are what make a standard error and a normal critical value usable in regression, in a proportion, and in many other models.{{cite:hansen2010}} (Ch. 5, §5.1, p. 65){{cite:openintro2019}} (Ch. 5, §5.1.3, p. 172)

The theory also marks its own boundary. A procedure proved unbiased under independence and a correct mean is not thereby proved unbiased under a different sampling scheme. A large-sample normal limit does not repair a parameter that the likelihood cannot identify. Using the theorems means keeping the assumptions that were used to prove them.{{cite:gelman_bda2013}} (Ch. 4, §4.3, p. 89){{cite:dodge2008}} (pp. 184–185)

## History

The name is attached, in a standard historical sketch, to the first mathematical treatments of estimation: Jacob Bernoulli’s *Ars Conjectandi* (1713), Laplace’s memoir on the probability of causes (1774), and Daniel Bernoulli’s comparison of discrepant observations (1778). Least squares, associated with Legendre and Gauss, and Pearson’s method of moments in the 1890s, were the large steps before Fisher. Fisher’s 1912 absolute criterion for fitting frequency curves introduced maximum likelihood. The 1922 and 1925 papers then separated the ideas of an estimator’s bias, efficiency, and sufficiency from the mere computing of a formula.{{cite:dodge2008}} (pp. 184–185)

Testing grew on a parallel track. Pearson’s chi-squared criterion, Gosset’s *t* distribution for a mean, and the Neyman–Pearson theory of tests gave hypothesis testing its sampling-theory form. By the middle of the twentieth century the subject had textbooks whose title was mathematical statistics and whose chapters were estimation, hypothesis testing, and the distributions required to carry them out. Introductions today still open the same chapters, with computing changed and the logical order intact.{{cite:dodge2008}} (pp. 263–264){{cite:openintro2019}} (Ch. 5, p. 169)

## Connections

[Estimation theory](estimation-theory.qmd) is the estimation half of this subject. [Frequentist inference](frequentist-inference.qmd) is the repeated-sampling interpretation of the probabilities the theorems produce. [Asymptotic analysis](asymptotic-analysis.qmd) is the limit theory used when finite-sample distributions are out of reach. [Inference](inference.qmd) is the scientific task the mathematics serves. Probability, as a separate subject, supplies the measure theory and the limit theorems. Mathematical statistics starts when those tools are aimed at an unknown parameter.
