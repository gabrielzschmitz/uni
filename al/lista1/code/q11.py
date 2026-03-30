import matplotlib.pyplot as plt
import numpy as np

# Função para desenhar vetores com origem em (0,0)
def draw_vector(ax, origin, vec, color='black', label=None):
    ax.quiver(*origin, *vec, angles='xy', scale_units='xy', scale=1, color=color)
    if label:
        ax.text(*(origin + vec + 0.1), label, fontsize=12)

# Configurações dos vetores u e v para cada caso com base na imagem
cases = {
    'a': {'u': np.array([1, 1.5]), 'v': np.array([-1, 1.5])},
    'b': {'u': np.array([1.5, 0]), 'v': np.array([1, 1.5])},
    'c': {'u': np.array([1, 1]), 'v': np.array([2, 0])},
    'd': {'u': np.array([1, -1]), 'v': np.array([1, 1.5])},
}

# Plotagem dos vetores u, v e u-v para cada caso
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs = axs.flatten()

for i, (label, vectors) in enumerate(cases.items()):
    u = vectors['u']
    v = vectors['v']
    u_minus_v = u - v

    ax = axs[i]
    ax.set_title(f'Caso ({label})')

    # Vetores u e v a partir da origem
    draw_vector(ax, np.array([0, 0]), u, 'blue', r'$\vec{u}$')
    draw_vector(ax, np.array([0, 0]), v, 'green', r'$\vec{v}$')
    draw_vector(ax, np.array([0, 0]), u_minus_v, 'red', r'$\vec{u} - \vec{v}$')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True)

plt.tight_layout()
plt.show()
