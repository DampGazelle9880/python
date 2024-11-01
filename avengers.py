import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Avengers Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50
bullets = []
bullet_speed = -10
enemies = []
enemy_speed = 5
enemy_size = 50
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
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10
    if keys[pygame.K_SPACE]:
        bullets.append([player_pos[0] + player_size // 2, player_pos[1]])

    # Update bullet positions
    for bullet in bullets[:]:
        bullet[1] += bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Create enemies
    if random.randint(1, 20) == 1:
        create_enemy()

    # Update enemy positions
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

        # Check for collision with bullets
        for bullet in bullets[:]:
            if (bullet[0] in range(enemy[0], enemy[0] + enemy_size) and
                bullet[1] in range(enemy[1], enemy[1] + enemy_size)):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw player (Avenger)
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, (bullet[0], bullet[1], 5, 10))
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Display score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
