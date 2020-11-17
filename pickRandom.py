import random

def pickColRandom(board, turn):
    possibleMoves = []
    for i in range(7):
        # Only adds the column if a piece can be dropped there.
        if board[i] == 0:
            possibleMoves.append(i)

    return random.choice(possibleMoves)
