def even_number_generator():
    num = 2
    while True:
        yield num
        num += 2


n = int(input("Enter N: "))

gen = even_number_generator()

print(f"First {n} even numbers:")
for _ in range(n):
    print(next(gen))
    