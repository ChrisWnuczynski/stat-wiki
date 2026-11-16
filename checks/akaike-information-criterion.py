"""Check rank-67 AIC comparisons, inherited mixture table, and practice."""
from pathlib import Path
from math import exp,isclose,log

body=(Path(__file__).resolve().parents[1]/'articles/akaike-information-criterion.qmd').read_text().split('## See also')[0]
rows=[(1,5,-1274.1,2576.7,2558.2,-1278.1),(2,11,-1076.9,2216.5,2175.8,-1088.4),(3,17,-1012.3,2121.6,2058.6,-1033.9),(4,23,-999.7,2130.6,2045.4,-1040.8),(5,29,-995.5,2156.4,2049.0,-1048.7),(6,35,-986.7,2173.0,2043.4,-1058.7)]
for h,d,ll,bic,aic,cv in rows:
 assert d==h*2+h*2*3//2+h-1
 assert round(-2*ll+d*log(300),1)==bic
 assert round(-2*ll+2*d,1)==aic
 for v in (str(d),str(ll),str(bic),str(aic),str(cv)):
  assert v in body,(h,v)
assert min(rows,key=lambda r:r[3])[0]==3
assert min(rows,key=lambda r:r[4])[0]==6
assert max(rows,key=lambda r:r[5])[0]==3
assert isclose(log(300),5.703782474656201)
assert round(17*log(300),3)==96.964
assert round(-2*(-1012.3)+17*log(300),1)==2121.6
assert (-2*(-140)+2*2,-2*(-136)+2*5)==(284,282)
assert (-2*(-50)+2*3,-2*(-48)+2*6)==(106,108)
assert 100>exp(2) and 300>exp(2)
for v in ('5.70378','96.964','2121.6','2043.4','284','282','106','108','7.389'):
 assert v in body,v
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and body.count('title="Answer"')>=3
for heading in ('Motivating example','Worked example','Properties','Common misconceptions','Assumptions and limits','History','Check yourself'):
 assert f'## {heading}' in body
for qid in ('ex-sl-06-2','ex-sl-06-5'):
 assert f'../questions/{qid}.qmd' in body
for key in ('akaike1974','drton_plummer2017','rstats_aic2026','hyndman_athanasopoulos2021'):
 assert f'data-cite-key="{key}"' in body
print('AIC table, model comparisons, penalty and practice passed')
