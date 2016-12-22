#! /bin/env python
# -*- coding: utf-8 -*-

import time, sys

if sys.version < '3':
    from Tkinter import *
else:
    from tkinter import *

delay_min = 20

def showMessage():
    root = Tk()
    root.withdraw()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight() - 100
    root.resizable(False, False)

    root.title("Warning!")
    frame = Frame(root, relief=RIDGE, borderwidth = 3)
    frame.pack(fill=BOTH, expand=1)

    label = Label(frame, text = "Please have a break!")
    label.pack(fill=BOTH, expand=1)

    button = Button(frame, text="OK", font="Cooper -25 bold", fg="red", command=root.destroy)
    button.pack(side=BOTTOM)

    root.update_idletasks()
    root.deiconify()
    root.withdraw()
    root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10, (screenwidth - root.winfo_width())/2, (screenheight - root.winfo_height())/2))
    root.deiconify()
    root.mainloop()

while True:
    time.sleep(delay_min * 60)
    showMessage()
