import numpy as np

sales = np.random.randint(100, 501, size=10)

print(f"Simulated 10-day sales: {sales}")

average_sales = sales.mean()
print(f"Average sales: {average_sales:.2f}")
