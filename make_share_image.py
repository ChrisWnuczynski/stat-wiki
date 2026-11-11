"""Draw the share image, share-icon.png: the browser-tab icon at 1200 by 630.

The icon (favicon.ico) is the filled-contour panel of a Julia script: a
bivariate normal density with sigma_x = 1, sigma_y = 1.5 and rho = 0.6, on a
151 by 151 grid over x in [-4, 4] and y in [-6, 6], drawn by Plots.jl with
contourf, 15 levels and the viridis palette. Plots.jl splits the density at 17
evenly spaced values from the grid's least to its greatest, giving 16 bands,
and colours band i with viridis(i / 15). The outer band is the background.

This draws the same bands on a finer grid, so the edges stay sharp at full size,
centred on the background colour. The icon's own square crop clips the outer
ellipse; here the whole ellipse fits, with a margin for the card's corners.

Run once, then commit the PNG: python make_share_image.py
Needs numpy, matplotlib and Pillow.
"""

from __future__ import annotations

import sys
from pathlib import Path

from matplotlib import colormaps
import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "share-icon.png"
WIDTH, HEIGHT = 1200, 630

SIGMA_X, SIGMA_Y, RHO = 1.0, 1.5, 0.6
LEVELS = 15  # Plots.jl's default
BANDS = LEVELS + 1

# The outer ellipse's height as a share of the card's height.
FILL = 0.84
SUPERSAMPLE = 4
LINE_WIDTH = 1.4  # pixels in the final image
LINE_ALPHA = 0.35


def density(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    zx = x / SIGMA_X
    zy = y / SIGMA_Y
    q = (zx * zx - 2 * RHO * zx * zy + zy * zy) / (1 - RHO * RHO)
    return np.exp(-q / 2) / (2 * np.pi * SIGMA_X * SIGMA_Y * np.sqrt(1 - RHO * RHO))


def julia_breaks() -> np.ndarray:
    """The 17 band edges Plots.jl uses for the 151 by 151 grid in the script."""
    x = np.linspace(-4 * SIGMA_X, 4 * SIGMA_X, 151)
    y = np.linspace(-4 * SIGMA_Y, 4 * SIGMA_Y, 151)
    z = density(*np.meshgrid(x, y))
    return np.linspace(z.min(), z.max(), LEVELS + 2)


def draw(width: int, height: int, units_per_pixel: float) -> Image.Image:
    """The bands and the lines between them, centred, at the given scale."""
    s = SUPERSAMPLE
    w, h = width * s, height * s
    step = units_per_pixel / s
    xs = (np.arange(w) - (w - 1) / 2) * step
    ys = ((h - 1) / 2 - np.arange(h)) * step  # rows run downwards; y runs up
    z = density(*np.meshgrid(xs, ys))

    breaks = julia_breaks()
    band = np.clip(np.searchsorted(breaks, z, side="right") - 1, 0, BANDS - 1)
    palette = (colormaps["viridis"](np.arange(BANDS) / (BANDS - 1))[:, :3] * 255).round().astype(np.uint8)
    rgb = palette[band].astype(np.float32)

    # A dark line wherever the band changes, as Plots.jl draws over its fills.
    edge = np.zeros((h, w), dtype=bool)
    edge[:, 1:] |= band[:, 1:] != band[:, :-1]
    edge[1:, :] |= band[1:, :] != band[:-1, :]
    mask = Image.fromarray(edge.astype(np.uint8) * 255)
    grow = max(1, round(LINE_WIDTH * s))
    if grow > 1:
        mask = mask.filter(ImageFilter.MaxFilter(grow if grow % 2 else grow + 1))
    line = np.asarray(mask, dtype=np.float32)[..., None] / 255 * LINE_ALPHA
    rgb = rgb * (1 - line)

    big = Image.fromarray(rgb.round().astype(np.uint8), "RGB")
    return big.resize((width, height), Image.LANCZOS)


def outer_height() -> float:
    """Height, in data units, of the outermost drawn contour."""
    breaks = julia_breaks()
    peak = density(np.array(0.0), np.array(0.0))
    r = np.sqrt(-2 * np.log(breaks[1] / peak))
    return 2 * r * SIGMA_Y


def main() -> None:
    units_per_pixel = outer_height() / (FILL * HEIGHT)
    image = draw(WIDTH, HEIGHT, units_per_pixel)
    image.save(OUT, optimize=True)
    print(f"{OUT.name}: {image.size[0]} by {image.size[1]}")


if __name__ == "__main__":
    sys.exit(main() or 0)
