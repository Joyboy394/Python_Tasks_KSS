def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

a = [10, 20, 30, 40, 50]
print(f"The sum of {a} is {find_sum(a)}")
