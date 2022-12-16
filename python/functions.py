def printBoard(c, ROWS, board):
    for x in range(ROWS):
        for y in range(board):
            print(c[y][x], end="")
        print(" ")

def checkX(board, player, col, index):
    x_cols = []
    for i in range(len(board)):
        x_cols.append(board[i][-(index + 1)])
    
    print("Row: ", x_cols)
    counter = "🔴" if player else "🟡"
    connected = 0
    right = col
    left = col
    
    while right >= 0 and right < len(x_cols) -1:
        if x_cols[right] != counter:
            print("Right: ", left)
            print("right fail")
            break
        else:
            connected += 1
            print("right pass")
            if connected >= 5:
                return True
        right += 1
        
    while left >= 0 and left < len(x_cols) -1:
        if x_cols[left] != counter:
            print("Left: ",  left)
            print("left fail")
            break
        else:
            connected += 1
            print("left pass")
            if connected >= 5:
                return True
        left -= 1
        
    return False
    
        

def checkY(board, player, col, index):
    counter = "🔴" if player else "🟡"
    connected = 0
    down = index
    up = index
    
    print("Col: ", board[col])
    
    while down >= 0 and down < len(board[col]):
        if board[col][down] != counter:
            break
        else:
            connected += 1
            if connected >= 4:
                return True
        down += 1
        
    while up >= 0 and up < len(board[col]):
        if board[col][up] != counter:
            break
        else:
            connected += 1
            if connected >= 4:
                return True
        up -= 1
        
    return False


def checkLeftD():
    pass

def checkRightD():
    pass

def takeTurn(board, player):
    global on
    ROWS = 6
    COLS = 7
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
        
        printBoard(board, ROWS, COLS)
                
        # check if winning move
        y = checkY(board, player, col, indexAt)
        x = checkX(board, player, col, indexAt)
        if (y or x) == True:
            return True
        # return false for winning game
        return False

    except (IndexError, ValueError):
        print("Oops!  That was no valid number.  Try again...")