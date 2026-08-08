import numpy as np

sales = [200, 300, 150, 400]

sales_array = np.array(sales)
print(f"Sales array: {sales_array}")

print("\nDaily sales:")
for sale in sales_array:
    print(sale)
    