import sqlite3
# connect to db
# create cursor obj
# 3 write an sql query
# 4 commit changes
# 5 close connection
def create_table():
	conn = sqlite3.connect("lite.db ")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert(item, quantity, price):
	conn = sqlite3.connect("lite.db ")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
	conn.commit()
	conn.close()


create_table()
#insert("Wine Glass", 8, 10)
#insert("Coffee Cup", 10, 5)

def view():
	conn = sqlite3.connect("lite.db ")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(item):
	conn = sqlite3.connect("lite.db ")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item =?", (item,))
	conn.commit()
	conn.close()

def update(quantity, price, item):
	conn = sqlite3.connect("lite.db ")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price = ? WHERE item =?", (quantity, price, item))
	conn.commit()
	conn.close()

