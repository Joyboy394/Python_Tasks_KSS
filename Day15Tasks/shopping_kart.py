# Prices for available items
item_prices = {
    "apple": 30,
    "banana": 10,
    "milk": 45,
    "bread": 25,
    "eggs": 60
}

# 1. Store items in a list (user adds items, possibly with duplicates/typos)
cart = ["apple", "banana", "apple", "milk", "bread", "banana", "cheese"]
print("Original cart:", cart)

# 2. Convert to set to remove duplicates
unique_items = set(cart)
print("Unique items:", unique_items)

# 3. Loop + condition to calculate total cost, with try-except for invalid items
total_cost = 0
valid_items = []
invalid_items = []

for item in unique_items:
    try:
        price = item_prices[item]  # raises KeyError if item not in price list
        total_cost += price
        valid_items.append(item)
    except KeyError:
        invalid_items.append(item)

print("\nValid items billed:", valid_items)
print("Invalid items (not found in price list):", invalid_items)
print("Total cost: ₹", total_cost)
