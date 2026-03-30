import numpy as np
import matplotlib.pyplot as plt

def plot_parallelogram():
    # Definição dos pontos do paralelogramo
    A = np.array([0, 0])
    B = np.array([4, 1])
    C = np.array([6, 4])
    D = np.array([2, 3])
    
    # Cálculo dos pontos médios das diagonais
    mid_AC = (A + C) / 2
    mid_BD = (B + D) / 2
    
    # Verificação
    assert np.allclose(mid_AC, mid_BD), "Os pontos médios não coincidem!"
    
    # Criar figura
    fig, ax = plt.subplots()
    
    # Desenhar o paralelogramo
    parallelogram = np.array([A, B, C, D, A])
    ax.plot(parallelogram[:, 0], parallelogram[:, 1], 'k-', label='Paralelogramo')
    
    # Desenhar diagonais
    ax.plot([A[0], C[0]], [A[1], C[1]], 'r--', label='Diagonal AC')
    ax.plot([B[0], D[0]], [B[1], D[1]], 'b--', label='Diagonal BD')
    
    # Marcar pontos médios
    ax.scatter(*mid_AC, color='g', label='Ponto médio')
    
    # Marcar vértices
    ax.scatter(*A, color='black')
    ax.scatter(*B, color='black')
    ax.scatter(*C, color='black')
    ax.scatter(*D, color='black')
    
    # Adicionar rótulos
    ax.text(A[0], A[1], ' A', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    ax.text(B[0], B[1], ' B', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
    ax.text(C[0], C[1], ' C', fontsize=12, verticalalignment='top', horizontalalignment='left')
    ax.text(D[0], D[1], ' D', fontsize=12, verticalalignment='top', horizontalalignment='right')
    ax.text(mid_AC[0], mid_AC[1], ' M', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='g')

    # Configurações do gráfico
    ax.legend()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Diagonais de um Paralelogramo")
    ax.grid(True, linestyle='--', linewidth=0.5)
    
    plt.show()

plot_parallelogram()
