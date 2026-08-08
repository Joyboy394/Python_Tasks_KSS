import numpy as np

transactions = [1200, 500, 800, 1500]

transactions_array = np.array(transactions)

print(f"Transactions array: {transactions_array}")
print(f"Type of object: {type(transactions_array)}")

is_ndarray = isinstance(transactions_array, np.ndarray)
print(f"Is it a NumPy ndarray? {is_ndarray}")
