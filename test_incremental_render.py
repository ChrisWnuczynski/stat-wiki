"""Tests for incremental Quarto rendering and clean-vs-warm output equivalence."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))

import incremental_render as ir  # noqa: E402
import search_meta  # noqa: E402

REDIRECT_STUB = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirect</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url={target}">
<script type="text/javascript">
var redirects = {{"": "{target}"}};
var hash = window.location.hash.startsWith('#') ? window.location.hash.slice(1) : window.location.hash;
var redirect = redirects[hash] || redirects[""] || "/";
window.document.title = 'Redirect to ' + redirect;
window.location.replace(redirect);
</script>
</head>
<body>
<p>This section is in <a href="{target}">{chapter}</a>.</p>
</body>
</html>
"""


def _tree_hashes(site: Path) -> dict[str, str]:
    return {
        p.relative_to(site).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(site.rglob("*"))
        if p.is_file()
    }


def _sitemap_locs(xml_text: str) -> list[str]:
    return sorted(re.findall(r"<loc>(.*?)</loc>", xml_text))


class IncrementalRenderUnitTests(unittest.TestCase):
    def test_real_quarto_yml_config_and_post_render_stripping(self) -> None:
        quarto_yml = ROOT / "_quarto.yml"
        if not quarto_yml.is_file():
            self.skipTest("_quarto.yml has not been generated in ROOT yet")
        yml_text = quarto_yml.read_text(encoding="utf-8")
        cfg = ir.parse_quarto_config(yml_text)
        self.assertEqual(cfg["output_dir"], "_site")
        self.assertEqual(cfg["site_url"], "https://www.statwiki.io")
        self.assertEqual(cfg["favicon"], "favicon.ico")
        self.assertEqual(cfg["css_files"], ["styles.css"])
        self.assertIn("canonical_redirects.py", cfg["post_render"])
        self.assertIn("search_meta.py", cfg["post_render"])
        self.assertIn("share_preview.py", cfg["post_render"])
        self.assertIn("sidebar_share.py", cfg["post_render"])
        self.assertEqual(
            set(cfg["includes"]),
            {"_theme-head.html", "_katex-macros.html", "_theme-body.html", "_random.html"},
        )
        self.assertEqual(cfg["scss_files"], ["theme.scss"])
        self.assertGreater(len(cfg["sidebar_qmds"]), 900)
        self.assertEqual(cfg["sidebar_qmds"][0], "index.qmd")

        stripped = ir.strip_post_render_block(yml_text)
        self.assertNotIn("post-render:", stripped)
        stripped_cfg = ir.parse_quarto_config(stripped)
        self.assertEqual(stripped_cfg["post_render"], [])
        self.assertEqual(stripped_cfg["sidebar_qmds"], cfg["sidebar_qmds"])
        self.assertEqual(stripped_cfg["resources"], cfg["resources"])

    def test_include_shortcode_and_figure_hash_invalidation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "labs").mkdir()
            (root / "articles").mkdir()
            (root / "figures").mkdir()

            partial = root / "labs" / "_partial.qmd"
            partial.write_text("```{ojs}\nx = 1\n```\n", encoding="utf-8")
            fig = root / "figures" / "plot.png"
            fig.write_bytes(b"PNG-V1")

            lab = root / "labs" / "demo.qmd"
            lab.write_text(
                "---\ntitle: Demo lab\n---\n{{< include _partial.qmd >}}\n",
                encoding="utf-8",
            )
            article = root / "articles" / "topic.qmd"
            article.write_text(
                "---\ntitle: Topic\n---\n![Plot](../figures/plot.png)\n",
                encoding="utf-8",
            )
            untouched = root / "articles" / "other.qmd"
            untouched.write_text("---\ntitle: Other\n---\nPlain prose.\n", encoding="utf-8")

            qmds = ir.discover_renderable_qmds(root, "_site")
            self.assertEqual(qmds, ["articles/other.qmd", "articles/topic.qmd", "labs/demo.qmd"])

            state1 = ir.collect_qmds_state(root, qmds, {})
            partial.write_text("```{ojs}\nx = 2\n```\n", encoding="utf-8")
            state2 = ir.collect_qmds_state(root, qmds, {})
            self.assertNotEqual(state1["labs/demo.qmd"]["sha256"], state2["labs/demo.qmd"]["sha256"])
            self.assertEqual(
                state1["articles/topic.qmd"]["sha256"],
                state2["articles/topic.qmd"]["sha256"],
            )
            self.assertEqual(
                state1["articles/other.qmd"]["sha256"],
                state2["articles/other.qmd"]["sha256"],
            )

            fig.write_bytes(b"PNG-V2")
            state3 = ir.collect_qmds_state(root, qmds, {})
            self.assertNotEqual(
                state2["articles/topic.qmd"]["sha256"],
                state3["articles/topic.qmd"]["sha256"],
            )
            self.assertEqual(
                state2["articles/other.qmd"]["sha256"],
                state3["articles/other.qmd"]["sha256"],
            )

    def test_companion_files_and_sidebar_title_neighbors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            yml = "project:\n  type: website\n  output-dir: _site\nwebsite:\n  sidebar:\n    contents:\n      - index.qmd\n      - a.qmd\n      - b.qmd\n      - c.qmd\n"
            cfg = ir.parse_quarto_config(yml)
            sig1 = ir.compute_global_signature(root, yml.encode("utf-8"), cfg, "1.6.40", {})
            (root / "table_a11y.py").write_text("# new accessibility pass\n", encoding="utf-8")
            sig2 = ir.compute_global_signature(root, yml.encode("utf-8"), cfg, "1.6.40", {})
            self.assertNotEqual(sig1, sig2)

            prev_qmds = {
                "index.qmd": {"title": "Home"},
                "a.qmd": {"title": "Alpha"},
                "b.qmd": {"title": "Beta"},
                "c.qmd": {"title": "Gamma"},
            }
            curr_qmds = {
                "index.qmd": {"title": "Home"},
                "a.qmd": {"title": "Alpha"},
                "b.qmd": {"title": "Beta Renamed"},
                "c.qmd": {"title": "Gamma"},
            }
            neighbors = ir._sidebar_title_neighbors(prev_qmds, curr_qmds, cfg["sidebar_qmds"])
            self.assertEqual(neighbors, {"index.qmd", "a.qmd", "c.qmd"})


@unittest.skipUnless(shutil.which("quarto"), "Quarto CLI is required for end-to-end equivalence tests")
class IncrementalRenderEquivalenceTests(unittest.TestCase):
    def _create_mini_statwiki(self, root: Path) -> None:
        for folder in (
            "articles",
            "notes",
            "labs",
            "questions",
            "reference",
            "katex",
            "ask/widget/dist/chunks",
        ):
            (root / folder).mkdir(parents=True, exist_ok=True)

        for name in (
            "canonical_redirects.py",
            "search_meta.py",
            "share_preview.py",
            "sidebar_share.py",
            "styles.css",
            "theme.scss",
            "_theme-head.html",
            "_theme-body.html",
            "share-icon.png",
            "favicon.ico",
            "robots.txt",
            "search-rank.js",
            "home-search.js",
        ):
            shutil.copy2(ROOT / name, root / name)
        shutil.copytree(ROOT / "katex", root / "katex", dirs_exist_ok=True)

        bw_src = (ROOT / "build_wiki.py").read_text(encoding="utf-8")
        sidebar_js_match = re.search(r'SIDEBAR_JS = """(.*?)"""', bw_src, re.S)
        self.assertIsNotNone(sidebar_js_match)
        (root / "_katex-macros.html").write_text("<!-- katex macros -->\n", encoding="utf-8")
        (root / "_random.html").write_text(sidebar_js_match.group(1), encoding="utf-8")
        (root / "wiki.json").write_text('{"version": 1, "entries": [{"id": "a"}]}\n', encoding="utf-8")
        (root / "search-aliases.json").write_text("{}\n", encoding="utf-8")
        (root / "ask/widget/dist/loader.js").write_text("console.log('loader');\n", encoding="utf-8")
        (root / "ask/widget/dist/chunks/app-111.js").write_text("console.log('111');\n", encoding="utf-8")
        (root / "articles/retired-heading.html").write_text(
            REDIRECT_STUB.format(target="../notes/prob-01.html#sec", chapter="Probability 1"),
            encoding="utf-8",
        )

        (root / "_quarto.yml").write_text(
            f"""lang: en
project:
  type: website
  output-dir: _site
  post-render:
    - canonical_redirects.py
    - search_meta.py
    - share_preview.py
    - sidebar_share.py
  render:
    - "*.qmd"
    - "labs/*.qmd"
    - "!labs/_*.qmd"
    - "!sources/"
  resources:
    - katex/
    - robots.txt
    - search-rank.js
    - home-search.js
    - search-aliases.json
    - articles/*.html
    - share-icon.png
    - wiki.json
    - ask/widget/dist/
website:
  title: "StatWiki"
  description: {json.dumps(search_meta.DESCRIPTION)}
  favicon: favicon.ico
  site-url: "https://www.statwiki.io"
  image: /share-icon.png
  image-alt: "Contours of a bivariate normal density in viridis, the StatWiki icon"
  open-graph:
    description: {json.dumps(search_meta.DESCRIPTION)}
    image: /share-icon.png
    image-alt: "Contours of a bivariate normal density in viridis, the StatWiki icon"
    image-width: 1200
    image-height: 630
  twitter-card:
    card-style: summary_large_image
    description: {json.dumps(search_meta.DESCRIPTION)}
    image: /share-icon.png
    image-alt: "Contours of a bivariate normal density in viridis, the StatWiki icon"
  search:
    location: navbar
    type: textbox
  sidebar:
    style: docked
    collapse-level: 2
    contents:
      - text: Main page
        href: index.qmd
      - section: Laboratories
        contents:
          - text: "All laboratories"
            href: labs/index.qmd
      - section: Topics
        href: notes/index.qmd
        contents:
          - section: "Probability distributions"
            contents:
              - text: Overview
                href: notes/probability-distributions.qmd
              - notes/prob-01.qmd
              - text: "Alpha concept"
                href: articles/alpha.qmd
              - text: "Beta concept"
                href: articles/beta.qmd
              - text: "Duplicate one"
                href: articles/dup1.qmd
              - text: "Duplicate two"
                href: articles/dup2.qmd
  page-navigation: true
  page-footer:
    center: "© 2026 StatWiki · Last updated 26 November 2026"
format:
  html:
    theme:
      light: [cosmo, theme.scss]
      dark: [darkly, theme.scss]
    css: styles.css
    toc: true
    html-math-method:
      method: katex
      url: /katex/
    include-in-header:
      - _theme-head.html
      - _katex-macros.html
    include-before-body: _theme-body.html
    include-after-body: _random.html
    canonical-url: true
""",
            encoding="utf-8",
        )

        shared_opening = (
            "An opening sentence exceeding fifty characters shared by two distinct concept pages."
        )
        (root / "index.qmd").write_text(
            "---\ntitle: StatWiki\n---\nWelcome to the statistics study wiki home page.\n",
            encoding="utf-8",
        )
        (root / "404.qmd").write_text(
            "---\ntitle: Page not found\n---\nThat page could not be found on StatWiki.\n",
            encoding="utf-8",
        )
        (root / "labs/index.qmd").write_text(
            '---\ntitle: Laboratories\ndescription: "Interactive browser laboratories for density estimation, updating, and coverage."\n---\nExplore the interactive laboratories.\n',
            encoding="utf-8",
        )
        (root / "notes/index.qmd").write_text(
            "---\ntitle: Topics\n---\nEvery topic chapter in the study wiki.\n",
            encoding="utf-8",
        )
        (root / "notes/probability-distributions.qmd").write_text(
            "---\ntitle: Probability distributions\n---\nOverview of discrete and continuous probability laws.\n",
            encoding="utf-8",
        )
        (root / "notes/prob-01.qmd").write_text(
            "---\ntitle: Probability 1\n---\nFoundational axioms and sample spaces for probability theory. {#sec}\n",
            encoding="utf-8",
        )
        (root / "articles/alpha.qmd").write_text(
            "---\ntitle: Alpha concept\naliases:\n  - alpha-legacy.html\n  - alpha-temp.html\n---\n**Alpha concept.** Detailed exposition of the alpha parameter in exponential families.\n",
            encoding="utf-8",
        )
        (root / "articles/beta.qmd").write_text(
            "---\ntitle: Beta concept\n---\n**Beta concept.** Initial version of the beta article before incremental edits.\n",
            encoding="utf-8",
        )
        (root / "articles/dup1.qmd").write_text(
            f"---\ntitle: Duplicate one\n---\n{shared_opening}\n",
            encoding="utf-8",
        )
        (root / "articles/dup2.qmd").write_text(
            f"---\ntitle: Duplicate two\n---\n{shared_opening}\n",
            encoding="utf-8",
        )
        (root / "questions/old-q.qmd").write_text(
            '---\ntitle: Old Question\ndescription: "Practice question"\n---\nCompute the sample variance from five observations.\n',
            encoding="utf-8",
        )

    def _assert_equivalent_to_clean_render(self, proj: Path, scratch: Path) -> None:
        warm_backup = scratch / "warm_site"
        quarto_backup = scratch / "warm_quarto"
        manifest_backup = scratch / "warm_manifest.json"
        if warm_backup.exists():
            shutil.rmtree(warm_backup)
        if quarto_backup.exists():
            shutil.rmtree(quarto_backup)
        shutil.copytree(proj / "_site", warm_backup)
        shutil.copytree(proj / ".quarto", quarto_backup)
        shutil.copy2(proj / "_build" / "incremental-manifest.json", manifest_backup)

        # Run a clean full Quarto render on the exact same project state.
        shutil.rmtree(proj / "_site")
        shutil.rmtree(proj / ".quarto")
        subprocess.run(["quarto", "render"], cwd=proj, check=True, capture_output=True)
        clean_site = scratch / "clean_site"
        if clean_site.exists():
            shutil.rmtree(clean_site)
        shutil.move(str(proj / "_site"), str(clean_site))
        shutil.rmtree(proj / ".quarto")

        # Restore warm state so subsequent passes continue incrementally.
        shutil.move(str(warm_backup), str(proj / "_site"))
        shutil.move(str(quarto_backup), str(proj / ".quarto"))
        shutil.copy2(manifest_backup, proj / "_build" / "incremental-manifest.json")

        clean_hashes = _tree_hashes(clean_site)
        warm_hashes = _tree_hashes(proj / "_site")
        self.assertEqual(set(clean_hashes), set(warm_hashes), "File set mismatch between clean and warm _site")

        for rel in sorted(clean_hashes):
            if rel in {"search.json", "sitemap.xml"}:
                continue
            self.assertEqual(
                clean_hashes[rel],
                warm_hashes[rel],
                f"Byte mismatch in {rel} between clean and warm render",
            )

        clean_search = {
            e["objectID"]: e
            for e in json.loads((clean_site / "search.json").read_text(encoding="utf-8"))
        }
        warm_search = {
            e["objectID"]: e
            for e in json.loads((proj / "_site" / "search.json").read_text(encoding="utf-8"))
        }
        self.assertEqual(clean_search, warm_search, "search.json entries differ between clean and warm render")

        clean_locs = _sitemap_locs((clean_site / "sitemap.xml").read_text(encoding="utf-8"))
        warm_locs = _sitemap_locs((proj / "_site" / "sitemap.xml").read_text(encoding="utf-8"))
        self.assertEqual(clean_locs, warm_locs, "sitemap.xml <loc> URLs differ between clean and warm render")

    def test_clean_vs_warm_equivalence_across_modes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outer = Path(tmp)
            proj = outer / "wiki"
            scratch = outer / "scratch"
            scratch.mkdir()
            self._create_mini_statwiki(proj)

            # Pass 1: Cold cache -> full render.
            s1 = ir.run_incremental_render(proj)
            self.assertEqual(s1["mode"], "full")
            self.assertEqual(s1["rendered_count"], 11)

            # Pass 2: Zero changes -> noop, refreshes wiki.json mtime.
            old_mtime = (proj / "_site" / "wiki.json").stat().st_mtime
            time.sleep(0.05)
            s2 = ir.run_incremental_render(proj)
            self.assertEqual(s2["mode"], "noop")
            self.assertEqual(s2["rendered_count"], 0)
            self.assertGreater((proj / "_site" / "wiki.json").stat().st_mtime, old_mtime)

            # Pass 2b: Missing cached alias output self-heals on dry-run, and exceeding
            # max_incremental_files falls back to a full render.
            alias_path = proj / "_site" / "articles" / "alpha-legacy.html"
            saved_alias = alias_path.read_bytes()
            alias_path.unlink()
            try:
                heal = ir.run_incremental_render(proj, dry_run=True)
                self.assertEqual(heal["mode"], "incremental")
                self.assertEqual(heal["rendered_qmds"], ["articles/alpha.qmd"])
                capped = ir.run_incremental_render(proj, max_incremental_files=0, dry_run=True)
                self.assertEqual(capped["mode"], "full")
            finally:
                alias_path.write_bytes(saved_alias)

            # Pass 3: Static resources + CSS + rotated Vite chunk -> resources-only.
            (proj / "styles.css").write_text(
                (proj / "styles.css").read_text(encoding="utf-8") + "\n/* warm test */\n",
                encoding="utf-8",
            )
            (proj / "ask/widget/dist/chunks/app-111.js").unlink()
            (proj / "ask/widget/dist/chunks/app-222.js").write_text(
                "console.log('222');\n", encoding="utf-8"
            )
            s3 = ir.run_incremental_render(proj)
            self.assertEqual(s3["mode"], "resources-only")
            self.assertEqual(s3["rendered_qmds"], ["404.qmd"])
            self._assert_equivalent_to_clean_render(proj, scratch)

            # Pass 4: Single-page edit -> renders only that 1 page!
            (proj / "articles/beta.qmd").write_text(
                "---\ntitle: Beta concept\n---\n**Beta concept.** Clarified the positive-denominator condition for beta.\n",
                encoding="utf-8",
            )
            (proj / "wiki.json").write_text(
                '{"version": 1, "entries": [{"id": "a"}, {"id": "b"}]}\n',
                encoding="utf-8",
            )
            s4 = ir.run_incremental_render(proj)
            self.assertEqual(s4["mode"], "incremental")
            self.assertEqual(s4["rendered_qmds"], ["articles/beta.qmd"])
            self._assert_equivalent_to_clean_render(proj, scratch)

            # Pass 5: Multi-page batch with meta-description de-collision, dropped alias,
            # deleted question, and added question.
            (proj / "articles/alpha.qmd").write_text(
                "---\ntitle: Alpha concept\naliases:\n  - alpha-legacy.html\n---\n**Alpha concept.** Updated exposition after dropping alpha-temp alias.\n",
                encoding="utf-8",
            )
            (proj / "articles/dup1.qmd").write_text(
                "---\ntitle: Duplicate one\n---\n**Duplicate one.** Now opens with its own distinct fifty-plus character sentence.\n",
                encoding="utf-8",
            )
            (proj / "questions/old-q.qmd").unlink()
            (proj / "questions/new-q.qmd").write_text(
                '---\ntitle: New Question\ndescription: "Practice question"\n---\nDerive the maximum likelihood estimator for the rate parameter.\n',
                encoding="utf-8",
            )
            s5 = ir.run_incremental_render(proj)
            self.assertEqual(s5["mode"], "incremental")
            self.assertEqual(
                s5["rendered_qmds"],
                ["articles/alpha.qmd", "articles/dup1.qmd", "questions/new-q.qmd"],
            )
            self.assertEqual(s5["deleted_qmds"], ["questions/old-q.qmd"])
            self._assert_equivalent_to_clean_render(proj, scratch)

            # Pass 6: Global template include edit -> automatic fallback to full render.
            (proj / "_theme-head.html").write_text(
                (proj / "_theme-head.html").read_text(encoding="utf-8") + "<!-- global head edit -->\n",
                encoding="utf-8",
            )
            s6 = ir.run_incremental_render(proj)
            self.assertEqual(s6["mode"], "full")
            self._assert_equivalent_to_clean_render(proj, scratch)


if __name__ == "__main__":
    unittest.main()
