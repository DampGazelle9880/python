import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Game")

# Define colors
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player class
class Player:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.width = 40
        self.height = 60
        self.vel = 5

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.vel
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vel

# Ball class
class Ball:
    def __init__(self):
        self.x = random.randint(200, 700)
        self.y = random.randint(50, 350)
        self.radius = 15
        self.vel_x = random.choice([-3, 3])
        self.vel_y = random.choice([-3, 3])

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

        # Bounce off walls
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.vel_x *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.vel_y *= -1

def main():
    clock = pygame.time.Clock()
    player = Player()
    ball = Ball()
    
    run = True
    while run:
        clock.tick(30)  # Set frame rate
        screen.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move()
        ball.move()

        # Check for collision between player and ball
        if (player.x < ball.x < player.x + player.width) and (player.y < ball.y < player.y + player.height):
            ball.vel_x *= -1  # Change ball direction

        player.draw()
        ball.draw()
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
