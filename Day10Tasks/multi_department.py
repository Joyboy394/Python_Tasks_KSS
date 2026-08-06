import numpy as np

branch_a = np.array([[10, 20],
                      [30, 40]])

branch_b = np.array([[5, 15],
                      [25, 35]])

print("Branch A:")
print(branch_a)

print("\nBranch B:")
print(branch_b)

combined_matrix = branch_a + branch_b

print("\nCombined Matrix (Department-wise totals):")
print(combined_matrix)

total_employees = combined_matrix.sum()
print(f"\nTotal employees across all departments: {total_employees}")
