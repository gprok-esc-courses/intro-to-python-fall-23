
board = [['-']*3 for i in range(3)]
player = 'X'
winner = None

while True:
    print("============")
    print(player, "plays")
    # Print board
    for r in range(3):
        for c in range(3):
            print(board[r][c], end=' ')
        print()
    # Get user's input for row and col
    try:
        row = int(input("Row (1-3): "))
        col = int(input("Col (1-3): "))
    except ValueError:
        print("Wrong input, please use integers")
        continue
    row -= 1
    col -= 1
    # Check for valid row and col
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Row or col vaue invalid")
    elif board[row][col] != '-':
        print("Position already used")
    else:
        # Correct, update board
        board[row][col] = player
        player = 'X' if player == 'O' else 'O'

        # Check for Winner

        # Check for Tie

