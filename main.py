# Tic Tac Toe Game

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap('C:/Users/along/Documents/Pycharm/Projects/Tic_Tac_Toe/pictures/peach_1f351.ICO')
root.resizable(False, False)
root.geometry("225x278")

# This code is for making the window windowed full-screen
# root.state("zoomed")


# X starts so True
clicked = True
count = 0


# Function  for disabling all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Function to check if x or o win:
def win():
    global winner
    winner = False

    # Check for X's wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X wins.")
        disable_all_buttons()

    # Check for O's wins
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O wins.")
        disable_all_buttons()

    elif count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a tie.")
        disable_all_buttons()


# Function for clicking the button
def b_click(b):
    global clicked, count

    if b["text"] == "" and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        win()
    elif b["text"] == "" and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        win()
    else:
        messagebox.showerror("Tic Tac Toe", "This box has already been selected\nPlease choose an empty box")


# Game reset5
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # Buttons
    b1 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text='', font="Helvetica", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # Grid for the button
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# Custom window for the bot
# def msg_win():
#     global bot_win
#     bot_win = Toplevel(root)
#     label = Label(bot_win, text="Choose X or O")
#     text = '''Please choose X or O'''
#     bot_win.title("Tic Tac Toe")
#     bot_win.iconbitmap('C:/Users/along/Documents/Pycharm/Projects/Tic_Tac_Toe/pictures/peach_1f351.ICO')
#     bot_win.resizable(False, False)
#     bot_win.geometry("200x100")
#     # Create button for next text.
#     bX = Button(bot_win, text="X", command=bot_win.destroy)
#     # Create an Exit button.
#     bO = Button(bot_win, text="O", command=bot_win.destroy)
#
#     # Grid for the button
#     bX.grid(row=3, column=0)
#     bO.grid(row=3, column=3)
#     bot_win.wm_attributes('-toolwindow', 'True')
#     bX.pack()
#     bO.pack()
#     bot_win.mainloop()


# Tic Tac Toe bot


def bot():
    messagebox.askquestion("Tic Tac Toe", message="Please Choose what you want to play as:")


# Menu
menu = Menu(root)
root.config(menu=menu)
menu.add_command(label="vs Player", command=reset)
menu.add_command(label="vs Bot", command=bot)
menu.add_command(label="Reset", command=reset)

reset()
mainloop()
