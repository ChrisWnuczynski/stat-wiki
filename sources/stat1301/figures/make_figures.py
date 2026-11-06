"""Draw the figures for the Data analysis chapters.

Run from anywhere: python sources/stat1301/figures/make_figures.py
It writes one PDF per figure next to this file. The build converts them to PNG.
Needs numpy, scipy, pandas and matplotlib. Random draws use fixed seeds.

The data are in ../data. heart.csv is the heart-failure clinical records data
of 299 patients (UCI Machine Learning Repository, CC BY 4.0). birthwt.csv is
the birthwt data of 189 births from the R package MASS.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
NAVY, RED, TAN, BLUE, GREY = "#1d4a7a", "#a83232", "#d6bf98", "#c9d6e6", "#8a8f98"

plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 10,
        "axes.edgecolor": "#444444",
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "grid.color": "#e3e6ea",
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "savefig.bbox": "tight",
    }
)

HEART = pd.read_csv(DATA / "heart.csv")
BIRTH = pd.read_csv(DATA / "birthwt.csv")


def save(fig, name):
    fig.savefig(HERE / f"{name}.pdf")
    plt.close(fig)


def strip(ax, groups, labels, rng, means=True):
    for j, g in enumerate(groups):
        g = np.asarray(g, float)
        ax.plot(j + rng.uniform(-0.08, 0.08, len(g)), g, "o", color=NAVY, ms=5, alpha=0.85)
        if means:
            ax.plot([j - 0.25, j + 0.25], [g.mean()] * 2, color=RED, lw=2)
    ax.set_xticks(range(len(groups)))
    ax.set_xticklabels(labels)


def two_sample_heights():
    rng = np.random.default_rng(1301)
    smoke = rng.normal(170, np.sqrt(200), 60)
    non = rng.normal(175, np.sqrt(100), 140)
    fig, ax = plt.subplots(figsize=(7, 2.8))
    bins = np.arange(130, 215, 4)
    ax.hist(non, bins=bins, color=BLUE, label="mother did not smoke (140)")
    ax.hist(smoke, bins=bins, color=RED, alpha=0.6, label="mother smoked (60)")
    ax.set_xlabel("height of son (cm)")
    ax.set_ylabel("count")
    ax.legend(loc="upper left")
    save(fig, "da-two-sample-heights")


def alice_strip():
    caf = [17, 22, 21, 16, 6, -2, 27, 15, 16, 20]
    dec = [4, 10, 7, -9, 5, 4, 5, 7, 6, 12]
    fig, ax = plt.subplots(figsize=(5, 3.0))
    strip(ax, [dec, caf], ["decaf", "caffeinated"], np.random.default_rng(3))
    ax.set_ylabel("change in heart rate (bpm)")
    save(fig, "da-alice-strip")


def anaemia_death():
    t = pd.crosstab(HEART.anaemia, HEART.DEATH_EVENT)
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.8))
    x = np.arange(2)
    axes[0].bar(x - 0.2, t[0], 0.4, color=BLUE, label="survived")
    axes[0].bar(x + 0.2, t[1], 0.4, color=RED, label="died")
    axes[0].set_ylabel("patients")
    axes[0].legend()
    p = t[1] / t.sum(axis=1)
    axes[1].bar(x, p, 0.5, color=RED)
    for xi, pi in zip(x, p):
        axes[1].text(xi, pi + 0.01, f"{pi:.3f}", ha="center")
    axes[1].set_ylabel("proportion who died")
    axes[1].set_ylim(0, 0.5)
    for ax in axes:
        ax.set_xticks(x)
        ax.set_xticklabels(["no anaemia", "anaemia"])
    fig.tight_layout()
    save(fig, "da-anaemia-death")


def creatinine_shape():
    sc = HEART.serum_creatinine.values
    fig, axes = plt.subplots(1, 3, figsize=(7.8, 2.8), gridspec_kw={"width_ratios": [0.6, 1.2, 1.2]})
    axes[0].boxplot(sc, widths=0.5, flierprops={"marker": "o", "ms": 3, "mfc": NAVY, "mec": NAVY},
                    medianprops={"color": RED})
    axes[0].set_xticks([])
    axes[0].set_ylabel("serum creatinine (mg/dL)")
    axes[1].hist(sc, bins=np.arange(0, 9.6, 0.25), density=True, color=BLUE)
    xs = np.linspace(0, 9.5, 400)
    axes[1].plot(xs, stats.gaussian_kde(sc)(xs), color=NAVY, lw=1.5)
    axes[1].set_xlabel("serum creatinine")
    axes[1].set_ylabel("density")
    ls = np.log10(sc)
    axes[2].hist(ls, bins=25, density=True, color=BLUE)
    xs = np.linspace(ls.min(), ls.max(), 300)
    axes[2].plot(xs, stats.gaussian_kde(ls)(xs), color=NAVY, lw=1.5)
    axes[2].set_xlabel(r"$\log_{10}$ serum creatinine")
    fig.tight_layout()
    save(fig, "da-creatinine-shape")


def creatinine_qq():
    sc = np.sort(HEART.serum_creatinine.values)
    n = len(sc)
    z = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.9))
    for ax, y, lab in ((axes[0], sc, "serum creatinine"), (axes[1], np.sort(1 / sc), "1 / serum creatinine")):
        ax.plot(z, y, "o", ms=3, color=NAVY)
        q1, q3 = np.quantile(y, [0.25, 0.75])
        slope = (q3 - q1) / (stats.norm.ppf(0.75) - stats.norm.ppf(0.25))
        ax.plot(z, np.median(y) + slope * z, color=RED, lw=1)
        ax.set_xlabel("standard normal quantile")
        ax.set_ylabel(lab)
    fig.tight_layout()
    save(fig, "da-creatinine-qq")


def creatinine_by_death():
    fig, ax = plt.subplots(figsize=(5, 3.0))
    groups = [HEART.serum_creatinine[HEART.DEATH_EVENT == k].values for k in (0, 1)]
    ax.boxplot(groups, widths=0.5, flierprops={"marker": "o", "ms": 3, "mfc": NAVY, "mec": NAVY},
               medianprops={"color": RED})
    ax.set_yscale("log")
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["survived", "died"])
    ax.set_ylabel("serum creatinine (mg/dL), log scale")
    save(fig, "da-creatinine-by-death")


def sodium_jitter():
    rng = np.random.default_rng(9)
    x, y = HEART.ejection_fraction.values, HEART.serum_sodium.values
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.9), sharey=True)
    axes[0].plot(x, y, "o", ms=3, color=NAVY, alpha=0.6)
    axes[0].set_title("as recorded", fontsize=10)
    axes[1].plot(x + rng.uniform(-1.2, 1.2, len(x)), y + rng.uniform(-0.4, 0.4, len(y)), "o", ms=3, color=NAVY, alpha=0.6)
    axes[1].set_title("jittered", fontsize=10)
    for ax in axes:
        ax.set_xlabel("ejection fraction (%)")
    axes[0].set_ylabel("serum sodium (mEq/L)")
    fig.tight_layout()
    save(fig, "da-sodium-jitter")


def power_by_n():
    n = np.arange(2, 61)
    power = [stats.nct.sf(stats.t.ppf(0.95, k - 1), k - 1, np.sqrt(k) * 0.5) for k in n]
    fig, ax = plt.subplots(figsize=(7, 2.8))
    ax.plot(n, power, color=NAVY, lw=1.8)
    ax.axhline(0.8, color=GREY, lw=0.9, ls="--")
    ax.plot([5, 27, 50], [power[3], power[25], power[48]], "o", color=RED, ms=4)
    for k, p in ((5, power[3]), (27, power[25]), (50, power[48])):
        ax.annotate(f"$n={k}$: {p:.2f}", (k, p), xytext=(k + 1.5, p - 0.12), fontsize=9, color=RED)
    ax.set_xlabel("sample size $n$")
    ax.set_ylabel("power")
    ax.set_ylim(0, 1.02)
    save(fig, "da-power-by-n")


def coldsore():
    cs = [[5, 8, 7, 7, 10, 8], [4, 6, 6, 3, 5, 6], [6, 4, 4, 5, 4, 3], [7, 4, 6, 6, 3, 5], [9, 3, 5, 7, 7, 6]]
    fig, ax = plt.subplots(figsize=(6, 3.0))
    strip(ax, cs, ["Placebo", "T2", "T3", "T4", "T5"], np.random.default_rng(11))
    ax.set_ylabel("days to heal")
    save(fig, "da-coldsore")


def interaction():
    w = np.array([9.18, 8.26, 8.57, 10.05, 8.92, 9.39, 11.23, 11.11, 9.72, 11.60, 9.83, 11.07,
                  9.69, 8.25, 9.83, 9.80, 10.90, 10.75, 12.13, 12.01, 9.67, 12.09, 10.15, 12.04,
                  7.87, 8.91, 7.78, 8.33, 8.18, 9.78, 9.38, 10.10, 10.90, 11.73, 8.86, 11.23]).reshape(3, 4, 3).mean(2)
    c = np.array([3.23, 3.20, 3.16, 2.99, 2.85, 2.77, 5.72, 5.77, 5.62,
                  6.78, 6.73, 6.79, 9.07, 9.09, 8.86, 8.12, 8.04, 8.31]).reshape(2, 3, 3).mean(2)
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.0))
    for i, col in enumerate((NAVY, RED, TAN)):
        axes[0].plot(range(1, 5), w[i], "-o", color=col, ms=4, label=f"fertilizer {i + 1}")
    axes[0].set_xticks(range(1, 5))
    axes[0].set_xlabel("region")
    axes[0].set_ylabel("mean wheat yield")
    axes[0].legend(fontsize=8)
    for i, (col, lab) in enumerate(((NAVY, "no pesticide"), (RED, "pesticide"))):
        axes[1].plot(range(3), c[i], "-o", color=col, ms=4, label=lab)
    axes[1].set_xticks(range(3))
    axes[1].set_xticklabels(["low", "medium", "high"])
    axes[1].set_xlabel("fertilizer")
    axes[1].set_ylabel("mean crop yield")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    save(fig, "da-interaction")


def pairs():
    d = pd.DataFrame({"age": HEART.age, r"log$_{10}$ creatinine": np.log10(HEART.serum_creatinine), "sodium": HEART.serum_sodium})
    k = d.shape[1]
    fig, axes = plt.subplots(k, k, figsize=(6.4, 6.0))
    for i in range(k):
        for j in range(k):
            ax = axes[i, j]
            if i == j:
                ax.hist(d.iloc[:, i], bins=20, color=BLUE)
                ax.set_title(d.columns[i], fontsize=9)
            else:
                ax.plot(d.iloc[:, j], d.iloc[:, i], "o", ms=1.8, color=NAVY, alpha=0.6)
            ax.tick_params(labelsize=7)
    fig.tight_layout()
    save(fig, "da-pairs")


def birthwt_interaction():
    fig, ax = plt.subplots(figsize=(7, 3.0))
    for s, col, lab in ((0, NAVY, "non-smokers"), (1, RED, "smokers")):
        g = BIRTH[BIRTH.smoke == s]
        ax.plot(g.age, g.bwt, "o", ms=3, color=col, alpha=0.6)
        fit = stats.linregress(g.age, g.bwt)
        xs = np.linspace(g.age.min(), g.age.max(), 50)
        ax.plot(xs, fit.intercept + fit.slope * xs, color=col, lw=1.8, label=f"{lab}: {fit.slope:+.1f} g per year")
    ax.set_xlabel("age of the mother (years)")
    ax.set_ylabel("birth weight (g)")
    ax.legend(loc="lower left", fontsize=9)
    save(fig, "da-birthwt-interaction")


def birthwt_residuals():
    b = BIRTH
    X = np.column_stack([np.ones(len(b)), b.smoke, b.age, b.lwt, b.race == 2, b.race == 3, b.ui, b.ht, b.smoke * b.age]).astype(float)
    y = b.bwt.values.astype(float)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    fit = X @ beta
    r = y - fit
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.9))
    axes[0].plot(fit, r, "o", ms=3, color=NAVY, alpha=0.7)
    axes[0].axhline(0, color=RED, lw=1)
    axes[0].set_xlabel("fitted birth weight (g)")
    axes[0].set_ylabel("residual (g)")
    rs = np.sort(r)
    z = stats.norm.ppf((np.arange(1, len(rs) + 1) - 0.5) / len(rs))
    axes[1].plot(z, rs, "o", ms=3, color=NAVY, alpha=0.7)
    axes[1].plot(z, rs.std(ddof=1) * z, color=RED, lw=1)
    axes[1].set_xlabel("standard normal quantile")
    axes[1].set_ylabel("residual (g)")
    fig.tight_layout()
    save(fig, "da-birthwt-residuals")


def chisq_simulation():
    rng = np.random.default_rng(100)
    counts = np.array([np.bincount(rng.integers(0, 10, 100), minlength=10) for _ in range(10000)])
    t = ((counts - 10) ** 2 / 10).sum(1)
    xs = np.linspace(0, 35, 400)
    fig, ax = plt.subplots(figsize=(7, 2.8))
    ax.hist(t, bins=60, range=(0, 35), density=True, color=BLUE)
    ax.plot(xs, stats.chi2.pdf(xs, 9), color=RED, lw=1.6, label=r"$\chi^2_9$ density")
    ax.set_xlabel("Pearson statistic $T$")
    ax.set_ylabel("density")
    ax.legend()
    save(fig, "da-chisq-simulation")


if __name__ == "__main__":
    for draw in (two_sample_heights, alice_strip, anaemia_death, creatinine_shape, creatinine_qq, creatinine_by_death,
                 sodium_jitter, power_by_n, coldsore, interaction, pairs, birthwt_interaction, birthwt_residuals,
                 chisq_simulation):
        draw()
    print("Figures written to", HERE)
