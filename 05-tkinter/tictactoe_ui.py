from tkinter import Tk, Button, Label, font



def set_player(event):
    global player
    b = event.widget
    b.configure(text=player)
    player = 'O' if player == 'X' else 'X' 


player = 'X'

window = Tk()
window.geometry("300x300")

gameFont = font.Font(size=40)

buttons = []
for r in range(3):
    button_row = []
    for c in range(3):
        btn = Button(window, text='-')
        btn.bind('<Button-1>', set_player)
        btn['font'] = gameFont
        btn.grid(row=r, column=c)
        button_row.append(btn)
    buttons.append(button_row)

window.mainloop()
