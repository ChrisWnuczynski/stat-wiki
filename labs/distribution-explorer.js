// Distribution laboratory. One family, parameter sliders, mass or density, and the distribution function.

import { controlRow, graphFrame, installLabChrome, readoutLine } from "./lab-chrome.js";
import { curve, FAMILIES, familyById } from "./distribution-explorer-math.js";
import { formatNumber } from "./stat-math.js";
import { axisScales, createPlot, drawAxes, message, niceTicks, plotBox, plotClip, stroke, svgEl } from "./svg-chart.js";

function field(labelText) {
  const label = document.createElement("label");
  label.className = "control-field";
  const span = document.createElement("span");
  span.textContent = labelText;
  label.appendChild(span);
  return label;
}

function sliderPair(spec) {
  const label = field(spec.label);
  const wrap = document.createElement("span");
  wrap.className = "control-slider";
  const slider = document.createElement("input");
  slider.type = "range";
  slider.min = String(spec.min);
  slider.max = String(spec.max);
  slider.step = String(spec.step);
  slider.value = String(spec.value);
  slider.setAttribute("aria-label", spec.label);
  const number = document.createElement("input");
  number.type = "number";
  number.min = String(spec.min);
  number.max = String(spec.max);
  number.step = String(spec.step);
  number.value = String(spec.value);
  number.setAttribute("aria-label", `${spec.label} as a number`);
  const sync = (raw) => {
    const value = Math.min(spec.max, Math.max(spec.min, Number(raw)));
    if (!Number.isFinite(value)) return;
    slider.value = String(value);
    number.value = String(value);
    spec.value = value;
  };
  slider.addEventListener("input", () => sync(slider.value));
  number.addEventListener("input", () => sync(number.value));
  wrap.append(slider, number);
  label.appendChild(wrap);
  return label;
}

function clipY(y, yMax) {
  if (y === Infinity) return yMax;
  if (!Number.isFinite(y)) return NaN;
  return Math.min(Math.max(y, 0), yMax);
}

// kind is "curve", "stems", or "step". Pixel positions use the inner frame,
// so a later change cannot treat the margins as the scale range.
export function panelGeometry({ xs, ys, width, height, yMax, kind }) {
  if (!xs || !xs.length || !(yMax > 0) || !(width > 0) || !(height > 0)) return null;
  const x0 = xs[0];
  const x1 = xs[xs.length - 1];
  if (!Number.isFinite(x0) || !Number.isFinite(x1)) return null;
  const box = plotBox(width, height);
  const scales = axisScales(box, [x0, x1], [0, yMax]);
  const yAt = (y) => {
    const clipped = clipY(y, yMax);
    return Number.isFinite(clipped) ? scales.y(clipped) : NaN;
  };
  let marks;
  if (kind === "stems") {
    const stems = [];
    for (let i = 0; i < xs.length; i += 1) {
      const y = yAt(ys[i]);
      if (!Number.isFinite(y)) continue;
      stems.push({ x: scales.x(xs[i]), y0: scales.y(0), y1: y });
    }
    marks = { kind: "stems", stems };
  } else if (kind === "step") {
    const points = [[scales.x(x0), scales.y(0)]];
    for (let i = 0; i < xs.length; i += 1) {
      const x = scales.x(xs[i]);
      const y = yAt(ys[i]);
      points.push([x, y]);
      if (i + 1 < xs.length) points.push([scales.x(xs[i + 1]), y]);
    }
    marks = { kind: "step", points };
  } else {
    marks = { kind: "curve", points: xs.map((x, i) => [scales.x(x), yAt(ys[i])]) };
  }
  return {
    box,
    scales,
    xTicks: niceTicks(x0, x1, 5),
    yTicks: niceTicks(0, yMax, 4),
    marks,
  };
}

function drawPanel(plot, series, label, yMax, kind) {
  plot.setLabel(label);
  plot.draw(({ svg, width, height, colors }) => {
    const geometry = panelGeometry({
      xs: series.xs,
      ys: series.ys,
      width,
      height,
      yMax,
      kind,
    });
    if (!geometry) {
      message(svg, width, height, colors, "Not drawn");
      return;
    }
    const { box, scales, marks } = geometry;
    drawAxes(svg, box, {
      xScale: scales.x,
      yScale: scales.y,
      xTicks: geometry.xTicks,
      yTicks: geometry.yTicks,
      colors,
      xFormat: (value) => formatNumber(value),
      yFormat: (value) => formatNumber(value),
    });
    const clip = plotClip(svg, box);
    const layer = svgEl(svg, "g", { "clip-path": `url(#${clip})` });
    if (marks.kind === "stems") {
      for (const stem of marks.stems) {
        svgEl(layer, "line", {
          x1: stem.x,
          x2: stem.x,
          y1: stem.y0,
          y2: stem.y1,
          stroke: colors.posterior,
          "stroke-width": 2,
          "vector-effect": "non-scaling-stroke",
        });
        svgEl(layer, "circle", { cx: stem.x, cy: stem.y1, r: 2.6, fill: colors.posterior });
      }
      return;
    }
    stroke(layer, marks.points, { stroke: colors.posterior, width: 2 });
  });
}

export function mount(root) {
  installLabChrome();
  const state = { id: "normal" };
  const form = controlRow("Distribution controls");
  const readout = document.createElement("div");
  const density = graphFrame("Probability mass or density");
  const cdf = graphFrame("Distribution function");
  root.append(form, readout, density.section, cdf.section);
  const densityPlot = createPlot(density.plot, { label: "Probability mass or density" });
  const cdfPlot = createPlot(cdf.plot, { label: "Distribution function" });

  const redraw = () => {
    const family = familyById(state.id);
    const values = {};
    for (const spec of family.params) values[spec.key] = spec.value;
    const drawn = curve(family, values);
    const finite = drawn.density.filter((y) => Number.isFinite(y) && y < 1e6);
    const yMax = Math.max(0.05, ...finite) * 1.1;
    const densityKind = family.discrete ? "stems" : "curve";
    const cdfKind = family.discrete ? "step" : "curve";
    drawPanel(densityPlot, { xs: drawn.xs, ys: drawn.density }, `${family.name} ${family.discrete ? "probability mass" : "density"}`, yMax, densityKind);
    drawPanel(cdfPlot, { xs: drawn.xs, ys: drawn.cdf }, `${family.name} distribution function`, 1, cdfKind);
    const bits = family.params.map((spec) => ({
      label: spec.label,
      value: formatNumber(spec.value),
    }));
    readout.replaceChildren(readoutLine([{ label: family.name, value: bits.map((bit) => `${bit.label} ${bit.value}`).join(", ") }]));
  };

  const renderControls = () => {
    form.replaceChildren();
    const selectLabel = field("Family");
    const select = document.createElement("select");
    select.setAttribute("aria-label", "Distribution family");
    for (const family of FAMILIES) {
      const option = document.createElement("option");
      option.value = family.id;
      option.textContent = family.name;
      select.appendChild(option);
    }
    select.value = state.id;
    select.addEventListener("change", () => {
      state.id = select.value;
      renderControls();
    });
    selectLabel.appendChild(select);
    const family = familyById(state.id);
    form.append(selectLabel, ...family.params.map(sliderPair));
    for (const input of form.querySelectorAll("input")) input.addEventListener("input", redraw);
    redraw();
  };
  renderControls();
}
