from baseline import pickColBaseline
from AIConnect4.Game.GameClass import *

player1Wins = 0
player2Wins = 0
tieCount = 0
for i in range(1000):
    board = [0 for _ in range(42)]
    count = 0
    while count < 42:
        turn = 1
        col = pickColBaseline(board, turn)
        if WillItWin(board, turn, col):
            board = ColumnDrop(board, turn, col)
            player1Wins += 1
            break
        board = ColumnDrop(board, turn, col)

        turn = 2
        col = pickColBaseline(board, turn)
        if WillItWin(board, turn, col):
            board = ColumnDrop(board, turn, col)
            player2Wins += 1
            break
        board = ColumnDrop(board, turn, col)
        count += 2
    if count == 42:
        tieCount += 1

print(f"Player 1 Wins: {player1Wins}")
print(f"Player 2 Wins: {player2Wins}")
print(f"Ties: {tieCount}")
