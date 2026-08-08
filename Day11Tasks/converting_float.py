import numpy as np

prices = [10.5, 20.8, 15.3]

prices_array = np.array(prices)
print(f"Original prices (float): {prices_array}")
print(f"Original dtype: {prices_array.dtype}")

integer_prices = prices_array.astype(int)
print(f"\nConverted prices (integer): {integer_prices}")
print(f"New dtype: {integer_prices.dtype}")
