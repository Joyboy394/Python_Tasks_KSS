num = int(input("Enter a number: "))

original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if reversed_num == original_num:
    print(f"{original_num} is a Palindrome number")
else:
    print(f"{original_num} is not a Palindrome number")
    