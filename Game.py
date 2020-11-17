'''
Created on Sep 23, 2020

@author: houstonwalley
'''
# Variables
BOARD_LENGTH = 7
BOARD_HEIGHT = 6
NUMBER_OF_SQUARES = BOARD_HEIGHT * BOARD_LENGTH
board = []
lastMove = 0

def PrintBoard(state):
    print("A | B | C | D | E | F | G")
    for i in range(BOARD_HEIGHT):
        line = ""
        for j in range(BOARD_LENGTH):
            square = (i * BOARD_LENGTH) + j
            # Print Blue
            if state[square] == 2:
                line += "\033[1;34;40mO\033[m"
            # Print Red
            elif state[square] == 1:
                line += "\033[1;31;40mO\033[m"
            # Print default
            else:
                line += "O"
            if not j == (BOARD_LENGTH - 1):
                line+= " | "
        print(line)

def RedColumnDrop(x):
    colFind = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    if x in colFind:
        colNum = colFind[x]
        for i in range(BOARD_HEIGHT - 1, -1 , -1):
            square = (BOARD_LENGTH * i) + colNum
            if board[square] == 0:
                board[square] = 1
                lastMove = square
                return True
        return False
    else:
        return False

def BlueColumnDrop(x):
    colFind = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    if x in colFind:
        colNum = colFind[x]
        for i in range(BOARD_HEIGHT - 1, -1, -1):
            square = (BOARD_LENGTH * i) + colNum
            if board[square] == 0:
                board[square] = 2
                lastMove = square
                return True
        return False
    else:
        return False

def GameOver():
    rowNum = lastMove / BOARD_LENGTH
    colNum = lastMove % BOARD_LENGTH
    return False

for i in range(NUMBER_OF_SQUARES):
    board.append(0)

turn = 0
while turn < 200:
    c = ""
    print(board)
    if (turn % 2) == 1:
        done = False
        while not done:
            print(chr(27) + "[2J")
            PrintBoard(board)
            print("Which column would you like to drop your piece down \033[1;31;40mRed\033[m? \n")
            c = input()
            done = RedColumnDrop(c)
    else:
        done = False
        while not done:
            print(chr(27) + "[2J")
            PrintBoard(board)
            print("Which column would you like to drop your piece down \033[1;34;40mBlue\033[m? \n")
            c = input()
            done = BlueColumnDrop(c)
    turn += 1
print(chr(27) + "[2J")
PrintBoard(board)
print("Congratulations \033[1;31;40mRed\033[m you won!")
