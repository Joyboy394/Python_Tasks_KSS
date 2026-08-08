import numpy as np

temperatures = [28, 31, 35, 27, 40, 22]

temperatures_array = np.array(temperatures)
print(f"Temperatures: {temperatures_array}")

high_temperatures = temperatures_array[temperatures_array > 30]

print(f"Temperatures above 30°C: {high_temperatures}")