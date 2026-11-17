## Lead context
The extinction probability of a branching process is the probability that some generation is empty, after which every later generation stays empty.

## Motivating example
Offspring probabilities $1/4$, $0$ and $3/4$ have mean $3/2$. The generating function $1/4+(3/4)s^2$ has fixed points $1/3$ and $1$. The extinction probability is the smaller root.

## Intuition — The offspring mean decides whether extinction is certain
Each individual has the same offspring law, independently of the others. If the mean number of offspring is below \(1\), the expected generation size shrinks geometrically and the probability of still being alive tends to \(0\). If the mean is above \(1\) and there is a real chance of having no children, extinction is still possible, but it is no longer certain: its probability is a root of the offspring generating function, strictly below \(1\). The deterministic law that always produces exactly one child has mean \(1\) and never dies.{{cite:durrett2019}} (Thm. 4.3.10, p. 231){{cite:durrett2019}} (Thm. 4.3.12, p. 232)

## Definition — The smallest fixed point of the generating function
Let \(f(s)=\sum_k p_k s^k\) be the probability generating function of the offspring law, and let \(Z_n\) be the size of generation \(n\), with \(Z_0=1\). Write \(q_n=\mathrm{P}(Z_n=0)\). Then \(q_{n+1}=f(q_n)\), the sequence increases, and its limit \(q=\mathrm{P}(Z_n=0\text{ for some }n)\) satisfies \(q=f(q)\). It is the smallest root in \([0,1]\).

## Properties — Subcritical extinction, and the supercritical root
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The generation sizes satisfy \(\mathrm{E}(Z_n)=m^n\) when \(m=\mathrm{E}(\xi)\) is the offspring mean and \(Z_0=1\). On \(\{Z_n>0\}\) one has \(Z_n\ge 1\), so \(\mathrm{P}(Z_n>0)\le m^n\). If \(m<1\) this bound tends to \(0\), and extinction has probability \(1\).{{cite:durrett2019}} (Thm. 4.3.10, p. 231)

Condition on the first generation. If it has size \(k\), the process dies out if and only if \(k\) independent copies die out, an event of probability \(q^k\). Therefore \(q=\sum_k p_k q^k=f(q)\). If \(m>1\), then \(f'(1)=m>1\) and \(f''(s)>0\) on \((0,1)\) whenever some \(p_k>0\) for a \(k\ge 2\). So \(f(s)<s\) on a left neighbourhood of \(1\), while \(f(0)=p_0>0\), and there is a root in \([0,1)\). Strict convexity makes it unique.{{cite:durrett2019}} (Thm. 4.3.12, p. 232)
:::
:::

## Worked example — A quadratic with mean \(3/2\)
Take \(p_0=1/4\), \(p_1=0\) and \(p_2=3/4\). The mean is \(2\cdot 3/4=3/2>1\), and
\[
f(s)=\frac14+\frac34 s^2.
\]
The fixed-point equation \(\frac34 s^2-s+\frac14=0\) is \(3s^2-4s+1=0\), or \((3s-1)(s-1)=0\). The roots are \(1/3\) and \(1\). The extinction probability is the smaller one, \(1/3\). Check: \(f(1/3)=1/4+(3/4)(1/9)=1/3\).

For a comparison, \(p_0=p_1=1/2\) has mean \(1/2<1\), so the bound \(\mathrm{P}(Z_n>0)\le 2^{-n}\) forces extinction probability \(1\). The generating function \(f(s)=(1+s)/2\) has no root in \([0,1)\) other than the failure of the supercritical hypothesis: its only fixed point in \([0,1]\) is \(1\).

**Your turn.** Take \(p_0=1/2\), \(p_1=1/4\), \(p_2=1/4\). Find the mean, and solve \(f(s)=s\).

::: {.callout-tip collapse="true" title="Answer"}
The mean is \(1/4+2/4=3/4<1\), so the extinction probability is \(1\) without solving further. The equation \(\frac12+\frac14 s+\frac14 s^2=s\) rearranges to \(s^2-3s+2=0\), or \((s-1)(s-2)=0\). The only root in \([0,1]\) is \(1\).
:::

## Connections — The mean, the generating function, and the one-child exception
The [Galton–Watson process](galton-watson-process.qmd) is the sequence \(Z_n\). The mean \(m\) is the derivative \(f'(1)\). When \(m=1\) and the offspring law is not concentrated at \(1\), extinction is still certain; the one-child law is the exception, with extinction probability \(0\).{{cite:durrett2019}} (Thm. 4.3.11, p. 231) The fixed-point picture is the whole criterion: certain extinction when the smallest root is \(1\), and a smaller root when the mean exceeds \(1\).

## Check yourself
Offspring probabilities \(p_0=1/8\), \(p_1=1/8\), \(p_2=3/4\). Is the mean above \(1\)?

::: {.callout-tip collapse="true" title="Answer"}
The mean is \(1/8+2\cdot 3/4=1/8+3/2=13/8>1\). Extinction is not certain. The probability itself is the smaller root of \(f(s)=s\), not the mean.
:::

If \(p_0=0\) and \(p_2=1\), what is the extinction probability, and what is the mean?

::: {.callout-tip collapse="true" title="Answer"}
Every individual has two children, so the mean is \(2\) and generation \(n\) has size \(2^n\). The process never hits \(0\), and the extinction probability is \(0\). The root \(s=0\) of \(f(s)=s^2\) is that probability.
:::
