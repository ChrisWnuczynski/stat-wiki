// Distribution laboratory. One family, parameter sliders, mass or density, and the distribution function.

import { controlRow, graphFrame, installLabChrome, readoutLine } from "./lab-chrome.js";
import { curve, FAMILIES, familyById } from "./distribution-explorer-math.js";
import { formatNumber } from "./stat-math.js";
import { chartColors, createPlot, drawAxes, niceTicks, plotBox, plotClip, scaleLinear, stroke, svgEl } from "./svg-chart.js";

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

function drawPanel(plot, series, label, yMax) {
  plot.setLabel(label);
  plot.draw(({ svg, width, height, colors }) => {
    const box = plotBox(width, height);
    const xScale = scaleLinear([series.xs[0], series.xs[series.xs.length - 1]], [box.left, box.right]);
    const yScale = scaleLinear([0, yMax], [box.bottom, box.top]);
    drawAxes(svg, box, {
      xScale,
      yScale,
      xTicks: niceTicks(series.xs[0], series.xs[series.xs.length - 1], 5),
      yTicks: niceTicks(0, yMax, 4),
      colors,
      xFormat: (v) => formatNumber(v),
      yFormat: (v) => formatNumber(v),
    });
    const clip = plotClip(svg, box);
    const layer = svgEl(svg, "g", { "clip-path": `url(#${clip})` });
    const points = series.xs.map((x, i) => [xScale(x), yScale(Math.min(series.ys[i], yMax))]);
        stroke(layer, points, { stroke: colors.posterior, width: 2 });
        if (series.discrete) {
          for (const [x, y] of points) {
            svgEl(layer, "line", { x1: x, x2: x, y1: yScale(0), y2: y, stroke: colors.posterior, "stroke-width": 2 });
          }
        }
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
    drawPanel(densityPlot, { xs: drawn.xs, ys: drawn.density, discrete: family.discrete }, `${family.name} ${family.discrete ? "probability mass" : "density"}`, yMax);
    drawPanel(cdfPlot, { xs: drawn.xs, ys: drawn.cdf, discrete: family.discrete }, `${family.name} distribution function`, 1);
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
