import sqlite3
# connect to db
# create cursor obj
# 3 write an sql query
# 4 commit changes
# 5 close connection


def create_table(db_name):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert(db_name, item, quantity, price):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
	conn.commit()
	conn.close()




def view(db_name):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(db_name, item):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item =?", (item,))
	conn.commit()
	conn.close()

def update(db_name, quantity, price, item):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price = ? WHERE item =?", (quantity, price, item))
	conn.commit()
	conn.close()
	
def search_db(db_name, item):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("SELECT * FROM store WHERE item =?", (item,))
	rows = cur.fetchall()
	conn.close()
	return rows

