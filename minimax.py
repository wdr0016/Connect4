from AIConnect4.Game.GameClass import *
import random

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

"""
Implements a minimax algorithm.

board: The connect4 board's current state.
turn: The number 1 or 2 dictating which it is picking for.
depth: The current depth of
"""
def pickColMinimax(board, turn):
    depth = getDepth(board, 2)

    bestMove, score = minimax(board, turn, depth, True, False)
    return bestMove

def minimax(board, turn, depth, maximizingPlayer, thisWon, col=-1):
    if thisWon:
        return None, 100 + (depth+1)
    if depth == 0:
        return None, boardScore(board, col)

    newPossibleMoves = getPossibleMoves(board)
    if turn == 1:
        newTurn = 2
    else:
        newTurn = 1

    bestMove = -1
    if maximizingPlayer:
        value = -9e999
        for newCol in newPossibleMoves:
            newBoard = ColumnDrop(board, turn, newCol)
            willItWin = WillItWin(board, turn, newCol)
            nextMove, nextScore = minimax(newBoard, newTurn, depth-1, False, willItWin, newCol)
            if depth == 5:
                #print(f"{newCol}: {nextScore}")
                pass
            if nextScore > value:
                value = nextScore
                bestMove = newCol
    else:
        value = 9e999
        for newCol in newPossibleMoves:
            newBoard = ColumnDrop(board, turn, newCol)
            willItWin = WillItWin(board, turn, newCol)
            nextMove, nextScore = minimax(newBoard, newTurn, depth-1, True, willItWin, newCol)
            nextScore *= -1
            if nextScore < value:
                value = nextScore
                bestMove = newCol

    return bestMove, value

def boardScore(board, col):
    return random.randint(0,10)

def getPossibleMoves(board):
    possibleMoves = []
    for i in range(7):
        # Only adds the column if a piece can be dropped there.
        if board[i] == 0:
            possibleMoves.append(i)
    return possibleMoves

def getDepth(board, maxDepth):
    zeroCount = 0
    depth = 1
    for i in board:
        if i == 0:
            zeroCount += 1
            if zeroCount > (maxDepth-1):
                depth = maxDepth
                break
            else:
                depth = zeroCount
    return depth




if __name__ == "__main__":
    board = [1, 2, 1, 0, 2, 0, 2, \
             2, 1, 2, 1, 1, 1, 2, \
             2, 2, 1, 2, 2, 1, 2, \
             1, 1, 1, 2, 1, 1, 2, \
             2, 1, 1, 2, 2, 2, 1, \
             1, 1, 2, 1, 2, 1, 2]

    """board = [0, 2, 0, 0, 0, 0, 0, \
             2, 1, 0, 0, 0, 0, 0, \
             2, 2, 0, 0, 0, 0, 0, \
             1, 1, 0, 0, 0, 0, 0, \
             1, 1, 1, 0, 0, 0, 0, \
             1, 1, 2, 2, 0, 0, 2]"""

    """board = [0,0,0,0,0,0,0, \
             0,0,0,0,0,0,0, \
             0,0,0,0,0,0,0, \
             0,0,0,0,0,0,0, \
             2,0,0,2,2,2,1, \
             2,0,0,1,1,2,1]"""

    board = [2, 1, 0, 0, 0, 0, 0, \
             1, 1, 0, 0, 2, 0, 0, \
             2, 2, 1, 0, 1, 0, 1, \
             2, 1, 2, 0, 2, 2, 1, \
             1, 1, 2, 0, 1, 1, 2, \
             1, 1, 2, 2, 2, 1, 2]

    """board = [2, 1, 0, 0, 0, 0, 0, \
             1, 1, 0, 0, 2, 0, 0, \
             2, 2, 1, 0, 1, 0, 1, \
             2, 1, 2, 0, 2, 2, 1, \
             1, 1, 2, 2, 1, 1, 2, \
             1, 1, 2, 2, 2, 1, 2]"""

    x = pickColMinimax(board, 1)
    print()
    print(x)
