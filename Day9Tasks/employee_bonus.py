def apply_bonus(func):
    def wrapper(self, *args, **kwargs):
        bonus = self.salary * 0.10
        self.salary += bonus
        print(f"Bonus of {bonus:.2f} added.")
        return func(self, *args, **kwargs)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @apply_bonus
    def display_salary(self):
        print(f"Name: {self.name}, Salary: {self.salary:.2f}")


employee1 = Employee("Rahul", 50000)
employee2 = Employee("Anita", 60000)

employee1.display_salary()
print()
employee2.display_salary()
