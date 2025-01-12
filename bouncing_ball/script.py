import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Colors
WHITE = (255, 255, 255)
BALL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ball properties
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 4  # Ball movement speed

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off walls and change color
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx = -ball_dx
        BALL_COLOR = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy = -ball_dy
        BALL_COLOR = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
