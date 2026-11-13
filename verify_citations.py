"""Verify every bibliographic entry in bibliography.json against live APIs.

Usage:
    python3 verify_citations.py            # full live Crossref/OpenAlex/OpenLibrary/URL check
    python3 verify_citations.py --offline  # schema, provenance, and banned-term validation only
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BIB_PATH = ROOT / "bibliography.json"

USER_AGENT = "StatWikiBibliographyVerifier/1.0 (https://www.statwiki.io)"
HEADERS = {"User-Agent": USER_AGENT}

BANNED_PATTERN = re.compile(
    r"STAT\s*\d{4}"
    r"|\bgithub\b"
    r"|\bapplied\s+practice\s+sets?\b"
    r"|\bpractice\s+sets?\b"
    r"|\bbooklets?\b"
    r"|\blecture\s+notes\b"
    r"|\bcourse\s+notes\b",
    re.I,
)

ALLOWED_KINDS = {"article", "book", "incollection"}
ALLOWED_SOURCES = {"crossref", "crossref_container", "openalex", "openlibrary", "archival_url"}


def fold(text: str) -> str:
    clean = "".join(
        ch for ch in unicodedata.normalize("NFKD", text or "") if not unicodedata.combining(ch)
    )
    return re.sub(r"[^a-z0-9 ]+", " ", clean.lower()).strip()


def title_tokens(text: str) -> set[str]:
    stop = {"a", "an", "and", "by", "de", "der", "des", "die", "for", "from", "in", "la", "le", "les", "of", "on", "sur", "the", "to", "und", "with"}
    return {tok for tok in fold(text).split() if len(tok) >= 3 and tok not in stop}


def primary_surname(author: str) -> str:
    head = author.split(",", 1)[0].split("[", 1)[0].strip()
    parts = fold(head).split()
    return parts[-1] if parts else ""


def fetch_json(url: str, retries: int = 4) -> dict:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=25) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            last_err = exc
            time.sleep(0.8 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed: {last_err}")


def check_url_resolves(url: str, retries: int = 3) -> int:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS, method="GET")
            with urllib.request.urlopen(req, timeout=25) as resp:
                return resp.status
        except Exception as exc:
            last_err = exc
            time.sleep(0.8 * (attempt + 1))
    raise RuntimeError(f"URL {url} did not resolve: {last_err}")


def validate_schema(bib: dict) -> list[str]:
    errors: list[str] = []
    works = bib.get("works")
    if not isinstance(works, dict) or not works:
        return ["bibliography.json must contain a non-empty 'works' mapping"]

    raw_blob = json.dumps(bib, ensure_ascii=False)
    for match in BANNED_PATTERN.finditer(raw_blob):
        errors.append(f"banned term in bibliography.json: {match.group(0)!r}")

    for key, work in sorted(works.items()):
        if not re.fullmatch(r"[a-z0-9_]+", key):
            errors.append(f"{key}: invalid citation key format")
        authors = work.get("authors")
        if not isinstance(authors, list) or not authors or not all(isinstance(a, str) and a.strip() for a in authors):
            errors.append(f"{key}: missing or invalid authors list")
        year = work.get("year")
        if not isinstance(year, int) or not (1600 <= year <= 2026):
            errors.append(f"{key}: invalid publication year {year!r}")
        title = work.get("title")
        if not isinstance(title, str) or len(title.strip()) < 3:
            errors.append(f"{key}: missing or invalid title")
        kind = work.get("kind")
        if kind not in ALLOWED_KINDS:
            errors.append(f"{key}: invalid kind {kind!r}")
        if kind == "article" and not work.get("venue"):
            errors.append(f"{key}: journal article must specify 'venue'")
        if kind == "book" and not work.get("publisher"):
            errors.append(f"{key}: book/monograph must specify 'publisher'")
        if kind == "incollection" and not (work.get("venue") or work.get("publisher")):
            errors.append(f"{key}: incollection must specify 'venue' or 'publisher'")
        doi = work.get("doi")
        url = work.get("url")
        if not doi and not url:
            errors.append(f"{key}: must provide either 'doi' or archival/publisher 'url'")
        if doi and (doi.startswith("http") or " " in doi or not doi.startswith("10.")):
            errors.append(f"{key}: malformed DOI {doi!r}")
        if url and not url.startswith(("https://", "http://")):
            errors.append(f"{key}: malformed URL {url!r}")
        ver = work.get("verification")
        if not isinstance(ver, dict) or ver.get("source") not in ALLOWED_SOURCES or not ver.get("id"):
            errors.append(f"{key}: missing or invalid verification provenance {ver!r}")
    return errors


def verify_one_live(item: tuple[str, dict]) -> list[str]:
    key, work = item
    ver = work["verification"]
    src = ver["source"]
    ident = ver["id"]
    problems: list[str] = []

    try:
        if src in {"crossref", "crossref_container"}:
            doi = work.get("doi")
            if not doi or doi.lower() != ident.lower():
                return [f"{key}: verification id {ident!r} does not match doi {doi!r}"]
            msg = fetch_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))["message"]
            cr_years: set[int] = set()
            for dk in ("published-print", "published-online", "issued", "created"):
                for part in msg.get(dk, {}).get("date-parts", []):
                    if part and isinstance(part[0], int):
                        cr_years.add(part[0])
            expected_year = int(ver.get("reprint_year") or work["year"])
            tol = int(ver.get("year_tolerance", 0))
            if cr_years and not any(abs(y - expected_year) <= tol for y in cr_years):
                problems.append(f"{key}: Crossref years {sorted(cr_years)} do not match expected {expected_year}")
            if src == "crossref":
                cr_title = " ".join(msg.get("title") or []) + " " + " ".join(msg.get("subtitle") or [])
                want = title_tokens(work["title"])
                got = title_tokens(cr_title)
                if want and got:
                    overlap = len(want & got) / min(len(want), len(got))
                    if overlap < 0.5:
                        problems.append(f"{key}: Crossref title mismatch ({cr_title!r} vs {work['title']!r})")
                cr_authors = fold(json.dumps(msg.get("author") or [], ensure_ascii=False)) + " " + fold(cr_title)
                surname = primary_surname(work["authors"][0])
                if msg.get("author") and surname and surname not in {"council", "student"} and surname not in cr_authors:
                    problems.append(f"{key}: primary author {surname!r} not found in Crossref metadata")

        elif src == "openalex":
            oa_id = ident.split("/")[-1]
            msg = fetch_json(f"https://api.openalex.org/works/{oa_id}")
            oa_year = msg.get("publication_year")
            if oa_year and abs(int(oa_year) - int(work["year"])) > 1:
                problems.append(f"{key}: OpenAlex year {oa_year} != {work['year']}")
            oa_title = (msg.get("display_name") or msg.get("title") or "") + " " + (work.get("venue") or "")
            want = title_tokens(work["title"] if work.get("kind") != "incollection" else (work.get("venue") or work["title"]))
            got = title_tokens(oa_title)
            if want and got and len(want & got) / min(len(want), len(got)) < 0.5:
                problems.append(f"{key}: OpenAlex title mismatch ({oa_title!r} vs {work['title']!r})")
            if work.get("url") and not work["url"].startswith("https://openalex.org/"):
                status = check_url_resolves(work["url"])
                if status >= 400:
                    problems.append(f"{key}: URL {work['url']} returned HTTP {status}")

        elif src == "openlibrary":
            ol_path = ident if ident.startswith("/") else f"/works/{ident}"
            msg = fetch_json(f"https://openlibrary.org{ol_path}.json")
            ol_title = msg.get("title") or ""
            want = title_tokens(work["title"])
            got = title_tokens(ol_title)
            if want and got and len(want & got) / min(len(want), len(got)) < 0.5:
                problems.append(f"{key}: OpenLibrary title mismatch ({ol_title!r} vs {work['title']!r})")

        elif src == "archival_url":
            url = work.get("url") or ident
            status = check_url_resolves(url)
            if status >= 400:
                problems.append(f"{key}: archival URL {url} returned HTTP {status}")
    except Exception as exc:
        problems.append(f"{key}: live verification error ({exc})")

    return problems


def verify_all(bib_path: Path = BIB_PATH, *, offline: bool = False, workers: int = 8) -> list[str]:
    bib = json.loads(bib_path.read_text(encoding="utf-8"))
    errors = validate_schema(bib)
    if errors or offline:
        return errors

    works = bib["works"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for errs in pool.map(verify_one_live, sorted(works.items())):
            errors.extend(errs)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Run schema and provenance checks without network calls")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent HTTP workers for live verification")
    args = parser.parse_args(argv)

    t0 = time.time()
    errors = verify_all(BIB_PATH, offline=args.offline, workers=args.workers)
    works_count = len(json.loads(BIB_PATH.read_text(encoding="utf-8")).get("works", {}))
    if errors:
        print(f"Verification FAILED ({len(errors)} problems across {works_count} works):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    mode = "offline schema" if args.offline else "live Crossref/OpenAlex/OpenLibrary/URL"
    print(f"Verified all {works_count} bibliography entries ({mode}) in {time.time() - t0:.1f}s.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
