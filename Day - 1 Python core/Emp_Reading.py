
import csv

with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    print("🔍 Woh log jinki salary 50k se zyada hai:")

    for row in reader:
        salary = int(row['Salary'])  # String ko Number banaya

        if salary > 50000:
            print(f"-> {row['Name']} (Salary: {salary})")