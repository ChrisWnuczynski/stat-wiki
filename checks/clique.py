"""Check clique enumeration and page structure."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/clique.qmd").read_text().split("## See also", 1)[0]
edges = {(1,2),(1,3),(2,3),(2,4),(3,4),(4,5),(4,6),(5,6)}
def complete(vs):
    return all((min(a,b), max(a,b)) in edges for a in vs for b in vs if a<b)
assert complete((1,2,3)) and complete((2,3,4)) and complete((4,5,6))
assert not complete((1,2,4))
# four-vertex graph
e2 = {(1,2),(2,3),(1,3),(3,4)}
def comp(vs, edges):
    return all((min(a,b), max(a,b)) in edges for a in vs for b in vs if a<b)
assert comp((1,2,3), e2) and comp((3,4), e2) and not comp((1,2,4), e2)
# added edge 14
e3 = e2 | {(1,4)}
assert comp((1,3,4), e3) and not comp((1,2,4), e3)
assert body.count('title="Proof"') >= 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="evans2025_graphical"' in body
print("clique passed")
