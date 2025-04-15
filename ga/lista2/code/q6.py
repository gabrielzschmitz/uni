import numpy as np
import matplotlib.pyplot as plt

# Definição dos vértices do triângulo
A = np.array([0, 0])
B = np.array([6, 0])
C = np.array([3, 5])

# Cálculo dos pontos médios
M = (A + C) / 2
N = (B + C) / 2

# Criar a figura
fig, ax = plt.subplots(figsize=(5,5))

# Plotar o triângulo
triangle = np.array([A, B, C, A])
ax.plot(triangle[:, 0], triangle[:, 1], 'k-', label='Triângulo ABC')

# Plotar o segmento médio
ax.plot([M[0], N[0]], [M[1], N[1]], 'k-', linewidth=2)  # Segmento MN

# Marcar pontos médios
ax.scatter(*M, color='black', s=50)
ax.scatter(*N, color='black', s=50)

# Adicionar rótulos aos pontos
ax.text(A[0]-0.3, A[1]-0.2, 'A', fontsize=12, ha='center')
ax.text(B[0]+0.3, B[1]-0.2, 'B', fontsize=12, ha='center')
ax.text(C[0], C[1]+0.3, 'C', fontsize=12, ha='center')
ax.text(M[0]-0.3, M[1], 'M', fontsize=12, ha='center')
ax.text(N[0]+0.3, N[1], 'N', fontsize=12, ha='center')

# Ajustes visuais
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 6)

plt.show()
