import pygame

pygame.init()

WIDTH, HEIGHT = 700, 700
BG_COLOR = (230, 172, 182)
BOARD = pygame.image.load('assets/Board.png')
BOARD = pygame.transform.scale(BOARD, (WIDTH-100, HEIGHT-100))
X = pygame.image.load('assets/X.png')
O = pygame.image.load('assets/O.png')
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((BG_COLOR))
WIN.blit(BOARD, (50, 50))
pygame.display.set_caption("First Game")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()