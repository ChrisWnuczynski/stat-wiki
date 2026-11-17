"""The approved prose-correction hook must fail visibly and stay page-scoped."""
import unittest
from unittest.mock import patch
import build_wiki


class SourceCorrectionTests(unittest.TestCase):
    def test_corrects_locator_without_changing_equations_or_figures(self):
        blocks = [(True, 'statement', '$E(X)=2$. {{cite:old}}\n![density](density.png)')]
        corrections = {'target': [('{{cite:old}}', '{{cite:proper}} (§2.1)')]}
        with patch.dict(build_wiki.ARTICLE_SOURCE_CORRECTIONS, corrections, clear=True):
            result = build_wiki.apply_article_source_corrections('target', blocks)
        self.assertEqual(result, [(True, 'statement', '$E(X)=2$. {{cite:proper}} (§2.1)\n![density](density.png)')])
        self.assertEqual(blocks[0][2], '$E(X)=2$. {{cite:old}}\n![density](density.png)')

    def test_does_not_change_another_page(self):
        blocks = [(True, 'statement', 'A source statement.')]
        with patch.dict(build_wiki.ARTICLE_SOURCE_CORRECTIONS, {'target': [('source', 'checked source')]}, clear=True):
            result = build_wiki.apply_article_source_corrections('another-page', blocks)
        self.assertIs(result, blocks)

    def test_absent_target_raises_instead_of_silently_passing(self):
        with patch.dict(build_wiki.ARTICLE_SOURCE_CORRECTIONS, {'target': [('absent fragment', 'replacement')]}, clear=True):
            with self.assertRaisesRegex(ValueError, 'target: source correction target is absent'):
                build_wiki.apply_article_source_corrections('target', [(True, 'statement', 'Different text.')])

    def test_empty_target_cannot_insert_text_everywhere(self):
        with patch.dict(build_wiki.ARTICLE_SOURCE_CORRECTIONS, {'target': [('', 'replacement')]}, clear=True):
            with self.assertRaises(ValueError):
                build_wiki.apply_article_source_corrections('target', [(True, 'statement', 'Text.')])


class ReferenceOverrideTests(unittest.TestCase):
    def test_explicit_override_leaves_other_pages_defaults_unchanged(self):
        from types import SimpleNamespace
        module = SimpleNamespace(ARTICLE_REFS={'target': ('old',), 'other': ('keep',)})
        with patch.dict(build_wiki.ARTICLE_REFERENCE_KEYS, {'target': ['proper']}, clear=True):
            build_wiki.apply_article_reference_keys(module)
        self.assertEqual(module.ARTICLE_REFS, {'target': ('proper',), 'other': ('keep',)})

    def test_empty_override_uses_inline_sources_without_alias_fallback(self):
        import citations
        with patch.dict(citations.ARTICLE_REFS, {'old-course': ('lecture',)}, clear=True):
            with patch.dict(build_wiki.ARTICLE_REFERENCE_KEYS, {'target': []}, clear=True):
                build_wiki.apply_article_reference_keys(citations)
            self.assertEqual(citations.citations_for_article({'slug': 'target', 'aliases': ['old-course']}), ())


if __name__ == '__main__':
    unittest.main()
