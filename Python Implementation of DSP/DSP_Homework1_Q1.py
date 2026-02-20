# Blaine Swieder
# Date: 2/1/2026
# Filename: DSP_Homework1_Q1.py

# ------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def fmt_val(v):
    if abs(v - 0.5) < 1e-12: return "1/2"
    if abs(v - 1.0) < 1e-12: return "1"
    return f"{v:g}"

def plot_seq(seq, title, nmin=-4, nmax=8):
    n = np.arange(nmin, nmax + 1)
    y = np.zeros_like(n, dtype=float)
    for i, ni in enumerate(n):
        if ni in seq:
            y[i] = seq[ni]

    plt.figure()
    plt.stem(n, y)
    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("amplitude")
    plt.grid(True)
    plt.xticks(np.arange(nmin, nmax + 1, 1))

    for k, v in sorted(seq.items()):
        if abs(v) > 1e-12:
            plt.text(k, v + 0.07, fmt_val(v), ha="center")

    plt.ylim(-0.2, 1.35)

x  = {-1:1, 0:1, 1:1, 2:1, 3:0.5, 4:0.5}
ya = {1:1, 2:1, 3:1, 4:1, 5:0.5, 6:0.5}
yb = {0:0.5, 1:0.5, 2:1, 3:1, 4:1, 5:1}
yc = {-1:1, 0:1, 1:1, 2:1}
yd = {3:1}
ye = {-2:0.5, -1:1, 0:1, 1:1, 2:0.5}

plot_seq(x,  "Original x(n)")
plot_seq(ya, "a) y(n) = x(n-2)")
plot_seq(yb, "b) y(n) = x(4-n)")
plot_seq(yc, "c) y(n) = x(n) u(2-n)")
plot_seq(yd, "d) y(n) = x(n-1) δ(n-3)")
plot_seq(ye, "e) y(n) = x(n^2)")

plt.show()
