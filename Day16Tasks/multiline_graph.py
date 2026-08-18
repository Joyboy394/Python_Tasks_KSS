import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

df = pd.DataFrame(data)

plt.figure(figsize=(7, 5))
plt.plot(df['Month'], df['Store_A'], marker='o', label='Store A', color='royalblue', linewidth=2)
plt.plot(df['Month'], df['Store_B'], marker='s', label='Store B', color='coral', linewidth=2)

plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Volume', fontsize=12)
plt.title('Sales Comparison: Store A vs Store B', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Stores", fontsize=11)

plt.show()
