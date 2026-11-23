"""Recompute every number in the potential-outcomes worked example and Your turn.

Science table (binary outcome, 1 = event):
    unit:   1 2 3 4 5 6
    Y^0:    1 0 0 0 1 0
    Y^1:    1 1 1 0 1 0
Confounded assignment in the worked example: A = 1 for units 1, 2, 5.
Your-turn assignment: A = 1 for units 3, 4 only.
Exit 0 only if every assertion passes.
"""
from fractions import Fraction as F

Y0 = [F(1), F(0), F(0), F(0), F(1), F(0)]
Y1 = [F(1), F(1), F(1), F(0), F(1), F(0)]
n = 6
assert len(Y0) == len(Y1) == n

def mean(xs):
    return sum(xs) / len(xs)

# Column means and ATE
assert sum(Y1) == 4 and mean(Y1) == F(2, 3), mean(Y1)
assert sum(Y0) == 2 and mean(Y0) == F(1, 3), mean(Y0)
ate = mean(Y1) - mean(Y0)
assert ate == F(1, 3), ate

# Individual effects and their mean; sharp and average nulls both fail
diffs = [a - b for a, b in zip(Y1, Y0)]
assert diffs == [F(0), F(1), F(1), F(0), F(0), F(0)], diffs
assert mean(diffs) == ate == F(1, 3)
assert not all(d == 0 for d in diffs)          # sharp null false (units 2, 3)
assert mean(Y1) != mean(Y0)                    # average null false

# Worked example: confounded assignment, treated = units 1, 2, 5 (indices 0, 1, 4)
A = [1, 1, 0, 0, 1, 0]
obs = [Y1[i] if A[i] == 1 else Y0[i] for i in range(n)]  # consistency: Y = Y^A
assert obs == [F(1), F(1), F(0), F(0), F(1), F(0)], obs
treated_obs = [obs[i] for i in range(n) if A[i] == 1]
untreated_obs = [obs[i] for i in range(n) if A[i] == 0]
assert mean(treated_obs) == F(1) and mean(untreated_obs) == F(0)
naive = mean(treated_obs) - mean(untreated_obs)
assert naive == F(1), naive
bias = naive - ate
assert bias == F(2, 3), bias

# Exchangeability failure, shown on Y^0
assert mean([Y0[i] for i in range(n) if A[i] == 1]) == F(2, 3)
assert mean([Y0[i] for i in range(n) if A[i] == 0]) == F(0)
assert mean(Y0) == F(1, 3)
# and on Y^1
assert mean([Y1[i] for i in range(n) if A[i] == 1]) == F(1)
assert mean([Y1[i] for i in range(n) if A[i] == 0]) == F(1, 3)

# Your turn: treated = units 3, 4 only (indices 2, 3)
A2 = [0, 0, 1, 1, 0, 0]
obs2 = [Y1[i] if A2[i] == 1 else Y0[i] for i in range(n)]
assert obs2 == [F(1), F(0), F(1), F(0), F(1), F(0)], obs2
t2 = mean([obs2[i] for i in range(n) if A2[i] == 1])
u2 = mean([obs2[i] for i in range(n) if A2[i] == 0])
assert t2 == F(1, 2) and u2 == F(1, 2), (t2, u2)
naive2 = t2 - u2
assert naive2 == F(0), naive2
assert naive2 - ate == F(-1, 3)

print("PASS")
print(f"  E[Y^1] = {mean(Y1)}, E[Y^0] = {mean(Y0)}, true ATE = {ate}")
print(f"  individual effects = {[str(d) for d in diffs]}")
print(f"  worked example: naive contrast = {naive}, bias = {bias}")
print(f"  your turn: naive contrast = {naive2}, bias = {naive2 - ate}")
