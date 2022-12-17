from functions import printBoard
from functions import takeTurn

# constants
ROWS = 6
COLS = 7

# board
board = [["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"]]

# game variables
player = False

# print starting board
printBoard(board)

# game loop
while True:
    win = takeTurn(board, player)
    if win:
        counter = "🔴" if player else "🟡"
        print(counter," won!")
        break
    
    if win != None:
        player = not player
