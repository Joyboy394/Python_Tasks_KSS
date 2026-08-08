import numpy as np

customer_names = ["Ravi", "Anil", "Sita", "John"]

names_array = np.array(customer_names)
print(f"Original names: {names_array}")

sorted_names = np.sort(names_array)
print(f"Sorted names (alphabetically): {sorted_names}")
