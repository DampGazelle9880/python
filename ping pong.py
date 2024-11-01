import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Ping Pong Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Game variables
player_pos = [50, HEIGHT // 2 - 50]
player_size = (10, 100)
opponent_pos = [WIDTH - 60, HEIGHT // 2 - 50]
opponent_size = (10, 100)
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_size = 15
ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

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
    if keys[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= 10
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - player_size[1]:
        player_pos[1] += 10

    # Move the opponent (simple AI)
    if opponent_pos[1] + opponent_size[1] / 2 < ball_pos[1]:
        opponent_pos[1] += 4
    if opponent_pos[1] + opponent_size[1] / 2 > ball_pos[1]:
        opponent_pos[1] -= 4

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - ball_size:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if (player_pos[0] < ball_pos[0] < player_pos[0] + player_size[0] and
        player_pos[1] < ball_pos[1] < player_pos[1] + player_size[1]):
        ball_speed[0] = -ball_speed[0]

    if (opponent_pos[0] < ball_pos[0] < opponent_pos[0] + opponent_size[0] and
        opponent_pos[1] < ball_pos[1] < opponent_pos[1] + opponent_size[1]):
        ball_speed[0] = -ball_speed[0]

    # Score points and reset the ball
    if ball_pos[0] < 0:
        opponent_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]

    if ball_pos[0] > WIDTH:
        player_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size[0], player_size[1]))
    pygame.draw.rect(screen, WHITE, (opponent_pos[0], opponent_pos[1], opponent_size[0], opponent_size[1]))

    # Draw ball
    pygame.draw.circle(screen, GREEN, (ball_pos[0], ball_pos[1]), ball_size)

    # Display scores
    score_text = font.render(f'Player: {player_score}  Opponent: {opponent_score}', True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
