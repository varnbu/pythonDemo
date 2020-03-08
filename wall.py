import pygame
import sys

pygame.init()
caption = pygame.display.set_caption('剑客')
screen = pygame.display.set_mode([1200, 900])

jk = pygame.image.load('image/jk.tiff').convert_alpha()
# 翻转方法
jkx = pygame.transform.flip(jk, 1, 0)
jky = pygame.transform.flip(jk, 0, 1)
# 放大缩小方法 按照尺寸
jkSmall = pygame.transform.scale(jk, (20, 20))
# 旋转
jkRotate = pygame.transform.rotate(jk, 20)
#  旋转并放大缩小  按照倍数
# jkRotateZoom = pygame.transform.rotozoom(jk, 20, 2)
jkRotateZoom = pygame.transform.rotozoom(jk, 20, 0.5)
#  裁切
jkChop = pygame.transform.chop(jk, (25, 29, 49, 32))


jk_x = 0
jk_y = 630

w1 = 'image/1.jpg'
w2 = 'image/2.jpg'
w_i_1 = pygame.image.load(w1).convert_alpha()
w_i_2 = pygame.image.load(w2).convert_alpha()
total = 30
wall = []
while total > 0:
    if total % 2 == 0:
        wall.append(w_i_1)
    else:
        wall.append(w_i_2)
    total -= 1


def fresh_wall():
    init_x = 0
    init_y = 600
    step_x = 62
    step_y = -30
    for w in wall:
        screen.blit(w, (init_x, init_y))
        init_x += step_x
        init_y += step_y
        pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            jk_x, jk_y = event.pos
            fresh_wall()
            screen.blit(jk, (jk_x, jk_y))
            # screen.blit(jky, (jk_x, jk_y))
            # screen.blit(jkChop, (jk_x, jk_y))
            pygame.display.update()
            screen.fill([25, 25, 25])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('w : 向上')
                jk_y += -30
                fresh_wall()
                screen.blit(jk, (jk_x, jk_y))
                pygame.display.update()
                screen.fill([25, 25, 25])
