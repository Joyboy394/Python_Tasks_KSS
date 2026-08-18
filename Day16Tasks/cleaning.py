import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

series = pd.Series(data, name="Values")

mean_value = series.mean()  # 187.5
series_cleaned = series.fillna(mean_value)

above_average = series_cleaned[series_cleaned > mean_value]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(series_cleaned.index, series_cleaned.values, marker='o', color='crimson', linewidth=2, label='Cleaned Series')
axes[0].axhline(mean_value, color='gray', linestyle='--', label=f'Mean ({mean_value:.1f})')
axes[0].set_title('Cleaned Data Trend (Line Graph)', fontsize=12)
axes[0].set_xlabel('Index')
axes[0].set_ylabel('Value')
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend()

axes[1].bar(above_average.index.astype(str), above_average.values, color='royalblue', edgecolor='black', width=0.4)
axes[1].set_title('Values > Average (Bar Chart)', fontsize=12)
axes[1].set_xlabel('Original Index')
axes[1].set_ylabel('Value')
axes[1].grid(axis='y', linestyle='--', alpha=0.6)

plt.suptitle('Data Cleaning & Filtering Dashboard', fontsize=15, y=1.02)
plt.tight_layout()
plt.show()
