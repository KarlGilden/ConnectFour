# constants
ROWS = 6
COLS = 7

def printBoard(board):
    for x in range(ROWS -1, -1, -1):
        for y in range(COLS):
            print(board[y][x], end="")
        print(" ")

def checkX(board, counter, col, row):  
    connected = 0
    left, right = col, col
    
    # search right
    while right >= 0 and right < COLS:
        if board[right][row] != counter: # go to search left
            break
        
        connected += 1
        
        if connected >= 5: # check for win
            return True
        right += 1
        
    # search left
    while left >= 0 and left < COLS:
        if board[left][row] != counter: # end search
            break
        
        connected += 1
        
        if connected >= 5: # check for win
            return True
        left -= 1
        
    return False  

def checkY(board, counter, col, row):
    connected = 0
    up, down = row, row
    
    # search down 
    while down >= 0 and down < len(board[col]):
        if board[col][down] != counter: # go to search up
            break
        
        connected += 1
        
        if connected >= 5: # check for win
            return True
        down -= 1
        
    # search up
    while up >= 0 and up < len(board[col]):
        if board[col][up] != counter: # end search
            break
        
        connected += 1
        
        if connected >= 5: # check for win
            return True
        up += 1
        
    return False

def checkLeftD(board, counter, col, row):
    connected = 0
    up, down = row, row
    left, right = col, col
    
    # search down and left
    while left >= 0 and down >= 0 and left < len(board[col]) and down < len(board[col]):
        if board[left][down] != counter: # go to search up and right if not a valid counter
            break
        
        connected += 1
        
        if connected >= 5: # check for win
            return True
        down -= 1
        left -= 1
        
    # search up and right
    while right >= 0 and up >= 0 and up < len(board[col]) and right < len(board[col]):
        if board[right][up] != counter: # end search if not a valid counter
            break
        
        connected += 1
        
        if connected >= 5: # check for win
            return True
        up += 1
        right += 1
        
    return False

def checkRightD(board, counter, col, row):
    connected = 0
    up, down = row, row
    left, right = col, col
    
    # search down and right
    while right >= 0 and down >= 0 and right < COLS and down < ROWS:
        if board[right][down] != counter: # go to search up and left if not a valid counter
            break
        
        connected += 1
        
        if connected >= 5: # check win
            return True
        down -= 1
        right += 1
        
    # search up and left
    while left >= 0 and up >= 0 and up < COLS and left < ROWS:
        if board[left][up] != counter: # go to search up and left if not a valid counter
            break
        
        connected += 1
        
        if connected >= 5: # check win
            return True
        up += 1
        left -= 1
        
    return False

def takeTurn(board, player):
    counter = "🔴" if player else "🟡"

    try:
        # user selects column
        col = int(input("Pick a column: "))
        
        # find next available slot in column
        indexAt = board[col].index("⚫")
        
        # fill slot
        board[col][indexAt] = counter

        # reprint board
        printBoard(board)
                
        # check if winning move
        y = checkY(board, counter, col, indexAt)
        x = checkX(board, counter, col, indexAt)
        dl = checkLeftD(board, counter, col, indexAt)
        dr = checkRightD(board, counter, col, indexAt)

        # return true if winning move
        if y or x or dl or dr:
            return True
        
        # return false if not winning move
        return False

    except (IndexError, ValueError):
        print("Oops!  That was not a valid column.  Try again...")