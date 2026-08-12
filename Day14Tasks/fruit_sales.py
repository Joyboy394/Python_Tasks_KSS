import pandas as pd

S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])

total_per_fruit = S1 + S2
grand_total = total_per_fruit.sum()

print("Total per fruit:\n", total_per_fruit)
print("Grand total:", grand_total)
