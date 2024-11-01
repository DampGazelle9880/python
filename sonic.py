import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic Game")

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
        self.is_rolling = False

    def draw(self):
        color = BLUE if not self.is_rolling else (0, 0, 255, 150)  # Semi-transparent when rolling
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vel
        if keys[pygame.K_DOWN]:
            self.is_rolling = True
        else:
            self.is_rolling = False

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
    enemies = [Enemy(random.randint(200, 600), HEIGHT - 60) for _ in range(3)]
    
    run = True
    while run:
        clock.tick(30)  # Set frame rate
        screen.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move()

        # Check for collision with enemies
        for enemy in enemies:
            enemy.move()
            enemy.draw()

            if (player.x < enemy.x + enemy.width and
                player.x + player.width > enemy.x and
                player.y < enemy.y + enemy.height and
                player.y + player.height > enemy.y):
                if player.is_rolling:
                    # Player hits the enemy while rolling
                    enemies.remove(enemy)  # Remove enemy on collision
                else:
                    print("Game Over! You hit an enemy.")
                    run = False

        player.draw()
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
 