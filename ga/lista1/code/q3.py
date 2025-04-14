import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(u, v):
    origin = np.array([0, 0])  # Ponto de origem
    vectors = {
        "u": u,
        "v": v,
        "u + v": u + v,
        "u - v": u - v,
        "v - u": v - u,
        "-u - v": -u - v,
        "-u": -u,
        "-v": -v
    }
    
    fig, ax = plt.subplots()
    ax.set_xlim(-max(abs(u[0]), abs(v[0])) - 2, max(abs(u[0]), abs(v[0])) + 2)
    ax.set_ylim(-max(abs(u[1]), abs(v[1])) - 2, max(abs(u[1]), abs(v[1])) + 2)
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.grid(True, linestyle='--', linewidth=0.5)
    
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'purple']
    
    for i, (label, vec) in enumerate(vectors.items()):
        ax.quiver(*origin, *vec, angles='xy', scale_units='xy', scale=1, color=colors[i], label=label)
        ax.text(vec[0], vec[1], label, fontsize=12, verticalalignment='bottom')
    
    # Desenhar o paralelogramo
    parallelogram = np.array([origin, u, u + v, v, origin])
    ax.plot(parallelogram[:, 0], parallelogram[:, 1], 'k--')
    
    plt.legend()
    plt.show()

# Exemplo de vetores
u = np.array([3, 1])
v = np.array([1, 2])
plot_vectors(u, v)
