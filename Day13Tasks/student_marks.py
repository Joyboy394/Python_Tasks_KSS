import numpy as np
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])
total_marks = np.sum(marks, axis=1)
class_average = np.mean(total_marks)
students = np.array(["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"])
above_average_mask = total_marks > class_average
top_students = students[above_average_mask]
top_marks = total_marks[above_average_mask]
print("--- Student Marks Analysis ---")
print(f"Total marks of each student: {total_marks}")
print(f"Class Average:               {class_average:.2f}\n")
print("Students above class average:")
for student, mark in zip(top_students, top_marks):
    print(f"{student}: {mark}")



