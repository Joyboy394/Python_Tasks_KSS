from utilities import math_operations
from utilities import string_operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = math_operations.add(num1, num2)
product_result = math_operations.multiply(num1, num2)

print(f"\nSum: {num1} + {num2} = {sum_result}")
print(f"Product: {num1} * {num2} = {product_result}")

text = input("\nEnter a string: ")

upper_text = string_operations.to_uppercase(text)
char_count = string_operations.count_characters(text)

print(f"\nUppercase: {upper_text}")
print(f"Character count: {char_count}")
