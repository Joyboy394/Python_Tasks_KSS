import numpy as np

sales = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

sales_array = np.array(sales)
print(f"Original array: {sales_array}")

reshaped_sales = sales_array.reshape(4, 3)

print("\nReshaped array (4 months x 3 products):")
print(reshaped_sales)
