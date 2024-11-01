import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Cricket Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50
ball_pos = [random.randint(0, WIDTH), 0]
ball_size = 20
ball_speed = 5
score = 0
font = pygame.font.Font(None, 36)
is_hit = False

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

    # Update ball position
    ball_pos[1] += ball_speed

    # Check if the ball is hit
    if is_hit and ball_pos[1] < HEIGHT:
        score += 1
        ball_pos = [random.randint(0, WIDTH - ball_size), 0]  # Reset ball position
        is_hit = False

    # Check for collision
    if (player_pos[0] < ball_pos[0] + ball_size and
        player_pos[0] + player_size > ball_pos[0] and
        player_pos[1] < ball_pos[1] + ball_size and
        player_pos[1] + player_size > ball_pos[1]):
        is_hit = True

    # Reset ball if it goes out of bounds
    if ball_pos[1] > HEIGHT:
        ball_pos = [random.randint(0, WIDTH - ball_size), 0]  # Reset ball position
        is_hit = False  # Missed the ball

    # Draw player (bat)
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    # Draw ball
    pygame.draw.circle(screen, RED, (ball_pos[0] + ball_size // 2, ball_pos[1] + ball_size // 2), ball_size // 2)

    # Display score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
