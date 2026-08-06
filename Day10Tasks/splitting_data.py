import numpy as np

data = [5, 10, 15, 20, 25, 30]

data_array = np.array(data)
print(f"Original data: {data_array}")

split_data = np.split(data_array, 3)

print("\nData split across 3 processors:")
for i, chunk in enumerate(split_data, start=1):
    print(f"Processor {i}: {chunk}")
    
