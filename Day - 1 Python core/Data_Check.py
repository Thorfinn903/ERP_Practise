import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Saara data maango
cursor.execute("SELECT * FROM Employees")
rows = cursor.fetchall()

print("--- Database Data ---")
for row in rows:
    print(row) # Output aayega: (1, 'Rahul', 25, 'Delhi')...

conn.close()