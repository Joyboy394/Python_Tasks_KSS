import copy

# ----- Shallow copy -----
employees = [[101, "A"], [102, "B"], [103, "C"]]
shallow_copy = employees.copy()   # or: list(employees), or: employees[:]

print("Before modification:")
print(f"employees: {employees}")
print(f"shallow_copy: {shallow_copy}")

employees[0][1] = "Z"   # modifying a NESTED list's element

print("\nAfter changing employees[0][1] = 'Z':")
print(f"employees: {employees}")
print(f"shallow_copy: {shallow_copy}")   # also changed!

print("\n" + "=" * 50 + "\n")

# ----- Deep copy (the fix) -----
employees2 = [[101, "A"], [102, "B"], [103, "C"]]
deep_copy = copy.deepcopy(employees2)

print("Before modification:")
print(f"employees2: {employees2}")
print(f"deep_copy: {deep_copy}")

employees2[0][1] = "Z"

print("\nAfter changing employees2[0][1] = 'Z':")
print(f"employees2: {employees2}")
print(f"deep_copy: {deep_copy}")   # stays unaffected
