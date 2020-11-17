import random

"""
Picks a move that will win it the game. Random if no winning move available

board: The connect4 board's current state.
turn: The number 1 or 2 dictating which it is picking for.
"""
def pickCol(board, turn):
    possibleMoves = []
    for i in range(7):
        if board[i] == 0:
            possibleMoves.append(i)

    for col in possibleMoves:
        newBoard, didItWin = dropCol(board, turn, col)
        if didItWin:
            return col

    return random.choice(possibleMoves)

# REPLACE LATER WITH houstonwalley CODE
def dropCol(x, y, z):
    if z == 3:
        return 1, True
    return 1, False

if __name__ == "__main__":
    x = [0,0,1,1,0,2,1,1,0,2,1]
    print(pickCol(x, 1))
