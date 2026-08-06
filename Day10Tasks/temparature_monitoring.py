import numpy as np

day1 = [30, 32, 31]
day2 = [29, 33, 34]

temperature_array = np.array([day1, day2])

print("Temperature Data:")
print(temperature_array)

total_temperature = temperature_array.sum()
print(f"\nTotal temperature recorded: {total_temperature}")
