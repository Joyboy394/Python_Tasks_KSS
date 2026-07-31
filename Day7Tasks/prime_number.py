num = int(input("Enter a number: "))

factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print(f"Factors = {', '.join(str(f) for f in factors)}")

if len(factors) == 2:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")
    