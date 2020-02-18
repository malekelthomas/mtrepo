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


#scrollbar for list

sb = Scrollbar(window)
sb.grid(row = 1, column = 1)

#listbox

mangaList = Listbox(window, yscrollcommand = sb.set)
mangaList.grid(row = 1, column = 0)

#test insert
for i in range(1000):
	mangaList.insert(END, str(i))

#
sb.config(command=mangaList.yview)

















window.mainloop()
