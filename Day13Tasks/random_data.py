import numpy as np

nums = np.random.randint(1, 100, 10)

filtered_sorted = np.sort(nums[nums % 5 == 0])

print("Original:", nums)
print("Divisible by 5 (sorted):", filtered_sorted)
