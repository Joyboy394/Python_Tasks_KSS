import numpy as np

inventory = np.array([[10, 15],
                       [20, 25]])

print("Original Inventory:")
print(inventory)

updated_inventory = inventory + 2

print("\nUpdated Inventory (after new shipment):")
print(updated_inventory)
