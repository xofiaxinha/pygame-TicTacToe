import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 700, 700
BG_COLOR = (230, 214, 207)
#loading assets
BOARD = pygame.image.load('assets/newboard.png')
X = pygame.image.load('assets/newx.png')
X = pygame.transform.scale(X, (150, 150))
O = pygame.image.load('assets/newo.png')
O = pygame.transform.scale(O, (150, 150))
X_WIN = pygame.image.load('assets/xwin.png')
X_WIN = pygame.transform.scale(X_WIN, (150, 150))
O_WIN = pygame.image.load('assets/owin.png')
O_WIN = pygame.transform.scale(O_WIN, (150, 150))
#creating the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((BG_COLOR))
WIN.blit(BOARD, (50, 50))
validMove = False
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
                graphical_board[i][j][1] = ximg.get_rect(center=(round((board_positions_x[i][0]+board_positions_x[i][1])/2), round((board_positions_y[j][0]+board_positions_y[j][1])/2)))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(round((board_positions_x[i][0]+board_positions_x[i][1])/2), round((board_positions_y[j][0]+board_positions_y[j][1])/2)))
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
    
def pcMove(board, valid):
    if(not valid): return board
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while board[x][y] != -1:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    board[x][y] = 'O'
    renderBoard(board, X, O)
    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] != None:
                WIN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
    return board
    
def addXO(board, graphical_board, valid):
    valid = False
    #gets the mouse position
    current_pos = pygame.mouse.get_pos()
    xpos, ypos = current_pos
    #checks the board
    if(board[findX(xpos)][findY(ypos)]==-1):
        board[findX(xpos)][findY(ypos)] = 'X'
        valid = True
     #   board[round(converted_x), round(converted_y)] = player
    renderBoard(board, X, O)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] != None:
                WIN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, valid

def checkWinner(board):
    winner = None
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != -1:
            winner = board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != -1:
            winner = board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != -1:
        winner = board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != -1:
        winner = board[0][2]
    
    if(winner != None):
        for i in range(3):
            for j in range(3):
                if board[i][j] == winner:
                    graphical_board[i][j][0] = X_WIN if winner == 'X' else O_WIN
                    WIN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
        pygame.display.update()
        return winner
    return None

def checkDraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                return False
    return True

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
            board, validMove = addXO(board, graphical_board, validMove)
            if((checkWinner(board) == None) and (not checkDraw(board))):
                board = pcMove(board, validMove)
                validMove = False
            if game_over:
                board, graphical_board = resetGame(board, graphical_board)
                game_over = False
            if checkDraw(board):
                game_over = True
            if checkWinner(board) != None:
                game_over = True
            pygame.display.update()


    pygame.display.update()

pygame.quit()