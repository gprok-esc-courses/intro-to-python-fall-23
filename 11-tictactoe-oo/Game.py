from Board import Board 

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 'X'
        self.winner = None
        self.tie = False

    def play_game(self):
        while self.winner is None and self.tie == False: 
            self.board.display()
            print(self.player, "plays")
            row = int(input("Row: "))
            col = int(input("Col: "))
            if self.board.play(row, col, self.player):
                self.winner = self.board.get_winner()
                if self.winner != None:
                    self.board.display()
                    print(self.winner, "wins!")
                elif self.board.is_tie():
                    self.tie = True
                    self.board.display()
                    print("Tie!")
                else:
                    self.change_player()

    def change_player(self):
        self.player = 'X' if self.player == 'O' else 'O'

if __name__ == "__main__":
    game = Game()
    game.play_game()
