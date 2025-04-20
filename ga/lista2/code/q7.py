import matplotlib.pyplot as plt

# Ponto final (extremidade) do vetor
B = (3, 1)

# Vetor dado
v = (-1, 3)

# Calcula o ponto inicial A tal que B = A + v ⇒ A = B - v
A = (B[0] - v[0], B[1] - v[1])  # (4, -2)

# Plot
fig, ax = plt.subplots()

ax.quiver(*A, *v, angles='xy', scale_units='xy', scale=1, color='blue', label='v')
ax.scatter(*A, color='black')
ax.scatter(*B, color='red')
ax.text(*A, 'A', fontsize=12, ha='right')
ax.text(*B, 'B', fontsize=12, ha='left')
ax.set_title(r"$\vec{v} = (-1, 3)$")
ax.set_xlim(0, 6)
ax.set_ylim(-3, 5)
ax.grid(True)
ax.set_aspect('equal')

plt.show()
