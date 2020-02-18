import sqlite3
# connect to db
# create cursor obj
# 3 write an sql query
# 4 commit changes
# 5 close connection


def create_table(db_name):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS catalog (book_name TEXT, isbn TEXT)")
	conn.commit()
	conn.close()

def insert(db_name, book_name, isbn):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("INSERT INTO catalog VALUES (?,?)",(book_name, isbn))
	conn.commit()
	conn.close()




def view(db_name):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("SELECT * FROM catalog")
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(db_name, book_name, isbn):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("DELETE FROM catalog WHERE book_name =? AND isbn =? ", (book_name, isbn))
	conn.commit()
	conn.close()

def update(db_name, newBookName, book_name, isbn):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("UPDATE catalog SET book_name=? WHERE book_name =? AND isbn =?", (newBookName, book_name, isbn))
	conn.commit()
	conn.close()
	
def search_db(db_name, book_name, isbn):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("SELECT * FROM catalog WHERE book_name =? AND isbn=?", (book_name, isbn))
	rows = cur.fetchall()
	conn.close()
	return rows

