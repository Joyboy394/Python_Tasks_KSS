def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

num = 123
print(f"The sum of digits of {num} is {sum_of_digits(num)}")
