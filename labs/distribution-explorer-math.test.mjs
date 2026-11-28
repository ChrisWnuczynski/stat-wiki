import assert from "node:assert/strict";
import test from "node:test";
import { curve, familyById } from "./distribution-explorer-math.js";

test("bernoulli masses sum to one", () => {
  const family = familyById("bernoulli");
  const drawn = curve(family, { p: 0.3 });
  assert.equal(drawn.density[0], 0.7);
  assert.equal(drawn.density[1], 0.3);
  assert.ok(Math.abs(drawn.density.reduce((s, y) => s + y, 0) - 1) < 1e-12);
});

test("normal density at the mean", () => {
  const family = familyById("normal");
  const atMean = family.pmf(0, { mu: 0, sigma: 1 });
  assert.ok(Math.abs(atMean - 1 / Math.sqrt(2 * Math.PI)) < 1e-12);
  assert.ok(Math.abs(family.cdf(0, { mu: 0, sigma: 1 }) - 0.5) < 1e-12);
});

test("exponential distribution function at the mean", () => {
  const family = familyById("exponential");
  const atMean = family.cdf(1, { lambda: 1 });
  assert.ok(Math.abs(atMean - (1 - Math.exp(-1))) < 1e-12);
});

test("poisson mean mass", () => {
  const family = familyById("poisson");
  const p0 = family.pmf(0, { lambda: 2 });
  assert.ok(Math.abs(p0 - Math.exp(-2)) < 1e-12);
  const drawn = curve(family, { lambda: 2 });
  const total = drawn.density.reduce((s, y) => s + y, 0);
  assert.ok(total > 0.99 && total <= 1);
});

test("the other families match their closed forms", () => {
  const at = (id, params, x, density, cdf) => {
    const family = familyById(id);
    assert.ok(Math.abs(family.pmf(x, params) - density) < 1e-12, `${id} density at ${x}`);
    assert.ok(Math.abs(family.cdf(x, params) - cdf) < 1e-12, `${id} cdf at ${x}`);
  };
  const binP = 120 * 0.3 ** 3 * 0.7 ** 7;
  at("binomial", { n: 10, p: 0.3 }, 3, binP, binP + 0.7 ** 10 + 10 * 0.3 * 0.7 ** 9 + 45 * 0.3 ** 2 * 0.7 ** 8);
  at("geometric", { p: 0.3 }, 2, 0.3 * 0.7, 1 - 0.7 ** 2);
  at("uniform", { a: 0, b: 1 }, 0.25, 1, 0.25);
  at("uniform", { a: 1.5, b: 0.6 }, 1, 1 / 0.9, (1 - 0.6) / 0.9);
  at("gamma", { shape: 2, rate: 1 }, 1, Math.exp(-1), 1 - 2 * Math.exp(-1));
  at("beta", { alpha: 2, beta: 2 }, 0.5, 1.5, 0.5);
  at("chi2", { df: 2 }, 2, 0.5 * Math.exp(-1), 1 - Math.exp(-1));
  at("t", { df: 1 }, 0, 1 / Math.PI, 0.5);
  at("cauchy", { x0: 0, gamma: 1 }, 1, 1 / (Math.PI * 2), 0.75);
  at("lognormal", { mu: 0, sigma: 1 }, 1, 1 / Math.sqrt(2 * Math.PI), 0.5);
  at("pareto", { xm: 1, alpha: 2 }, 2, 2 / 8, 0.75);
  at("weibull", { k: 1, lambda: 1 }, 1, Math.exp(-1), 1 - Math.exp(-1));
  at("f", { d1: 2, d2: 2 }, 1, 0.25, 0.5);
});

test("gamma, chi-squared and F densities take their right-hand limit at zero", () => {
  const close = (a, b) => Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(b));
  const cases = [
    // Divergent: shape below one, so the density blows up as x falls to zero.
    { id: "gamma", params: { shape: 0.5, rate: 1 }, limit: Infinity },
    { id: "chi2", params: { df: 1 }, limit: Infinity },
    { id: "f", params: { d1: 1, d2: 10 }, limit: Infinity },
    // Finite: shape exactly one, so the density approaches a positive constant.
    { id: "gamma", params: { shape: 1, rate: 2 }, limit: 2 },
    { id: "chi2", params: { df: 2 }, limit: 0.5 },
    { id: "f", params: { d1: 2, d2: 10 }, limit: 1 },
    // Vanishing: shape above one, so the density falls to zero.
    { id: "gamma", params: { shape: 2, rate: 1 }, limit: 0 },
    { id: "chi2", params: { df: 4 }, limit: 0 },
    { id: "f", params: { d1: 5, d2: 10 }, limit: 0 },
  ];
  for (const { id, params, limit } of cases) {
    const family = familyById(id);
    const label = `${id} ${JSON.stringify(params)}`;
    const atZero = family.pmf(0, params);
    if (limit === Infinity) {
      assert.equal(atZero, Infinity, `${label} diverges at zero`);
      // Strictly decreasing just to the right of zero: no false dip.
      const near = [1e-8, 1e-6, 1e-4, 1e-2].map((x) => family.pmf(x, params));
      for (let i = 1; i < near.length; i += 1) assert.ok(near[i] < near[i - 1], `${label} falls away from zero`);
    } else {
      assert.ok(close(atZero, limit), `${label} limit ${atZero} should be ${limit}`);
      assert.ok(Math.abs(family.pmf(1e-9, params) - limit) < 1e-6, `${label} is continuous at zero`);
    }
    // The first plotted point is the left edge, x = 0.
    const drawn = curve(family, params);
    assert.equal(drawn.xs[0], 0);
    assert.equal(drawn.density[0], atZero);
    // The distribution function is unchanged: zero at and below zero.
    assert.equal(family.cdf(0, params), 0, `${label} cdf at zero`);
    assert.equal(drawn.cdf[0], 0);
    assert.equal(family.pmf(-0.5, params), 0, `${label} density left of zero`);
    assert.equal(family.cdf(-0.5, params), 0, `${label} cdf left of zero`);
  }
});

test("finite zero limits match the closed forms", () => {
  // Gamma(1, rate) is Exponential(rate); chi-squared(2) is Exponential(1/2).
  assert.ok(Math.abs(familyById("gamma").pmf(0, { shape: 1, rate: 2 }) - familyById("exponential").pmf(0, { lambda: 2 })) < 1e-12);
  assert.ok(Math.abs(familyById("chi2").pmf(0, { df: 2 }) - familyById("exponential").pmf(0, { lambda: 0.5 })) < 1e-12);
  // F(2, d2) has density (1 + 2x/d2)^(-(1 + d2/2)), which is 1 at zero for every d2.
  for (const d2 of [1, 2, 10, 40]) {
    assert.ok(Math.abs(familyById("f").pmf(0, { d1: 2, d2 }) - 1) < 1e-12, `F(2, ${d2})`);
  }
});
