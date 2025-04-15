import numpy as np
import matplotlib.pyplot as plt

# Coordenadas aproximadas dos pontos
A = np.array([0, 0])
B = np.array([2, 2])
C = np.array([2, 0])

# Vetores
AB = B - A
BA = A - B
BC = C - B
CA = A - C
CB = B - C

# Cálculo dos vetores para cada item
x_a = BA + 2 * BC
x_b = 2 * CA + 2 * BA
x_c = 3 * AB - 2 * BC
x_d = 0.5 * AB - 2 * CB

# Função auxiliar para desenhar vetores
def draw_vector(ax, origin, vector, color, label):
    ax.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Plot
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()
titles = ['(a) x = BA + 2BC', '(b) x = 2CA + 2BA', '(c) x = 3AB - 2BC', '(d) x = 1/2 AB - 2CB']
vectors = [x_a, x_b, x_c, x_d]

for i, ax in enumerate(axs):
    ax.set_title(titles[i])
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True)
    
    # Plot points
    ax.plot(*A, 'ko')
    ax.text(*A, 'A', fontsize=12, ha='right')
    ax.plot(*B, 'ko')
    ax.text(*B, 'B', fontsize=12, ha='right')
    ax.plot(*C, 'ko')
    ax.text(*C, 'C', fontsize=12, ha='right')

    # Plot vector x
    draw_vector(ax, A, vectors[i], 'blue', f'x_{chr(97+i)}')

plt.tight_layout()
plt.show()
