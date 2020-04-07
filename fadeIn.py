import sys
import pygame

pygame.init()
caption = pygame.display.set_caption('淡入淡出')
screen = pygame.display.set_mode([1200, 900])

a = 0
bg = pygame.image.load('image/bg.png').convert()
while True:
    # bg.set_alpha(a)
    # screen.blit(bg, (0, 0))
    pygame.display.update()
    if a > 255:
        a = 0
    screen.fill([a, a, a])
    a += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
