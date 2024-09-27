import pygame
pygame.init()
screen = pygame.display.set_mode((900,700))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(90,90,10,10))
    pygame.display.flip()