// Beta-Binomial updating for the laboratory. No DOM.
//
//   prior        theta ~ Beta(alpha, beta)
//   data         x heads in n tosses, X | theta ~ Bin(n, theta)
//   posterior    theta | x ~ Beta(alpha + x, beta + n - x)
//   prediction   K heads in m future tosses: K | x ~ BetaBinomial(m, alpha + x, beta + n - x)
//
// The posterior mean is a weighted average of the prior mean and x/n, with
// weight w = (alpha + beta)/(alpha + beta + n) on the prior. The prior counts
// as alpha + beta tosses.

import { betaBinomPmf, betaPdf, betaQuantile, binomPmf, mulberry32 } from "./stat-math.js";

export const DEFAULTS = Object.freeze({ alpha: 5, beta: 5, n: 10, x: 3, future: 5, level: 0.95, truth: 0.3, seed: 2026 });

export const LIMITS = Object.freeze({ shapeMin: 0.1, shapeMax: 200, nMax: 1000, futureMax: 60 });

// The three priors of the Beta-Binomial chapter.
export const PRESETS = [
  { id: "near-half", label: "Beta(5, 5)", alpha: 5, beta: 5, detail: "concentrated near 1/2: an ordinary coin" },
  { id: "uniform", label: "Beta(1, 1)", alpha: 1, beta: 1, detail: "uniform on [0, 1]" },
  { id: "u-shaped", label: "Beta(0.6, 0.6)", alpha: 0.6, beta: 0.6, detail: "more weight near 0 and 1: suspicion of a biased coin" },
];

export function validate({ alpha, beta, n, x }) {
  for (const [name, value] of [["α", alpha], ["β", beta]]) {
    if (!(Number.isFinite(value) && value >= LIMITS.shapeMin && value <= LIMITS.shapeMax)) {
      return `${name} must be a number from ${LIMITS.shapeMin} to ${LIMITS.shapeMax}.`;
    }
  }
  if (!Number.isInteger(n) || n < 0 || n > LIMITS.nMax) return `The number of tosses must be a whole number from 0 to ${LIMITS.nMax}.`;
  if (!Number.isInteger(x) || x < 0 || x > n) return "The number of heads must be a whole number from 0 to the number of tosses.";
  return null;
}

export function betaSummary(a, b, level = 0.95) {
  const sum = a + b;
  const mean = a / sum;
  const variance = (a * b) / (sum * sum * (sum + 1));
  let mode = null;
  let modeNote = "";
  if (a > 1 && b > 1) mode = (a - 1) / (sum - 2);
  else if (a === 1 && b === 1) modeNote = "every point: the density is flat";
  else if (a <= 1 && b > 1) mode = 0;
  else if (a > 1 && b <= 1) mode = 1;
  else modeNote = "none: the density is unbounded at both ends";
  const tail = (1 - level) / 2;
  return {
    a,
    b,
    mean,
    variance,
    sd: Math.sqrt(variance),
    mode,
    modeNote,
    lower: betaQuantile(tail, a, b),
    upper: betaQuantile(1 - tail, a, b),
    level,
  };
}

export function update({ alpha, beta, n, x, level = 0.95 }) {
  const problem = validate({ alpha, beta, n, x });
  if (problem) return { error: problem };
  const prior = betaSummary(alpha, beta, level);
  const posterior = betaSummary(alpha + x, beta + n - x, level);
  const weight = (alpha + beta) / (alpha + beta + n);
  const proportion = n > 0 ? x / n : null;
  return {
    prior,
    posterior,
    weight,
    proportion,
    // The same mean, written as the weighted average.
    blended: proportion === null ? prior.mean : weight * prior.mean + (1 - weight) * proportion,
  };
}

// Densities on a grid in (0, 1). The likelihood theta^x (1 - theta)^(n - x) is
// scaled to integrate to 1, which makes it the Beta(x + 1, n - x + 1) density:
// the posterior under the uniform prior.
export function densityCurves({ alpha, beta, n, x }, points = 400) {
  const thetas = [];
  // Denser near the ends, where a shape below 1 makes the density climb.
  for (let i = 1; i < points; i++) {
    const u = i / points;
    thetas.push(0.5 - 0.5 * Math.cos(Math.PI * u));
  }
  return thetas.map((theta) => ({
    theta,
    prior: betaPdf(theta, alpha, beta),
    likelihood: betaPdf(theta, x + 1, n - x + 1),
    posterior: betaPdf(theta, alpha + x, beta + n - x),
  }));
}

// Heads in m future tosses: the posterior predictive against the plug-in
// binomial that fixes theta at its posterior mean.
export function prediction({ alpha, beta, n, x }, m) {
  if (!Number.isInteger(m) || m < 1 || m > LIMITS.futureMax) return { error: `Future tosses must be a whole number from 1 to ${LIMITS.futureMax}.` };
  const a = alpha + x;
  const b = beta + n - x;
  const mean = a / (a + b);
  const rows = [];
  for (let k = 0; k <= m; k++) rows.push({ k, predictive: betaBinomPmf(k, m, a, b), plugIn: binomPmf(k, m, mean) });
  const predictiveVariance = (m * a * b * (a + b + m)) / ((a + b) ** 2 * (a + b + 1));
  const plugInVariance = m * mean * (1 - mean);
  return { m, rows, mean: m * mean, predictiveVariance, plugInVariance };
}

// Seeded tosses of a coin with probability truth, continued from a count of
// tosses already made. Toss i is the same draw however the tosses are batched.
export function tosses(seed, truth, start, count) {
  if (!(truth >= 0 && truth <= 1)) return { error: "The true probability must be from 0 to 1." };
  const next = mulberry32(seed);
  for (let i = 0; i < start; i++) next();
  let heads = 0;
  for (let i = 0; i < count; i++) if (next() < truth) heads++;
  return { heads, tails: count - heads };
}
