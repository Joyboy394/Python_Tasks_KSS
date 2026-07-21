a = input("Enter a string: ")
substring = input("Enter the substring to search for: ")

if substring in a:
    print(f"'{substring}' exists in the string")
else:
    print(f"'{substring}' does not exist in the string")
    