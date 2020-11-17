from baseline import pickCol
from AIConnect4.Game.GameClass import *

BOARD_LENGTH = 7
BOARD_HEIGHT = 6

def printBoard(state):
    print("0 | 1 | 2 | 3 | 4 | 5 | 6")
    print("-------------------------")
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

board = [0 for _ in range(42)]

while True:
    printBoard(board)
    print("Choose a column: ")
    col = int(input())
    turn = 1
    if WillItWin(board, turn, col):
        print(board)
        board = ColumnDrop(board, turn, col)
        printBoard(board)
        print("YOU WON")
        break
    board = ColumnDrop(board, turn, col)

    turn = 2
    col = pickCol(board, turn)
    if WillItWin(board, turn, col):
        print(board)
        board = ColumnDrop(board, turn, col)
        printBoard(board)
        print("YOU LOST")
        break
    board = ColumnDrop(board, turn, col)
