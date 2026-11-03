"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def total_error(k):
    # k is passed by minimize as an array [k_val]
    k_val = k[0]
    C_model = C0 * np.exp(-k_val * t)
    return np.sum((C - C_model)**2)

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
result = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fitted = result.x[0]
print(f"Fitted rate constant k = {k_fitted:.4f}")

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
t_smooth = np.linspace(t.min(), t.max(), 200)
C_smooth = C0 * np.exp(-k_fitted * t_smooth)

plt.figure(figsize=(8, 5))
plt.scatter(t, C, color='red', label='Measured Data', zorder=5)
plt.plot(t_smooth, C_smooth, color='blue', label=f'Fitted Curve ($k = {k_fitted:.4f}$)', lw=2)

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('First-Order Reaction Kinetics Fit')
plt.legend()
plt.grid(True)

plt.savefig('kinetics.png', dpi=300)
print("Plot saved to kinetics.png")
plt.show()
