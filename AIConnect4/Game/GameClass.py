'''
Created on Nov 16, 2020

@author: houstonwalley
'''
BOARD_HEIGHT = 6
BOARD_LENGTH = 7



# board = the current board -> array of length 42
# turnNum = turn number -> int
# x = column -> int
def ColumnDrop(board, turnNum, x):
    boardCopy = board[:]
    for i in range(BOARD_HEIGHT - 1, -1 , -1):
        square = (BOARD_LENGTH * i) + x
        if boardCopy[square] == 0:
            boardCopy[square] = turnNum
            break
    return boardCopy

# board = the current board -> array of length 42
# turnNum = turn number -> int
# x = column -> int
def WillItWin(boardOG, turnNum, x):
    board = boardOG[:]
    for i in range(BOARD_HEIGHT - 1, -1 , -1):
        square = (BOARD_LENGTH * i) + x
        if board[square] == 0:
            board[square] = turnNum
            break
    rowNum = square // BOARD_LENGTH
    colNum = x
    # Test vertical
    touching = 1
    if square < 21:
        for i in range(rowNum + 1, rowNum + 4, 1):
            if board[(i * BOARD_LENGTH) + x] == turnNum:
                touching += 1
    if touching == 4:
        return True
    # Test horizontal
    for i in range(4):
        if board[(rowNum * BOARD_LENGTH) + i] == board[(rowNum * BOARD_LENGTH) + i + 1] and \
            board[(rowNum * BOARD_LENGTH) + i] == board[(rowNum * BOARD_LENGTH) + i + 2] and \
            board[(rowNum * BOARD_LENGTH) + i] == board[(rowNum * BOARD_LENGTH) + i + 3] and \
            board[(rowNum * BOARD_LENGTH) + i] == turnNum:
            return True
    # Test 1 diagonal
    diagDQ = [0,1,2,7,8,14,27,33,34,39,40,41]
    if square not in diagDQ:
        while rowNum < 5 and colNum > 0:
            rowNum += 1
            colNum -= 1
        possible = True
        while (possible):
            if board[(rowNum * BOARD_LENGTH) + colNum] == board[((rowNum - 1) * BOARD_LENGTH) + colNum + 1] and \
                board[(rowNum * BOARD_LENGTH) + colNum] == board[((rowNum - 2) * BOARD_LENGTH) + colNum + 2] and \
                board[(rowNum * BOARD_LENGTH) + colNum] == board[((rowNum - 3) * BOARD_LENGTH) + colNum + 3] and \
                board[(rowNum * BOARD_LENGTH) + colNum] == turnNum:
                return True
            elif rowNum - 4 >= 0 and colNum + 4 < 7:
                rowNum -= 1
                colNum += 1
            else:
                possible = False
    # Test -1 diagonal
    diagDQ = [4,5,6,12,13,20,21,28,29,35,36,37]
    rowNum = square // BOARD_LENGTH
    colNum = x
    if square not in diagDQ:
        while rowNum < 5 and colNum < 6:
            rowNum += 1
            colNum += 1
        possible = True
        while (possible):
            if board[(rowNum * BOARD_LENGTH) + colNum] == board[((rowNum - 1) * BOARD_LENGTH) + colNum - 1] and \
                board[(rowNum * BOARD_LENGTH) + colNum] == board[((rowNum - 2) * BOARD_LENGTH) + colNum - 2] and \
                board[(rowNum * BOARD_LENGTH) + colNum] == board[((rowNum - 3) * BOARD_LENGTH) + colNum - 3] and \
                board[(rowNum * BOARD_LENGTH) + colNum] == turnNum:
                return True
            elif rowNum - 4 >= 0 and colNum - 4 >= 0:
                rowNum -= 1
                colNum -= 1
            else:
                possible = False
    return False

def threeMan(boardOG, turnNum, x):
    board = boardOG[:]
    for i in range(BOARD_HEIGHT - 1, -1 , -1):
        square = (BOARD_LENGTH * i) + x
        if board[square] == 0:
            board[square] = turnNum
            break
    rowNum = square // BOARD_LENGTH
    # Test vertical
    touching = 1
    if square < 28:
        for i in range(rowNum + 1, rowNum + 3, 1):
            if board[(i * BOARD_LENGTH) + x] == turnNum:
                touching += 1
    if touching == 3:
        return True
    # Test horizontal
    if x != 5 and x != 6 and board[square] == board[square + 1] and board[square] == board[square + 2]:
        return True
    elif x != 0 and x != 1 and board[square] == board[square - 1] and board[square] == board[square - 2]:
        return True
    elif x != 0 and x != 6 and board[square] == board[square - 1] and board[square] == board[square + 1]:
        return True
    # Test 1 diagonal
    if x != 5 and x != 6 and rowNum > 1 and board[square] == board[square - 6] and board[square] == board[square - 12]:
        return True
    elif x != 0 and x != 6 and rowNum > 0 and rowNum < 5 and board[square] == board[square - 6] and board[square] == board[square + 6]:
        return True
    elif x != 0 and x != 1 and rowNum < 4 and board[square] == board[square + 6] and board[square] == board[square + 12] and x != 0 and x != 1 and rowNum < 4:
        return True 
    # Test -1 diagonal
    if x != 0 and x != 1 and rowNum > 1 and board[square] == board[square - 8] and board[square] == board[square - 16]:
        return True
    elif x != 0 and x != 6 and rowNum > 0 and rowNum < 5 and board[square] == board[square - 8] and board[square] == board[square + 8]:
        return True
    elif x != 5 and x != 6 and rowNum < 4 and board[square] == board[square + 8] and board[square] == board[square + 16]:
        return True
    return False

def twoMan(boardOG, turnNum, x):
    board = boardOG[:]
    for i in range(BOARD_HEIGHT - 1, -1 , -1):
        square = (BOARD_LENGTH * i) + x
        if board[square] == 0:
            board[square] = turnNum
            break
    rowNum = square // BOARD_LENGTH
    # Test vertical
    touching = 1
    if square < 35:
        for i in range(rowNum + 1, rowNum + 2, 1):
            if board[(i * BOARD_LENGTH) + x] == turnNum:
                touching += 1
    if touching == 2:
        return True
    # Test horizontal
    if x != 6 and board[square] == board[square + 1]:
        return True
    elif x != 0 and board[square] == board[square - 1]:
        return True
    # Test 1 diagonal
    if x != 6 and rowNum > 0 and board[square] == board[square - 6]:
        return True
    elif x != 0 and rowNum < 5 and board[square] == board[square + 6]:
        return True 
    # Test -1 diagonal
    if x != 0 and rowNum > 0 and board[square] == board[square - 8]:
        return True
    elif x != 6 and rowNum < 5 and board[square] == board[square + 8]:
        return True
    return False