import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Paramètres
n_circles = 100
colors = ["red", "yellow"]
radius = 0.05
dt = 0.01

# Créer les cercles
circles = []
for _ in range(n_circles):
    x = np.random.uniform(radius, 1-radius)
    y = np.random.uniform(radius, 1-radius)
    color = np.random.choice(colors)
    circle = patches.Circle((x, y), radius, color=color, alpha=0.6)
    circles.append(circle)

# Initialiser la figure et les axes
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

for circle in circles:
    ax.add_patch(circle)

# Générer les vitesses aléatoires
velocities = np.random.uniform(-0.01, 0.01, size=(n_circles, 2))

def update(frame):
    for i, circle in enumerate(circles):
        if circle is None:
            continue

        # Mettre à jour la position du cercle
        x, y = circle.center
        dx, dy = velocities[i]
        x_new, y_new = x + dx * dt, y + dy * dt

        # Vérifier les collisions avec les bords
        if x_new < radius or x_new > 1 - radius:
            velocities[i, 0] = -velocities[i, 0]
        if y_new < radius or y_new > 1 - radius:
            velocities[i, 1] = -velocities[i, 1]

        # Mettre à jour la position
        circle.center = x_new, y_new

        # Vérifier les collisions avec les autres cercles
        for j, other_circle in enumerate(circles):
            if other_circle is None or i == j:
                continue
            distance = np.sqrt((x_new - other_circle.center[0])**2 + (y_new - other_circle.center[1])**2)
            if distance <= 2 * radius:
                circles[i] = None
                circles[j] = None
                circle.set_visible(False)
                other_circle.set_visible(False)

    return circles

animation = FuncAnimation(fig, update, frames=1000, interval=20, blit=True)
plt.show()
