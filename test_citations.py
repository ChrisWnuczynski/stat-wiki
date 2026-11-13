"""Tests for academic bibliography records, concept-specific mappings, and site rules."""

from __future__ import annotations

import json
import re
import unittest
from collections import Counter
from pathlib import Path

import build_wiki
import citations
import verify_citations

ROOT = Path(__file__).resolve().parent

BANNED_VISIBLE = re.compile(
    r"STAT\s*\d"
    r"|\bgithub\b"
    r"|\bapplied\s+practice\s+sets?\b"
    r"|\bpractice\s+sets?\b"
    r"|\bbooklets?\b"
    r"|\blecture\s+notes\b"
    r"|\bcourse\s+notes\b",
    re.I,
)


class CitationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bib = json.loads((ROOT / "bibliography.json").read_text(encoding="utf-8"))
        self.works = self.bib["works"]

    def test_bibliography_schema_and_provenance(self) -> None:
        errors = verify_citations.validate_schema(self.bib)
        self.assertEqual(errors, [])
        self.assertGreaterEqual(len(self.works), 300)

    def test_zero_banned_terms_in_bibliography_and_mappings(self) -> None:
        for rel in ("bibliography.json", "citations.py", "overview.qmd"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            match = BANNED_VISIBLE.search(text)
            self.assertIsNone(match, f"Banned term {match.group(0)!r} in {rel}" if match else "")
        for lab in sorted((ROOT / "labs").glob("*.qmd")):
            if lab.name.startswith("_"):
                continue
            text = lab.read_text(encoding="utf-8")
            match = BANNED_VISIBLE.search(text)
            self.assertIsNone(match, f"Banned term {match.group(0)!r} in {lab}" if match else "")

    def test_every_mapped_citation_key_exists(self) -> None:
        missing: list[tuple[str, str]] = []
        for k in citations.OVERVIEW_REFS:
            if k not in self.works:
                missing.append(("overview.qmd", k))
        for page, keys in citations.REFERENCE_REFS.items():
            for k in keys:
                if k not in self.works:
                    missing.append((f"reference/{page}", k))
        for page, keys in citations.LAB_REFS.items():
            for k in keys:
                if k not in self.works:
                    missing.append((f"labs/{page}", k))
        for qid, keys in citations.QUESTION_REFS.items():
            for k in keys:
                if k not in self.works:
                    missing.append((f"questions/{qid}", k))
        for fname, keys in citations.CHAPTER_REFS.items():
            self.assertTrue(keys, f"Chapter {fname} has empty citation tuple")
            for k in keys:
                if k not in self.works:
                    missing.append((f"notes/{fname}", k))
        for slugs, keys in citations.ARTICLE_GROUPS:
            self.assertTrue(slugs)
            self.assertTrue(keys)
            for k in keys:
                if k not in self.works:
                    missing.append((f"article:{slugs[0]}", k))
        for needle, keys in citations.KEYWORD_FALLBACKS:
            for k in keys:
                if k not in self.works:
                    missing.append((f"fallback:{needle}", k))
        self.assertEqual(missing, [])

    def test_all_chapters_in_parts_are_mapped_and_preserve_source_attributions(self) -> None:
        part_chapters = [fname for _, files in build_wiki.PARTS for fname, kind in files if kind == "notes"]
        self.assertEqual(len(part_chapters), 97)
        for fname in part_chapters:
            self.assertIn(fname, citations.CHAPTER_REFS, f"Unmapped chapter {fname}")
            self.assertGreaterEqual(len(citations.CHAPTER_REFS[fname]), 2, fname)

        required_chapter_pairs = [
            ("02-inference-and-counts.qmd", "bliss1935"),
            ("02-inference-and-counts.qmd", "myers_glm2010"),
            ("02-inference-and-counts.qmd", "conway_maxwell1962"),
            ("02-inference-and-counts.qmd", "shmueli2005"),
            ("02-inference-and-counts.qmd", "huang2017_cmp"),
            ("03-gamma-and-quasi.qmd", "cameron_johansson1997"),
            ("03-gamma-and-quasi.qmd", "huang_rathouz2017"),
            ("03-gamma-and-quasi.qmd", "wedderburn1974"),
            ("04-categorical-responses.qmd", "mccullagh1980"),
            ("04-categorical-responses.qmd", "yee2015"),
            ("05-comparisons-and-deviance.qmd", "bradley_terry1952"),
            ("05-comparisons-and-deviance.qmd", "mccullagh_nelder1989"),
            ("06-pit-residuals.qmd", "dunn_smyth1996"),
            ("06-smooth-means.qmd", "green_silverman1994"),
            ("06-smooth-means.qmd", "ruppert_wand_carroll2003"),
            ("07-additive-and-mixed.qmd", "hastie_tibshirani1986"),
            ("07-additive-and-mixed.qmd", "hastie_tibshirani1990"),
            ("09-marginal-models.qmd", "liang_zeger1986"),
            ("09-marginal-models.qmd", "song2007_burn"),
            ("12-time-series.qmd", "wold1938"),
            ("11-forecasting.qmd", "hyndman_khandakar2008"),
            ("bayes-04-mcmc.qmd", "metropolis1953"),
            ("bayes-04-mcmc.qmd", "hastings1970"),
            ("bayes-04-mcmc.qmd", "geman_geman1984"),
            ("bayes-04-mcmc.qmd", "gubernatis2005"),
            ("bayes-08-hierarchy.qmd", "dempster_selwyn_weeks1983"),
            ("bayes-08-hierarchy.qmd", "gelman2006"),
            ("bayes-08-hierarchy.qmd", "gelman_bda2013"),
            ("sl-05-mixtures-em.qmd", "dempster_laird_rubin1977"),
            ("sl-05-mixtures-em.qmd", "wu1983"),
            ("sl-05-mixtures-em.qmd", "mclachlan_peel2000_book"),
            ("sl-05-mixtures-em.qmd", "peel_mclachlan2000_t"),
            ("sl-06-model-selection.qmd", "akaike1974"),
            ("sl-06-model-selection.qmd", "schwarz1978"),
            ("sl-06-model-selection.qmd", "smyth2000"),
            ("sl-09-error-rates.qmd", "efron1979"),
            ("sl-09-error-rates.qmd", "cawley_talbot2010"),
            ("sl-11-nearest-neighbours.qmd", "olshen1977"),
            ("sl-11-nearest-neighbours.qmd", "devroye1978"),
            ("sl-13-ensembles.qmd", "schapire1990"),
            ("sl-13-ensembles.qmd", "freund_schapire1995"),
            ("sl-13-ensembles.qmd", "friedman_hastie_tibshirani2000"),
            ("sl-13-ensembles.qmd", "breiman2001_rf"),
            ("sl-16-networks-in-practice.qmd", "bridle1990"),
            ("sl-16-networks-in-practice.qmd", "krogh_hertz1992"),
            ("sl-16-networks-in-practice.qmd", "pomerleau1989"),
            ("sl-16-networks-in-practice.qmd", "lecun1998"),
            ("sl-17-support-vectors.qmd", "boser_guyon_vapnik1992"),
            ("sl-17-support-vectors.qmd", "cortes_vapnik1995"),
            ("sl-18-high-dimensional.qmd", "dempster1958"),
            ("sl-18-high-dimensional.qmd", "hoerl_kennard1970"),
            ("sl-18-high-dimensional.qmd", "donoho_johnstone1994"),
            ("sl-18-high-dimensional.qmd", "breiman1995_garrote"),
            ("sl-18-high-dimensional.qmd", "tibshirani1996"),
            ("sl-18-high-dimensional.qmd", "zou2006"),
            ("sl-18-high-dimensional.qmd", "benjamini_hochberg1995"),
            ("sl-18-high-dimensional.qmd", "alon1999"),
            ("sl-19-graphical-models.qmd", "lauritzen1996"),
            ("sl-19-graphical-models.qmd", "speed_kiiveri1986"),
            ("sl-19-graphical-models.qmd", "friedman_glasso2008"),
            ("sl-19-graphical-models.qmd", "foygel_drton2010"),
            ("ur-04-mixtures-and-clustering.qmd", "baek_mclachlan_flack2010"),
        ]
        for fname, key in required_chapter_pairs:
            self.assertIn(key, citations.CHAPTER_REFS[fname], f"{fname} missing {key}")

    def test_article_mappings_are_concept_specific_not_generic(self) -> None:
        counts = Counter(citations.ARTICLE_REFS.values())
        most_common_refs, top_count = counts.most_common(1)[0]
        self.assertLessEqual(
            top_count,
            10,
            f"Reference tuple {most_common_refs} reused {top_count} times; mappings must stay concept-specific",
        )
        self.assertGreaterEqual(len(counts), 120)

        specific_checks = [
            ("bayes-rule", "bayes1763"),
            ("student-t-distribution", "student1908"),
            ("wald-interval", "wilson1927"),
            ("neyman-pearson-lemma", "neyman_pearson1933"),
            ("cramer-rao-lower-bound", "rao1945"),
            ("rao-blackwell-theorem", "blackwell1947"),
            ("lehmann-scheffe-theorem", "lehmann_scheffe1950"),
            ("basu-s-theorem", "basu1955"),
            ("wilks-theorem", "wilks1938"),
            ("welch-interval", "welch1947"),
            ("metropolis-hastings-update", "hastings1970"),
            ("systematic-scan-gibbs-sampler", "geman_geman1984"),
            ("generalised-linear-model", "nelder_wedderburn1972"),
            ("quasi-likelihood", "wedderburn1974"),
            ("bradley-terry-model", "bradley_terry1952"),
            ("conway-maxwell-poisson-distribution", "conway_maxwell1962"),
            ("wold-decomposition", "wold1938"),
            ("little-s-law", "little1961"),
            ("akaike-information-criterion", "akaike1974"),
            ("bayesian-information-criterion", "schwarz1978"),
            ("em-algorithm", "dempster_laird_rubin1977"),
            ("bootstrap", "efron1979"),
            ("lasso", "tibshirani1996"),
            ("ridge-regression", "hoerl_kennard1970"),
            ("benjamini-hochberg", "benjamini_hochberg1995"),
            ("random-forest", "breiman2001_rf"),
            ("adaboost", "freund_schapire1997"),
            ("graphical-lasso", "friedman_glasso2008"),
            ("iris-data", "fisher1936"),
            ("birth-weight-data", "hosmer_lemeshow2000"),
            ("sleep-deprivation-data", "belenky2003"),
            ("heart-failure-data", "chicco_jurman2020"),
            ("alon-colon-cancer-data", "alon1999"),
        ]
        for slug, expected_key in specific_checks:
            self.assertIn(expected_key, citations.ARTICLE_REFS[slug], f"{slug} missing {expected_key}")

    def test_alias_retirement_and_unknown_article_resilience(self) -> None:
        # American spelling / plural / alias resolution
        aliased = {
            "slug": "glm",
            "term": "GLM",
            "aliases": ["generalized-linear-models.html"],
            "box": {"chapter": Path("notes/01-introduction-to-glms.qmd")},
        }
        self.assertIn("nelder_wedderburn1972", citations.citations_for_article(aliased))

        # Chapter-disambiguated slug resolution
        disambig = {
            "slug": "normal-distribution-sl-01-multivariate-normal",
            "term": "Normal distribution",
            "aliases": [],
            "box": {"chapter": Path("notes/sl-01-multivariate-normal.qmd")},
        }
        self.assertIn("gauss1809", citations.citations_for_article(disambig))

        # Brand-new future slug falls back cleanly by keyword or chapter without crashing
        future_kw = {
            "slug": "adaptive-metropolis-sampler",
            "term": "Adaptive Metropolis sampler",
            "aliases": [],
            "box": {"chapter": Path("notes/bayes-04-mcmc.qmd")},
        }
        refs_kw = citations.citations_for_article(future_kw)
        self.assertIn("metropolis1953", refs_kw)
        self.assertTrue(all(k in self.works for k in refs_kw))

        future_ch = {
            "slug": "completely-new-concept-xyz",
            "term": "Completely new concept",
            "aliases": [],
            "box": {"chapter": Path("notes/sp-08-queues.qmd")},
        }
        refs_ch = citations.citations_for_article(future_ch)
        self.assertTrue(refs_ch)
        self.assertTrue(all(k in self.works for k in refs_ch))

    def test_built_pages_carry_references_and_no_banned_labels(self) -> None:
        notes_dir = ROOT / "notes"
        articles_dir = ROOT / "articles"
        if not notes_dir.is_dir() or not articles_dir.is_dir():
            self.skipTest("Generated wiki directories are not built yet")

        # 1. All 97 PARTS chapters + 3 final-prep chapters
        part_chapters = [fname for _, files in build_wiki.PARTS for fname, kind in files if kind == "notes"]
        for fname in part_chapters + ["final-preparation.qmd", "final-bayesian.qmd", "final-applied.qmd"]:
            path = notes_dir / fname
            self.assertTrue(path.is_file(), f"Missing chapter {path}")
            text = path.read_text(encoding="utf-8")
            self.assertIn("## References {#references}", text, fname)
            self.assertRegex(text, r"https?://", fname)
            self.assertIsNone(BANNED_VISIBLE.search(text), f"Banned term in {path}")

        # 2. All ~725 concept articles
        article_files = sorted(articles_dir.glob("*.qmd"))
        self.assertGreaterEqual(len(article_files), 700)
        for path in article_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("## References {#references}", text, path.name)
            self.assertRegex(text, r"https?://", path.name)
            self.assertIsNone(BANNED_VISIBLE.search(text), f"Banned term in {path}")

        # 3. Overview, reference sheets, labs, and dataset questions
        static_and_sheets = [
            ROOT / "overview.qmd",
            ROOT / "reference" / "distributions.qmd",
            ROOT / "reference" / "formulas.qmd",
            *[ROOT / "labs" / name for name in citations.LAB_REFS],
            *[ROOT / "questions" / f"{qid}.qmd" for qid in citations.QUESTION_REFS],
        ]
        for path in static_and_sheets:
            self.assertTrue(path.is_file(), f"Missing page {path}")
            text = path.read_text(encoding="utf-8")
            self.assertIn("## References {#references}", text, str(path))
            self.assertRegex(text, r"https?://", str(path))
            self.assertIsNone(BANNED_VISIBLE.search(text), f"Banned term in {path}")


if __name__ == "__main__":
    unittest.main()
