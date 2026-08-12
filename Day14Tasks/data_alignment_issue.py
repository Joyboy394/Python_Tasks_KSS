import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

result = S1 + S2
print("Direct addition:\n", result)

result_filled = S1.add(S2, fill_value=0)
print("\nWith fill_value=0:\n", result_filled)