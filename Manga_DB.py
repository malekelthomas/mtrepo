#!/usr/bin/env python3

from tkinter import *
from sqliteoperations import *
import re


def manga_search():
	books = search_db("mangadb.db", title_val.get(), isbn_val.get())
	if books != []:
		mangaList.delete(0, END)
		for book, isbn in books:
			mangaList.insert(END, "{} {}".format(book, isbn))
		return True
	else:
		if len(mangaList.get(0, END)) == 0:
			mangaList.insert(END, "Book not found")
		else:
			mangaList.delete(0, END)
			mangaList.insert(END, "Book not found")
		return False

def addManga():
	if not manga_search():
		insert("mangadb.db", title_val.get(), isbn_val.get())

def showAllFromCatalog():
	catalog = view("mangadb.db")
	mangaList.delete(0, END)
	for book, isbn in catalog:
		#pattern = r"{([\w\-\s]*)}\s{(\d*)}"
		#result = re.match(pattern, book)
		mangaList.insert(END, "{} {}".format(book, isbn))


create_table("mangadb.db")

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


#connect scrollbar to listbox vertically
sb.config(command=mangaList.yview)


#view all, search, add, update, delete, close buttons

viewALL = Button(window, height = 1, width = 5, text = "View All", command = showAllFromCatalog) 
viewALL.grid(row = 1, column = 4)

search = Button(window, height = 1, width = 5, text = "Search", command = manga_search) 
search.grid(row = 2, column = 4)

add_entry = Button(window, height = 1, width = 5, text = "Add", command = addManga) 
add_entry.grid(row = 3, column = 4)

update_entry = Button(window, height = 1, width = 5, text = "Update") 
update_entry.grid(row = 4, column = 4)

delete_entry = Button(window, height = 1, width = 5, text = "Delete") 
delete_entry.grid(row = 5, column = 4)

close = Button(window, height = 1, width = 5, text = "Close") 
close.grid(row = 6, column = 4)

window.mainloop()

