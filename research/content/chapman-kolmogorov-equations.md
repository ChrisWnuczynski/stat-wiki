## Lead context
The Chapman–Kolmogorov equations add the probabilities of every route a Markov chain can take between two times.

## Intuition — Stop in the middle, then continue
To be in state \(j\) after \(m+n\) steps, the chain is in some state \(k\) after \(m\) steps and then travels from \(k\) to \(j\) in the remaining \(n\) steps. The Markov property makes that second trip depend on the past only through \(k\). Adding the products over \(k\) is matrix multiplication of the two transition blocks. The same addition is what a two-step probability is when \(m=n=1\).

## Definition — The product of transition matrices
Let \(X_0,X_1,\ldots\) be a time-homogeneous Markov chain on a finite set, with transition matrix \(P\) given by \(P_{ij}=\mathbb{P}(X_{1}=j\mid X_0=i)\). The Chapman–Kolmogorov equations are
\[
\mathbb{P}(X_{m+n}=j\mid X_0=i)=\sum_k\mathbb{P}(X_m=k\mid X_0=i)\,\mathbb{P}(X_n=j\mid X_0=k),
\]
or, in matrices, \(P^{m+n}=P^m P^n\).

## Properties — Condition on the intermediate state
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Partition on the state at time \(m\):
\[
\mathbb{P}(X_{m+n}=j\mid X_0=i)
=\sum_k\mathbb{P}(X_{m+n}=j\mid X_m=k,X_0=i)\,\mathbb{P}(X_m=k\mid X_0=i).
\]
Time-homogeneous Markov transitions give \(\mathbb{P}(X_{m+n}=j\mid X_m=k,X_0=i)=\mathbb{P}(X_n=j\mid X_0=k)=P^n_{kj}\), and \(\mathbb{P}(X_m=k\mid X_0=i)=P^m_{ik}\). The sum is the \((i,j)\) entry of \(P^m P^n\). The case \(m=n=1\) is the square \(P^2\).
:::
:::

The identity is about the transition mechanism. It does not by itself say that \(P^n\) converges.

## Worked example — Two steps of a two-state chain
Let
\[
P=\begin{pmatrix}0.8&0.2\\0.4&0.6\end{pmatrix}.
\]
Then
\[
P^2=\begin{pmatrix}0.72&0.28\\0.56&0.44\end{pmatrix}.
\]
The entry \(0.28\) is the probability of going from state \(1\) to state \(2\) in two steps. The route through state \(1\) contributes \(0.8\times 0.2=0.16\), and the route through state \(2\) contributes \(0.2\times 0.6=0.12\). The sum is \(0.28\), which is the Chapman–Kolmogorov total.

**Your turn.** Starting from state \(2\), what is the probability of being in state \(1\) after two steps? Name the two routes.

::: {.callout-tip collapse="true" title="Answer"}
The probability is \(0.56\). The route through state \(1\) contributes \(0.4\times 0.8=0.32\). The route through state \(2\) contributes \(0.6\times 0.4=0.24\). The sum is \(0.56\), the \((2,1)\) entry of \(P^2\).
:::

## Connections — The distribution after \(n\) steps
If the row vector \(\pi^{(0)}\) is the distribution of \(X_0\), the distribution of \(X_n\) is \(\pi^{(0)}P^n\), and Chapman–Kolmogorov is the reason \(P^{m+n}\) can be built from \(P^m\) and \(P^n\). A [finite-state Markov chain](finite-state-markov-chain.qmd) is the process whose one-step conditional probabilities are the entries of \(P\). The [limiting distribution](limiting-distribution.qmd) is a different statement: it asks when the rows of \(P^n\) settle, which needs irreducibility and aperiodicity and is not part of the product identity.

## Check yourself — One step, and a three-step check
### After one step
Starting from state \(1\), what is \(\mathbb{P}(X_1=1)\)? What is \(\mathbb{P}(X_2=1)\)?

::: {.callout-tip collapse="true" title="Answer"}
\(\mathbb{P}(X_1=1)=0.8\), the \((1,1)\) entry of \(P\). \(\mathbb{P}(X_2=1)=0.72\), the \((1,1)\) entry of \(P^2\). The one-step probability is not the two-step probability.
:::

### A route of length three
Using \(P^2_{11}=0.72\) and \(P_{11}=0.8\), and \(P^2_{12}=0.28\) and \(P_{21}=0.4\), give \(\mathbb{P}(X_3=1\mid X_0=1)\).

::: {.callout-tip collapse="true" title="Answer"}
Condition on the state at time \(2\): \(0.72\times 0.8+0.28\times 0.4=0.576+0.112=0.688\). This is the \((1,1)\) entry of \(P^2 P\), which Chapman–Kolmogorov identifies with \(P^3\).
:::
