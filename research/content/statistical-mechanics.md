

## Lead context

A gas, a magnet, and a lattice of spins are too large to follow particle by particle. What is observed is a pressure, a magnetisation, a temperature. Statistical mechanics is the probabilistic account of how those macroscopic regularities arise from an enormous number of microscopic configurations. The same counting of configurations reappears as entropy in the mathematical theory of communication. The models are probability models. The subject that uses them is physics, and the tools it shares with statistics are distributions on huge product spaces, Markov dependence, and simulation.

## Definition

Statistical mechanics describes the equilibrium and the evolution of systems with many components by putting a probability distribution on their microscopic states. Stochastic processes, as a mathematical subject, grew in part from that applied work: Gibbs, Boltzmann, Poincaré, Smoluchowski, and Langevin are the names attached to the early physical sources, before the measure-theoretic treatment associated with Doob. The scope is the passage from a law for one particle, or one spin, to a law for an average. It is not the same as a sample survey. The "sample" is an idealisation of the configurations a physical system can occupy, and the probabilities are part of the physical model.{{cite:dodge2008}} (p. 521)

Entropy is the quantity both traditions share. Shannon's uncertainty measure, whose form is fixed by his assumptions, is the entropy used in formulations of statistical mechanics in which $p_i$ is the probability that the system is in cell $i$ of its phase space. He identifies that quantity with the $H$ of Boltzmann's H theorem. A communication system and a physical system are then using one functional of a probability distribution, for different reasons.{{cite:shannon1948}} (Theorem 2)

## Statistical use

The working objects are distributions on many coordinates and the summaries that survive after most of the coordinates are integrated out. The [Ising model](ising-model.qmd) is the standard lattice example: binary spins, a probability that favours agreement of neighbours, and macroscopic magnetisation as a function of temperature. A [Markov chain](markov-chain.qmd) is the usual dynamical picture when the next state depends on the present configuration and not on the path that led there. The [Monte Carlo method](monte-carlo-method.qmd) estimates averages over those configurations when the normalising constant cannot be written in closed form. Entropy, relative entropy, and the associated inequalities are the analytic tools that say which macroscopic state is typical.{{cite:shannon1948}} (Theorem 2){{cite:dodge2008}} (p. 521)

None of this replaces a designed experiment on a small sample. A simulation from an Ising model answers a question about that model. It does not, by itself, estimate a regression coefficient from a survey.



The integer list used above is a device for keeping the target fixed. With 10 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

The physical subject is late nineteenth and early twentieth century. Boltzmann's H theorem and Gibbs's ensembles put probability at the centre of thermodynamics. The mathematicians who built stochastic-process theory did so after, and partly because of, those applications, together with Brownian motion. Shannon's 1948 paper then recognised the information-theoretic entropy as the same functional, and pointed to Tolman's *Principles of Statistical Mechanics* for the physical reading. Later computational work made sampling from those distributions a statistical method in its own right.{{cite:dodge2008}} (p. 521){{cite:shannon1948}} (Theorem 2)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 10. Their total is 55, so their mean is 5.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 3.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Statistical mechanics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 5.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Ising model](ising-model.qmd), [Markov chain](markov-chain.qmd), [Monte Carlo method](monte-carlo-method.qmd), [stochastic processes](stochastic-process.qmd).

Two further limits are algebraic. The sum of deviations from the mean 5.5 is zero, so the mean is the least-squares centre of these 10 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 5.5.

## Connections

Statistical mechanics is a parent of parts of the theory of [stochastic processes](stochastic-process.qmd) and a neighbour of information theory. The Ising model is also a standard test case for [Markov chain](markov-chain.qmd) Monte Carlo, so the subject re-enters statistics as a source of algorithms. Entropy here is a property of a probability distribution on configurations. It is not a measure of how surprising a data set is unless that data set has been given such a distribution. Confusing the two makes a physical constant sound like a p-value.{{cite:shannon1948}} (Theorem 2){{cite:dodge2008}} (p. 521)
