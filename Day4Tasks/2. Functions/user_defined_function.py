# User-defined function to add two numbers
def add(a, b):
    return a + b

# Main program
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = add(a, b)   # calling the user-defined function

print("Sum =", sum)
