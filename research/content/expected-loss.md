## Lead context

Expected loss is the risk of a decision: the probability-weighted average of the loss of one action, given the information available when the action is chosen. The action with the smallest expected loss is the one the score recommends.{{cite:gelman_bda2013}} (§9.1, pp. 237–238) [Loss and risk](loss-and-risk.qmd) is the pair of objects used to judge a statistical procedure: a loss that scores an estimate when the parameter is known, and the risk function obtained by taking the expected loss of the procedure at a fixed parameter. Expected loss ranks actions. Loss and risk name that pair.

## Motivating example

A 95-year-old man with a lung tumour chooses radiotherapy, surgery, or no treatment. There is a 90 percent chance the tumour is malignant. If it is not, life expectancy is 34.8 months. If it is, radiotherapy gives 16.7 months, no treatment gives 5.6 months, and surgery kills immediately with probability 0.35 and otherwise follows a life expectancy of 20.3 months if the tumour is malignant. Treatment also costs a month of discomfort. Quality-adjusted life expectancy subtracts that month and averages over the malignancy:

$$
0.9\times 16.7+0.1\times 34.8-1=17.5
$$

months for radiotherapy, $13.5$ months for surgery, and $8.5$ months for no treatment. Radiotherapy is preferred. Writing the score as months forfeited, a loss, reverses the sign and leaves the ranking unchanged: the preferred action is the one whose expected loss is smallest. No single state, malignant or not, is treated as certain. The average is the decision.{{cite:gelman_bda2013}} (§9.3, p. 245)

## Intuition

A loss $L(x,d)$ charges action $d$ when the outcome is $x$. If $x$ is still random given $d$, the charge that guides the action is the mean of $L$, not the loss in the most dramatic state and not the loss in the most probable state. A small probability of a large loss can outweigh a likely small loss. Computing the mean forces that tradeoff into the open. In a tree, the mean at a later node is computed with the information available there, and the earlier node averages those later means, weighted by the probability of reaching them. The same construction with a utility $U$ maximises $E[U(x)\mid d]$ instead of minimising a loss. The two agree when the loss is the negative of the utility, up to a constant that does not change the ranking.{{cite:gelman_bda2013}} (§9.1, p. 238; §9.3, p. 245)

## Definition

Decision analysis under uncertainty has four steps. List the decisions $d$ and the outcomes $x$. For each $d$, specify the distribution $p(x\mid d)$. The decision itself is not given a probability. Map outcomes to a utility $U(x)$, and choose the $d$ that maximises the expected utility $E[U(x)\mid d]$. In a tree the expectation at each decision node is conditional on the information available at that node. The expected loss of $d$ is this expectation with the sign flipped,

$$
E\bigl(L(x,d)\mid d\bigr)=\int L(x,d)\,p(x\mid d)\,dx,
$$

with a sum in place of the integral when $x$ is discrete, and with $L=-U$. The recommended action is the one with the lowest expected loss. The expectation for a branch that says "measure, then act" is the expected loss of the policy that will actually be followed after the measurement. It is not the expected loss of measuring and then ignoring the result.{{cite:gelman_bda2013}} (§9.1, pp. 237–238; §9.4, p. 253)

When the action is a point report about a parameter, the loss is attached to the report. If the loss is quadratic, $l(\hat\theta,\theta)=(\hat\theta-\theta)^2$, the report that minimises the expected loss under the distribution calculated for $\theta$ is the mean of that distribution. A Bayes estimate for squared-error loss is the posterior mean, when the mean exists. Absolute loss selects a median. Those facts are about the average of the loss under the distribution in hand. The sampling risk $R(\theta,T)$ still depends on $\theta$ and is defined with the loss on the loss-and-risk page.{{cite:dodge2008}} (p. 34){{cite:gelman_bda2013}} (Ch. 4, Exercise 6, p. 99)

## Properties

Expected loss is linear in the mixture of outcomes. In the tumour example the radiotherapy score $0.9\times 16.7+0.1\times 34.8-1$ is exactly that mixture, with the final $-1$ a sure loss from discomfort. Changing the probability $0.9$ changes the expected loss without changing the loss attached to either state. The surgery figure $13.5$ and the no-treatment figure $8.5$ are the same kind of mixture, with surgery's immediate death contributing a term $0.35\times 0$.{{cite:gelman_bda2013}} (§9.3, p. 245)

The law of total expectation is what makes a tree computable. The expected value of "test, then act optimally" equals the average, over the test result, of the expected value of the optimal action given that result, plus any loss charged by the test itself. If every result leads to the same treatment, the test cannot improve on taking that treatment immediately once the test itself has a cost. Bronchoscopy in the same example has a positive chance of death and, on the probabilities used there, still leads to radiotherapy whether the test is positive or negative. The quality-adjusted value of testing and then choosing is $0.632\times 15.0+0.368\times 19.5=16.656$ months, reported as $16.6$, against $17.5$ for radiotherapy with no test. The test adds risk and does not change the action.{{cite:gelman_bda2013}} (§9.3, p. 245)

A quadratic loss on a parameter report selects one action, the mean, because the expectation has already been taken under the distribution calculated for the parameter. That is a property of the posterior, or of whatever distribution the loss is averaged over. It does not say that the sample mean minimises squared-error risk at every parameter value. That comparison is the sampling risk on the loss-and-risk page.{{cite:dodge2008}} (p. 34)

## Worked example

Suppose an action "treat" has loss $1$ if the condition is present and loss $8$ if it is absent, and an action "watch" has loss $10$ if present and loss $0$ if absent. At a base rate $p=0.2$,

$$
E(L\mid\text{treat})=0.2\times 1+0.8\times 8=6.6,
$$
$$
E(L\mid\text{watch})=0.2\times 10+0.8\times 0=2.
$$

Watching has the smaller expected loss. The most probable state is "absent," and watching is also best in that state, but that coincidence is not the reason. The reason is the average. The losses are a utility with the sign flipped, so the same arithmetic maximises expected utility if every loss is multiplied by $-1$.{{cite:gelman_bda2013}} (§9.1, p. 238)

**Your turn.** Keep the same losses and set the base rate to $0.7$. Which action has the smaller expected loss, and what are the two values?

::: {.callout-tip collapse="true" title="Answer"}
Treating has expected loss $0.7\times 1+0.3\times 8=3.1$. Watching has expected loss $0.7\times 10=7$. Treating is smaller. The ranking flipped because the base rate changed, not because the losses changed.
:::

## Assumptions and limits

The expectation exists only when the loss has a finite mean under $p(x\mid d)$. A utility or loss that the decision maker does not accept will rank actions they would not rank. The tumour calculation uses life expectancies and a one-month discomfort penalty taken as inputs. Changing either input changes the expected score. The tree calculation for a later action assumes that the stated policy will be followed. An expected loss computed for "measure, then remediate if high" does not apply to a household that will remediate regardless of the measurement. In the radon analysis the expected loss of the measurement branch is defined as the average of the better of the two later actions, and that average is the right number only for someone who will take the better action.{{cite:gelman_bda2013}} (§9.4, p. 253; §9.3, p. 245)

Quadratic loss selects the mean only when the mean exists. A distribution of the parameter with no mean has no Bayes estimate under that loss. Absolute loss selects a median, which can exist when the mean does not. The choice of loss is part of the decision, not a property of the parameter.{{cite:gelman_bda2013}} (Ch. 4, Exercise 6, p. 99){{cite:dodge2008}} (p. 34)

## Connections

A [decision problem](decision-problem.qmd) names the actions whose expected losses are compared. The [base rate](base-rate.qmd) is a probability weight inside the average, as $0.2$ and $0.7$ are in the worked example. [Loss and risk](loss-and-risk.qmd) name the loss function and the sampling risk $R(\theta,T)$ of a procedure. [Mean squared error](mean-squared-error.qmd) is that risk when the loss is squared error. The quadratic calculation above is the calculated-distribution version of squared error: it selects a mean. The sampling identity of squared-error risk with mean squared error belongs to [loss and risk](loss-and-risk.qmd). Choosing a point estimate by minimising an expected loss is the decision-theoretic step in the Bayesian calculation.{{cite:dodge2008}} (pp. 33–34){{cite:gelman_bda2013}} (§9.1, pp. 237–238)
