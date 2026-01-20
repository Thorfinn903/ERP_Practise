import sqlite3  # Database library
import csv

# 1. Database se Connect karo (Warehouse ka darwaza kholo)
# Agar 'company.db' nahi hogi, to ye khud bana dega.
conn = sqlite3.connect('company.db')
cursor = conn.cursor()  # Ye humara 'Pen' hai likhne ke liye

print("--- Database Connected ---")

# 2. Table banao (Warehouse mein Shelf lagao)
# SQL Query: Agar table nahi hai to banao
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Employees
               (
                   id
                   INTEGER
                   PRIMARY
                   KEY
                   AUTOINCREMENT,
                   name
                   TEXT,
                   age
                   INTEGER,
                   city
                   TEXT
               )
               ''')

# 3. CSV File kholo (Truck kholo)
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # 4. Loop chalao (Ek-ek packet uthao aur shelf pe rakho)
    for row in reader:
        name = row['Name']
        age = int(row['Age'])  # Database mein number chahiye, string nahi
        city = row['City']

        # INSERT Query (Dhyan de: Humne '?' use kiya hai values ki jagah)
        # Isse 'SQL Injection' hack nahi ho sakta. Ye professional tarika hai.
        cursor.execute('INSERT INTO Employees (name, age, city) VALUES (?, ?, ?)',
                       (name, age, city))

        print(f"Inserted: {name}")

# 5. Save karo (Commit)
# Agar commit nahi kiya, to data save nahi hoga (Bas RAM mein rahega)
conn.commit()

# 6. Connection close karo (Warehouse band karo)
conn.close()

print("\n✅ Sab data Database mein save ho gaya!")