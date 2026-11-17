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
