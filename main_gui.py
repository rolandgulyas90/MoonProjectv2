import pygame
import sys
from src.planet import Planet
from src.buggy import Buggy

# --- Konstansok és beállítások ---
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CELL_SIZE = SCREEN_WIDTH // 10

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
MARS_COLOR = (192, 100, 45)
OBSTACLE_COLOR = (200, 50, 50)
BUGGY_COLOR = (50, 200, 50)
COMPASS_POINTER_COLOR = (255, 100, 100)  # ÚJ SZÍN az iránytű mutatójának

# ÚJ KONSTANSOK az iránytűhöz
COMPASS_CENTER = (SCREEN_WIDTH - 60, 60)
COMPASS_RADIUS = 40


def draw_grid(screen, planet):
    # ... ez a függvény változatlan ...
    for y in range(planet.latitudes):
        for x in range(planet.longitudes):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)


def draw_elements(screen, buggy, planet):
    # ... ez a függvény változatlan ...
    for (ox, oy) in planet.obstacles:
        rect = pygame.Rect(ox * CELL_SIZE, oy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, OBSTACLE_COLOR, rect)

    buggy_rect = pygame.Rect(buggy.x * CELL_SIZE, buggy.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BUGGY_COLOR, buggy_rect)

    center_x, center_y = buggy.x * CELL_SIZE + CELL_SIZE / 2, buggy.y * CELL_SIZE + CELL_SIZE / 2
    triangle_size = CELL_SIZE / 4
    if buggy.direction == 'N':
        points = [(center_x, center_y - triangle_size), (center_x - triangle_size, center_y + triangle_size),
                  (center_x + triangle_size, center_y + triangle_size)]
    elif buggy.direction == 'S':
        points = [(center_x, center_y + triangle_size), (center_x - triangle_size, center_y - triangle_size),
                  (center_x + triangle_size, center_y - triangle_size)]
    elif buggy.direction == 'E':
        points = [(center_x + triangle_size, center_y), (center_x - triangle_size, center_y - triangle_size),
                  (center_x - triangle_size, center_y + triangle_size)]
    else:
        points = [(center_x - triangle_size, center_y), (center_x + triangle_size, center_y - triangle_size),
                  (center_x + triangle_size, center_y + triangle_size)]
    pygame.draw.polygon(screen, WHITE, points)


# --- ÚJ FÜGGVÉNY: IRÁNYTŰ RAJZOLÁSA ---
def draw_compass(screen, direction):
    """Kirajzol egy iránytűt a képernyőre a jármű aktuális irányával."""
    # Betűtípus beállítása
    font = pygame.font.Font(None, 28)

    # Az iránytű körvonala
    pygame.draw.circle(screen, WHITE, COMPASS_CENTER, COMPASS_RADIUS, 1)

    # Égtájak betűinek kirajzolása
    directions = {"N": (0, -1), "S": (0, 1), "W": (-1, 0), "E": (1, 0)}
    for char, (dx, dy) in directions.items():
        text = font.render(char, True, WHITE)
        text_rect = text.get_rect(
            center=(COMPASS_CENTER[0] + dx * (COMPASS_RADIUS - 15), COMPASS_CENTER[1] + dy * (COMPASS_RADIUS - 15)))
        screen.blit(text, text_rect)

    # A mutató (egy piros háromszög) kirajzolása az aktuális irányba
    pointer_length = COMPASS_RADIUS - 5
    if direction in directions:
        dx, dy = directions[direction]
        # A háromszög csúcsa, ami az irányba mutat
        p1 = (COMPASS_CENTER[0] + dx * pointer_length, COMPASS_CENTER[1] + dy * pointer_length)
        # A háromszög alapjának két pontja (az iránymutató vektorára merőlegesen)
        base_offset = 8
        p2 = (COMPASS_CENTER[0] - dy * base_offset, COMPASS_CENTER[1] + dx * base_offset)
        p3 = (COMPASS_CENTER[0] + dy * base_offset, COMPASS_CENTER[1] - dx * base_offset)
        pygame.draw.polygon(screen, COMPASS_POINTER_COLOR, [p1, p2, p3])


def run_simulation_gui():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Marsjáró Szimulátor")
    clock = pygame.time.Clock()

    planet_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    planet_radius = SCREEN_WIDTH // 2 - 5

    akadalyok = [(1, 4), (5, 8), (7, 2)]
    bolygo = Planet(latitudes=10, longitudes=10, obstacles=akadalyok)
    marsjaro = Buggy(x=0, y=0, direction='S', planet=bolygo)

    running = True
    while running:
        # 1. Eseménykezelés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                command = None
                if event.key == pygame.K_UP:
                    command = 'f'
                elif event.key == pygame.K_DOWN:
                    command = 'b'
                elif event.key == pygame.K_LEFT:
                    command = 'l'
                elif event.key == pygame.K_RIGHT:
                    command = 'r'
                elif event.key == pygame.K_q:
                    running = False

                if command:
                    report = marsjaro.move(command)
                    if report == "AKADÁLY":
                        print("Jelentés: AKADÁLY!")

        # 2. Rajzolás
        screen.fill(BLACK)
        pygame.draw.circle(screen, MARS_COLOR, planet_center, planet_radius)
        draw_grid(screen, bolygo)
        draw_elements(screen, marsjaro, bolygo)
        draw_compass(screen, marsjaro.direction)  # <<< AZ IRÁNYTŰ MEGHÍVÁSA

        # 3. Képernyő frissítése
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run_simulation_gui()