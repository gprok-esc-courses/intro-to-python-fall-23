def print_board(b, p):
    print("============")
    print(p, "plays")
    for r in range(3):
        for c in range(3):
            print(b[r][c], end=' ')
        print()

def get_user_input(b):
    try:
        row = int(input("Row (1-3): "))
        col = int(input("Col (1-3): "))
        if row < 1 or row > 3 or col < 1 or col > 3:
            return -1, -1, "Row or col vaue invalid"
        elif b[row-1][col-1] != '-':
            return -1, -1, "Position already used"
        else:
            row -= 1
            col -= 1
            return row, col, None
    except ValueError:
        return -1, -1, "Wrong input, please use integers"
    
def change_player(p):
    return 'X' if p == 'O' else 'O'


def check_for_winner(b):
    # check rows and columns
    for i in range(3):
        if b[i][0] == b[i][1] and b[i][0] == b[i][2] and b[i][0] != '-':
            return b[i][0]
        if b[0][i] == b [1][i] and b[0][i] == b[2][i] and b[0][i] != '-':
            return b[0][i]
    # check diagonals
    if b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] != '-':
        return b[0][0]
    if b[0][2] == b[1][1] and b[0][2] == b[2][0] and b[0][2] != '-':
        return b[0][2]
    return None

def is_tie(b):
    for r in range(3):
        for c in range(3):
            if b[r][c] == '-':
                return False
    return True