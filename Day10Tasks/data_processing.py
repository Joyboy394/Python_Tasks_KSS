import numpy as np

data = [12, 7, 25, 3, 18, 10]

data_array = np.array(data)
print(f"Original array: {data_array}")

sorted_array = np.sort(data_array)
print(f"Sorted array: {sorted_array}")

part1, part2 = np.split(sorted_array, 2)
print(f"\nPart 1: {part1}")
print(f"Part 2: {part2}")

sum_part1 = part1.sum()
sum_part2 = part2.sum()

print(f"\nSum of Part 1: {sum_part1}")
print(f"Sum of Part 2: {sum_part2}")
