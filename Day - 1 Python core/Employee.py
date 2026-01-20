import csv

# Ye data hum file mein daal rahe hain
data = [
    {'Name': 'Rohan', 'Dept': 'IT', 'Salary': 45000},
    {'Name': 'Sara', 'Dept': 'HR', 'Salary': 60000},
    {'Name': 'Vikram', 'Dept': 'Sales', 'Salary': 80000},
    {'Name': 'Neha', 'Dept': 'IT', 'Salary': 48000}
]

# File create kar rahe hain
with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Dept', 'Salary'])
    writer.writeheader()
    writer.writerows(data)

print("File 'employees.csv' ban gayi! Ab tera kaam shuru.")