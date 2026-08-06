import numpy as np

store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])

print(f"Store A sales: {store_a}")
print(f"Store B sales: {store_b}")

sales_difference = store_a - store_b
print(f"\nDaily sales difference (Store A - Store B): {sales_difference}")
