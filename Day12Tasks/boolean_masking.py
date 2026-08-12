import numpy as np

salaries = [25000, 40000, 15000, 50000, 30000]

salaries_array = np.array(salaries)
print(f"Salaries: {salaries_array}")

high_salaries = salaries_array[salaries_array > 30000]
print(f"Salaries above 30000: {high_salaries}")

count = high_salaries.size
print(f"Number of employees earning above 30000: {count}")
