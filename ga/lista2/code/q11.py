import matplotlib.pyplot as plt

# Define points
A = (-3, 2)
B = (5, -2)

# Vector AB
AB = (B[0] - A[0], B[1] - A[1])

# Points M, N, and P
M = (A[0] + 0.5 * AB[0], A[1] + 0.5 * AB[1])
print(M)
N = (A[0] + 2/3 * AB[0], A[1] + 2/3 * AB[1])
print(N)
P = (A[0] + 1.5 * AB[0], A[1] + 1.5 * AB[1])
print(P)

# Plotting
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot([A[0], B[0]], [A[1], B[1]], 'k--')  # Segment AB
ax.plot(A[0], A[1], 'ro')
ax.plot(B[0], B[1], 'bo')
ax.plot(M[0], M[1], 'go')
ax.plot(N[0], N[1], 'mo')
ax.plot(P[0], P[1], 'co')

# Annotate points
ax.text(A[0] - 0.5, A[1] + 0.3, 'A')
ax.text(B[0] + 0.2, B[1], 'B')
ax.text(M[0] + 0.2, M[1], 'M')
ax.text(N[0] + 0.2, N[1], 'N')
ax.text(P[0] + 0.2, P[1], 'P')

# Set axis limits
ax.set_xlim(-5, 11)
ax.set_ylim(-6, 4)
ax.set_aspect('equal')
ax.grid(True)
plt.tight_layout()
plt.show()
