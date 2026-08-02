class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    pass


manager1 = Manager("Rahul", 50000)
manager1.display()
