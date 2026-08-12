import numpy as np
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
average_sales = np.mean(sales)
filtered_sales = sales[sales > average_sales]
print(f"Original Sales Data: {sales}")
print(f"Average Sales:       {average_sales:.2f}")
print(f"Sales Above Average: {filtered_sales}")
