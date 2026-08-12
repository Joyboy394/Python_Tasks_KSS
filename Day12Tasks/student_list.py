marks = [50, 60, 70, 80]
backup = marks

print("Before modification:")
print(f"marks: {marks}")
print(f"backup: {backup}")

marks[0] = 999

print("\nAfter modifying marks[0] = 999:")
print(f"marks: {marks}")
print(f"backup: {backup}")

print(f"\nAre marks and backup the same object? {marks is backup}")
print(f"marks id: {id(marks)}")
print(f"backup id: {id(backup)}")
