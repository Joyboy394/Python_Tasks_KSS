a = input("Enter a string: ")

unique_chars = ""
for char in a:
    if char not in unique_chars:
        unique_chars += char

print(f"Without duplicates: {unique_chars}")
