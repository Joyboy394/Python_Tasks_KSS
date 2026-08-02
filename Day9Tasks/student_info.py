class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")


student1 = Student("Rahul", 101, 85)
student2 = Student("Anita", 102, 90)
student3 = Student("Ravi", 103, 78)

students = [student1, student2, student3]

print("Student Details:")
for student in students:
    student.display()
    