import numpy as np

matrix = np.random.randint(0, 51, size=(3, 3))

print("Random 3x3 matrix:")
print(matrix)

filtered_values = matrix[matrix > 25]

print(f"\nValues greater than 25: {filtered_values}")
