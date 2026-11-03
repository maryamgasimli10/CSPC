"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  uv run warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

print("=== Part 2A: Easy Convex Function ===")
x0 = 0.0

# (1) Gradient descent by hand
x_gd = x0
lr = 0.1
step = 1.0
while abs(step) > 1e-6:
    gradient = df(x_gd)
    x_gd -= lr * gradient
    step = lr * gradient
print(f"(1) Gradient Descent: x ≈ {x_gd:.5f}")

# (2) Newton's method on df(x)=0 with fprime=d2f
res_newton_a = newton(df, x0, fprime=d2f)
print(f"(2) Newton's Method:  x ≈ {res_newton_a:.5f}")

# (3) SLSQP minimize
res_slsqp_a = minimize(f, x0, method="SLSQP")
print(f"(3) SLSQP Minimize:   x ≈ {res_slsqp_a.x[0]:.5f}\n")


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

print("=== Part 2B: Harder Landscape ===")
for start_x in [0.0, 2.0]:
    print(f"\n--- Starting from x0 = {start_x} ---")
    
    # (1) Gradient descent by hand
    x_gd = start_x
    lr = 0.01
    step = 1.0
    for _ in range(10000):
        if abs(step) <= 1e-7:
            break
        gradient = dg(x_gd)
        x_gd -= lr * gradient
        step = lr * gradient
    print(f"(1) Gradient Descent: x ≈ {x_gd:.5f}, g(x) = {g(x_gd):.5f}")
    
    # (2) Newton's method on dg(x)=0
    try:
        res_newton_b = newton(dg, start_x, fprime=d2g)
        curvature = d2g(res_newton_b)
        st_type = "minimum" if curvature > 0 else ("maximum" if curvature < 0 else "inflection")
        print(f"(2) Newton's Method:  x ≈ {res_newton_b:.5f} (d2g = {curvature:.2f} -> {st_type})")
    except Exception as e:
        print(f"(2) Newton's Method:  Failed ({e})")
        
    # (3) SLSQP minimize
    res_slsqp_b = minimize(g, start_x, method="SLSQP")
    print(f"(3) SLSQP Minimize:   x ≈ {res_slsqp_b.x[0]:.5f}, g(x) = {res_slsqp_b.fun:.5f}")