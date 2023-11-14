# from tictactoe_lib import print_board, get_user_input, change_player, check_for_winner, is_tie
# from tictactoe_lib import *
import tictactoe_lib as tlib

board = [['-']*3 for i in range(3)]
player = 'X'
winner = None

while True:
    tlib.print_board(board, player)
    row, col, err =  tlib.get_user_input(board)
    if err is not None:
        print(err)
    else:
        board[row][col] = player
        player = tlib.change_player(player)

        winner = tlib.check_for_winner(board)
        if winner is not None:
            tlib.print_board(board, player)
            print(winner + " wins!")
            break
        elif tlib.is_tie(board):
            tlib.print_board(board, player)
            print("Tie")
            break

