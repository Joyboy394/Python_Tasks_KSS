students = {
    "Alex": 85,
    "Sam": 92,
    "Riya": 78
}

top_student = max(students, key=students.get)
top_marks = students[top_student]

print(f"Top student: {top_student} with {top_marks} marks")
