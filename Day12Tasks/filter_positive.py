import numpy as np

arr = [-5, 10, 15, -2, 20, 25, 30]

arr_array = np.array(arr)
print(f"Original array: {arr_array}")

positive_even = arr_array[(arr_array > 0) & (arr_array % 2 == 0)]

print(f"Positive even numbers: {positive_even}")
