a = input("Enter a string: ")
frequency = {}
for char in a:
    frequency[char] = frequency.get(char, 0) + 1
for char, count in frequency.items():
    print(f"'{char}': {count}")
    