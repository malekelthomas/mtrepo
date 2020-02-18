#!/usr/bin/env python3

from tkinter import *


window = Tk()

#label for title  and ISBN entries

titleLabel = Label(window, height = 1, width = 5, text = "Title") 
titleLabel.grid(row = 0, column = 0)

isbnLabel = Label(window, height = 1, width = 5, text = "ISBN") 
isbnLabel.grid(row = 0, column = 2)

#title and ISBN entries

title_val = StringVar()
title = Entry(window, textvariable = title_val)
title.grid(row = 0, column = 1)

isbn_val = StringVar()
isbn = Entry(window, textvariable = title_val)
isbn.grid(row = 0, column = 3)

#scrollbar for list

sb = Scrollbar(window)
sb.grid(row = 1, column = 1)

#listbox

mangaList = Listbox(window, height = 10, width = 20, yscrollcommand = sb.set)
mangaList.grid(row = 1, column = 0)

#test insert
for i in range(1000):
	mangaList.insert(END, str(i))

#connect scrollbar to listbox vertically
sb.config(command=mangaList.yview)


#search, add buttons

search = Button(window, height = 1, width = 5, text = "Search") 
search.grid(row = 1, column = 4)

add = Button(window, height = 1, width = 5, text = "Add") 
add.grid(row = 2, column = 4)

update = Button(window, height = 1, width = 5, text = "Update") 
update.grid(row = 3, column = 4)

delete = Button(window, height = 1, width = 5, text = "Delete") 
delete.grid(row = 4, column = 4)

close = Button(window, height = 1, width = 5, text = "Close") 
close.grid(row = 5, column = 4)


















window.mainloop()
