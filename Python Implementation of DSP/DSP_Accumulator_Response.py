# Blaine Swieder
# ECE 5020: Digital Signal Processing
# Date: 2/1/2026
# File Name: DSP_Accumulator_Response.py
# Purpose: To determine the accumulator response (in closed-form expression)




# -----------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 21)

u = (n >= 0).astype(int)      # unit step
x = n * u                     # x(n) = n u(n)
y = np.cumsum(x)              # accumulator

# print a few rows
for ni, xi, yi in zip(n, x, y):
    print(f"n={ni:3d}  x={xi:3d}  y={yi:3d}")

# plots
plt.figure()
plt.stem(n, x, basefmt=" ")
plt.grid(True)
plt.title("x(n) = n u(n)")
plt.xlabel("n"); plt.ylabel("x(n)")

plt.figure()
plt.stem(n, y, basefmt=" ")
plt.grid(True)
plt.title("Accumulator output y(n)")
plt.xlabel("n"); plt.ylabel("y(n)")
plt.show()


# ------------------------------------------------------


y_init = 1
yB = np.cumsum(x) + y_init * (n >= -1).astype(int)
