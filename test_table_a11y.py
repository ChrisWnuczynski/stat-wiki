"""Captions, column scope, and row headers on generated tables."""

from __future__ import annotations

import unittest

import table_a11y


PAGE = """<!DOCTYPE html><html><body>
<header id="quarto-header"><nav>
<table><tr><td>Menu</td><td>Link</td></tr></table>
</nav></header>
<main id="quarto-document-content">
<h2>Estimates</h2>
<table class="caption-top table">
<thead>
<tr class="header">
<th style="text-align: right;">Event time</th>
<th style="text-align: right;">At risk</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2</td>
<td style="text-align: right;">8</td>
</tr>
<tr class="even">
<td style="text-align: right;">3</td>
<td style="text-align: right;"><span class="math inline">\\mu</span></td>
</tr>
</tbody>
</table>
<div class="infobox">
<div class="infobox-title">
<p>Normal distribution</p>
</div>
<table class="caption-top table">
<thead>
<tr class="header">
<th style="text-align: left;">Fact</th>
<th style="text-align: left;">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">Mean</td>
<td style="text-align: left;"><span class="math inline">\\mu</span></td>
</tr>
</tbody>
</table>
</div>
<table role="presentation"><tr><td>Only</td></tr></table>
<table><caption>Author caption</caption><tbody>
<tr><td>Kept</td><td>1</td></tr>
</tbody></table>
</main>
</body></html>
"""


class TableAccessibilityTests(unittest.TestCase):
    def test_content_tables_gain_captions_scope_and_row_headers(self) -> None:
        fixed = table_a11y.accessible_tables(PAGE)
        self.assertEqual(table_a11y.accessible_tables(fixed), fixed)
        self.assertIn('<th style="text-align: right;" scope="col">Event time</th>', fixed)
        self.assertIn('<th style="text-align: right;" scope="col">At risk</th>', fixed)
        # The first number is a measurement, not a row label.
        self.assertIn('<td style="text-align: right;">2</td>', fixed)
        self.assertNotIn('scope="row">2<', fixed)
        self.assertIn('<td style="text-align: right;"><span class="math inline">\\mu</span></td>', fixed)
        self.assertIn('<caption class="a11y-caption">Estimates: Event time, At risk</caption>', fixed)
        self.assertIn('<caption class="a11y-caption">Normal distribution</caption>', fixed)
        self.assertNotIn("Fact, Value", fixed)
        self.assertIn('<th style="text-align: left;" scope="row">Mean</th>', fixed)
        self.assertIn('<th style="text-align: left;" scope="col">Fact</th>', fixed)
        # The navigation table and a presentation table are not data tables.
        self.assertIn("<nav>\n<table><tr><td>Menu</td><td>Link</td></tr></table>", fixed)
        self.assertIn('<table role="presentation"><tr><td>Only</td></tr></table>', fixed)
        self.assertEqual(fixed.count("<caption>Author caption</caption>"), 1)
        self.assertIn("<td>Kept</td>", fixed)
        self.assertNotIn('scope="col" scope="col"', fixed)
        self.assertNotIn('scope="row" scope="row"', fixed)

    def test_numeric_body_cells_stay_data_and_grouped_headers_are_left_alone(self) -> None:
        page = """<main id="quarto-document-content">
<h2>Residuals</h2>
<table>
<thead><tr><th>Residual A</th><th>Residual B</th></tr></thead>
<tbody><tr><td>3</td><td>8</td></tr></tbody>
</table>
<table>
<thead>
<tr><th colspan="2">Residuals</th></tr>
<tr><th>A</th><th>B</th></tr>
</thead>
<tbody><tr><td>3</td><td>8</td></tr></tbody>
</table>
<table>
<thead><tr><th scope="colgroup" colspan="2">Already named</th></tr></thead>
<tbody><tr><td>1</td><td>2</td></tr></tbody>
</table>
</main>"""
        fixed = table_a11y.accessible_tables(page)
        self.assertIn("<th>Residual A</th>", fixed.replace(' scope="col"', ""))
        self.assertIn('<th scope="col">Residual A</th>', fixed)
        self.assertIn("<td>3</td>", fixed)
        self.assertIn("<td>8</td>", fixed)
        self.assertNotIn('scope="row"', fixed)
        grouped = fixed.split("<table>", 2)[2]
        self.assertIn('<th colspan="2">Residuals</th>', grouped)
        self.assertIn("<th>A</th>", grouped)
        self.assertNotIn("scope=", grouped.split("</table>", 1)[0])
        self.assertIn('<th scope="colgroup" colspan="2">Already named</th>', fixed)
        self.assertNotIn('scope="col" colspan="2">Already named', fixed)

    def test_a_break_inside_a_heading_still_names_the_table(self) -> None:
        page = """<main id="quarto-document-content">
<h2>Results<br>by model</h2>
<table><thead><tr><th>A</th><th>B</th></tr></thead>
<tbody><tr><td>1</td><td>2</td></tr></tbody></table>
<h2>Results<br/>by picture <img alt="of the fit"></h2>
<table><thead><tr><th>C</th><th>D</th></tr></thead>
<tbody><tr><td>4</td><td>5</td></tr></tbody></table>
</main>"""
        fixed = table_a11y.accessible_tables(page)
        self.assertIn('<caption class="a11y-caption">Results by model: A, B</caption>', fixed)
        self.assertIn("Results by picture of the fit: C, D", fixed)
        self.assertNotIn("Resultsby model", fixed)


if __name__ == "__main__":
    unittest.main()
