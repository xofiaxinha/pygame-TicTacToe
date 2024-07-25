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

board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
board_positions_x = [(50,230), (250, 460), (490, 650)]
board_positions_y = [(50, 220), (245, 450), (475, 640)]

def renderBoard(board, X, O):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Create an X image and rect
                graphical_board[i][j][0] = X
                graphical_board[i][j][1] = X.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = O
                graphical_board[i][j][1] = O.get_rect(center=(j*300+150, i*300+150))
def findX(xpos):
    if(xpos<230):
        return 0
    elif(xpos<460):
        return 1
    else:
        return 2
def findY(ypos):
    if(ypos<220):
        return 0
    elif(ypos<450):
        return 1
    else:
        return 2
def addXO(board, graphical_board, player):
    #gets the mouse position
    current_pos = pygame.mouse.get_pos()
    xpos, ypos = current_pos
    #checks the board
    if(board[findX(xpos)][findY(ypos)]==-1):
        board[findX(xpos)][findY(ypos)] = player
     #   board[round(converted_x), round(converted_y)] = player
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            addXO(board, graphical_board, 'X')


    pygame.display.update()

pygame.quit()