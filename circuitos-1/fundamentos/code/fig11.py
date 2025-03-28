import numpy as np
import matplotlib.pyplot as plt

# Define time intervals
t1 = np.linspace(0, 2, 100)
t2 = np.linspace(2, 4, 100)

# Define power functions
p1 = 150 * t1  # 0 < t < 2
p2 = -600 + 150 * t2  # 2 ≤ t ≤ 4

# Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(t1, p1, label="$p(t) = 150t$", color="blue", linewidth=2)
plt.plot(t2, p2, label="$p(t) = -600 + 150t$", color="red", linewidth=2)

# Add grid and labels
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.axvline(2, color="black", linestyle="--", linewidth=1)
plt.text(0.5, 200, "Absorvendo energia", fontsize=14, color="blue")
plt.text(2.5, -100, "Fornecendo energia", fontsize=14, color="red")
plt.xlabel("t (s)", fontsize=16)
plt.ylabel("ρ(t) (mW)", fontsize=16)
plt.title("Potência liberada para o dispositivo para t > 0", fontsize=18)
plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)

# Show plot
plt.show()
