import random

"""
Picks a move that will win it the game. If no such move available, it picks a
    move that would block the opponent from winning.

board: The connect4 board's current state.
turn: The number 1 or 2 dictating which it is picking for.
"""
def pickCol(board, turn):
    possibleMoves = []
    for i in range(7):
        # Only adds the column if a piece can be dropped there.
        if board[i] == 0:
            possibleMoves.append(i)

    # This checks all possible moves to see if any move will win the game.
    for col in possibleMoves:
        newBoard, didItWin = dropCol(board, turn, col)
        if didItWin:
            return col

    # This flips the turn to see what the opponent could do.
    if turn == 1:
        newTurn = 2
    else:
        newTurn = 1

    # This goes through all possible moves to see if any move will
    #   block the opponent from winning.
    for col in possibleMoves:
        newBoard, didItWin = dropCol(board, newTurn, col)
        if didItWin:
            return col

    # Returns a random possible move if it cannot win or block a win.
    return random.choice(possibleMoves)

# REPLACE LATER WITH houstonwalley CODE
def dropCol(x, y, z):
    if y == 2:
        return 5, True
    if z == 3:
        return 1, True
    return 1, False

if __name__ == "__main__":
    x = [0,0,1,1,0,2,1,1,0,2,1]
    print(pickCol(x, 1))
