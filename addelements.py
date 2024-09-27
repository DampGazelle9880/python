import pygame
import sys
pygame.init()
screen_width = 800
screen_height = 600

black = 0,0,0
white = 255,255,255
blue = 0,0,255
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pygame example!')

font = pygame.font.Font(None,74)

text = font.render('Hello Pygame!', True,white)
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
rect_width = 200
rect_height = 100
rect_x = (screen_width - rect_height)/2
rect_y = (screen_height - rect_height)/2-100
rect = pygame.Rect(rect_x,rect_y,rect_width,rect_height)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    pygame.draw.rect(screen,blue,rect)
    screen.blit(text,text_rect)
    pygame.display.flip()
pygame.quit()
sys.exit()
