// The R blocks of a chapter source, in reading order.
// Only fences tagged r (```r or ```{r ...}) count. Output fences have no tag.

export function rBlocks(source) {
  const blocks = [];
  const lines = String(source).split(/\r?\n/);
  let open = null;
  let body = [];
  for (const line of lines) {
    if (open === null) {
      const start = line.match(/^(`{3,})\s*(\{\s*\.?r\b[^}]*\}|r)\s*$/);
      if (start) {
        open = start[1];
        body = [];
      }
      continue;
    }
    if (line.startsWith(open) && line.slice(open.length).trim() === "") {
      blocks.push(body.join("\n"));
      open = null;
      continue;
    }
    body.push(line);
  }
  return blocks;
}
