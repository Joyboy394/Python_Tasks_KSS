import numpy as np

marks = [45, 67, 89, 56, 72]

marks_array = np.array(marks)
print(f"Original marks: {marks_array}")

updated_marks = marks_array + 5
print(f"Updated marks (with 5 grace marks): {updated_marks}")
