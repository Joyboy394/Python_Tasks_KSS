class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def display(self):
        print(f"Name: {self.name}, Staff ID: {self.staff_id}")


class Professor(Staff):
    def __init__(self, name, staff_id, department):
        super().__init__(name, staff_id)
        self.department = department

    def display(self):
        super().display()
        print(f"Role: Professor, Department: {self.department}")


class LabAssistant(Staff):
    def __init__(self, name, staff_id, lab_name):
        super().__init__(name, staff_id)
        self.lab_name = lab_name

    def display(self):
        super().display()
        print(f"Role: Lab Assistant, Lab: {self.lab_name}")


class Administrator(Staff):
    def __init__(self, name, staff_id, office):
        super().__init__(name, staff_id)
        self.office = office

    def display(self):
        super().display()
        print(f"Role: Administrator, Office: {self.office}")


professor1 = Professor("Dr. Sharma", 201, "Computer Science")
lab_assistant1 = LabAssistant("Rakesh", 202, "Physics Lab")
administrator1 = Administrator("Meena", 203, "Registrar Office")

staff_members = [professor1, lab_assistant1, administrator1]

print("University Staff Details:")
for staff in staff_members:
    staff.display()
    print()
    