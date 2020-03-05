import pygame

pygame.init()
caption = pygame.display.set_caption('Python app')
screen = pygame.display.set_mode([1000, 600])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen, [255, 0, 0], [150, 10, 20, 40], 0)
    pygame.draw.circle(screen, [0, 0, 0], [20, 50], 20, 1)
    pygame.display.update()
    screen.fill([255, 255, 255])

sys.exit()
