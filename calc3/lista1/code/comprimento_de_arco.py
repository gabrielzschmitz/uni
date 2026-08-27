import numpy as np
import matplotlib.pyplot as plt

# Curva completa: duas voltas antes de 0 e duas depois de 2π
t_full = np.linspace(-2 * np.pi, 4 * np.pi, 2000)

x_full = np.cos(t_full)
y_full = np.sin(t_full)
z_full = t_full

# Trecho cujo comprimento de arco queremos destacar
t_highlight = np.linspace(0, 2 * np.pi, 1000)

x_highlight = np.cos(t_highlight)
y_highlight = np.sin(t_highlight)
z_highlight = t_highlight

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Hélice completa
ax.plot(
    x_full,
    y_full,
    z_full,
    linewidth=2,
    label=r"$\mathbf{r}(t)=\langle\cos t,\sin t,t\rangle$"
)

# Intervalo de 0 a 2π destacado
ax.plot(
    x_highlight,
    y_highlight,
    z_highlight,
    linewidth=5,
    label=r"$0\leq t\leq2\pi$ → $L=2\pi\sqrt{2}$"
)

# Pontos t = 0 e t = 2π
ax.scatter(
    [1, 1],
    [0, 0],
    [0, 2 * np.pi],
    s=70
)

ax.text(1, 0, 0, r"  $t=0$", fontsize=11)
ax.text(1, 0, 2 * np.pi, r"  $t=2\pi$", fontsize=11)

# Eixos
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")

ax.set_title(
    r""
)

# Limites
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-2 * np.pi - 0.5, 4 * np.pi + 0.5)

# Deixa o gráfico menos alto visualmente
ax.set_box_aspect((1, 1, 3))

ax.legend(loc="upper left")

plt.tight_layout()

plt.savefig(
    "comprimento_de_arco.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
