// Probability mass or density, and the distribution function, for the
// univariate families the distribution laboratory draws. Parameterisations
// match distributions.json. No DOM.

import { betaCdf, betaPdf, binomPmf, gammaP, lgamma, normalCdf, normalPdf } from "./stat-math.js";

const PI = Math.PI;

function poissonPmf(k, lambda) {
  if (!Number.isInteger(k) || k < 0 || !(lambda > 0)) return 0;
  return Math.exp(-lambda + k * Math.log(lambda) - lgamma(k + 1));
}

function poissonCdf(k, lambda) {
  if (!(lambda > 0)) return NaN;
  if (k < 0) return 0;
  const m = Math.floor(k);
  let total = 0;
  for (let j = 0; j <= m; j += 1) total += poissonPmf(j, lambda);
  return total;
}

function binomCdf(k, n, p) {
  if (!Number.isInteger(n) || n < 0) return NaN;
  if (k < 0) return 0;
  const m = Math.min(n, Math.floor(k));
  let total = 0;
  for (let j = 0; j <= m; j += 1) total += binomPmf(j, n, p);
  return total;
}

export const FAMILIES = [
  {
    id: "bernoulli",
    name: "Bernoulli",
    discrete: true,
    params: [{ key: "p", label: "p", min: 0.05, max: 0.95, step: 0.01, value: 0.3 }],
    domain: () => [0, 1],
    pmf(x, { p }) {
      if (x === 0) return 1 - p;
      if (x === 1) return p;
      return 0;
    },
    cdf(x, { p }) {
      if (x < 0) return 0;
      if (x < 1) return 1 - p;
      return 1;
    },
  },
  {
    id: "binomial",
    name: "Binomial",
    discrete: true,
    params: [
      { key: "n", label: "n", min: 1, max: 40, step: 1, value: 10 },
      { key: "p", label: "p", min: 0.05, max: 0.95, step: 0.01, value: 0.3 },
    ],
    domain: ({ n }) => [0, n],
    pmf(x, { n, p }) { return binomPmf(x, n, p); },
    cdf(x, { n, p }) { return binomCdf(x, n, p); },
  },
  {
    id: "poisson",
    name: "Poisson",
    discrete: true,
    params: [{ key: "lambda", label: "λ", min: 0.2, max: 20, step: 0.1, value: 3 }],
    domain: ({ lambda }) => [0, Math.max(8, Math.ceil(lambda + 4 * Math.sqrt(lambda)))],
    pmf(x, { lambda }) { return poissonPmf(x, lambda); },
    cdf(x, { lambda }) { return poissonCdf(x, lambda); },
  },
  {
    id: "geometric",
    name: "Geometric",
    discrete: true,
    params: [{ key: "p", label: "p", min: 0.05, max: 0.95, step: 0.01, value: 0.3 }],
    domain: ({ p }) => [1, Math.max(8, Math.ceil(Math.log(0.01) / Math.log(1 - p)))],
    pmf(x, { p }) {
      if (!Number.isInteger(x) || x < 1) return 0;
      return p * (1 - p) ** (x - 1);
    },
    cdf(x, { p }) {
      if (x < 1) return 0;
      return 1 - (1 - p) ** Math.floor(x);
    },
  },
  {
    id: "uniform",
    name: "Uniform",
    discrete: false,
    params: [
      { key: "a", label: "a", min: -2, max: 2, step: 0.1, value: 0 },
      { key: "b", label: "b", min: 0.5, max: 5, step: 0.1, value: 1 },
    ],
    domain: ({ a, b }) => [Math.min(a, b) - 0.5, Math.max(a, b) + 0.5],
    pmf(x, { a, b }) {
      const lo = Math.min(a, b);
      const hi = Math.max(a, b);
      if (!(hi > lo) || x < lo || x > hi) return 0;
      return 1 / (hi - lo);
    },
    cdf(x, { a, b }) {
      const lo = Math.min(a, b);
      const hi = Math.max(a, b);
      if (x < lo) return 0;
      if (x > hi) return 1;
      return (x - lo) / (hi - lo);
    },
  },
  {
    id: "exponential",
    name: "Exponential",
    discrete: false,
    params: [{ key: "lambda", label: "λ", min: 0.2, max: 3, step: 0.05, value: 1 }],
    domain: ({ lambda }) => [0, 8 / lambda],
    pmf(x, { lambda }) { return x < 0 ? 0 : lambda * Math.exp(-lambda * x); },
    cdf(x, { lambda }) { return x < 0 ? 0 : 1 - Math.exp(-lambda * x); },
  },
  {
    id: "normal",
    name: "Normal",
    discrete: false,
    params: [
      { key: "mu", label: "μ", min: -3, max: 3, step: 0.1, value: 0 },
      { key: "sigma", label: "σ", min: 0.3, max: 3, step: 0.05, value: 1 },
    ],
    domain: ({ mu, sigma }) => [mu - 4 * sigma, mu + 4 * sigma],
    pmf(x, { mu, sigma }) { return normalPdf((x - mu) / sigma) / sigma; },
    cdf(x, { mu, sigma }) { return normalCdf((x - mu) / sigma); },
  },
  {
    id: "gamma",
    name: "Gamma",
    discrete: false,
    params: [
      { key: "shape", label: "shape", min: 0.5, max: 10, step: 0.1, value: 2 },
      { key: "rate", label: "rate", min: 0.2, max: 4, step: 0.1, value: 1 },
    ],
    domain: ({ shape, rate }) => [0, (shape + 4 * Math.sqrt(shape)) / rate],
    pmf(x, { shape, rate }) {
      if (x <= 0) return 0;
      return Math.exp(-rate * x + (shape - 1) * Math.log(x) + shape * Math.log(rate) - lgamma(shape));
    },
    cdf(x, { shape, rate }) { return x <= 0 ? 0 : gammaP(shape, rate * x); },
  },
  {
    id: "beta",
    name: "Beta",
    discrete: false,
    params: [
      { key: "alpha", label: "α", min: 0.5, max: 8, step: 0.1, value: 2 },
      { key: "beta", label: "β", min: 0.5, max: 8, step: 0.1, value: 2 },
    ],
    domain: () => [0, 1],
    pmf(x, { alpha, beta }) { return betaPdf(x, alpha, beta); },
    cdf(x, { alpha, beta }) { return betaCdf(x, alpha, beta); },
  },
  {
    id: "chi2",
    name: "Chi-squared",
    discrete: false,
    params: [{ key: "df", label: "df", min: 1, max: 20, step: 1, value: 4 }],
    domain: ({ df }) => [0, df + 4 * Math.sqrt(2 * df)],
    pmf(x, { df }) {
      if (x <= 0) return 0;
      const shape = df / 2;
      const rate = 0.5;
      return Math.exp(-rate * x + (shape - 1) * Math.log(x) + shape * Math.log(rate) - lgamma(shape));
    },
    cdf(x, { df }) { return x <= 0 ? 0 : gammaP(df / 2, x / 2); },
  },
  {
    id: "t",
    name: "Student t",
    discrete: false,
    params: [{ key: "df", label: "df", min: 1, max: 30, step: 1, value: 5 }],
    domain: () => [-6, 6],
    pmf(x, { df }) {
      const c = lgamma((df + 1) / 2) - lgamma(df / 2) - 0.5 * Math.log(df * PI);
      return Math.exp(c - ((df + 1) / 2) * Math.log1p((x * x) / df));
    },
    cdf(x, { df }) {
      const z = df / (df + x * x);
      const tail = 0.5 * betaCdf(z, df / 2, 0.5);
      return x >= 0 ? 1 - tail : tail;
    },
  },
  {
    id: "cauchy",
    name: "Cauchy",
    discrete: false,
    params: [
      { key: "x0", label: "x₀", min: -3, max: 3, step: 0.1, value: 0 },
      { key: "gamma", label: "γ", min: 0.3, max: 3, step: 0.05, value: 1 },
    ],
    domain: ({ x0, gamma }) => [x0 - 8 * gamma, x0 + 8 * gamma],
    pmf(x, { x0, gamma }) { return gamma / (PI * ((x - x0) ** 2 + gamma ** 2)); },
    cdf(x, { x0, gamma }) { return 0.5 + Math.atan((x - x0) / gamma) / PI; },
  },
  {
    id: "lognormal",
    name: "Lognormal",
    discrete: false,
    params: [
      { key: "mu", label: "μ", min: -1, max: 1, step: 0.05, value: 0 },
      { key: "sigma", label: "σ", min: 0.2, max: 1.5, step: 0.05, value: 0.5 },
    ],
    domain: ({ mu, sigma }) => [0, Math.exp(mu + 3 * sigma)],
    pmf(x, { mu, sigma }) {
      if (x <= 0) return 0;
      return normalPdf((Math.log(x) - mu) / sigma) / (x * sigma);
    },
    cdf(x, { mu, sigma }) { return x <= 0 ? 0 : normalCdf((Math.log(x) - mu) / sigma); },
  },
  {
    id: "pareto",
    name: "Pareto",
    discrete: false,
    params: [
      { key: "xm", label: "xₘ", min: 0.5, max: 3, step: 0.1, value: 1 },
      { key: "alpha", label: "α", min: 0.5, max: 5, step: 0.1, value: 2 },
    ],
    domain: ({ xm, alpha }) => [0, xm * (1 + 8 / alpha)],
    pmf(x, { xm, alpha }) { return x < xm ? 0 : alpha * xm ** alpha / x ** (alpha + 1); },
    cdf(x, { xm, alpha }) { return x < xm ? 0 : 1 - (xm / x) ** alpha; },
  },
  {
    id: "weibull",
    name: "Weibull",
    discrete: false,
    params: [
      { key: "k", label: "k", min: 0.5, max: 5, step: 0.1, value: 1.5 },
      { key: "lambda", label: "λ", min: 0.3, max: 4, step: 0.1, value: 1 },
    ],
    domain: ({ k, lambda }) => [0, lambda * (6 ** (1 / k))],
    pmf(x, { k, lambda }) {
      if (x < 0) return 0;
      const z = x / lambda;
      return (k / lambda) * z ** (k - 1) * Math.exp(-(z ** k));
    },
    cdf(x, { k, lambda }) { return x < 0 ? 0 : 1 - Math.exp(-((x / lambda) ** k)); },
  },
  {
    id: "f",
    name: "F",
    discrete: false,
    params: [
      { key: "d1", label: "d₁", min: 1, max: 20, step: 1, value: 5 },
      { key: "d2", label: "d₂", min: 1, max: 40, step: 1, value: 10 },
    ],
    domain: ({ d1, d2 }) => [0, d2 > 2 ? 3 * d2 / (d2 - 2) : 8],
    pmf(x, { d1, d2 }) {
      if (x <= 0) return 0;
      const a = d1 / 2;
      const b = d2 / 2;
      const log = a * Math.log(d1 / d2) + (a - 1) * Math.log(x) - lgamma(a) - lgamma(b) + lgamma(a + b)
        - (a + b) * Math.log1p((d1 * x) / d2);
      return Math.exp(log);
    },
    cdf(x, { d1, d2 }) {
      if (x <= 0) return 0;
      const z = (d1 * x) / (d1 * x + d2);
      return betaCdf(z, d1 / 2, d2 / 2);
    },
  },
];

export function familyById(id) {
  return FAMILIES.find((family) => family.id === id);
}

export function readParams(family, values) {
  const out = {};
  for (const spec of family.params) out[spec.key] = values[spec.key];
  return out;
}

export function curve(family, values, points = 160) {
  const params = readParams(family, values);
  const [lo, hi] = family.domain(params);
  if (family.discrete) {
    const xs = [];
    for (let x = Math.ceil(lo); x <= Math.floor(hi); x += 1) xs.push(x);
    return {
      xs,
      density: xs.map((x) => family.pmf(x, params)),
      cdf: xs.map((x) => family.cdf(x, params)),
    };
  }
  const xs = [];
  const step = (hi - lo) / (points - 1);
  for (let i = 0; i < points; i += 1) xs.push(lo + i * step);
  return {
    xs,
    density: xs.map((x) => family.pmf(x, params)),
    cdf: xs.map((x) => family.cdf(x, params)),
  };
}
