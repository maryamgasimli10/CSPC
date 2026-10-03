#part 2
import numpy as np

data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]  
y = data[:, 1] 

v = np.gradient(y, t)  
a = np.gradient(v, t)  

mean_a = np.mean(a)
print(f"Mean acceleration: {mean_a:.2f} m/s^2")

#part 3
std_a = a.std()
print(f"Acceleration standard deviation: {std_a:.2f} m/s^2")

#part 4
from scipy.integrate import cumulative_trapezoid

v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
max_diff = np.max(np.abs(y - y_rec))
print(f"Max difference between original and recovered position: {max_diff:.4f} m")

#part5 
import matplotlib.pyplot as plt

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, color='blue', label='Position y(t)')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion from Tracking Data')
ax1.grid(True)
ax1.legend()

ax2.plot(t, v, color='orange', label='Velocity v(t)')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

ax3.plot(t, a, color='red', label='Acceleration a(t)')
ax3.axhline(-9.81, color='black', linestyle='--', label='g = -9.81 m/s²')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png')
print("Plot successfully saved as motion.png")