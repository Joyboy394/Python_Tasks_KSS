import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]
deep_copy_classes = copy.deepcopy(classes)

print("Before modification:")
print(f"classes: {classes}")
print(f"deep_copy_classes: {deep_copy_classes}")

# Modify a student count nested two levels deep
classes[0][1][0] = 999   # Math's first student count changed

print("\nAfter changing classes[0][1][0] = 999 (Math student count):")
print(f"classes: {classes}")
print(f"deep_copy_classes: {deep_copy_classes}")   # remains unaffected

print(f"\nAre the outer lists the same object? {classes is deep_copy_classes}")
print(f"Are the 'Math' sub-lists the same object? {classes[0] is deep_copy_classes[0]}")
print(f"Are the student count lists the same object? {classes[0][1] is deep_copy_classes[0][1]}")
