import numpy as np

# ----- Using copy() -----
original = np.array([10, 20, 30, 40])
copy_array = original.copy()

print("Before modifying original:")
print(f"Original: {original}")
print(f"Copy: {copy_array}")

original[0] = 999

print("\nAfter modifying original[0] = 999:")
print(f"Original: {original}")
print(f"Copy: {copy_array}")   # unaffected, since copy() makes an independent array

print("\n" + "=" * 50 + "\n")

# ----- Using view() -----
original2 = np.array([10, 20, 30, 40])
view_array = original2.view()

print("Before modifying original2:")
print(f"Original2: {original2}")
print(f"View: {view_array}")

original2[0] = 999

print("\nAfter modifying original2[0] = 999:")
print(f"Original2: {original2}")
print(f"View: {view_array}")   # DOES change, since view() shares the same underlying data
