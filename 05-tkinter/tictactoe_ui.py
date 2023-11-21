from tkinter import Tk, Button, Label, font



def set_player(event):
    global player
    b = event.widget
    b.configure(text=player)
    player = 'O' if player == 'X' else 'X' 


def change_player(p):
    return 'O' if p == 'X' else 'X' 

def play(event):
    global player
    event.widget.configure(text=player)
    player = change_player(player)
    if is_tie():
        print("TIE")

def is_tie():
    for r in range(3):
        for c in range(3):
            if buttons[r][c].cget('text') == '-':
                return False
    return True


player = 'X'

window = Tk()
window.geometry("300x200")

gameFont = font.Font(size=40)

buttons = []
for r in range(3):
    button_row = []
    for c in range(3):
        btn = Button(window, text='-')
        btn.bind('<Button-1>', lambda event: play(event))
        btn['font'] = gameFont
        btn.grid(row=r, column=c)
        button_row.append(btn)
    buttons.append(button_row)

window.mainloop()
