"""Recompute every number in the propensity-score article's worked example
and Your turn exercise, from the raw counts, using exact fractions.
Exit 0 only if all assertions pass.
"""
from fractions import Fraction as F
import math

# ---------- Worked example ----------
# Younger (X=0): 40 patients, 10 treated (4 events), 30 untreated (6 events)
# Older   (X=1): 40 patients, 30 treated (24 events), 10 untreated (6 events)
y_t_n, y_t_e, y_c_n, y_c_e = 10, 4, 30, 6
o_t_n, o_t_e, o_c_n, o_c_e = 30, 24, 10, 6
N = y_t_n + y_c_n + o_t_n + o_c_n
assert N == 80

e_young = F(y_t_n, y_t_n + y_c_n)
e_old = F(o_t_n, o_t_n + o_c_n)
assert e_young == F(1, 4) and e_old == F(3, 4)

r_y_t, r_y_c = F(y_t_e, y_t_n), F(y_c_e, y_c_n)
r_o_t, r_o_c = F(o_t_e, o_t_n), F(o_c_e, o_c_n)
assert (r_y_t, r_y_c) == (F(2, 5), F(1, 5))
assert (r_o_t, r_o_c) == (F(4, 5), F(3, 5))
assert r_y_t - r_y_c == F(1, 5) and r_o_t - r_o_c == F(1, 5)

t_n, t_e = y_t_n + o_t_n, y_t_e + o_t_e
c_n, c_e = y_c_n + o_c_n, y_c_e + o_c_e
assert (t_n, t_e, c_n, c_e) == (40, 28, 40, 12)
crude = F(t_e, t_n) - F(c_e, c_n)
assert F(t_e, t_n) == F(7, 10) and F(c_e, c_n) == F(3, 10) and crude == F(2, 5)

# Composition / standardised difference for age
p_t_old, p_c_old = F(o_t_n, t_n), F(o_c_n, c_n)
assert (p_t_old, p_c_old) == (F(3, 4), F(1, 4)) and p_t_old - p_c_old == F(1, 2)
pooled_var = (p_t_old * (1 - p_t_old) + p_c_old * (1 - p_c_old)) / 2
assert pooled_var == F(3, 16)
sd = float(p_t_old - p_c_old) / math.sqrt(float(pooled_var))
assert abs(sd - 2 / math.sqrt(3)) < 1e-12 and abs(sd - 1.155) < 5e-4

# Stratified (standardised) ATE, population weights 1/2 each
w_y = F(y_t_n + y_c_n, N); w_o = F(o_t_n + o_c_n, N)
assert w_y == w_o == F(1, 2)
ate_strat = w_y * (r_y_t - r_y_c) + w_o * (r_o_t - r_o_c)
assert ate_strat == F(1, 5)
assert crude - ate_strat == F(1, 5) and crude == 2 * ate_strat

# IPW ATE
ey1 = (F(y_t_e) / e_young + F(o_t_e) / e_old) / N
ey0 = (F(y_c_e) / (1 - e_young) + F(o_c_e) / (1 - e_old)) / N
assert ey1 == F(48, 80) == F(3, 5) and ey0 == F(32, 80) == F(2, 5)
assert ey1 - ey0 == F(1, 5)
# intermediate sums stated in the article: 16+32 and 8+24
assert F(y_t_e) / e_young == 16 and F(o_t_e) / e_old == 32
assert F(y_c_e) / (1 - e_young) == 8 and F(o_c_e) / (1 - e_old) == 24

# ATT: treated weight 1; control weights e/(1-e) = 1/3 (young), 3 (old)
w_y_c, w_o_c = e_young / (1 - e_young), e_old / (1 - e_old)
assert (w_y_c, w_o_c) == (F(1, 3), F(3))
att_c_events = y_c_e * w_y_c + o_c_e * w_o_c
att_c_total = y_c_n * w_y_c + o_c_n * w_o_c
assert att_c_events == 20 and att_c_total == 40
assert att_c_events / att_c_total == F(1, 2)
att = F(t_e, t_n) - att_c_events / att_c_total
assert att == F(1, 5)

# Check-yourself Q2 uses the same ATT numbers (1/2 and 7/10 - 1/2 = 1/5) -- asserted above.
# Check-yourself Q3's 0.35 / 0.1 are stated thresholds, not computed quantities.

print("Worked example: e=(1/4, 3/4), crude=2/5, stratum effects=1/5,1/5, "
      f"standardised ATE={ate_strat}, IPW=({ey1}-{ey0})={ey1-ey0}, ATT={att}, "
      f"standardised difference={sd:.3f} (=2/sqrt(3))")

# ---------- Your turn ----------
# Low-risk (X=0): 60 patients, 20 treated (10 events), 40 untreated (10 events)
# High-risk (X=1): 60 patients, 40 treated (30 events), 20 untreated (10 events)
l_t_n, l_t_e, l_c_n, l_c_e = 20, 10, 40, 10
h_t_n, h_t_e, h_c_n, h_c_e = 40, 30, 20, 10
N2 = l_t_n + l_c_n + h_t_n + h_c_n
assert N2 == 120
e_low = F(l_t_n, l_t_n + l_c_n); e_high = F(h_t_n, h_t_n + h_c_n)
assert (e_low, e_high) == (F(1, 3), F(2, 3))

t2_n, t2_e = l_t_n + h_t_n, l_t_e + h_t_e
c2_n, c2_e = l_c_n + h_c_n, l_c_e + h_c_e
assert (t2_n, t2_e, c2_n, c2_e) == (60, 40, 60, 20)
crude2 = F(t2_e, t2_n) - F(c2_e, c2_n)
assert F(t2_e, t2_n) == F(2, 3) and F(c2_e, c2_n) == F(1, 3) and crude2 == F(1, 3)

d_low = F(l_t_e, l_t_n) - F(l_c_e, l_c_n)
d_high = F(h_t_e, h_t_n) - F(h_c_e, h_c_n)
assert d_low == F(1, 2) - F(1, 4) == F(1, 4)
assert d_high == F(3, 4) - F(1, 2) == F(1, 4)
ate2 = F(1, 2) * d_low + F(1, 2) * d_high
assert ate2 == F(1, 4)

ey1_2 = (F(l_t_e) / e_low + F(h_t_e) / e_high) / N2
ey0_2 = (F(l_c_e) / (1 - e_low) + F(h_c_e) / (1 - e_high)) / N2
assert F(l_t_e) / e_low == 30 and F(h_t_e) / e_high == 45
assert F(l_c_e) / (1 - e_low) == 15 and F(h_c_e) / (1 - e_high) == 30
assert ey1_2 == F(75, 120) == F(5, 8) and ey0_2 == F(45, 120) == F(3, 8)
assert ey1_2 - ey0_2 == F(1, 4)

w_l_c, w_h_c = e_low / (1 - e_low), e_high / (1 - e_high)
assert (w_l_c, w_h_c) == (F(1, 2), F(2))
att2_c = (l_c_e * w_l_c + h_c_e * w_h_c) / (l_c_n * w_l_c + h_c_n * w_h_c)
assert l_c_e * w_l_c + h_c_e * w_h_c == 25
assert l_c_n * w_l_c + h_c_n * w_h_c == 60
assert att2_c == F(25, 60) == F(5, 12)
att2 = F(t2_e, t2_n) - att2_c
assert att2 == F(2, 3) - F(5, 12) == F(1, 4)

print(f"Your turn: e=(1/3, 2/3), crude={crude2}, stratum effects=1/4,1/4, "
      f"standardised ATE={ate2}, IPW=({ey1_2}-{ey0_2})={ey1_2-ey0_2}, ATT={att2}")
print("PASS: all worked-example and Your-turn numbers verified exactly (fractions).")

# ---------- Review-fix additions (2026-11-23) ----------
# Identification bounds for the worked example's observed table:
# treated events 28/40, untreated events 12/40; 40 potential outcomes are
# missing under each arm. Extreme fillings bound the finite-population ATE.
obs_y1, obs_y0 = 28, 12
ate_min = F(obs_y1 + 0 - (obs_y0 + 40), 80)
ate_max = F(obs_y1 + 40 - (obs_y0 + 0), 80)
assert ate_min == F(-3, 10) and float(ate_min) == -0.30
assert ate_max == F(7, 10) and float(ate_max) == 0.70
print(f"Review-fix: observed table allows finite-population ATE in [{ate_min}, {ate_max}] = [-0.30, 0.70]; standardised contrast 1/5 is the ATE only under conditional exchangeability given age.")
print("PASS: review-fix numbers verified.")
