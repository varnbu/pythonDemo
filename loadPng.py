import sys

import pygame

import random

pygame.init()
caption = pygame.display.set_caption('python app')
screen = pygame.display.set_mode([1200, 900])

obj = pygame.image.load("image/bg.png").convert_alpha()

random.randrange(10, 100)

plane = 'image/fj.tiff'
enemy = 'image/dj.tiff'

pln = pygame.image.load(plane).convert_alpha()
enm = pygame.image.load(enemy).convert_alpha()

px = 300
py = 500

ex1 = random.randrange(20, 100)
ey1 = random.randrange(10, 50)
ex2 = random.randrange(300, 600)
ey2 = random.randrange(10, 50)
ex3 = random.randrange(600, 900)
ey3 = random.randrange(10, 50)

y_move = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.blit(obj, (0, y_move))
        screen.blit(pln, (px, py))
        screen.blit(enm, (ex1, ey1))
        screen.blit(enm, (ex2, ey2))
        screen.blit(enm, (ex3, ey3))

        pygame.display.update()
        # y_move -= 1
        py -= 1
        ey1 += 1
        ey2 += 1
        ey3 += 1
    screen.fill([25, 25, 25])
