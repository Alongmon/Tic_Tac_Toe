from tkinter import *

win = Tk()
win.title("Test")
win.resizable(False, False)
win.geometry("300x400")


def b_click():
    pass


b1 = Button(win, text='', font="Helvetica", height=5, width=8, command=lambda: b_click(b1))
b2 = Button(win, text='', font="Helvetica", height=5, width=8, command=lambda: b_click(b2))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)

win.mainloop()
