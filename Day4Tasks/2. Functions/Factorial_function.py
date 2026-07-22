def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(f"The factorial of 5 is {factorial(5)}")
