a = (10, 20, 30, 40, 50)
print(f"Original tuple: {a}")

b = list(a)
b[2] = 99

print(f"Modified list: {b}")

c = tuple(b)
print(f"New tuple: {c}")
