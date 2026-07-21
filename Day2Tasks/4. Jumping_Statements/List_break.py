a = [4, 8, 15, 16, 23, 42]
target = 1

for num in a:
    if num == target:
        print(f"{target} found in the list!")
        break
else:
    print(f"{target} not found in the list.")