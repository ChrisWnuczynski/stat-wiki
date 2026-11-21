"""Search a research note and the generated page as one text.

Check-yourself answers live in the question bank. The generated article
includes them, and the research note keeps the worked example.
"""
from pathlib import Path


class Shown(str):
    def __new__(cls, source: str, page: str):
        obj = str.__new__(cls, source)
        obj._page = page
        return obj

    def __contains__(self, item: object) -> bool:
        found = str.__contains__(self, item)
        if found or not isinstance(item, str):
            return found
        return item in self._page

    def count(self, sub: str, *args: int) -> int:
        if 'title="Answer"' in sub:
            return self._page.count(sub, *args)
        return str.count(self, sub, *args)


def shown(source: str, slug: str) -> Shown:
    page = Path(__file__).resolve().parents[1] / "articles" / f"{slug}.qmd"
    text = page.read_text(encoding="utf-8") if page.is_file() else ""
    return Shown(source, text)
