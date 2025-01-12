import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BASKET_COLOR = (0, 128, 255)

# Basket properties
basket_width, basket_height = 80, 20
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 7

# Falling object properties
obj_width, obj_height = 20, 20
obj_x = random.randint(0, WIDTH - obj_width)
obj_y = -obj_height
obj_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Draw the basket
    pygame.draw.rect(
        screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height)
    )

    # Move the falling object
    obj_y += obj_speed
    pygame.draw.rect(screen, RED, (obj_x, obj_y, obj_width, obj_height))

    # Check if the object is caught
    if (
        basket_y < obj_y + obj_height
        and basket_x < obj_x + obj_width
        and basket_x + basket_width > obj_x
    ):
        score += 1
        obj_x = random.randint(0, WIDTH - obj_width)
        obj_y = -obj_height
        obj_speed += 0.5  # Increase difficulty

    # Reset the object if it goes off-screen
    if obj_y > HEIGHT:
        obj_x = random.randint(0, WIDTH - obj_width)
        obj_y = -obj_height

    # Display the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
