import assert from "node:assert/strict";
import test from "node:test";
import { FAMILIES, curve, familyById } from "./distribution-explorer-math.js";
import { mount, panelGeometry } from "./distribution-explorer.js";
import { installLabDom, pressKey } from "./test/dom.mjs";

function gaps(values) {
  return values.slice(1).map((value, index) => value - values[index]);
}

test("a normal curve and its ticks spread across the frame", () => {
  const family = familyById("normal");
  const drawn = curve(family, { mu: 0, sigma: 1 });
  const peak = Math.max(...drawn.density);
  const yMax = peak * 1.1;
  const geometry = panelGeometry({
    xs: drawn.xs,
    ys: drawn.density,
    width: 920,
    height: 320,
    yMax,
    kind: "curve",
  });
  const { box, scales, marks } = geometry;
  const xs = marks.points.map((point) => point[0]);
  const ys = marks.points.map((point) => point[1]);
  assert.equal(xs.every(Number.isFinite) && ys.every(Number.isFinite), true);
  assert.equal(xs[0], box.left);
  assert.ok(Math.abs(xs[xs.length - 1] - (box.left + box.innerWidth)) < 1e-6);
  assert.ok(xs[xs.length - 1] - xs[0] > 700);
  for (let i = 1; i < xs.length; i += 1) assert.ok(xs[i] > xs[i - 1]);
  const top = Math.min(...ys);
  assert.ok(top < box.top + box.innerHeight * 0.2);
  assert.ok(Math.max(...ys) - top > box.innerHeight * 0.7);

  const tickX = geometry.xTicks.map((tick) => scales.x(tick));
  const tickY = geometry.yTicks.map((tick) => scales.y(tick));
  assert.ok(geometry.xTicks[0] < geometry.xTicks.at(-1));
  assert.ok(tickX[0] < tickX.at(-1));
  assert.ok(tickX.at(-1) - tickX[0] > 700);
  assert.ok(Math.max(...gaps(tickX)) - Math.min(...gaps(tickX)) < 1e-6);
  assert.ok(tickY[0] > tickY.at(-1));
  assert.ok(tickY[0] - tickY.at(-1) > 200);
  assert.ok(Math.max(...gaps(tickY).map((gap) => Math.abs(gap))) - Math.min(...gaps(tickY).map((gap) => Math.abs(gap))) < 1e-6);
});

test("a discrete mass is stems and the distribution function is a step", () => {
  const family = familyById("bernoulli");
  const drawn = curve(family, { p: 0.3 });
  const mass = panelGeometry({
    xs: drawn.xs,
    ys: drawn.density,
    width: 640,
    height: 320,
    yMax: 1,
    kind: "stems",
  });
  assert.equal(mass.marks.stems.length, 2);
  assert.ok(mass.marks.stems[0].x < mass.marks.stems[1].x);
  assert.ok(mass.marks.stems[0].y1 < mass.marks.stems[1].y1);
  assert.equal(mass.marks.stems[0].y0, mass.box.top + mass.box.innerHeight);
  for (const stem of mass.marks.stems) {
    assert.equal(Number.isFinite(stem.x) && Number.isFinite(stem.y0) && Number.isFinite(stem.y1), true);
    assert.ok(stem.y1 < stem.y0);
  }

  const cdf = panelGeometry({
    xs: drawn.xs,
    ys: drawn.cdf,
    width: 640,
    height: 320,
    yMax: 1,
    kind: "step",
  });
  const points = cdf.marks.points;
  assert.equal(points.length, 4);
  assert.equal(points[0][0], points[1][0]);
  assert.ok(points[1][1] < points[0][1]);
  assert.equal(points[1][1], points[2][1]);
  assert.ok(points[1][0] < points[2][0]);
  assert.equal(points[2][0], points[3][0]);
  assert.ok(points[3][1] < points[2][1]);
  assert.equal(points.every((point) => point.every(Number.isFinite)), true);
  assert.ok(points[2][0] - points[0][0] > 400);
});

test("an empty series is not drawn", () => {
  assert.equal(panelGeometry({ xs: [], ys: [], width: 640, height: 320, yMax: 1, kind: "curve" }), null);
  assert.equal(panelGeometry({ xs: [0, 1], ys: [0, 1], width: 0, height: 320, yMax: 1, kind: "curve" }), null);
});

test("Shift-arrows accelerate parameter sliders by ten steps, keep twins synced and update the hint", (t) => {
  const defaults = FAMILIES.map((family) => family.params.map((spec) => spec.value));
  t.after(() => {
    FAMILIES.forEach((family, i) => {
      family.params.forEach((spec, j) => {
        spec.value = defaults[i][j];
      });
    });
  });
  const { document, root, cleanup } = installLabDom(t);
  cleanup(mount(root));

  const hint = root.querySelector(".control-hint");
  assert.ok(hint?.id);
  assert.equal(hint.textContent, "Arrow keys move a focused slider. Shift changes μ by 1 and σ by 0.5.");

  const muSlider = root.querySelector('input[aria-label="μ"]');
  const muNumber = root.querySelector('input[aria-label="μ as a number"]');
  const sigmaSlider = root.querySelector('input[aria-label="σ"]');
  const sigmaNumber = root.querySelector('input[aria-label="σ as a number"]');
  assert.equal(muSlider.getAttribute("aria-describedby"), hint.id);
  assert.equal(sigmaSlider.getAttribute("aria-describedby"), hint.id);
  assert.notEqual(muNumber.getAttribute("aria-describedby"), hint.id);

  assert.equal(pressKey(muSlider, "ArrowRight").defaultPrevented, false);
  assert.equal(pressKey(muSlider, "ArrowRight", { shiftKey: true, ctrlKey: true }).defaultPrevented, false);

  assert.equal(pressKey(muSlider, "ArrowRight", { shiftKey: true }).defaultPrevented, true);
  assert.equal(muSlider.value, "1");
  assert.equal(muNumber.value, "1");
  assert.match(root.querySelector(".readout-line").textContent, /μ 1, σ 1/);

  // Invalid text on the numeric twin clears when Shift-arrow moves the slider.
  sigmaNumber.value = "1.23";
  sigmaNumber.dispatchEvent({ type: "input" });
  assert.equal(sigmaNumber.getAttribute("aria-invalid"), "true");
  assert.equal(pressKey(sigmaSlider, "ArrowUp", { shiftKey: true }).defaultPrevented, true);
  assert.equal(sigmaSlider.value, "1.5");
  assert.equal(sigmaNumber.value, "1.5");
  assert.equal(sigmaNumber.getAttribute("aria-invalid"), null);

  for (let i = 0; i < 6; i += 1) pressKey(sigmaSlider, "ArrowDown", { shiftKey: true });
  assert.equal(sigmaSlider.value, "0.3");
  assert.equal(sigmaNumber.value, "0.3");

  const select = root.querySelector('select[aria-label="Distribution family"]');
  select.value = "binomial";
  select.dispatchEvent({ type: "change" });
  assert.equal(document.getElementById(hint.id).textContent, "Arrow keys move a focused slider. Shift changes n by 10 and p by 0.1.");
  const nSlider = root.querySelector('input[aria-label="n"]');
  const pSlider = root.querySelector('input[aria-label="p"]');
  const pNumber = root.querySelector('input[aria-label="p as a number"]');
  assert.equal(nSlider.getAttribute("aria-describedby"), hint.id);
  assert.equal(pSlider.getAttribute("aria-describedby"), hint.id);

  pressKey(nSlider, "ArrowRight", { shiftKey: true });
  assert.equal(nSlider.value, "20");
  pressKey(pSlider, "ArrowLeft", { shiftKey: true });
  assert.equal(pSlider.value, "0.2");
  assert.equal(pNumber.value, "0.2");
});
