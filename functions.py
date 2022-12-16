def printBoard(c, ROWS, board):
    for x in range(ROWS):
        for y in range(board):
            print(c[y][x], end="")
        print(" ")

def checkX(board, player, col, index):
    x_cols = []
    for i in range(len(board)-1, -1, -1):
        x_cols.append(board[i][index])
        print(i)
    
    counter = "🔴" if player else "🟡"
    connected = 0
    right = index + 1
    left = index - 1
    
    while right >= 0 and right < len(x_cols):
        if x_cols[right] != counter:
            break
        else:
            connected += 1
            if connected >= 3:
                return True
        right += 1
        
    while left >= 0 and left < len(x_cols):
        if x_cols[left] != counter:
            break
        else:
            connected += 1
            if connected >= 3:
                return True
        left -= 1
        
    return False
    
        

def checkY(board, player, col, index):
    counter = "🔴" if player else "🟡"
    connected = 0
    down = index + 1
    up = index - 1
    
    while down >= 0 and down < len(board[col]):
        if board[col][down] != counter:
            break
        else:
            connected += 1
            if connected >= 3:
                return True
        down += 1
        
    while up >= 0 and up < len(board[col]):
        if board[col][up] != counter:
            break
        else:
            connected += 1
            if connected >= 3:
                return True
        up -= 1
        
    return False


def checkLeftD():
    pass

def checkRightD():
    pass

def takeTurn(board, player):
    global on
    try:
        # column selection
        col = int(input("Pick a column: "))
        
        # reverse list find next available slot in column
        copy = board[int(col)]
        copy.reverse()
        indexAt = copy.index("⚫")
        
        # fill slot
        if player:
            copy[indexAt] = "🔴"
        else:
            copy[indexAt] = "🟡"
        
        # insert copy back into game board
        copy.reverse()
        board[int(col)] = copy
                
        # check if winning move
        y = checkY(board, player, col, indexAt)
        x = checkX(board, player, col, indexAt)
        if (x or y) == True:
            print("You won") 
        # end turn
        return not player

    except (IndexError, ValueError):
        print("Oops!  That was no valid number.  Try again...")