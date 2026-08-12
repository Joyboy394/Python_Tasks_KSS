import numpy as np

data = [5, 12, 18, 7, 25, 30]

data_array = np.array(data)
print(f"Original array: {data_array}")

data_array[data_array > 15] = 0

print(f"Updated array (values > 15 replaced with 0): {data_array}")
