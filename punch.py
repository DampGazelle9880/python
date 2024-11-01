import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Punching Enemies Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
player_pos = [WIDTH // 2, HEIGHT - 100]
enemies = []
enemy_speed = 5
score = 0
font = pygame.font.Font(None, 36)

# Function to create enemies
def create_enemy():
    x_pos = random.randint(0, WIDTH - 50)
    enemies.append([x_pos, 0])

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 50:
        player_pos[0] += 10

    # Punching mechanic
    punching = keys[pygame.K_SPACE]

    # Create enemies
    if random.randint(1, 20) == 1:
        create_enemy()

    # Update enemy positions
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

        # Check for collision with punch
        if punching and player_pos[0] in range(enemy[0] - 20, enemy[0] + 70) and enemy[1] in range(player_pos[1], player_pos[1] + 50):
            enemies.remove(enemy)
            score += 1

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], 50, 50))
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, GREEN, (enemy[0], enemy[1], 50, 50))

    # Display score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
