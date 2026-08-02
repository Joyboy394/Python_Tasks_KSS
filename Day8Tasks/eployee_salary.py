def display_employees():
    print("Employee Details:")
    for name, salary in employees:
        print(f"{name} : {salary}")


def find_highest_salary():
    highest = employees[0]
    for employee in employees:
        if employee[1] > highest[1]:
            highest = employee

    print(f"\nHighest Paid Employee: {highest[0]} with salary {highest[1]}")


def append_employee():
    name = input("\nEnter new employee name: ")

    try:
        salary = int(input("Enter salary: "))
    except ValueError:
        print("Invalid salary! Please enter a numeric value.")
        return

    with open("employees.txt", "a") as file:
        file.write(f"{name} {salary}\n")

    employees.append((name, salary))
    print("New employee record added successfully.")


try:
    with open("employees.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("employees.txt not found. Please make sure the file exists in the same folder as this program.")
    lines = []

employees = []
for line in lines:
    line = line.strip()
    if line == "":
        continue
    name, salary = line.split()
    employees.append((name, int(salary)))

if employees:
    display_employees()
    find_highest_salary()
else:
    print("No employee records found.")

append_employee()
