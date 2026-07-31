num = int(input("Enter a number: "))

original_num = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** 3
    num //= 10

if total == original_num:
    print(f"{original_num} is an Armstrong number")
else:
    print(f"{original_num} is not an Armstrong number")
    