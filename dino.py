import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

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

def main():
    clock = pygame.time.Clock()
    player = Player()
    
    run = True
    while run:
        clock.tick(30)  # Set frame rate
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move()
        player.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
