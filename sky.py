import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40
BLOCK_COLOR = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sky Blox Game")
clock = pygame.time.Clock()

# Game variables
blocks = []

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, block)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                x, y = event.pos
                # Snap to grid
                block_rect = pygame.Rect(x // BLOCK_SIZE * BLOCK_SIZE, 
                                          y // BLOCK_SIZE * BLOCK_SIZE, 
                                          BLOCK_SIZE, BLOCK_SIZE)
                blocks.append(block_rect)

        screen.fill((135, 206, 235))  # Sky blue background
        draw_blocks()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
