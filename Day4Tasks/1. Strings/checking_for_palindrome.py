a = input("Enter a string: ")
b = a.lower().replace(" ", "")

if b == b[::-1]:
    print(f"'{a}' is a palindrome")
else:
    print(f"'{a}' is not a palindrome")
