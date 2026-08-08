import numpy as np

scores = [50, 60, 70, 80, 90, 100, 110, 120]

scores_array = np.array(scores)
print(f"Original scores: {scores_array}")

split_scores = np.array_split(scores_array, 4)

print("\nScores split across 4 servers:")
for i, chunk in enumerate(split_scores, start=1):
    print(f"Server {i}: {chunk}")
    