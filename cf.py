from functions import printBoard
from functions import takeTurn

# constants
ROWS = 6
COLS = 7

# board
board = [["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"]]

# game variables
playing = True
player = False

# print starting board
printBoard(board, ROWS, COLS)

# game loop
while playing:
    player = takeTurn(board, player)
    if player == "You win":
        break
    printBoard(board, ROWS, COLS)
