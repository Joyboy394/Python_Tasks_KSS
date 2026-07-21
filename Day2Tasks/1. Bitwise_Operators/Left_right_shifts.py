num = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))

left_shift = num << shift
right_shift = num >> shift

print(f"{num} left shifted by {shift} is {left_shift}")
print(f"{num} right shifted by {shift} is {right_shift}")
