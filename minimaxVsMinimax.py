from minimax import pickColMinimax
from AIConnect4.Game.GameClass import *

player1Wins = 0
player2Wins = 0
tieCount = 0
for i in range(100):
    board = [0 for _ in range(42)]
    count = 0
    while count < 42:
        turn = 1
        col = pickColMinimax(board, turn)
        if WillItWin(board, turn, col):
            board = ColumnDrop(board, turn, col)
            player1Wins += 1
            break
        board = ColumnDrop(board, turn, col)

        turn = 2
        col = pickColMinimax(board, turn)
        if WillItWin(board, turn, col):
            board = ColumnDrop(board, turn, col)
            player2Wins += 1
            break
        board = ColumnDrop(board, turn, col)
        count += 2
    if count == 42:
        tieCount += 1

print(f"Minimax Player 1 Wins: {player1Wins}")
print(f"Minimax Player 2 Wins: {player2Wins}")
print(f"Ties: {tieCount}")
