import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.Font(None, 20)

# Create matrix columns
columns = WIDTH // 20
drops = [random.randint(-20, HEIGHT) for _ in range(columns)]

# Clock to control frame rate
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw matrix rain
    for i in range(len(drops)):
        # Random ASCII character
        char = chr(random.randint(33, 126))
        x = i * 20
        y = drops[i] * 20
        text = font.render(char, True, GREEN)
        screen.blit(text, (x, y))

        # Update drop position
        drops[i] += 1
        if drops[i] * 20 > HEIGHT or random.random() > 0.98:
            drops[i] = random.randint(-20, 0)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
