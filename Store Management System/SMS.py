import csv

products = [
    {'Product_Name': 'Gaming Laptop', 'Price': 65000, 'Stock': 5},
    {'Product_Name': 'Wireless Mouse', 'Price': 800, 'Stock': 0},      # <-- Isko INSERT nahi hona chahiye
    {'Product_Name': 'Mechanical Keyboard', 'Price': 3500, 'Stock': 12},
    {'Product_Name': 'HDMI Cable', 'Price': 450, 'Stock': 0},          # <-- Isko bhi skip karna hai
    {'Product_Name': '24 inch Monitor', 'Price': 12000, 'Stock': 4}
]

with open('product.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Product_Name', 'Price', 'Stock'])
    writer.writeheader()
    writer.writerows(products)

print("✅ 'product.csv' ban gayi!")