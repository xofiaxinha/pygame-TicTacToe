# Tic-Tac-Toe with PyGame!
That's an easy Tic-Tac-Toe game developed using the PyGame Library.
This project was created to learn and experiment with the library and its resources.

## Requirements
- Python3
- PyGame

## Initialization
1. Clone this repo to get all the necessary files to run the game:
``` bash
git clone https://github.com/xofiaxinha/pygame-TicTacToe
cd pygame-TicTacToe
```
2. Install PyGame
``` bash
pip install pygame
```

## Playing the game
1. Start the game
``` bash
python main.py
```
2. Click in any square.
   - As you do this, the computer will make its move.
   - Wins the one who aligns three pieces in a line, column or diagonal
  
## Development process
1. Initial config:
   - Import the libraries
   - Start PyGame
        ```python
        pygame.init()
        ```
    - Define colors and dimensions
        ``` python
        WIDTH, HEIGHT = 700, 700
        BG_COLOR = (230, 214, 207)
        ```
    - Load the assets into variables (so it's easier to acces inside the code)
        ```python
        BOARD = pygame.image.load('assets/newboard.png')
        X = pygame.image.load('assets/newx.png')
        O = pygame.image.load('assets/newo.png')
        X_WIN = pygame.image.load('assets/xwin.png')
        O_WIN = pygame.image.load('assets/owin.png')
        ```
        - If necessary, you can scale the assets to fit the screen using ```pygame.transform.scale(variable, (x dimension, y dimension))```.
    - Create the variables for the board
        ```python
        board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        graphical_board = [[[None, None], [None, None], [None, None]], 
                            [[None, None], [None, None], [None, None]], 
                            [[None, None], [None, None], [None, None]]]
        board_positions_x = [(50,240), (240, 470), (470, 650)]
        board_positions_y = [(50, 235), (235, 460), (460, 640)]
        ```
        - board: matrix that guards the positions from X and O
        - graphical_board: 3-dimentional matrix that will guard the image of X or O, along a ```rect``` 
        - board_positions: array of tuples that mark the starting and ending pixels of each square
2. Main logic
    - This game uses varied functions to mark the moves in the board, check the cells and the victories.
     - Main loop
       - Runs the game events, in this case, quitting and clicking on the board to make a move
  
## Code snippets
1. addXO function:
    ```python
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
    ```
    <details><summary>This funcion starts by setting ``valid`` to False, just in case the variable enters as True.</summary>
    I did this to prevent the case where, if the user makes an invalid move, the computer makes its move anyways.</details>
2. pcMove function
   ```python
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
   ```
   - This function starts by verifying if the user made an valid move (hence the ``valid`` parameter), and, if it isn't, the function just returns the board without doing anything.
   - Otherwise, it gets a random number between 0 and 2, which will be the coordinates in the ``board`` matrix.
   - Afterwards, the function enters a while that repeats itself until the coordinates point to a valid position on the board, and, when it gets to a valid position, it marks it as 'O'.
   - After that, it calls ``renderBoard()``, which changes the graphical board to add the new move, and then it enters a for, to render the new board to the screen.
   - Finally, it returns the new board.
  
## Final considerations
- This project heavily referenced [this video](https://www.youtube.com/watch?v=IL_PMGVxEUY&list=WL&index=3) by [baraltech](https://www.youtube.com/@baraltech) as a guide to both the project and PyGame.
  - You can find their project [here](https://github.com/baraltech/Tic-Tac-Toe)!
- Alongside the video, I also used a project using HTML, CSS and JavaScript of the same game that I've made a few months ago (and forgot to upload to GitHub 🤭).
- Any contribuitions are welcome! Feel free to open issues and pull requests to make the project even better.