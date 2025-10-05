import matplotlib.pyplot as plt
from src.buggy import Buggy
from src.planet import Planet

# Hozd létre a bolygót a megadott méretekkel
planet = Planet(latitudes=10, longitudes=10)

# Hozd létre a Buggy-t a kiinduló pozícióval
buggy = Buggy(x=5, y=0, direction='N', planet=planet)

# A mozgásparancsok sorozata
commands = ['f'] * 10 + ['l'] + ['f'] * 5 + ['r'] + ['f'] * 5 + ['r'] + ['f'] * 5

# Kövesd a Buggy útját és irányát
path = [(buggy.x, buggy.y)]
directions = [buggy.direction]

for command in commands:
    buggy.move(command)
    path.append((buggy.x, buggy.y))
    directions.append(buggy.direction)

# Vizuális megjelenítés
fig, ax = plt.subplots(figsize=(8, 8))

# Rajzold meg a rácsot
ax.set_xticks(range(planet.longitudes + 1))
ax.set_yticks(range(planet.latitudes + 1))
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Fordítsd meg az Y tengelyt, hogy az Észak felül legyen
ax.invert_yaxis()

# Címkék és cím
ax.set_xlabel('Hosszúság (X)')
ax.set_ylabel('Szélesség (Y)')
ax.set_title('Buggy mozgásának vizualizációja')
ax.set_aspect('equal', adjustable='box')

# Ábrázold az utat és a pontokat
x_coords = [p[0] for p in path]
y_coords = [p[1] for p in path]

ax.plot(x_coords, y_coords, 'o-', color='blue', markersize=8, linewidth=2, label='Buggy útja')
ax.plot(x_coords[0], y_coords[0], 'go', markersize=10, label='Kezdőpont')
ax.plot(x_coords[-1], y_coords[-1], 'ro', markersize=10, label='Végpont')

# Jelöld meg az átfordulásokat
for i in range(len(path) - 1):
    if abs(x_coords[i] - x_coords[i+1]) > 1 or abs(y_coords[i] - y_coords[i+1]) > 1:
        ax.plot([x_coords[i], x_coords[i+1]], [y_coords[i], y_coords[i+1]], 'r--', linewidth=1)

ax.set_xlim(-1, planet.longitudes)
ax.set_ylim(-1, planet.latitudes)

# Készíts egyedi jelmagyarázatot
handles, labels = plt.gca().get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), loc='upper left')

plt.tight_layout()
plt.show()