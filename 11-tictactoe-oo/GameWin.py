from tkinter import Tk, Button, Frame, Label
from Board import Board


def deactivate_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = "disabled"


def button_clicked(row, col, btn: Button, board: Board, player):
    print("Clicked", row, col)
    if board.play(row, col, player[0]):
        btn.configure(text=player[0])
        player[0] = 'X' if player[0]=='O' else 'O'
        w = board.get_winner()
        if  w is not None:
            label.configure(text="winner " + w)
            deactivate_buttons()

window = Tk()
frame = Frame(window)
label = Label(window, text="game in progress")
board = Board()
player = ['X']


buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = Button(frame, text="-")
        btn.configure(command=lambda row=i, col=j, b=btn: button_clicked(row, col, b, board, player))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)


frame.grid(row=0, column=0)
label.grid(row=1, column=0)

window.mainloop()