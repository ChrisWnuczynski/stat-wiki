import assert from "node:assert/strict";
import test from "node:test";
import { curve, familyById } from "./distribution-explorer-math.js";
import { panelGeometry } from "./distribution-explorer.js";

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
