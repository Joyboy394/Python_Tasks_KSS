import numpy as np

random_values = np.random.rand(8)
print(f"Random values (0-1): {random_values}")

normalized = random_values * 100
print(f"\nNormalized values (x100): {normalized}")

filtered = normalized[normalized > 50]
print(f"\nValues greater than 50: {filtered}")

sorted_filtered = np.sort(filtered)
print(f"\nSorted filtered values: {sorted_filtered}")
