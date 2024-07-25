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
player = 'X'
game_over = False

board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
board_positions_x = [(50,240), (240, 470), (470, 650)]
board_positions_y = [(50, 235), (235, 460), (460, 640)]

def renderBoard(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Create an X image and rect
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(topleft=(board_positions_x[i][0]+20, board_positions_y[j][0]+30))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(topleft=(board_positions_x[i][0]+20, board_positions_y[j][0]+30))
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

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] != None:
                WIN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, player

def checkWinner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != -1:
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != -1:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != -1:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != -1:
        return board[0][2]

    return None

def resetGame(board, graphical_board):
    board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
    WIN.fill((BG_COLOR))
    WIN.blit(BOARD, (50, 50))
    return board, graphical_board

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, player = addXO(board, graphical_board, player)
            if game_over:
                board, graphical_board = resetGame(board, graphical_board)
                game_over = False
            if checkWinner(board) != None:
                game_over = True

            pygame.display.update()


    pygame.display.update()

pygame.quit()