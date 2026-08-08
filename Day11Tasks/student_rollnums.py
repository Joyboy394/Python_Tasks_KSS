import numpy as np

roll_numbers = [101, 102, 103, 104, 105, 106]

roll_numbers_array = np.array(roll_numbers)
print(f"All roll numbers: {roll_numbers_array}")

middle_students = roll_numbers_array[2:5]
print(f"Middle students (index 2 to 4): {middle_students}")
