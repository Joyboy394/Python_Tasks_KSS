import numpy as np

image = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Original 2D image data:")
print(image)

flattened_image = image.flatten()

print(f"\nFlattened 1-D array: {flattened_image}")
