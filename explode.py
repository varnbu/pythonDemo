import pygame


class Explode(pygame.sprite):
    def __init__(self, target, frame, single_w, single_h, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
