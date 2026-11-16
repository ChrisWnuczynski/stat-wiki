# Local sources

The private Dodge (2008) source is outside this repo at `~/statwiki-sources/dodge2008/`. On a managed workspace where home is read-only, use `/workspace/statwiki-sources/dodge2008/` or set `STATWIKI_DODGE_DIR`. Before writing a new research page, run `python research/check_sources.py`; if it fails, stop and report the missing source. Search `index.tsv` for an entry name, then open its `pages/pdf-NNNN.txt` file; each file marks both the PDF page and the printed book page. The original PDF is there as `dodge2008.pdf`. Do not commit the PDF or extracted text.

- Use Dodge for orientation, history, and pointers to original papers.
- Cite only material actually read there, always with the printed page number: `{{cite:dodge2008}} (p. n)`.
- For named results and proofs, prefer the original paper or a standard textbook; check important claims against a second source.
- Write in your own words; never copy entries.
