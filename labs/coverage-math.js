// Coverage of confidence intervals for the laboratory. No DOM.
//
// A mean from a normal sample: the t interval, and the interval that uses the
// normal quantile with the sample standard deviation s. Under normality the t
// interval covers with probability exactly 1 - alpha. The z-with-s interval
// covers with probability 2 F_{t, n-1}(z) - 1, which is less than 1 - alpha.
//
// A proportion: the Wald interval and the Wilson interval. Coverage at a fixed
// p is the binomial sum over the counts whose interval contains p. An endpoint
// counts as a hit.
//
// An exponential sample has no closed coverage for these intervals. The
// long-run figure is a Monte Carlo estimate with a fixed seed.
//
// draw is prefix-stable in the number of intervals. The generator is not R's.

import { binomPmf, mulberry32, normalQuantile, normalStream, tCdf, tQuantile } from "./stat-math.js";

export const POPULATIONS = [
  {
    id: "normal",
    label: "Normal mean",
    kind: "mean",
    truth: 10,
    sd: 2,
    detail: "Independent draws from a normal distribution with mean 10 and standard deviation 2.",
  },
  {
    id: "exponential",
    label: "Exponential mean",
    kind: "mean",
    truth: 2,
    detail: "Independent draws from an exponential distribution with mean 2. The normal-theory interval is no longer exact.",
  },
  {
    id: "bernoulli",
    label: "Proportion",
    kind: "proportion",
    detail: "Independent yes-or-no draws. The unknown is the probability p of a yes.",
  },
];

export const METHODS = {
  mean: [
    { id: "t", label: "t interval" },
    { id: "z-with-s", label: "z with s" },
  ],
  proportion: [
    { id: "wald", label: "Wald" },
    { id: "wilson", label: "Wilson" },
  ],
};

export const DEFAULTS = Object.freeze({
  population: "normal",
  method: "t",
  n: 10,
  level: 0.95,
  count: 40,
  seed: 2026,
  p: 0.3,
});

export const LIMITS = Object.freeze({
  nMinMean: 2,
  nMinProportion: 1,
  nMax: 200,
  countMax: 400,
  mcReps: 20000,
  mcSeed: 20261110,
});

const COVER_TOL = 1e-10;

export function populationById(id) {
  return POPULATIONS.find((item) => item.id === id) ?? null;
}

export function validate(config) {
  const population = populationById(config.population);
  if (!population) return "Choose a population.";
  if (!METHODS[population.kind].some((item) => item.id === config.method)) return "That interval does not belong to this population.";
  if (!(config.level > 0 && config.level < 1)) return "The confidence level must be between 0 and 1.";
  const nMin = population.kind === "mean" ? LIMITS.nMinMean : LIMITS.nMinProportion;
  if (!Number.isInteger(config.n) || config.n < nMin || config.n > LIMITS.nMax) {
    return population.kind === "mean"
      ? `The sample size must be a whole number from ${nMin} to ${LIMITS.nMax}, because s uses the divisor n − 1.`
      : `The sample size must be a whole number from ${nMin} to ${LIMITS.nMax}.`;
  }
  if (population.kind === "proportion" && !(config.p >= 0 && config.p <= 1)) return "The probability must be from 0 to 1.";
  if (!Number.isInteger(config.seed)) return "The seed must be a whole number.";
  return null;
}

export function criticalZ(level) {
  return normalQuantile((1 + level) / 2);
}

export function hitsTruth(lower, upper, truth) {
  return lower - COVER_TOL <= truth && truth <= upper + COVER_TOL;
}

export function meanInterval(values, method, level) {
  const n = values.length;
  if (!Number.isInteger(n) || n < 2) return { error: "A mean interval needs at least two observations." };
  if (!values.every((value) => Number.isFinite(value))) return { error: "The sample has an observation that is not finite." };
  if (method !== "t" && method !== "z-with-s") return { error: "A mean uses the t interval or z with s." };
  let sum = 0;
  for (const value of values) sum += value;
  const estimate = sum / n;
  let ss = 0;
  for (const value of values) {
    const gap = value - estimate;
    ss += gap * gap;
  }
  const s = Math.sqrt(ss / (n - 1));
  const critical = method === "t" ? tQuantile(1 - (1 - level) / 2, n - 1) : criticalZ(level);
  if (!Number.isFinite(critical)) return { error: "The critical value is not finite." };
  const half = (critical * s) / Math.sqrt(n);
  return { lower: estimate - half, upper: estimate + half, estimate, s, se: s / Math.sqrt(n), critical, degenerate: s === 0 };
}

export function proportionInterval(successes, n, method, level) {
  if (!Number.isInteger(successes) || !Number.isInteger(n) || n < 1 || successes < 0 || successes > n) {
    return { error: "The number of yeses must be a whole number from 0 to the sample size." };
  }
  if (method !== "wald" && method !== "wilson") return { error: "A proportion uses the Wald or the Wilson interval." };
  const critical = criticalZ(level);
  if (!Number.isFinite(critical)) return { error: "The critical value is not finite." };
  const estimate = successes / n;
  if (method === "wald") {
    const se = Math.sqrt((estimate * (1 - estimate)) / n);
    return { lower: estimate - critical * se, upper: estimate + critical * se, estimate, se, critical, degenerate: se === 0 };
  }
  const z2 = critical * critical;
  const denom = 1 + z2 / n;
  const centre = (estimate + z2 / (2 * n)) / denom;
  const half = (critical * Math.sqrt((estimate * (1 - estimate)) / n + z2 / (4 * n * n))) / denom;
  return { lower: centre - half, upper: centre + half, estimate, critical, degenerate: false };
}

export function truthOf(config) {
  const population = populationById(config.population);
  if (!population) return NaN;
  return population.kind === "proportion" ? config.p : population.truth;
}

function openStream(config) {
  const population = populationById(config.population);
  const uniform = mulberry32(config.seed >>> 0);
  if (population.id === "normal") return { population, normal: normalStream(uniform) };
  return { population, uniform };
}

function oneSample(config, stream) {
  const values = [];
  if (stream.population.id === "normal") {
    for (let i = 0; i < config.n; i++) values.push(stream.population.truth + stream.population.sd * stream.normal());
    return { values };
  }
  if (stream.population.id === "exponential") {
    for (let i = 0; i < config.n; i++) values.push(-stream.population.truth * Math.log(stream.uniform()));
    return { values };
  }
  let successes = 0;
  for (let i = 0; i < config.n; i++) if (stream.uniform() < config.p) successes += 1;
  return { successes };
}

function intervalOf(config, sample) {
  if (sample.values) return meanInterval(sample.values, config.method, config.level);
  return proportionInterval(sample.successes, config.n, config.method, config.level);
}

// count intervals from one seed. Keeping the rows is optional: the Monte Carlo
// tally does not store 20,000 intervals.
function repeat(config, count, keep) {
  const truth = truthOf(config);
  const stream = openStream(config);
  const intervals = [];
  let hits = 0;
  for (let i = 0; i < count; i++) {
    const sample = oneSample(config, stream);
    const interval = intervalOf(config, sample);
    if (interval.error) return interval;
    const covers = hitsTruth(interval.lower, interval.upper, truth);
    if (covers) hits += 1;
    if (keep) intervals.push({ ...interval, covers, successes: sample.successes });
  }
  return { truth, hits, intervals, fraction: count > 0 ? hits / count : null };
}

export function draw(seed, config, count) {
  const full = { ...config, seed };
  const problem = validate(full);
  if (problem) return { error: problem };
  if (!Number.isInteger(count) || count < 0 || count > LIMITS.countMax) {
    return { error: `The number of intervals must be a whole number from 0 to ${LIMITS.countMax}.` };
  }
  return repeat(full, count, true);
}

export function exactMeanCoverage(n, level, method) {
  if (!Number.isInteger(n) || n < 2 || !(level > 0 && level < 1)) return NaN;
  if (method === "t") return level;
  if (method === "z-with-s") return 2 * tCdf(criticalZ(level), n - 1) - 1;
  return NaN;
}

export function exactProportionCoverage(n, p, level, method) {
  if (!Number.isInteger(n) || n < 1 || !(p >= 0 && p <= 1)) return NaN;
  let total = 0;
  for (let successes = 0; successes <= n; successes++) {
    const interval = proportionInterval(successes, n, method, level);
    if (interval.error) return NaN;
    if (hitsTruth(interval.lower, interval.upper, p)) total += binomPmf(successes, n, p);
  }
  return total;
}

export function runningFraction(intervals) {
  let hits = 0;
  return intervals.map((row, index) => {
    if (row.covers) hits += 1;
    const m = index + 1;
    return { m, hits, fraction: hits / m };
  });
}

// Normal approximation to the sampling distribution of the realised fraction.
// The band can fall outside [0, 1]. It is not a confidence interval for a parameter.
export function fractionBand(m, coverage, level = 0.95) {
  if (!Number.isInteger(m) || m < 1) return { error: "The band needs at least one interval." };
  if (!(coverage >= 0 && coverage <= 1) || !Number.isFinite(coverage)) return { error: "The coverage in the band must be a probability." };
  const z = criticalZ(level);
  const se = Math.sqrt((coverage * (1 - coverage)) / m);
  return { lower: coverage - z * se, upper: coverage + z * se, se, normalApproximation: true };
}

export function exponentialMonteCarlo({ n = 10, level = 0.95, method = "t", reps = LIMITS.mcReps, seed = LIMITS.mcSeed } = {}) {
  const config = { population: "exponential", method, n, level, seed, p: 0 };
  const problem = validate(config);
  if (problem) return { error: problem };
  if (!Number.isInteger(reps) || reps < 1) return { error: "The Monte Carlo needs at least one repetition." };
  const result = repeat(config, reps, false);
  if (result.error) return result;
  const coverage = result.hits / reps;
  return {
    coverage,
    se: Math.sqrt((coverage * (1 - coverage)) / reps),
    hits: result.hits,
    reps,
    seed,
    n,
    level,
    method,
    monteCarlo: true,
  };
}
