import numpy as np

prices = [499, 299, 799, 199, 599]

prices_array = np.array(prices)
print(f"Original prices: {prices_array}")

sorted_prices = np.sort(prices_array)
print(f"Sorted prices (ascending): {sorted_prices}")
