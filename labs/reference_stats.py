#!/usr/bin/env python3
"""SciPy and NumPy reference for the laboratory distribution functions.

Writes labs/fixtures/stats-reference.json. Does not import the JavaScript.
A short Node run checks that the Python copy of mulberry32 matches
labs/stat-math.js, the same way the kernel-density reference checks R.
The distribution numbers themselves come from SciPy.
"""

from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.linalg import null_space
from scipy.special import betaln, gammaln

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "fixtures" / "stats-reference.json"
JS = ROOT / "stat-math.js"

# |JS - reference| <= abs + rel * |reference|, except where a case says otherwise.
TOLERANCES = {
    "lgammaAbs": 1e-9,
    "lgammaRel": 1e-12,
    "betaAbs": 1e-9,
    "betaRel": 1e-8,
    "quantileAbs": 1e-8,
    "quantileRel": 1e-6,
    "pmfAbs": 1e-12,
    "pmfRel": 1e-9,
    "stationaryAbs": 1e-9,
    "coverageAbs": 1e-8,
    "intervalAbs": 1e-7,
    "sampleAbs": 1e-9,
    "coverTol": 1e-10,
    "note": (
        "lgammaAbs/Rel: log-gamma and log-beta. "
        "betaAbs/Rel: beta pdf, cdf and survival. "
        "quantileAbs/Rel: beta, normal and t quantiles, and normal cdf. "
        "pmfAbs/Rel: binomial and beta-binomial pmf. "
        "stationaryAbs: |JS stationary - NumPy null-space vector|. "
        "coverageAbs: exact coverage probabilities. "
        "intervalAbs: interval endpoints on the hand samples and the Wald and Wilson formulas. "
        "sampleAbs: the shared mulberry32 / Box-Muller draws. "
        "coverTol: an endpoint counts as covering when it is within this distance of the truth."
    ),
}

BETA_SHAPES = [(0.5, 0.5), (0.6, 0.6), (1, 1), (2, 5), (8, 12), (0.3, 4), (4, 0.3), (500, 500), (500, 2), (2, 500)]
BETA_X = [0.0, 1e-6, 0.01, 0.1, 0.5, 0.9, 0.99, 1 - 1e-6, 1.0]
BETA_P = [1e-8, 1e-4, 0.01, 0.025, 0.1, 0.5, 0.9, 0.975, 0.99, 1 - 1e-4]
NORMAL_Z = [-8, -7, -5, -3, -1.96, -1, 0, 0.5, 1, 1.96, 3, 5, 7, 8]
NORMAL_P = [1e-12, 1e-10, 1e-8, 1e-6, 0.001, 0.025, 0.05, 0.1, 0.5, 0.9, 0.95, 0.975, 0.995, 1 - 1e-6, 1 - 1e-8, 1 - 1e-10, 1 - 1e-12]
T_DF = [1, 2, 5, 30, 1000]
T_VALUES = [-30, -10, -2, -1, 0, 1, 2, 3, 10]
T_P = [1e-6, 0.025, 0.05, 0.5, 0.95, 0.975, 1 - 1e-6]

THIRD = 1.0 / 3.0
HALF = 0.5
STEPPING = [
    [0, THIRD, 0, THIRD, THIRD, 0],
    [HALF, 0, HALF, 0, 0, 0],
    [HALF, 0, 0, HALF, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, HALF, 0, HALF],
    [0, 0, HALF, 0, HALF, 0],
]
WEATHER = [[0.8, 0.2], [0.4, 0.6]]
CYCLE = [[0, 1], [1, 0]]
STAY = 0.96
MOVE = (1.0 - STAY) / 2.0
STICKY = [[STAY if i == j else MOVE for j in range(3)] for i in range(3)]
REDUCIBLE = [
    [0, 0.5, 0, 0.5],
    [0, 0.8, 0.2, 0],
    [0, 0.4, 0.6, 0],
    [0, 0, 0, 1],
]
# A transient pair, used to check absorption rather than a preset.
ABSORBING = [
    [0, 1, 0, 0],
    [0, 0, 0.5, 0.5],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]


def to_int32(value: int) -> int:
    value &= 0xFFFFFFFF
    return value - 0x100000000 if value >= 0x80000000 else value


def to_uint32(value: int) -> int:
    return value & 0xFFFFFFFF


def bitxor(left: int, right: int) -> int:
    return to_int32(to_uint32(left) ^ to_uint32(right))


def mulberry32(seed: int):
    """The generator in labs/stat-math.js. Uniforms lie in (0, 1)."""
    state = to_int32(seed)

    def uniform() -> float:
        nonlocal state
        state = to_int32(state + 0x6D2B79F5)
        mixed = bitxor(state, to_uint32(state) >> 15)
        generated = to_int32(mixed * to_int32(1 | to_uint32(state)))
        mixed = bitxor(generated, to_uint32(generated) >> 7)
        product = to_int32(mixed * to_int32(61 | to_uint32(generated)))
        generated = bitxor(to_int32(generated + product), generated)
        return (to_uint32(bitxor(generated, to_uint32(generated) >> 14)) + 0.5) / 4294967296

    return uniform


def normal_stream(uniform):
    spare = None

    def nxt() -> float:
        nonlocal spare
        if spare is not None:
            out = spare
            spare = None
            return out
        radius = math.sqrt(-2.0 * math.log(uniform()))
        angle = 2.0 * math.pi * uniform()
        spare = radius * math.sin(angle)
        return radius * math.cos(angle)

    return nxt


def node_generator() -> dict:
    script = """
import { mulberry32, normalStream } from "./stat-math.js";
const uniforms = mulberry32(2026);
const seq = Array.from({ length: 8 }, () => uniforms());
const normals = normalStream(mulberry32(2026));
const draws = Array.from({ length: 6 }, () => normals());
console.log(JSON.stringify({ seq, draws }));
"""
    completed = subprocess.run(
        ["node", "--input-type=module", "-e", script],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(completed.stderr[-2000:])
    return json.loads(completed.stdout)


def stationary(matrix: list[list[float]]) -> dict:
    array = np.asarray(matrix, dtype=float)
    basis = null_space(array.T - np.eye(len(array)))
    vectors = []
    for column in range(basis.shape[1]):
        vector = basis[:, column]
        if vector.sum() < 0:
            vector = -vector
        total = vector.sum()
        vectors.append((vector / total).tolist())
    return {"nullity": int(basis.shape[1]), "vectors": vectors}


def subclass_stationary(matrix: list[list[float]], states: list[int]) -> list[float]:
    """Stationary distribution of one closed class, zeros elsewhere. NumPy solve."""
    block = np.asarray([[matrix[i][j] for j in states] for i in states], dtype=float)
    size = len(states)
    system = block.T - np.eye(size)
    system[-1, :] = 1
    rhs = np.zeros(size)
    rhs[-1] = 1
    local = np.linalg.solve(system, rhs)
    full = np.zeros(len(matrix))
    for index, state in enumerate(states):
        full[state] = local[index]
    full /= full.sum()
    return full.tolist()


def hits(lower: float, upper: float, truth: float) -> bool:
    tol = TOLERANCES["coverTol"]
    return lower - tol <= truth <= upper + tol


def proportion_interval(successes: int, n: int, method: str, level: float) -> tuple[float, float]:
    z = float(stats.norm.ppf((1 + level) / 2))
    estimate = successes / n
    if method == "wald":
        se = math.sqrt(estimate * (1 - estimate) / n)
        return estimate - z * se, estimate + z * se
    z2 = z * z
    denom = 1 + z2 / n
    centre = (estimate + z2 / (2 * n)) / denom
    half = z * math.sqrt(estimate * (1 - estimate) / n + z2 / (4 * n * n)) / denom
    return centre - half, centre + half


def proportion_coverage(n: int, p: float, level: float, method: str) -> float:
    total = 0.0
    for successes in range(n + 1):
        lower, upper = proportion_interval(successes, n, method, level)
        if hits(lower, upper, p):
            total += float(stats.binom.pmf(successes, n, p))
    return total


def mean_interval(values: list[float], method: str, level: float) -> tuple[float, float, float]:
    array = np.asarray(values, dtype=float)
    n = len(array)
    mean = float(array.mean())
    s = float(array.std(ddof=1))
    if method == "t":
        critical = float(stats.t.ppf((1 + level) / 2, n - 1))
    else:
        critical = float(stats.norm.ppf((1 + level) / 2))
    half = critical * s / math.sqrt(n)
    return mean - half, mean + half, mean


def main() -> None:
    node = node_generator()
    uniforms = mulberry32(2026)
    py_seq = [uniforms() for _ in range(8)]
    normals = normal_stream(mulberry32(2026))
    py_normals = [normals() for _ in range(6)]
    for got, expected in zip(py_seq, node["seq"], strict=True):
        if got != expected:
            raise SystemExit(f"mulberry32 disagreed with stat-math.js: {got} vs {expected}")
    for got, expected in zip(py_normals, node["draws"], strict=True):
        if abs(got - expected) > 1e-12:
            raise SystemExit(f"Box-Muller disagreed with stat-math.js: {got} vs {expected}")

    lgamma_rows = [{"x": x, "value": float(gammaln(x))} for x in (0.1, 0.5, 1, 1.5, 2, 3, 5, 10, 20, 50, 100, 500, 1000)]
    lbeta_rows = [{"a": a, "b": b, "value": float(betaln(a, b))} for a, b in BETA_SHAPES + [(0.1, 0.2), (1, 100), (35, 75)]]

    beta_pdf = []
    beta_cdf = []
    beta_sf = []
    for a, b in BETA_SHAPES:
        for x in BETA_X:
            pdf = float(stats.beta.pdf(x, a, b))
            beta_pdf.append({"a": a, "b": b, "x": x, "value": None if math.isinf(pdf) else pdf, "infinite": math.isinf(pdf)})
            beta_cdf.append({"a": a, "b": b, "x": x, "value": float(stats.beta.cdf(x, a, b))})
            beta_sf.append({"a": a, "b": b, "x": x, "value": float(stats.beta.sf(x, a, b))})
    beta_ppf = [
        {"a": a, "b": b, "p": p, "value": float(stats.beta.ppf(p, a, b))}
        for a, b in BETA_SHAPES
        for p in BETA_P
    ]

    normal_cdf = [{"z": z, "value": float(stats.norm.cdf(z))} for z in NORMAL_Z]
    normal_ppf = [{"p": p, "value": float(stats.norm.ppf(p))} for p in NORMAL_P]
    t_cdf = [{"t": t, "df": df, "value": float(stats.t.cdf(t, df))} for df in T_DF for t in T_VALUES]
    t_ppf = [{"p": p, "df": df, "value": float(stats.t.ppf(p, df))} for df in T_DF for p in T_P]

    binom_rows = []
    for n, p in ((1, 0.0), (1, 1.0), (10, 0.3), (10, 0.0), (10, 1.0), (20, 0.1), (100, 0.03), (500, 0.5)):
        ks = sorted({0, 1, n // 2, n, max(0, int(round(n * p)))})
        for k in ks:
            if 0 <= k <= n:
                binom_rows.append({"k": k, "n": n, "p": p, "value": float(stats.binom.pmf(k, n, p))})

    beta_binom_rows = []
    for m, a, b in ((5, 8, 12), (5, 4, 8), (10, 0.6, 0.6), (1, 1, 1), (20, 2, 2), (5, 0.5, 3), (8, 35, 75)):
        for k in range(m + 1):
            beta_binom_rows.append({"k": k, "m": m, "a": a, "b": b, "value": float(stats.betabinom.pmf(k, m, a, b))})

    beta_lab = []
    for alpha, beta, n, x, level, future in (
        (5, 5, 10, 3, 0.95, 5),
        (1, 1, 10, 3, 0.95, 5),
        (0.6, 0.6, 10, 3, 0.95, 5),
        (5, 5, 100, 30, 0.95, 5),
        (2, 2, 10, 8, 0.95, 5),
        (5, 5, 0, 0, 0.95, 1),
        (0.5, 2, 4, 1, 0.9, 3),
        (2, 0.5, 4, 4, 0.99, 2),
    ):
        post_a, post_b = alpha + x, beta + n - x
        weight = (alpha + beta) / (alpha + beta + n)
        proportion = None if n == 0 else x / n
        post_mean = post_a / (post_a + post_b)
        blended = post_mean if proportion is None else weight * (alpha / (alpha + beta)) + (1 - weight) * proportion
        if abs(blended - post_mean) > 1e-12:
            raise SystemExit("posterior mean is not the blended mean")
        mode = None
        if post_a > 1 and post_b > 1:
            mode = (post_a - 1) / (post_a + post_b - 2)
        elif post_a <= 1 and post_b > 1:
            mode = 0
        elif post_a > 1 and post_b <= 1:
            mode = 1
        tail = (1 - level) / 2
        pred_mean, pred_var = stats.betabinom.stats(future, post_a, post_b, moments="mv")
        plug_mean = future * post_mean
        beta_lab.append(
            {
                "alpha": alpha,
                "beta": beta,
                "n": n,
                "x": x,
                "level": level,
                "future": future,
                "postA": post_a,
                "postB": post_b,
                "postMean": post_mean,
                "postSd": math.sqrt(post_a * post_b / ((post_a + post_b) ** 2 * (post_a + post_b + 1))),
                "postMode": mode,
                "lower": float(stats.beta.ppf(tail, post_a, post_b)),
                "upper": float(stats.beta.ppf(1 - tail, post_a, post_b)),
                "weight": weight,
                "blended": blended,
                "proportion": proportion,
                "predMean": float(pred_mean),
                "predVar": float(pred_var),
                "plugVar": float(future * post_mean * (1 - post_mean)),
            }
        )

    chains = []
    specs = [
        ("stepping", STEPPING, [[0, 1, 2, 3, 4, 5]], [12, 4, 20, 25, 22, 36]),
        ("weather", WEATHER, [[0, 1]], [2, 1]),
        ("cycle", CYCLE, [[0, 1]], [1, 1]),
        ("sticky", STICKY, [[0, 1, 2]], [1, 1, 1]),
        ("reducible", REDUCIBLE, [[1, 2], [3]], None),
        ("absorbing", ABSORBING, [[2], [3]], None),
    ]
    for name, matrix, classes, exact_counts in specs:
        array = np.asarray(matrix, dtype=float)
        space = stationary(matrix)
        extremal = [subclass_stationary(matrix, states) for states in classes]
        for vector in extremal:
            residual = np.asarray(vector) @ array - np.asarray(vector)
            if np.max(np.abs(residual)) > 1e-9:
                raise SystemExit(f"{name} subclass stationary is not stationary")
        if exact_counts is not None:
            exact = (np.asarray(exact_counts, dtype=float) / sum(exact_counts)).tolist()
            if np.max(np.abs(np.asarray(extremal[0]) - np.asarray(exact))) > 1e-9:
                raise SystemExit(f"{name} null-space vector missed the exact stationary distribution")
            if space["nullity"] != 1:
                raise SystemExit(f"{name} nullity was {space['nullity']}")
        else:
            exact = None
            if space["nullity"] != len(classes):
                raise SystemExit(f"{name} nullity {space['nullity']} != {len(classes)} closed classes")
        powers = []
        for steps in (1, 2, 10):
            powered = np.linalg.matrix_power(array, steps)
            powers.append({"steps": steps, "rows": powered.tolist()})
        chains.append(
            {
                "name": name,
                "matrix": matrix,
                "closedClasses": classes,
                "nullity": space["nullity"],
                "nullVectors": space["vectors"],
                "extremal": extremal,
                "exactPi": exact,
                "powers": powers,
            }
        )

    stepping = np.asarray(STEPPING, dtype=float)
    two = stepping @ stepping
    expected_two = np.array([1 / 6, 0, 1 / 6, 1 / 6, 0, 1 / 2])
    if np.max(np.abs(two[0] - expected_two)) > 1e-12:
        raise SystemExit(f"stepping-stone P^2 row 1 was {two[0]}")
    ten = np.linalg.matrix_power(stepping, 10)
    if round(float(ten[0, 0]), 4) != 0.1049:
        raise SystemExit(f"P^10 back on stone 1 was {ten[0, 0]}, not 0.1049 to four decimals")
    weather = np.asarray(WEATHER, dtype=float)
    weather_two = weather @ weather
    if abs(float(weather_two[1, 0]) - 0.56) > 1e-12:
        raise SystemExit(f"weather P^2 wet to dry was {weather_two[1, 0]}")
    rate = sorted((abs(value) for value in np.linalg.eigvals(weather)), reverse=True)[1]
    if abs(rate - 0.4) > 1e-12:
        raise SystemExit(f"weather rate was {rate}")

    z_with_s = []
    for n in (2, 5, 10, 20, 30, 51, 100):
        for level in (0.9, 0.95, 0.99):
            z = float(stats.norm.ppf((1 + level) / 2))
            z_with_s.append({"n": n, "level": level, "value": float(2 * stats.t.cdf(z, n - 1) - 1)})

    proportion_rows = []
    for n, p, level, method in (
        (10, 0.5, 0.95, "wald"),
        (10, 0.5, 0.95, "wilson"),
        (10, 0.1, 0.95, "wald"),
        (10, 0.1, 0.95, "wilson"),
        (10, 0.05, 0.95, "wald"),
        (10, 0.05, 0.95, "wilson"),
        (20, 0.3, 0.95, "wald"),
        (20, 0.3, 0.95, "wilson"),
        (20, 0.9, 0.9, "wald"),
        (20, 0.9, 0.9, "wilson"),
        (5, 0.2, 0.99, "wald"),
        (5, 0.2, 0.99, "wilson"),
        (10, 0.0, 0.95, "wald"),
        (10, 0.0, 0.95, "wilson"),
        (10, 1.0, 0.95, "wald"),
        (10, 1.0, 0.95, "wilson"),
        (50, 0.02, 0.95, "wald"),
        (50, 0.02, 0.95, "wilson"),
    ):
        value = proportion_coverage(n, p, level, method)
        # Keep the fixture off an endpoint, so a 1e-12 quantile gap cannot flip the sum.
        if 0 < p < 1:
            closest = min(
                min(abs(p - endpoint) for endpoint in proportion_interval(x, n, method, level))
                for x in range(n + 1)
            )
            if closest < 1e-6:
                raise SystemExit(f"{method} n={n} p={p} sits {closest} from an endpoint")
        proportion_rows.append({"n": n, "p": p, "level": level, "method": method, "value": value})

    intervals = []
    for values, method, level in (
        ([1, 2, 3], "t", 0.95),
        ([1, 2, 3], "z-with-s", 0.95),
        ([10, 10, 10, 10], "t", 0.95),
        ([8, 9, 10, 11, 12], "t", 0.9),
        ([8, 9, 10, 11, 12], "z-with-s", 0.9),
    ):
        lower, upper, mean = mean_interval(values, method, level)
        intervals.append({"kind": "mean", "values": values, "method": method, "level": level, "lower": lower, "upper": upper, "estimate": mean})
    for successes, n, method, level in (
        (0, 10, "wald", 0.95),
        (0, 10, "wilson", 0.95),
        (3, 10, "wald", 0.95),
        (3, 10, "wilson", 0.95),
        (10, 10, "wald", 0.95),
        (10, 10, "wilson", 0.95),
        (1, 1, "wald", 0.9),
        (1, 1, "wilson", 0.9),
        (0, 1, "wilson", 0.99),
    ):
        lower, upper = proportion_interval(successes, n, method, level)
        intervals.append(
            {
                "kind": "proportion",
                "x": successes,
                "n": n,
                "method": method,
                "level": level,
                "lower": lower,
                "upper": upper,
                "estimate": successes / n,
            }
        )

    uniform = mulberry32(2026)
    normal = normal_stream(uniform)
    normal_sample = [10 + 2 * normal() for _ in range(10)]
    exponential_uniforms = mulberry32(2026)
    exponential_sample = [-2 * math.log(exponential_uniforms()) for _ in range(10)]
    t_lower, t_upper, t_mean = mean_interval(normal_sample, "t", 0.95)
    z_lower, z_upper, _ = mean_interval(normal_sample, "z-with-s", 0.95)

    payload = {
        "tolerances": TOLERANCES,
        "lgamma": lgamma_rows,
        "lbeta": lbeta_rows,
        "betaPdf": beta_pdf,
        "betaCdf": beta_cdf,
        "betaSf": beta_sf,
        "betaPpf": beta_ppf,
        "normalCdf": normal_cdf,
        "normalPpf": normal_ppf,
        "tCdf": t_cdf,
        "tPpf": t_ppf,
        "binomPmf": binom_rows,
        "betaBinomPmf": beta_binom_rows,
        "betaLab": beta_lab,
        "markov": chains,
        "markovChecks": {
            "steppingP2Row0": expected_two.tolist(),
            "steppingP10State0": float(ten[0, 0]),
            "weatherP2FromWet": weather_two[1].tolist(),
            "weatherRate": float(rate),
            "steppingRounded3dp": [round(value, 3) for value in (np.array([12, 4, 20, 25, 22, 36]) / 119).tolist()],
        },
        "zWithS": z_with_s,
        "proportionCoverage": proportion_rows,
        "intervals": intervals,
        "seededNormal": {
            "seed": 2026,
            "n": 10,
            "truth": 10,
            "sd": 2,
            "values": normal_sample,
            "t": {"lower": t_lower, "upper": t_upper, "estimate": t_mean},
            "zWithS": {"lower": z_lower, "upper": z_upper, "estimate": t_mean},
        },
        "seededExponential": {"seed": 2026, "n": 10, "truth": 2, "values": exponential_sample},
    }
    DEST.parent.mkdir(exist_ok=True)
    DEST.write_text(json.dumps(payload), encoding="utf-8")
    print(f"wrote {DEST}")


if __name__ == "__main__":
    main()
