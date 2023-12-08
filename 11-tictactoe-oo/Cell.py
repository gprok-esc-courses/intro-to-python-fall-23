
class Cell:
    def __init__(self, row, col) -> None:
        self.content = '-'
        self.row = row
        self.col = col

    def is_empty(self):
        return self.content == '-'
    
    def play(self, user_symbol):
        if self.is_empty():
            self.content = user_symbol
        else:
            print("tried to play in non empty cell", self.row, self.col)

    def __str__(self) -> str:
        return ' ' + self.content
    

if __name__ == "__main__":
    cell = Cell(2, 1)
    cell.play('X')
    print(cell)
    cell.play('O')
    print(cell.is_empty() == True)