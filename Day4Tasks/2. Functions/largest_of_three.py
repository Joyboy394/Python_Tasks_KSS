def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = find_largest(15, 42, 8)
print(f"The largest number is {result}")
