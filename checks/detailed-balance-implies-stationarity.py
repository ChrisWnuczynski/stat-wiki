from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
P=[[F(3,4),F(1,4)],[F(1,2),F(1,2)]];pi=[F(2,3),F(1,3)]
assert pi[0]*P[0][1]==pi[1]*P[1][0]==F(1,6)
assert [sum(pi[i]*P[i][j] for i in range(2)) for j in range(2)]==pi
C=[[0,1,0],[0,0,1],[1,0,0]];u=[F(1,3)]*3
assert [sum(u[i]*C[i][j] for i in range(3)) for j in range(3)]==u
assert u[0]*C[0][1]!=u[1]*C[1][0]
printed=['1/6','2/3','3/4']

article=(ROOT/"articles"/"detailed-balance-implies-stationarity.qmd").read_text()
for token in printed:
    assert token in article,("detailed-balance-implies-stationarity",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["detailed-balance-implies-stationarity"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("detailed-balance-implies-stationarity: numerical examples, self-checks and generated text verified")
