data = [[1, 2, 3], [4, 5], [6]]

# Step 1: Flatten the nested list using list comprehension
flattened = [num for sublist in data for num in sublist]

print(f"Original nested data: {data}")
print(f"Flattened list: {flattened}")

# Step 2: Squares of only even numbers, from the flattened list
even_squares = [num ** 2 for num in flattened if num % 2 == 0]

print(f"Squares of even numbers: {even_squares}")
