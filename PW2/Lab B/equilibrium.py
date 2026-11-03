"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
    # Clip x to stay within valid bounds (0 to 1) avoiding division by zero
    x_safe = np.clip(x, 0.0, 0.999)
    return (2 * x_safe)**2 / ((a - x_safe) * (b - x_safe)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
res_slsqp = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium extent x (Newton): {x_newton:.4f}")
print(f"Equilibrium extent x (SLSQP):  {x_slsqp:.4f}")

# Report the equilibrium amounts
h2_eq = a - x_newton
i2_eq = b - x_newton
hi_eq = 2 * x_newton
print(f"\nEquilibrium Amounts:")
print(f"  [H2] = {h2_eq:.3f} mol")
print(f"  [I2] = {i2_eq:.3f} mol")
print(f"  [HI] = {hi_eq:.3f} mol")

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
x_vals = np.linspace(0, 0.95, 100)
h2_vals = a - x_vals
i2_vals = b - x_vals
hi_vals = 2 * x_vals

plt.figure(figsize=(8, 5))
plt.plot(x_vals, h2_vals, label='$H_2$', color='blue', lw=2)
plt.plot(x_vals, i2_vals, label='$I_2$', color='green', lw=2)
plt.plot(x_vals, hi_vals, label='$HI$', color='orange', lw=2)
plt.axvline(x_newton, color='red', linestyle='--', label=f'Equilibrium ($x \\approx {x_newton:.2f}$)')

plt.xlabel('Reaction Extent ($x$)')
plt.ylabel('Amount (mol)')
plt.title('Chemical Equilibrium Composition')
plt.legend()
plt.grid(True)

plt.savefig('equilibrium.png', dpi=300)
print("Plot saved to equilibrium.png")
plt.show()