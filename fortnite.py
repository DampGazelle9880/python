import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Battle Royale Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 50
enemies = []
enemy_size = 50
enemy_speed = 3
score = 0
font = pygame.font.Font(None, 36)

# Function to create enemies
def create_enemy():
    x_pos = random.randint(0, WIDTH - enemy_size)
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
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 5
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += 5

    # Create enemies
    if random.randint(1, 20) == 1:
        create_enemy()

    # Update enemy positions
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
            score += 1  # Increase score for every enemy that falls off

        # Check for collision
        if (player_pos[0] < enemy[0] + enemy_size and
            player_pos[0] + player_size > enemy[0] and
            player_pos[1] < enemy[1] + enemy_size and
            player_pos[1] + player_size > enemy[1]):
            running = False  # End the game on collision

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Display score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
