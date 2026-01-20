import csv

data = [
    {'Name': 'Rahul', 'Age': 25, 'City': 'Delhi'},
    {'Name': 'Priya', 'Age': 30, 'City': 'Mumbai'},
    {'Name': 'Amit', 'Age': 22, 'City': 'Surat'}
]

with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Age', 'City'])
    writer.writeheader()
    writer.writerows(data)

print("✅ 'users.csv' ban gayi!")