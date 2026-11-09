// Gaussian kernel density math for the laboratory.
// No DOM, no Observable, no Quarto. The page imports this module.
//
// The generator below is not R's RNG. Reference checks use the arrays this
// module actually produced, then recompute ISE, MISE, and bw.nrd0 elsewhere.
//
// Bandwidth h is the standard deviation of each bump (the chapter's H = h^2,
// and R density()'s gaussian bandwidth).
//
//   fhat_h(x) = (1/n) sum_i phi_h(x - X_i)
//   phi_h = Normal(0, h^2) density
//   f(x) = sum_k w_k phi_{sigma_k}(x - mu_k)
//   integral phi_a(x-u) phi_b(x-v) dx = phi_{sqrt(a^2+b^2)}(u-v)
//
// ISE is one sample. MISE = E[ISE] = integrated variance + integrated squared bias.
// Both are the closed forms below. They are not numerical integrals.

export const MAX_N = 200;

export const DEFAULTS = Object.freeze({
  seed: 3500,
  n: 120,
  population: "mixture",
});

// Search window for the risk curves. Minima are grid minima on this window.
export const BAND_LO = 0.04;
export const BAND_HI = 2.5;
export const CURVE_COUNT = 41;
export const MISE_STEP = 0.002;
export const ISE_FINE = 0.005;

export const ERRORS = Object.freeze({
  kdeTooSmall: "A kernel estimate needs at least one observation.",
  iseTooSmall: "ISE needs at least one observation.",
  miseTooSmall: "MISE needs an integer sample size of at least 1.",
  bandwidthTooSmall: "R bw.nrd0 needs at least 2 observations.",
  bandwidthNotPositive: "Bandwidth must be a positive finite number.",
});

// R bw.nrd0, not bw.nrd. The constant is 0.9. s uses divisor n-1.
// Quartiles are R's type 7. The fallback matches stats::bw.nrd0 when
// min(s, IQR/1.34) is not strictly positive.
export const SILVERMAN_RULE =
  "Silverman rule of thumb, R bw.nrd0: 0.9 min(s, IQR/1.34) n^(-1/5), with s the sample standard deviation using divisor n-1 and IQR the gap between type-7 quartiles.";

export const POPULATIONS = [
  {
    id: "normal",
    label: "Normal",
    detail: "N(0, 1)",
    components: [{ weight: 1, mean: 0, sd: 1 }],
  },
  {
    id: "mixture",
    label: "Bimodal mixture",
    detail: "1/2 N(-1.5, 0.5^2) + 1/2 N(1.5, 0.5^2)",
    components: [
      { weight: 0.5, mean: -1.5, sd: 0.5 },
      { weight: 0.5, mean: 1.5, sd: 0.5 },
    ],
  },
];

const TWO_PI = 2 * Math.PI;

export function population(id) {
  const found = POPULATIONS.find((item) => item.id === id);
  if (!found) return { error: `Unknown distribution "${id}".` };
  return found;
}

export function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return (t ^ (t >>> 14)) >>> 0;
  };
}

export function uniformStream(seed, count) {
  const next = mulberry32(seed);
  const out = new Array(count);
  for (let i = 0; i < count; i++) out[i] = (next() + 0.5) / 4294967296;
  return out;
}

// Three uniforms per index: two for one Box-Muller normal, one for the
// mixture label. A one-component population ignores the label and still
// consumes it, so index i is the same underlying draw for every population.
export function sequence(seed, count = MAX_N) {
  if (!Number.isInteger(count) || count < 1) {
    return { error: "The sequence length must be a positive integer." };
  }
  const uniforms = uniformStream(seed, count * 3);
  const out = new Array(count);
  for (let i = 0; i < count; i++) {
    const u1 = uniforms[3 * i];
    const u2 = uniforms[3 * i + 1];
    const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(TWO_PI * u2);
    if (!Number.isFinite(z)) {
      return { error: `Draw ${i} from seed ${seed >>> 0} was not finite.` };
    }
    out[i] = { z, u: uniforms[3 * i + 2] };
  }
  return out;
}

export function realise(seq, components, n) {
  const problem = validateMixture(components);
  if (problem) return problem;
  if (!Array.isArray(seq)) return { error: "The pre-generated sequence is missing." };
  if (!Number.isInteger(n) || n < 1 || n > seq.length) {
    return { error: `Sample size must be an integer from 1 to ${seq.length}.` };
  }
  const values = new Array(n);
  for (let i = 0; i < n; i++) {
    const draw = seq[i];
    let acc = 0;
    let chosen = components[components.length - 1];
    for (const component of components) {
      acc += component.weight;
      if (draw.u < acc) {
        chosen = component;
        break;
      }
    }
    values[i] = chosen.mean + chosen.sd * draw.z;
    if (!Number.isFinite(values[i])) {
      return { error: `Observation ${i} was not finite.` };
    }
  }
  return { values };
}

export function samplePrefix(seq, id, n) {
  const dist = population(id);
  if (dist.error) return dist;
  return realise(seq, dist.components, n);
}

export function normalPdf(x, mean, sd) {
  if (!(sd > 0) || !Number.isFinite(sd) || !Number.isFinite(x) || !Number.isFinite(mean)) return NaN;
  const z = (x - mean) / sd;
  return Math.exp(-0.5 * z * z - Math.log(sd) - 0.5 * Math.log(TWO_PI));
}

export function mixturePdf(x, components) {
  let sum = 0;
  for (const component of components) {
    const term = component.weight * normalPdf(x, component.mean, component.sd);
    if (!Number.isFinite(term)) return NaN;
    sum += term;
  }
  return sum;
}

export function kdeAt(x, sample, h) {
  if (!Number.isFinite(x)) return { error: "The evaluation point is not finite." };
  if (!(h > 0) || !Number.isFinite(h)) return { error: ERRORS.bandwidthNotPositive };
  if (!sample || sample.length < 1) return { error: ERRORS.kdeTooSmall };
  let sum = 0;
  for (let i = 0; i < sample.length; i++) {
    const term = normalPdf(x, sample[i], h);
    if (!Number.isFinite(term)) return { error: "A kernel term was not finite." };
    sum += term;
  }
  const value = sum / sample.length;
  if (!Number.isFinite(value)) return { error: "The kernel estimate was not finite." };
  return { value };
}

export function kdeOnGrid(xs, sample, h) {
  const values = new Array(xs.length);
  for (let j = 0; j < xs.length; j++) {
    const point = kdeAt(xs[j], sample, h);
    if (point.error) return point;
    values[j] = point.value;
  }
  return { values };
}

function sampleSd(sample) {
  const n = sample.length;
  let mean = 0;
  for (let i = 0; i < n; i++) mean += sample[i];
  mean /= n;
  let acc = 0;
  for (let i = 0; i < n; i++) {
    const d = sample[i] - mean;
    acc += d * d;
  }
  return Math.sqrt(acc / (n - 1));
}

function quantileType7(sorted, p) {
  const n = sorted.length;
  const pos = (n - 1) * p;
  const lo = Math.floor(pos);
  const gamma = pos - lo;
  if (gamma === 0 || lo >= n - 1) return sorted[Math.min(lo, n - 1)];
  return (1 - gamma) * sorted[lo] + gamma * sorted[lo + 1];
}

export function silvermanNrd0(sample) {
  if (!sample || sample.length < 2) return { error: ERRORS.bandwidthTooSmall };
  const n = sample.length;
  for (let i = 0; i < n; i++) {
    if (!Number.isFinite(sample[i])) return { error: "bw.nrd0 cannot use a non-finite observation." };
  }
  const hi = sampleSd(sample);
  if (!Number.isFinite(hi)) return { error: "The sample standard deviation was not finite." };
  const sorted = sample.slice().sort((a, b) => a - b);
  const iqr = quantileType7(sorted, 0.75) - quantileType7(sorted, 0.25);
  if (!Number.isFinite(iqr)) return { error: "The interquartile range was not finite." };
  // R: if (!(lo <- min(hi, IQR(x)/1.34))) (lo <- hi) || (lo <- abs(x[1])) || (lo <- 1)
  let lo = Math.min(hi, iqr / 1.34);
  if (!(lo > 0)) {
    lo = hi;
    if (!(lo > 0)) lo = Math.abs(sample[0]);
    if (!(lo > 0)) lo = 1;
  }
  const value = 0.9 * lo * n ** -0.2;
  if (!(value > 0) || !Number.isFinite(value)) {
    return { error: "bw.nrd0 did not return a positive finite bandwidth. No substitute was used." };
  }
  return { value, rule: "R bw.nrd0" };
}

function validateMixture(components) {
  if (!Array.isArray(components) || components.length === 0) {
    return { error: "The population needs at least one Gaussian component." };
  }
  let weight = 0;
  for (const component of components) {
    if (!component || !(component.sd > 0) || !Number.isFinite(component.sd) || !Number.isFinite(component.mean) || !Number.isFinite(component.weight)) {
      return { error: "Each component needs a finite mean, a finite weight, and a positive finite standard deviation." };
    }
    weight += component.weight;
  }
  if (!Number.isFinite(weight) || Math.abs(weight - 1) > 1e-8) {
    return { error: `Mixture weights must sum to 1. The sum was ${weight}.` };
  }
  return null;
}

function requireBandwidth(h) {
  if (!(h > 0) || !Number.isFinite(h)) return { error: ERRORS.bandwidthNotPositive };
  return null;
}

// Upper triangle of squared distances, plus the values. Reused for every h.
export function pairCache(values) {
  if (!values || values.length < 1) return { error: ERRORS.iseTooSmall };
  const n = values.length;
  const copy = new Array(n);
  for (let i = 0; i < n; i++) {
    if (!Number.isFinite(values[i])) return { error: "ISE cannot use a non-finite observation." };
    copy[i] = values[i];
  }
  const upper = new Float64Array((n * (n - 1)) / 2);
  let p = 0;
  for (let i = 0; i < n; i++) {
    const xi = copy[i];
    for (let j = i + 1; j < n; j++) {
      const d = xi - copy[j];
      upper[p++] = d * d;
    }
  }
  return { n, upper, values: copy };
}

export function iseFromCache(cache, h, components) {
  if (!cache || cache.error) return cache && cache.error ? cache : { error: "The pairwise cache is missing." };
  const bandwidth = requireBandwidth(h);
  if (bandwidth) return bandwidth;
  const problem = validateMixture(components);
  if (problem) return problem;
  const n = cache.n;
  if (n < 1) return { error: ERRORS.iseTooSmall };
  // phi_{h*sqrt(2)}(d) = exp(-d^2 / (4 h^2)) / (h * sqrt(2) * sqrt(2 pi))
  const scale = -1 / (4 * h * h);
  const inv = 1 / (h * Math.SQRT2 * Math.sqrt(TWO_PI));
  let off = 0;
  const upper = cache.upper;
  for (let p = 0; p < upper.length; p++) off += Math.exp(scale * upper[p]);
  const fit = (inv * (n + 2 * off)) / (n * n);
  if (!Number.isFinite(fit)) return { error: "A term in the integrated square of the estimate was not finite." };

  let crossSum = 0;
  const xs = cache.values;
  for (let i = 0; i < n; i++) {
    const x = xs[i];
    for (let k = 0; k < components.length; k++) {
      const component = components[k];
      const term = component.weight * normalPdf(x - component.mean, 0, Math.hypot(h, component.sd));
      if (!Number.isFinite(term)) return { error: "A term in the cross integral was not finite." };
      crossSum += term;
    }
  }
  const cross = (2 / n) * crossSum;

  let truth = 0;
  for (let k = 0; k < components.length; k++) {
    for (let l = 0; l < components.length; l++) {
      const left = components[k];
      const right = components[l];
      const term = left.weight * right.weight * normalPdf(left.mean - right.mean, 0, Math.hypot(left.sd, right.sd));
      if (!Number.isFinite(term)) return { error: "A term in the integrated square of the true density was not finite." };
      truth += term;
    }
  }
  const value = fit - cross + truth;
  if (!Number.isFinite(value)) return { error: "ISE was not finite. No substitute was used." };
  return { value, fit, cross, truth };
}

export function iseExact(values, h, components) {
  const cache = pairCache(values);
  if (cache.error) return cache;
  return iseFromCache(cache, h, components);
}

function omegaQuadratic(a, h, components) {
  const kCount = components.length;
  let form = 0;
  for (let k = 0; k < kCount; k++) {
    for (let l = 0; l < kCount; l++) {
      const left = components[k];
      const right = components[l];
      const sd = Math.sqrt(a * h * h + left.sd * left.sd + right.sd * right.sd);
      const density = normalPdf(left.mean - right.mean, 0, sd);
      if (!Number.isFinite(density)) return NaN;
      form += left.weight * density * right.weight;
    }
  }
  return form;
}

export function miseParts(n, h, components) {
  if (!Number.isInteger(n) || n < 1) return { error: ERRORS.miseTooSmall };
  const bandwidth = requireBandwidth(h);
  if (bandwidth) return bandwidth;
  const problem = validateMixture(components);
  if (problem) return problem;
  const q0 = omegaQuadratic(0, h, components);
  const q1 = omegaQuadratic(1, h, components);
  const q2 = omegaQuadratic(2, h, components);
  if (![q0, q1, q2].every(Number.isFinite)) {
    return { error: "A Gaussian overlap in MISE was not finite. No substitute was used." };
  }
  const kernelSquare = 1 / (2 * Math.sqrt(Math.PI) * h);
  const integratedVariance = (kernelSquare - q2) / n;
  const integratedSquaredBias = q2 - 2 * q1 + q0;
  const mise = integratedVariance + integratedSquaredBias;
  if (![integratedVariance, integratedSquaredBias, mise].every(Number.isFinite)) {
    return { error: "MISE was not finite. No substitute was used." };
  }
  return { integratedVariance, integratedSquaredBias, mise, kernelSquare, q0, q1, q2 };
}

export function bandwidthGrid(min, max, count) {
  if (!(max > min) || !Number.isInteger(count) || count < 2) {
    return { error: "The bandwidth grid needs a positive span and at least two points." };
  }
  const out = new Array(count);
  for (let i = 0; i < count; i++) out[i] = min + ((max - min) * i) / (count - 1);
  return out;
}

export function gridMin(xs, ys) {
  if (!xs || !ys || xs.length !== ys.length || xs.length < 1) {
    return { error: "The grid minimum needs paired bandwidths and values." };
  }
  let index = -1;
  for (let i = 0; i < ys.length; i++) {
    if (!Number.isFinite(ys[i]) || !Number.isFinite(xs[i])) {
      return { error: "The grid minimum cannot use a non-finite value. No substitute was used." };
    }
    if (index < 0 || ys[i] < ys[index]) index = i;
  }
  return { x: xs[index], y: ys[index], index };
}

// Coarse scan, then a fine step around the best coarse point. Every value is
// the closed form. This is not a continuous optimiser.
export function minimiseRisk(evaluate, lo, hi, coarseCount, fineStep) {
  const coarse = bandwidthGrid(lo, hi, coarseCount);
  if (coarse.error) return coarse;
  const ys = new Array(coarse.length);
  for (let i = 0; i < coarse.length; i++) {
    const row = evaluate(coarse[i]);
    if (row.error) return row;
    ys[i] = row.value;
  }
  const best = gridMin(coarse, ys);
  if (best.error) return best;
  const left = Math.max(lo, best.x - (hi - lo) / (coarseCount - 1));
  const right = Math.min(hi, best.x + (hi - lo) / (coarseCount - 1));
  let x = best.x;
  let y = best.y;
  if (fineStep > 0 && right > left) {
    for (let t = left; t <= right + fineStep * 0.25; t += fineStep) {
      const row = evaluate(t);
      if (row.error) return row;
      if (row.value < y) {
        x = t;
        y = row.value;
      }
    }
  }
  return { x, y, grid: coarse, values: ys };
}

export function iseCurve(cache, bandwidths, components) {
  const values = new Array(bandwidths.length);
  for (let i = 0; i < bandwidths.length; i++) {
    const row = iseFromCache(cache, bandwidths[i], components);
    if (row.error) return row;
    values[i] = row.value;
  }
  return { values };
}

export function miseCurve(n, bandwidths, components) {
  const integratedVariance = new Array(bandwidths.length);
  const integratedSquaredBias = new Array(bandwidths.length);
  const mise = new Array(bandwidths.length);
  for (let i = 0; i < bandwidths.length; i++) {
    const row = miseParts(n, bandwidths[i], components);
    if (row.error) return row;
    integratedVariance[i] = row.integratedVariance;
    integratedSquaredBias[i] = row.integratedSquaredBias;
    mise[i] = row.mise;
  }
  return { integratedVariance, integratedSquaredBias, mise };
}
