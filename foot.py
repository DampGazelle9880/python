import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Mario Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 60
        self.width = 40
        self.height = 60
        self.vel = 5
        self.is_jumping = False
        self.jump_count = 10

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vel
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

# Platform class
class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, BROWN, (self.x, self.y, self.width, self.height))

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.vel = 3

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.vel
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.vel *= -1

def main():
    clock = pygame.time.Clock()
    player = Player()
    platforms = [Platform(100, HEIGHT - 100, 200, 10), Platform(400, HEIGHT - 200, 200, 10)]
    enemies = [Enemy(300, HEIGHT - 60), Enemy(600, HEIGHT - 60)]

    run = True
    while run:
        clock.tick(30)  # Set frame rate
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move()

        # Check for collision with platforms
        for platform in platforms:
            if (player.x + player.width > platform.x and 
                player.x < platform.x + platform.width and 
                player.y + player.height >= platform.y and 
                player.y + player.height <= platform.y + platform.height):
                player.y = platform.y - player.height
                player.is_jumping = False
                player.jump_count = 10

        # Move and draw enemies
        for enemy in enemies:
            enemy.move()
            enemy.draw()

            # Check for collision with enemy
            if (player.x < enemy.x + enemy.width and
                player.x + player.width > enemy.x and
                player.y < enemy.y + enemy.height and
                player.y + player.height > enemy.y):
                print("Game Over! You hit an enemy.")
                run = False

        player.draw()
        for platform in platforms:
            platform.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
