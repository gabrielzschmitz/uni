import matplotlib.pyplot as plt

# Coordinates
A = (2, -3)
P1 = (6, 0)
P2 = (-2, 0)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(*A, 'ro', label='A(2, -3)')
plt.plot(*P1, 'bo', label='P₁(6, 0)')
plt.plot(*P2, 'go', label='P₂(-2, 0)')

# Add lines from A to each P
plt.plot([A[0], P1[0]], [A[1], P1[1]], 'b--', alpha=0.5)
plt.plot([A[0], P2[0]], [A[1], P2[1]], 'g--', alpha=0.5)

# Labels and grid
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.xlim(-4, 8)
plt.ylim(-5, 2)
plt.gca().set_aspect('equal')

plt.tight_layout()
plt.show()
