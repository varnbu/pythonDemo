import sys

import pygame

pygame.init()

caption = pygame.display.set_caption('精灵图')
screen = pygame.display.set_mode([1200, 900])
bg = pygame.image.load('image/bg.png').convert_alpha()


class Explode(pygame.sprite.Sprite):
    def __init__(self, target, frame, single_w, single_h, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(target).convert_alpha()
        self.main_image = self.image
        self.frame = frame
        self.rect = self.image.get_rect()
        self.count = 0
        self.single_w, self.single_h = single_w, single_h
        self.rect.topleft = pos

    def update(self):
        if self.count < self.frame - 1:
            self.count += 1
        else:
            self.count = 0
        self.image = self.main_image.subsurface([self.count * self.single_w, 0, self.single_w, self.single_h])


exp = Explode('image/22.jpg', 3, 276, 278, (100, 100))
group = pygame.sprite.Group()
group.add(exp)

while True:
    screen.blit(bg, (0, 0))
    group.update()
    group.draw(screen)
    pygame.time.wait(200)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # else:
        #     screen.blit(bg, (0, 0))
        #     group.update()
        #     group.draw(screen)
        #     pygame.display.update()
