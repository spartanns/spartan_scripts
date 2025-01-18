import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks Simulation")

# Colors
BLACK = (0, 0, 0)

# Clock to control frame rate
clock = pygame.time.Clock()

# Firework properties
fireworks = []


def create_firework():
    """Creates a new firework with random properties."""
    x = random.randint(50, WIDTH - 50)
    y = HEIGHT
    color = [random.randint(50, 255) for _ in range(3)]
    speed = random.uniform(3, 6)
    particles = []
    for _ in range(random.randint(30, 50)):
        angle = random.uniform(0, 360)
        velocity = random.uniform(1, 4)
        particles.append(
            {
                "x": x,
                "y": y,
                "dx": velocity * math.cos(math.radians(angle)),
                "dy": velocity * math.sin(math.radians(angle)),
                "color": color,
                "life": random.randint(30, 60),
            }
        )
    return {"x": x, "y": y, "speed": speed, "particles": particles, "exploded": False}


running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new fireworks periodically
    if random.randint(1, 10) == 1:
        fireworks.append(create_firework())

    # Update fireworks
    for firework in fireworks[:]:
        if not firework["exploded"]:
            firework["y"] -= firework["speed"]
            pygame.draw.circle(
                screen,
                firework["particles"][0]["color"],
                (firework["x"], int(firework["y"])),
                3,
            )
            if firework["y"] < random.randint(100, 300):
                firework["exploded"] = True
        else:
            for particle in firework["particles"]:
                particle["x"] += particle["dx"]
                particle["y"] += particle["dy"]
                particle["life"] -= 1
                particle["color"] = [max(c - 5, 0) for c in particle["color"]]
                pygame.draw.circle(
                    screen,
                    tuple(particle["color"]),
                    (int(particle["x"]), int(particle["y"])),
                    2,
                )
            firework["particles"] = [p for p in firework["particles"] if p["life"] > 0]
            if not firework["particles"]:
                fireworks.remove(firework)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
