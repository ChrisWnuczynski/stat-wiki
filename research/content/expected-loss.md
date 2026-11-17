## Lead context

Two treatments can be scored by how many months of life they leave, or two estimators by how far they fall from a parameter. Expected loss is the average of that score, taken under the probability distribution that still applies when the action is chosen. The action with the smallest expected loss is the one the score recommends. A different score can recommend a different action from the same probabilities.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238; §9.4, p. 249)

## Motivating example

Radiotherapy, surgery, and no treatment for a suspected lung tumour are scored by quality-adjusted months of life, which is an expected lifetime minus a month if treatment is undergone. With a $90\%$ chance the tumour is malignant, those expectations are about $17.5$, $13.5$, and $8.5$ months. Writing the score as a loss equal to months forfeited would reverse the sign and leave the ranking unchanged: the preferred action is the one whose expected loss is smallest, and here that is radiotherapy. The expectation is doing the work. No single state, “cancer” or “not,” is treated as certain.{{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245)

## Intuition

A loss $L(x,d)$ charges action $d$ when the outcome is $x$. If $x$ is still random given $d$, the charge that guides the action is the mean of $L$, not the loss in the most dramatic state and not the loss in the most probable state. A small probability of a large loss can outweigh a likely small loss, or the other way around, depending on the numbers. Computing the mean forces that tradeoff into the open. In a tree, the mean at a later node is computed with the information available there, and the earlier node averages those later means, weighted by the probability of reaching them.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238; §9.3, pp. 245–246)

When the unknown is a parameter $\theta$ and the action is an estimator $T$, the same average taken over the sampling distribution of $T$ at a fixed $\theta$ is the risk of $T$ at $\theta$. Expected loss is the general average. Risk is expected loss in that repeated-sample sense.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 92)

## Definition

Given a decision $d$ and a random outcome $x$ with distribution $p(x\mid d)$, and a loss $L(x,d)$, the expected loss of $d$ is

$$
E\bigl(L(x,d)\mid d\bigr)=\int L(x,d)\,p(x\mid d)\,dx,
$$

with a sum in place of the integral when $x$ is discrete. If the problem is scored by a utility $U$ instead, the expected utility is the same construction with $U$ in place of $L$, and one maximises it rather than minimising it. The two agree when $L=-U$, up to a constant that does not change the ranking.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238)

In the radon decision the comparison is stated directly in losses. The expected loss of immediate remediation, the expected loss of doing nothing, and the expected loss of measuring and then choosing, are three numbers. The recommended action is the one with the lowest expected loss. The expectation for the measurement branch is valid for the policy that will actually be followed after the measurement. It is not the expected loss of measuring and then ignoring the result.{{cite:gelman_bda2013}} (Ch. 9, §9.4, p. 249)

For an estimator $T$ of a parameter $\theta$, with loss $\ell(\theta,T)$, the sampling expected loss is $R(\theta,T)=E_\theta\bigl(\ell(\theta,T)\bigr)$. Squared error makes this the mean squared error. That risk is a frequentist expected loss, indexed by the unknown $\theta$. A Bayesian expected loss instead averages the loss over the posterior distribution of $\theta$ as well, and the action can be the choice of an estimator or of a treatment.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 92; Ch. 9, §9.1, p. 238)

In that Bayesian point-estimation problem the loss is attached to reporting an estimate in place of the parameter. If the loss is quadratic, the estimate that the score selects is the mean of the distribution calculated for the parameter.{{cite:dodge2008}} (p. 34)

## Properties

Expected loss ranks actions at a given information state. It is linear in the loss: the expected loss of a mixture of outcomes is the mixture of the expected losses. In the tumour example the radiotherapy score $0.9\times 16.7+0.1\times 34.8-1$ is exactly that mixture, with the final $-1$ a sure loss from discomfort. Changing the probability $0.9$ changes the expected loss without changing the loss attached to either state.{{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245)

The law of total expectation is what makes a tree computable. The expected loss of “test, then act optimally” equals the average, over the test result, of the expected loss of the optimal action given that result, plus any loss charged by the test itself. If the optimal action does not depend on the result, this cannot beat the expected loss of taking that action immediately, once the test itself has a positive loss. The bronchoscopy calculation is an instance: every result still leads to radiotherapy, and the test adds a chance of death, so its expected quality-adjusted lifetime is worse.{{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246)

Sampling risk does not pick a uniformly best estimator. An estimator that has the smallest expected squared error at one $\theta$ generally fails at another. Restricting the class, for example to unbiased estimators, is what makes a further optimality claim possible. Expected posterior loss can still pick a single action, because the posterior has already averaged over $\theta$.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 92)

## Statistical use

For a treatment or a policy, list the loss in each state, weight by the current probabilities, and compare the averages. State whether the loss includes sure costs, such as a month of discomfort or the price of a measurement. For an estimator, say whether the expectation is a sampling risk at a fixed parameter or a posterior expected loss. The two numbers answer different questions. A point estimate chosen to minimise posterior expected squared error is a posterior mean. A point estimate discussed only through its sampling mean squared error is being judged as a procedure.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238; Ch. 4, §4.4, p. 92)

[Loss and risk](loss-and-risk.qmd) develop the sampling version. A [decision problem](decision-problem.qmd) is the list of actions inside which expected loss is computed. [Mean squared error](mean-squared-error.qmd) is expected squared error loss.

## Worked example

Suppose an action “treat” has loss $1$ if the condition is present and loss $8$ if it is absent, and an action “watch” has loss $10$ if present and loss $0$ if absent. At a base rate $p=0.2$,

$$
E(L\mid\text{treat})=0.2\times 1+0.8\times 8=6.6,
$$
$$
E(L\mid\text{watch})=0.2\times 10+0.8\times 0=2.
$$

Watching has the smaller expected loss. The most probable state is “absent,” and watching is also best in that state, but that coincidence is not the reason. The reason is the average.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238)

**Your turn.** Keep the same losses and set the base rate to $0.7$. Which action has the smaller expected loss, and what are the two values?

::: {.callout-tip collapse="true" title="Answer"}
Treating has expected loss $0.7\times 1+0.3\times 8=3.1$. Watching has expected loss $0.7\times 10=7$. Treating is smaller. The ranking flipped because the base rate changed, not because the losses changed.
:::

## Common misconceptions

Expected loss is not the loss of the expected outcome, unless the loss is linear. It is not the loss in the worst state, and it is not the loss in the most probable state. Minimising expected loss under one base rate does not minimise it under another. A sampling risk $R(\theta,T)$ is not a posterior expected loss: the first still depends on $\theta$, and the second has averaged $\theta$ out. Two losses that charge the same states differently can rank the same actions in opposite orders.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238; Ch. 4, §4.4, p. 92)

## Assumptions and limits

The expectation exists only when the loss has a finite mean under $p(x\mid d)$. A utility or loss that the decision maker does not accept will rank actions they would not rank. The radon and tumour calculations make the tradeoff explicit and therefore easy to dispute. The tree calculation for a later action assumes that the stated policy will be followed. An expected loss computed for “measure, then remediate if high” does not apply to a household that will remediate regardless of the measurement.{{cite:gelman_bda2013}} (Ch. 9, §9.4, p. 249; §9.3, p. 245)

## Connections

A [decision problem](decision-problem.qmd) names the actions whose expected losses are compared. The [base rate](base-rate.qmd) is a probability weight inside the average. [Loss and risk](loss-and-risk.qmd) are the sampling-theory names for a loss and its expectation at a fixed parameter. [Mean squared error](mean-squared-error.qmd) is expected squared error. [Least absolute deviations](least-absolute-deviations.qmd) minimises an expected absolute loss for a median, in the population version of that criterion.

## History

Decision analysis scores an action by an expectation: expected utility if the score is a gain, expected loss if it is a cost. The applied Bayesian layout computes that expectation from $p(x\mid d)$ after the actions and the utility have been written down, and it repeats the computation at each node of a tree. Medical calculations made the arithmetic public, by turning life expectancies and a discomfort penalty into one expected score per treatment. Sampling theory had already used the same word for an estimator: the risk function is the expected loss under repeated samples at a fixed parameter, and posterior expected loss is what selects a Bayes action once a posterior distribution is in hand. The two traditions share the average and differ in what is being averaged over.{{cite:gelman_bda2013}} (Ch. 9, §9.1, pp. 237–238; Ch. 9, §9.3, p. 245; Ch. 4, §4.4, p. 92)
