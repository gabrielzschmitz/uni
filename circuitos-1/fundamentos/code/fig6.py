import numpy as np
import matplotlib.pyplot as plt

# Define time vector
t = np.linspace(0, 5, 1000, endpoint=True)

# Initialize i and q
i = np.zeros_like(t)
q = np.zeros_like(t)

# Define piecewise functions
mask = (t >= 0) & (t < 1)
i[mask] = 10
q[mask] = 10 * t[mask]

mask = (t >= 1) & (t < 2)
i[mask] = -5 * t[mask] + 15
q[mask] = -2.5 * t[mask] ** 2 + 15 * t[mask] - 2.5

mask = (t >= 2) & (t < 4)
i[mask] = 5
q[mask] = 5 * t[mask] + 7.5

mask = (t >= 4) & (t <= 5)
i[mask] = -5 * t[mask] + 25
q[mask] = -2.5 * t[mask] ** 2 + 25 * t[mask] - 32.5

# Create the plot
fig, ax1 = plt.subplots()

# Set title
ax1.set_title("Gráfico das Funções i(t) e q(t)", fontsize=16)

# Plot i(t) on the left y-axis
ax1.plot(t, i, "b", linewidth=2, label="i(t)")
ax1.set_xlabel("t (s)", fontsize=16)
ax1.set_ylabel("i(t) (A)", color="b", fontsize=16)
ax1.set_xlim([0, 5])
ax1.set_ylim([0, 12])
ax1.tick_params(axis="y", labelcolor="b", labelsize=14)
ax1.tick_params(axis="x", labelsize=14)

# Create a secondary y-axis for q(t)
ax2 = ax1.twinx()
ax2.plot(t, q, "r", linewidth=2, label="q(t)")
ax2.set_ylabel("q(t) (C)", color="r", fontsize=16)
ax2.set_ylim([0, 32])
ax2.tick_params(axis="y", labelcolor="r", labelsize=14)

# Add legend with colors
ax1.legend(loc="upper left", fontsize=14, facecolor="white", edgecolor="b")
ax2.legend(loc="upper right", fontsize=14, facecolor="white", edgecolor="r")

# Add grid and show the plot
ax1.grid(True)
plt.show()
