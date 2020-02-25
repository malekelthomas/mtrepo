#!/usr/bin/env python3

from tkinter import *
from MangaDB import *

initDB()

def showAllFromCatalog():
	catalog = view("mangadb.db")
	mangaList.delete(0, END)
	for book, isbn in catalog:
		mangaList.insert(END, "{} {}".format(book, isbn))

def checkBothEntries():
	if title_val.get() == ""  and isbn_val.get() == "":
		mangaList.delete(0, END)
		mangaList.insert(END, "Enter manga name and ISBN")
		return False
	elif title_val.get() == "":
		mangaList.delete(0, END)
		mangaList.insert(END, "Enter manga name")
		return False
	elif isbn_val.get() == "":
		mangaList.delete(0, END)
		mangaList.insert(END, "Enter ISBN")
		return False
	else:
		return True 

def bookSearch(title_val, isbn_val):
	if checkBothEntries():
		manga_search(title_val, isbn_val)

def bookAdd(title_val, isbn_val):
	if checkBothEntries():
		if addManga(title_val, isbn_val):
			mangaList.delete(0, END)
			mangaList.insert(END, "{} added to catalog".format(title_val.get()))
		else:
			mangaList.delete(0, END)
			mangaList.insert(END, "{} already in catalog".format(title_val.get()))


def bookDelete(title_val, isbn_val):
	if checkBothEntries():
		if deleteFromCatalog(title_val, isbn_val):
			mangaList.delete(0, END)
			mangaList.insert(END, "{} deleted from catalog".format(title_val.get()))
		else:
			mangaList.delete(0, END)
			mangaList.insert(END, "{} not in catalog".format(title_val.get()))


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
isbn_Entry= Entry(window, textvariable = isbn_val)
isbn_Entry.grid(row = 0, column = 3)

#scrollbar for list

sb = Scrollbar(window)
sb.grid(row = 1, column = 1)

#listbox

mangaList = Listbox(window, height = 10, width = 25, yscrollcommand = sb.set)
mangaList.grid(row = 1, column = 0)


#connect scrollbar to listbox vertically
sb.config(command=mangaList.yview)


#view all, search, add, update, delete, close buttons

viewALL = Button(window, height = 1, width = 5, text = "View All", command = showAllFromCatalog) 
viewALL.grid(row = 1, column = 4)

search = Button(window, height = 1, width = 5, text = "Search", command = lambda x = title_val, y=isbn_val:bookSearch(x,y)) 
search.grid(row = 2, column = 4)

add_entry = Button(window, height = 1, width = 5, text = "Add", command = lambda x = title_val, y=isbn_val:bookAdd(x,y)) 
add_entry.grid(row = 3, column = 4)

update_entry = Button(window, height = 1, width = 5, text = "Update") 
update_entry.grid(row = 4, column = 4)

delete_entry = Button(window, height = 1, width = 5, text = "Delete", command = lambda x = title_val, y=isbn_val:bookDelete(x,y)) 
delete_entry.grid(row = 5, column = 4)

close = Button(window, height = 1, width = 5, text = "Close") 
close.grid(row = 6, column = 4)

window.mainloop()