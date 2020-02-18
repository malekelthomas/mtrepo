#!/usr/bin/env python3

from tkinter import *


window = Tk()

#label for title entry
titleLabel = Label(window, height = 1, width = 5, text = "Title") 
titleLabel.grid(row = 0, column = 0)

#title entry

title_val = StringVar()
title = Entry(window, textvariable = title_val)
title.grid(row = 0, column = 1)














window.mainloop()
