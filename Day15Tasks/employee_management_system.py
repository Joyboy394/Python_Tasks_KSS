class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}"


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.employees = {}   # emp_id -> Employee object
        self.filename = filename

    def add_employee(self, emp_id, name, salary_input):
        try:
            salary = float(salary_input)
            if salary < 0:
                raise ValueError("Salary cannot be negative")
        except ValueError as e:
            print(f"Invalid salary '{salary_input}': {e}. Employee not added.")
            return

        self.employees[emp_id] = Employee(emp_id, name, salary)
        print(f"Added employee {name} (ID: {emp_id})")

    def display_all(self):
        if not self.employees:
            print("No employees to display.")
            return
        print("\n--- Employee List ---")
        for emp_id, emp in self.employees.items():
            print(emp)

    def save_to_file(self):
        try:
            with open(self.filename, "w") as f:
                for emp in self.employees.values():
                    f.write(f"{emp.emp_id},{emp.name},{emp.salary}\n")
            print(f"\nData saved to {self.filename}")
        except IOError as e:
            print(f"Error saving file: {e}")


# --- Demo usage ---
manager = EmployeeManager()

# Sample data, including one invalid salary to demonstrate exception handling
raw_data = [
    (101, "Alice", "50000"),
    (102, "Bob", "abc"),        # invalid salary
    (103, "Charlie", "-2000"),  # negative salary
    (104, "David", "62000.50")
]

for emp_id, name, salary in raw_data:
    manager.add_employee(emp_id, name, salary)

manager.display_all()
manager.save_to_file()
