import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Products")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
