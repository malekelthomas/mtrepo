#!/usr/bin/env python3

from sqliteoperations import *
import os

def manga_search(title_val, isbn_val):
	books = search_db("mangadb.db", title_val.get(), isbn_val.get())
	if books != []:
		return True
	else:
		return False

def addManga(title_val, isbn_val):
	if not manga_search(title_val, isbn_val):
		insert("mangadb.db", title_val.get(), isbn_val.get())
		return True
	else:
		return False

def deleteFromCatalog(title_val, isbn_val):
	if manga_search(title_val, isbn_val):
		delete("mangadb.db", title_val.get(), isbn_val.get())

def updateManga(title_val, isbn_val):
	if manga_search(title_val, isbn_val):
		update("mangadb.db", title_val.get(), isbn_val.get())

def initDB():
	if not os.path.exists("mangadb.db"):
		create_table("mangadb.db")