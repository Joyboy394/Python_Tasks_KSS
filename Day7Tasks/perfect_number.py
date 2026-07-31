num = int(input("Enter a number: "))

divisors = []
for i in range(1, num):
    if num % i == 0:
        divisors.append(i)

total = sum(divisors)

print(f"Divisors: {', '.join(str(d) for d in divisors)}")
print(f"Sum = {' + '.join(str(d) for d in divisors)} = {total}")

if total == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")
    