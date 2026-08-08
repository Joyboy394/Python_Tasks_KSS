import numpy as np

marks = np.array([[78, 85],
                   [90, 88],
                   [67, 72]])

print("Marks matrix:")
print(marks)

second_student_second_subject = marks[1, 1]
print(f"\nSecond student's second subject mark: {second_student_second_subject}")
