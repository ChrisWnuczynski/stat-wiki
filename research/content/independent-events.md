## Motivating example
A machine has two sensors. Suppose the first misses a fault with probability $0.1$ and the second with probability $0.2$. Multiplying these numbers gives $0.02$ only under an independence model for their misses. A common power failure or shared temperature effect can invalidate that multiplication. Independence specifies the joint probability law; separate marginal failure rates do not determine it.{{cite:dodge2008}} (pp. 254–255)

The mathematical question is precise: does information that one event occurred change the probability of the other? For an event of positive probability, conditional probabilities answer that question. The product definition also handles probability-zero events, where elementary conditioning would require division by zero.{{cite:durrett2019}} (§2.1, pp. 43–44)

## Definition — Products for every finite subcollection
For two events $A$ and $B$, independence means $P(A\cap B)=P(A)P(B)$. When $P(B)>0$, this is equivalent to $P(A\mid B)=P(A)$. For a family, mutual independence requires this factorization for every finite subcollection, including pairs, triples and larger selections. Pairwise independence imposes only the pair conditions. Those two requirements coincide for two events and can diverge for three.{{cite:durrett2019}} (§2.1, pp. 43–45)

Probabilities zero and one are boundary cases rather than exceptions to the definition. If $P(A)=0$, monotonicity gives $P(A\cap B)=0$ for every $B$. If $P(A)=1$, removing $A^c$ does not change the probability of $B$. Either way, $A$ is independent of every event. Such events need not be literally empty or equal to the entire sample space.

## Properties — Complements preserve the factorization
Subtract the intersection probability from $P(B)$:
$$P(A^c\cap B)=P(B)-P(A\cap B)=(1-P(A))P(B).$$
Thus $A^c$ and $B$ are independent whenever $A$ and $B$ are. Repeating this calculation handles $A$ with $B^c$, and then both complements. For a mutually independent finite family, the same repeated subtraction establishes independence after any selection of events is replaced by its complement.{{cite:durrett2019}} (§2.1, thm. 2.1.2, p. 44)

Disjoint events with strictly positive probabilities cannot be independent: their intersection probability is zero while the product of their probabilities is positive. Conversely, independence need not mean geometric or verbal separation. Two events can refer to the same random experiment and still satisfy the product identity. The outcome space and its probability measure decide the issue.{{cite:dodge2008}} (pp. 254–255)

For indicators $I_A$ and $I_B$, $\E(I_AI_B)=P(A\cap B)$ and $\E(I_A)\E(I_B)=P(A)P(B)$. Hence their covariance is zero exactly when these two events are independent. This equivalence for binary indicators does not extend to arbitrary random variables: a zero covariance usually tests only one numerical aspect of their joint distribution.{{cite:durrett2019}} (§2.1, thm. 2.1.2 and ex. 2.1.14, pp. 44, 49)

## Worked example — Pairwise independence without joint independence
Toss two fair independent coins and label outcomes $HH,HT,TH,TT$, each with probability $1/4$. Let $A$ be heads on the first coin, $B$ heads on the second, and $C$ agreement between the coins. Each event has probability $1/2$. Each pairwise intersection contains one outcome, so its probability is $1/4=(1/2)(1/2)$. But $A\cap B\cap C=\{HH\}$ has probability $1/4$, whereas the product of the three probabilities is $1/8$. The events are pairwise independent and fail mutual independence. This finite construction directly checks the distinction in the definition.{{cite:durrett2019}} (§2.1, definition of independent collections, pp. 44–45)

Conditioning on $C$ leaves two equally likely outcomes, $HH$ and $TT$. Within that restricted space $P(A\mid C)=P(B\mid C)=1/2$, but $P(A\cap B\mid C)=1/2$. Thus the first two events, independent without conditioning, become dependent after conditioning on agreement. Conditional independence is a different statement involving the conditional measure.

**Your turn.** Using the same four outcomes, calculate $P(A\cap C^c)$ and decide whether $A$ and $C^c$ are independent.

::: {.callout-tip collapse="true" title="Answer"}
Their intersection is the single outcome $HT$, so its probability is $1/4$. Both marginal probabilities are $1/2$, and their product is $1/4$. They are independent.
:::

## Statistical use — State the probability model before multiplying
For mutually independent component failures with probability $q$, a pair fails together with probability $q^2$, and two independent such pairs both avoid total failure with probability $(1-q^2)^2$. The algebra is useful only after identifying which component events and groups are independent. Dependence caused by a shared environment is a change to the probability model, even when the marginal rate $q$ is unchanged.{{cite:durrett2019}} (§2.1, thm. 2.1.10, pp. 47–48)

Independence also simplifies repeated-trial likelihoods into products. Drawing with replacement from a stable population can motivate such a model; drawing without replacement from a finite collection generally changes later conditional probabilities. The dependence can be checked by comparing a conditional probability with its marginal rather than appealing to the physical act of making two draws.{{cite:dodge2008}} (pp. 255–256)

Pairwise products can all hold while the probability of the triple intersection is twice the product of the three separate probabilities, as in the two-coin agreement example.
