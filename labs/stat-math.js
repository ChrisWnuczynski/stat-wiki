// Distribution functions shared by the Beta-Binomial, Markov chain and
// confidence-interval laboratories. No DOM. Checked against SciPy in
// stat-math.test.mjs, from the numbers labs/reference_stats.py writes.
//
//   lgamma          Lanczos, g = 7, nine terms
//   betaCdf         regularised incomplete beta, Lentz continued fraction
//   gammaP, gammaQ  regularised incomplete gamma: series below a + 1, continued fraction above
//   normalCdf       from gammaQ(1/2, z^2/2), so each tail keeps its relative accuracy
//   normalQuantile  Acklam's approximation, then one Halley step on normalCdf
//   t and Beta quantiles  bisection on the distribution function
//
// The generator is not R's. A seed reproduces this page, not an R session.

const LANCZOS = [
  0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313,
  -176.61502916214059, 12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6,
  1.5056327351493116e-7,
];
const LOG_SQRT_TWO_PI = 0.5 * Math.log(2 * Math.PI);
const EPS = 1e-15;
const TINY = 1e-300;

export function lgamma(x) {
  if (!(x > 0)) return NaN;
  if (x < 0.5) return Math.log(Math.PI / Math.sin(Math.PI * x)) - lgamma(1 - x);
  const y = x - 1;
  let sum = LANCZOS[0];
  for (let i = 1; i < LANCZOS.length; i++) sum += LANCZOS[i] / (y + i);
  const t = y + 7.5;
  return LOG_SQRT_TWO_PI + (y + 0.5) * Math.log(t) - t + Math.log(sum);
}

export function lbeta(a, b) {
  return lgamma(a) + lgamma(b) - lgamma(a + b);
}

export function lchoose(n, k) {
  return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1);
}

// Continued fraction for the incomplete beta (modified Lentz).
function betaFraction(x, a, b) {
  const qab = a + b;
  const qap = a + 1;
  const qam = a - 1;
  let c = 1;
  let d = 1 - (qab * x) / qap;
  if (Math.abs(d) < TINY) d = TINY;
  d = 1 / d;
  let h = d;
  for (let m = 1; m <= 10000; m++) {
    const m2 = 2 * m;
    let aa = (m * (b - m) * x) / ((qam + m2) * (a + m2));
    d = 1 + aa * d;
    if (Math.abs(d) < TINY) d = TINY;
    c = 1 + aa / c;
    if (Math.abs(c) < TINY) c = TINY;
    d = 1 / d;
    h *= d * c;
    aa = (-(a + m) * (qab + m) * x) / ((a + m2) * (qap + m2));
    d = 1 + aa * d;
    if (Math.abs(d) < TINY) d = TINY;
    c = 1 + aa / c;
    if (Math.abs(c) < TINY) c = TINY;
    d = 1 / d;
    const step = d * c;
    h *= step;
    if (Math.abs(step - 1) < EPS) return h;
  }
  return h;
}

// P(Beta(a, b) <= x).
export function betaCdf(x, a, b) {
  if (!(a > 0 && b > 0) || Number.isNaN(x)) return NaN;
  if (x <= 0) return 0;
  if (x >= 1) return 1;
  const logFront = a * Math.log(x) + b * Math.log1p(-x) - lbeta(a, b);
  if (x < (a + 1) / (a + b + 2)) return (Math.exp(logFront) * betaFraction(x, a, b)) / a;
  return 1 - (Math.exp(logFront) * betaFraction(1 - x, b, a)) / b;
}

// P(Beta(a, b) > x), without the cancellation of 1 - betaCdf near 1.
export function betaSurvival(x, a, b) {
  if (!(a > 0 && b > 0) || Number.isNaN(x)) return NaN;
  if (x <= 0) return 1;
  if (x >= 1) return 0;
  return betaCdf(1 - x, b, a);
}

export function betaPdf(x, a, b) {
  if (!(a > 0 && b > 0) || Number.isNaN(x)) return NaN;
  if (x < 0 || x > 1) return 0;
  if (x === 0) return a < 1 ? Infinity : a === 1 ? Math.exp(-lbeta(a, b)) : 0;
  if (x === 1) return b < 1 ? Infinity : b === 1 ? Math.exp(-lbeta(a, b)) : 0;
  return Math.exp((a - 1) * Math.log(x) + (b - 1) * Math.log1p(-x) - lbeta(a, b));
}

// Smallest x with betaCdf(x) >= p, by bisection to the last bit.
export function betaQuantile(p, a, b) {
  if (!(a > 0 && b > 0) || !(p >= 0 && p <= 1)) return NaN;
  if (p === 0) return 0;
  if (p === 1) return 1;
  // Work in the tail that keeps relative accuracy.
  const upper = p > 0.5;
  const target = upper ? 1 - p : p;
  const tail = upper ? (x) => betaSurvival(x, a, b) : (x) => betaCdf(x, a, b);
  let lo = 0;
  let hi = 1;
  for (let i = 0; i < 1100 && hi - lo > 0; i++) {
    const mid = lo + (hi - lo) / 2;
    if (mid === lo || mid === hi) break;
    const value = tail(mid);
    if (upper ? value > target : value < target) lo = mid;
    else hi = mid;
  }
  return lo + (hi - lo) / 2;
}

// Regularised incomplete gamma P(a, x) and Q(a, x) = 1 - P(a, x).
function gammaSeries(a, x) {
  let sum = 1 / a;
  let term = sum;
  for (let n = 1; n < 10000; n++) {
    term *= x / (a + n);
    sum += term;
    if (Math.abs(term) < Math.abs(sum) * EPS) break;
  }
  return sum * Math.exp(-x + a * Math.log(x) - lgamma(a));
}

function gammaFraction(a, x) {
  let b = x + 1 - a;
  let c = 1 / TINY;
  let d = 1 / b;
  let h = d;
  for (let i = 1; i < 10000; i++) {
    const an = -i * (i - a);
    b += 2;
    d = an * d + b;
    if (Math.abs(d) < TINY) d = TINY;
    c = b + an / c;
    if (Math.abs(c) < TINY) c = TINY;
    d = 1 / d;
    const step = d * c;
    h *= step;
    if (Math.abs(step - 1) < EPS) break;
  }
  return Math.exp(-x + a * Math.log(x) - lgamma(a)) * h;
}

export function gammaP(a, x) {
  if (!(a > 0) || Number.isNaN(x)) return NaN;
  if (x <= 0) return 0;
  return x < a + 1 ? gammaSeries(a, x) : 1 - gammaFraction(a, x);
}

export function gammaQ(a, x) {
  if (!(a > 0) || Number.isNaN(x)) return NaN;
  if (x <= 0) return 1;
  return x < a + 1 ? 1 - gammaSeries(a, x) : gammaFraction(a, x);
}

export function normalPdf(z) {
  return Math.exp(-0.5 * z * z - LOG_SQRT_TWO_PI);
}

export function normalCdf(z) {
  if (Number.isNaN(z)) return NaN;
  if (z === Infinity) return 1;
  if (z === -Infinity) return 0;
  const half = 0.5 * gammaQ(0.5, 0.5 * z * z);
  return z < 0 ? half : z === 0 ? 0.5 : 1 - half;
}

const ACKLAM_A = [-3.969683028665376e1, 2.209460984245205e2, -2.759285104469687e2, 1.38357751867269e2, -3.066479806614716e1, 2.506628277459239];
const ACKLAM_B = [-5.447609879822406e1, 1.615858368580409e2, -1.556989798598866e2, 6.680131188771972e1, -1.328068155288572e1];
const ACKLAM_C = [-7.784894002430293e-3, -3.223964580411365e-1, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783];
const ACKLAM_D = [7.784695709041462e-3, 3.224671290700398e-1, 2.445134137142996, 3.754408661907416];

export function normalQuantile(p) {
  if (!(p >= 0 && p <= 1)) return NaN;
  if (p === 0) return -Infinity;
  if (p === 1) return Infinity;
  const low = 0.02425;
  let x;
  if (p < low || p > 1 - low) {
    const q = Math.sqrt(-2 * Math.log(p < low ? p : 1 - p));
    x = (((((ACKLAM_C[0] * q + ACKLAM_C[1]) * q + ACKLAM_C[2]) * q + ACKLAM_C[3]) * q + ACKLAM_C[4]) * q + ACKLAM_C[5])
      / ((((ACKLAM_D[0] * q + ACKLAM_D[1]) * q + ACKLAM_D[2]) * q + ACKLAM_D[3]) * q + 1);
    if (p > 1 - low) x = -x;
  } else {
    const q = p - 0.5;
    const r = q * q;
    x = ((((((ACKLAM_A[0] * r + ACKLAM_A[1]) * r + ACKLAM_A[2]) * r + ACKLAM_A[3]) * r + ACKLAM_A[4]) * r + ACKLAM_A[5]) * q)
      / (((((ACKLAM_B[0] * r + ACKLAM_B[1]) * r + ACKLAM_B[2]) * r + ACKLAM_B[3]) * r + ACKLAM_B[4]) * r + 1);
  }
  // One Halley step against the accurate distribution function.
  for (let i = 0; i < 2; i++) {
    const e = x < 0 ? normalCdf(x) - p : (1 - p) - (1 - normalCdf(x));
    const u = e / normalPdf(x);
    x -= u / (1 + (x * u) / 2);
  }
  return x;
}

export function tCdf(t, df) {
  if (!(df > 0) || Number.isNaN(t)) return NaN;
  if (t === Infinity) return 1;
  if (t === -Infinity) return 0;
  const tail = 0.5 * betaCdf(df / (df + t * t), df / 2, 0.5);
  return t > 0 ? 1 - tail : tail;
}

export function tQuantile(p, df) {
  if (!(df > 0) || !(p >= 0 && p <= 1)) return NaN;
  if (p === 0) return -Infinity;
  if (p === 1) return Infinity;
  if (p === 0.5) return 0;
  const q = p < 0.5 ? p : 1 - p;
  const x = betaQuantile(2 * q, df / 2, 0.5);
  const t = Math.sqrt((df * (1 - x)) / x);
  return p < 0.5 ? -t : t;
}

export function binomPmf(k, n, p) {
  if (!Number.isInteger(k) || !Number.isInteger(n) || n < 0 || !(p >= 0 && p <= 1)) return NaN;
  if (k < 0 || k > n) return 0;
  if (p === 0) return k === 0 ? 1 : 0;
  if (p === 1) return k === n ? 1 : 0;
  return Math.exp(lchoose(n, k) + k * Math.log(p) + (n - k) * Math.log1p(-p));
}

// P(K = k) when K | theta ~ Bin(m, theta) and theta ~ Beta(a, b).
export function betaBinomPmf(k, m, a, b) {
  if (!Number.isInteger(k) || !Number.isInteger(m) || m < 0 || !(a > 0 && b > 0)) return NaN;
  if (k < 0 || k > m) return 0;
  return Math.exp(lchoose(m, k) + lbeta(k + a, m - k + b) - lbeta(a, b));
}

// Seeded uniforms on (0, 1), never 0 or 1. The same generator as the kernel density laboratory.
export function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return (((t ^ (t >>> 14)) >>> 0) + 0.5) / 4294967296;
  };
}

// Box-Muller with both normals kept, so one seed gives one sequence of normals.
export function normalStream(uniform) {
  let spare = null;
  return function () {
    if (spare !== null) {
      const out = spare;
      spare = null;
      return out;
    }
    const r = Math.sqrt(-2 * Math.log(uniform()));
    const angle = 2 * Math.PI * uniform();
    spare = r * Math.sin(angle);
    return r * Math.cos(angle);
  };
}

// Readable numbers for the readouts: four significant figures, exponent outside [1e-3, 1e4).
export function formatNumber(value, digits = 4) {
  if (!Number.isFinite(value)) return value === Infinity ? "∞" : value === -Infinity ? "−∞" : "not finite";
  if (value === 0) return "0";
  const magnitude = Math.abs(value);
  if (magnitude < 1e-3 || magnitude >= 1e4) return value.toExponential(digits - 1).replace("-", "−");
  return Number(value.toPrecision(digits)).toString().replace("-", "−");
}
