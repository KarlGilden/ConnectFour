from functions import printBoard
from functions import takeTurn

# board
board = [["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"],["⚫","⚫","⚫","⚫","⚫","⚫"]]

# game variables
player = False

# print starting board
printBoard(board)

# game loop
while True:
    #take turn
    is_winner = takeTurn(board, player)
    
    # check if winner
    if is_winner:
        counter = "🔴" if player else "🟡"
        print(counter," won!")
        break
    
    # if move is valid, switch player
    if win != None:
        player = not player
