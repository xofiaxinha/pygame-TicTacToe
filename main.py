import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
BG_COLOR = (230, 172, 182)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    WIN.fill((BG_COLOR))
    pygame.display.update()

pygame.quit()