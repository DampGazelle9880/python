import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Dinosaur class
class Dino:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 60
        self.width = 50
        self.height = 50
        self.is_jumping = False
        self.jump_count = 10

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def jump(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

# Cactus class
class Cactus:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT - 50
        self.width = 20
        self.height = 40
        self.speed = 10

    def draw(self):
        pygame.draw.rect(screen, BROWN, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= self.speed

def main():
    clock = pygame.time.Clock()
    dino = Dino()
    cactus = Cactus()
    score = 0
    font = pygame.font.Font(None, 36)

    run = True
    while run:
        clock.tick(30)  # Set frame rate
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not dino.is_jumping:
                    dino.is_jumping = True

        # Move cactus and check for collision
        cactus.move()
        if cactus.x < 0:
            cactus.x = WIDTH
            score += 1  # Increment score when cactus resets

        # Check for collision
        if (cactus.x < dino.x + dino.width and
                cactus.x + cactus.width > dino.x and
                dino.y + dino.height >= cactus.y):
            print("Game Over! Your score was:", score)
            run = False

        # Draw objects
        dino.jump()
        dino.draw() 
        cactus.draw()

        # Display score 
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
