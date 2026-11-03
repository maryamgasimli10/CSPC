"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V = data[:, 0]
ph = data[:, 1]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(ph, V)
max_idx = np.argmax(slope)
equivalence_volume = V[max_idx]
print(f"Equivalence point volume: {equivalence_volume} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: pH curve
ax1.plot(V, ph, color='purple', lw=2)
ax1.axvline(equivalence_volume, color='red', linestyle='--', label=f'Equivalence Point: {equivalence_volume} mL')
ax1.set_xlabel('Base Volume (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.legend()
ax1.grid(True)

# Right plot: Slope (derivative) curve
ax2.plot(V, slope, color='teal', lw=2)
ax2.axvline(equivalence_volume, color='red', linestyle='--', label=f'Max Slope Peak: {equivalence_volume} mL')
ax2.set_xlabel('Base Volume (mL)')
ax2.set_ylabel('Slope ($dpH / dV$)')
ax2.set_title('Titration First Derivative (Slope)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png', dpi=300)
print("Plot saved to titration.png")
plt.show()