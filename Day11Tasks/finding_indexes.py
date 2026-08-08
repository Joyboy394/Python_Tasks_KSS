import numpy as np

defect_codes = [2, 4, 1, 4, 3, 4, 5]

defect_codes_array = np.array(defect_codes)
print(f"Defect codes: {defect_codes_array}")

indexes = np.where(defect_codes_array == 4)

print(f"Indexes where value = 4: {indexes[0]}")
