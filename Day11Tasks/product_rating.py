import numpy as np

ratings = [4, 5, 3, 4, 2]

ratings_array = np.array(ratings)
print(f"Ratings: {ratings_array}")

first_rating = ratings_array[0]
last_rating = ratings_array[-1]

print(f"First rating: {first_rating}")
print(f"Last rating: {last_rating}")
