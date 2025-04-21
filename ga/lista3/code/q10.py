import matplotlib.pyplot as plt
import numpy as np

# Coordenadas dos pontos
A = np.array([0, 0])
B = np.array([20, 0])

# Ângulo de 60 graus para o triângulo equilátero
angle_deg = 60
angle_rad = np.radians(angle_deg)

# Coordenadas de C usando trigonometria
C = np.array([20 * np.cos(angle_rad), 20 * np.sin(angle_rad)])

# Vetores AB e AC
AB = B - A
AC = C - A

# Plot
fig, ax = plt.subplots()
ax.quiver(*A, *AB, angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\vec{AB}$')
ax.quiver(*A, *AC, angles='xy', scale_units='xy', scale=1, color='green', label=r'$\vec{AC}$')

# Pontos
ax.plot(*A, 'ko')
ax.text(*A, '  A', verticalalignment='bottom', fontsize=12)
ax.plot(*B, 'ko')
ax.text(*B, '  B', verticalalignment='bottom', fontsize=12)
ax.plot(*C, 'ko')
ax.text(*C, '  C', verticalalignment='bottom', fontsize=12)

# Ajustes
ax.set_xlim(-5, 25)
ax.set_ylim(-5, 20)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
