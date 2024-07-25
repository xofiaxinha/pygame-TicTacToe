import pygame

pygame.init()

WIDTH, HEIGHT = 700, 700
BG_COLOR = (230, 172, 182)
#loading assets
BOARD = pygame.image.load('assets/Board.png')
BOARD = pygame.transform.scale(BOARD, (WIDTH-100, HEIGHT-100))
X = pygame.image.load('assets/X.png')
O = pygame.image.load('assets/O.png')
#creating the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((BG_COLOR))
WIN.blit(BOARD, (50, 50))
pygame.display.set_caption("First Game")

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]

def addXO(board, graphical_board, player):
    #gets the mouse position
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0] - 25)/433 * 2
    converted_y = current_pos[1]/433 * 2
    #checks the board
    if(board[round(converted_x), round(converted_y)]==0):
        board[round(converted_x), round(converted_y)] = player
        if(player == 'X'):
            player = 'O'
        else:
            player = 'X'
    renderBoard(board, X, O)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()