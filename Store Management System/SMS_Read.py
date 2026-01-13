import sqlite3
import csv


conn = sqlite3.connect('store.db')
cursor = conn.cursor()

print("--- Database Connected ---")

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Products
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Product_Name TEXT,
        Price INTEGER,
        Stock INTEGER NOT NULL
    )
    '''
)

with open('product.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        product_name = row['Product_Name']
        price = int(row['Price'])
        stock = int(row['Stock'])

        if stock > 0:
            cursor.execute(
                'INSERT INTO Products (Product_Name, Price, Stock) VALUES (?, ?, ?)',
                (product_name, price, stock)
            )
            print(f"Inserted: {product_name}")

        else:
            print(f"Skipped (Out of Stock): {product_name}")

conn.commit()

conn.close()

print("Data Uploaded Successfully!")


