"""Deterministic PDF/PMF and CDF previews for the distribution catalogue."""

from __future__ import annotations

import math
import os
from pathlib import Path


def write_plots(facts: dict, target: Path) -> None:
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/statwiki-matplotlib")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats

    target.mkdir(parents=True, exist_ok=True)
    discrete = {"bernoulli", "binom", "compoisson", "geom", "hypergeom", "nbinom", "poisson"}
    for slug, item in facts.items():
        spec = item["plot"]
        lo, hi = spec["domain"]
        kind = spec["scipy"]
        x = np.arange(int(lo), int(hi) + 1) if kind in discrete else np.linspace(lo, hi, 500)
        if kind == "compoisson":
            lam, nu = spec["args"]
            weights = np.array([math.exp(k * math.log(lam) - nu * math.lgamma(k + 1)) for k in range(120)])
            weights /= weights.sum()
            y_pdf = weights[x.astype(int)]
            y_cdf = np.cumsum(weights)[x.astype(int)]
        else:
            law = getattr(stats, kind)(*spec["args"])
            y_pdf = law.pmf(x) if kind in discrete else law.pdf(x)
            y_cdf = law.cdf(x)
        for label, y in (("pdf", y_pdf), ("cdf", y_cdf)):
            fig, ax = plt.subplots(figsize=(4.6, 2.7))
            if kind in discrete:
                ax.vlines(x, 0, y, color="#2563a6", linewidth=1.8)
                ax.plot(x, y, "o", color="#2563a6", markersize=3)
            else:
                ax.plot(x, y, color="#2563a6", linewidth=2)
            ax.set(xlabel="x", ylabel="PMF" if kind in discrete and label == "pdf" else label.upper(),
                   title=f"{item['name']} distribution")
            ax.set_xlim(lo, hi)
            ax.set_ylim(bottom=0, top=1.04 if label == "cdf" else None)
            ax.grid(alpha=0.18)
            fig.tight_layout()
            fig.savefig(target / f"{slug}-{label}.png", dpi=120)
            plt.close(fig)
