import random

numbers = [random.randint(1, 50) for _ in range(10)]
print("Generated numbers:", numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)

unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)
print("Number of duplicates removed:", len(numbers) - len(unique_numbers))
