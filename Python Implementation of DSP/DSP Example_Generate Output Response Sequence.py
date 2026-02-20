import numpy as np
import matplotlib.pyplot as plt

# Define n range
n = np.arange(-6, 7)

# Define input signal x[n]
x = np.zeros_like(n, dtype=float)

# x[n] = |n| for -3 <= n <= 3
for i, k in enumerate(n):
    if -3 <= k <= 3:
        x[i] = abs(k)

# -----------------------------
# 1) Moving Average Filter
# y[n] = (1/3)(x[n+1] + x[n] + x[n-1])
# -----------------------------
y1 = np.zeros_like(x)

for i in range(1, len(x)-1):
    y1[i] = (x[i+1] + x[i] + x[i-1]) / 3


# -----------------------------
# 2) Median Filter
# y[n] = median(x[n+1], x[n], x[n-1])
# -----------------------------
y2 = np.zeros_like(x)

for i in range(1, len(x)-1):
    y2[i] = np.median([x[i+1], x[i], x[i-1]])


# -----------------------------
# 3) Accumulator
# y[n] = sum from -inf to n of x[k]
# -----------------------------
y3 = np.cumsum(x)


# -----------------------------
# Plot x[n]
# -----------------------------
plt.figure()
plt.stem(n, x)
plt.title("Input Signal x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()


# -----------------------------
# Plot y1[n]
# -----------------------------
plt.figure()
plt.stem(n, y1)
plt.title("Moving Average Output y_1[n]")
plt.xlabel("n")
plt.ylabel("y1[n]")
plt.grid(True)
plt.show()


# -----------------------------
# Plot y2[n]
# -----------------------------
plt.figure()
plt.stem(n, y2)
plt.title("Median Filter Output y_2[n]")
plt.xlabel("n")
plt.ylabel("y2[n]")
plt.grid(True)
plt.show()


# -----------------------------
# Plot y3[n]
# -----------------------------
plt.figure()
plt.stem(n, y3)
plt.title("Accumulator Output y3[n]")
plt.xlabel("n")
plt.ylabel("y3[n]")
plt.grid(True)
plt.show()
