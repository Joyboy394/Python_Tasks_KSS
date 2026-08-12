import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = values.mean()
std = values.std()

# Keep only values within 2 standard deviations of the mean
filtered = values[np.abs(values - mean) <= 2 * std]

print("Mean:", mean)
print("Std Dev:", std)
print("Filtered values:", filtered)
