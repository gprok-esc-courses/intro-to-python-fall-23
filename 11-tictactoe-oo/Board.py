from Cell import Cell

class Board:
    def __init__(self) -> None:
        self.cells = []
        for r in range(3):
            row = []
            for c in range(3):
                cell = Cell(r, c)
                row.append(cell)
            self.cells.append(row)

    def display(self):
        for r in range(3):
            for c in range(3):
                print(self.cells[r][c], end='')
            print()

    def play(self, row, col, player_symbol):
        row = row - 1
        col = col - 1
        if row < 0 or col < 0 or row > 2 or col > 2:
            print("Invalid row/col", row, col)
            return False 
        elif self.cells[row][col].is_empty():
            self.cells[row][col].play(player_symbol)
            return True
        else:
            print("Cell", row, col, "not empty")
            return False 
        
    def check_row(self, i):
        if self.cells[i][0].content == self.cells[i][1].content and \
            self.cells[i][0].content == self.cells[i][2].content and \
            not self.cells[i][0].is_empty():
            return self.cells[i][0].content
        else:
            return None
        
    def check_col(self, i):
        if self.cells[0][i].content == self.cells[1][i].content and \
            self.cells[0][i].content == self.cells[2][i].content and \
            not self.cells[0][i].is_empty():
            return self.cells[0][i].content
        else:
            return None
        
    def check_diagonals(self):
        if self.cells[0][0].content == self.cells[1][1].content and \
            self.cells[0][0].content == self.cells[2][2].content and \
            not self.cells[0][0].is_empty():
            return self.cells[0][0].content
        elif self.cells[0][2].content == self.cells[1][1].content and \
            self.cells[0][2].content == self.cells[2][0].content and \
            not self.cells[0][2].is_empty():
            return self.cells[0][2].content
        else:
            return None
        
    def is_tie(self):
        for r in range(3):
            for c in range(3):
                if self.cells[r][c].is_empty():
                    return False
        return True
        
        
    def get_winner(self):
        for i in range(3):
            w = self.check_row(i)
            if w != None:
                return w
            w = self.check_col(i)
            if w != None:
                return w
            w = self.check_diagonals()
            if w != None:
                return w
            
            

if __name__ == '__main__':
    board = Board()
    board.display()
