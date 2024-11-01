import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 40
FPS = 60

# Colors
SKY_COLOR = (135, 206, 235)
GRASS_COLOR = (0, 255, 0)
DIRT_COLOR = (139, 69, 19)
STONE_COLOR = (128, 128, 128)

# Define blocks
BLOCK_TYPES = {
    'grass': GRASS_COLOR,
    'dirt': DIRT_COLOR,
    'stone': STONE_COLOR
}

# Create the grid
grid = [[random.choice(list(BLOCK_TYPES.keys())) for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]

# Player class
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.inventory = {'grass': 0, 'dirt': 0, 'stone': 0}

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def update(self, grid):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= BLOCK_SIZE
        if keys[pygame.K_RIGHT] and self.x < WIDTH - BLOCK_SIZE:
            self.x += BLOCK_SIZE
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= BLOCK_SIZE
        if keys[pygame.K_DOWN] and self.y < HEIGHT - BLOCK_SIZE:
            self.y += BLOCK_SIZE

        # Placing and breaking blocks
        if keys[pygame.K_SPACE]:
            grid[self.y // BLOCK_SIZE][self.x // BLOCK_SIZE] = 'grass'
            self.inventory['grass'] += 1

        if keys[pygame.K_b]:  # Break block
            block_type = grid[self.y // BLOCK_SIZE][self.x // BLOCK_SIZE]
            if block_type in self.inventory:
                self.inventory[block_type] -= 1
            grid[self.y // BLOCK_SIZE][self.x // BLOCK_SIZE] = 'grass'  # Replace with empty

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minecraft Clone")
    clock = pygame.time.Clock()
    player = Player()

    run = True
    while run:
        clock.tick(FPS)
        screen.fill(SKY_COLOR)

        # Draw the grid
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                block_type = grid[y][x]
                pygame.draw.rect(screen, BLOCK_TYPES[block_type], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Draw the player
        player.draw(screen)
        player.update(grid)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
