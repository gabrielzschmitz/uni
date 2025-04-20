import matplotlib.pyplot as plt

# Pontos
P = (2, 3)
Q = (4, 2)
R = (3, 5)

# Vetores
u = (Q[0] - P[0], Q[1] - P[1])  # (2, -1)
v = (R[0] - Q[0], R[1] - Q[1])  # (-1, 3)
w = (P[0] - R[0], P[1] - R[1])  # (-1, -2)

# Plot
fig, ax = plt.subplots()

# Vetores a partir de seus pontos de origem
ax.quiver(*P, *u, angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\vec{u}$')
ax.quiver(*Q, *v, angles='xy', scale_units='xy', scale=1, color='green', label=r'$\vec{v}$')
ax.quiver(*R, *w, angles='xy', scale_units='xy', scale=1, color='orange', label=r'$\vec{w}$')

# Pontos
ax.scatter(*P, color='black')
ax.scatter(*Q, color='red')
ax.scatter(*R, color='purple')
ax.text(*P, 'P', fontsize=12, ha='right')
ax.text(*Q, 'Q', fontsize=12, ha='left')
ax.text(*R, 'R', fontsize=12, ha='left')

# Ajustes do gráfico
ax.set_title("Vetores posição: $\\vec{u}$, $\\vec{v}$ e $\\vec{w}$")
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.grid(True)
ax.set_aspect('equal')
ax.legend()

plt.show()
