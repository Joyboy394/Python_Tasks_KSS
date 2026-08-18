import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({
    'Month': months,
    'Sales': sales
})

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

axes[0, 0].plot(df['Month'], df['Sales'], marker='o', color='navy', linewidth=2)
axes[0, 0].set_title('1. Sales Trend (Line Graph)', fontsize=12)
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

axes[0, 1].bar(df['Month'], df['Sales'], color='mediumseagreen', edgecolor='black', width=0.5)
axes[0, 1].set_title('2. Month-Wise Comparison (Bar Chart)', fontsize=12)
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Sales')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

axes[0, 2].pie(
    df['Sales'], 
    labels=df['Month'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0', '#ffb3e6']
)
axes[0, 2].set_title('3. Monthly Contribution (Pie Chart)', fontsize=12)

axes[1, 0].hist(df['Sales'], bins=5, color='coral', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('4. Frequency of Sales (Histogram)', fontsize=12)
axes[1, 0].set_xlabel('Sales Value Bins')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

axes[1, 1].scatter(df.index, df['Sales'], color='darkred', s=80, zorder=3)
axes[1, 1].set_title('5. Month Index vs Sales (Scatter Plot)', fontsize=12)
axes[1, 1].set_xlabel('Month Index')
axes[1, 1].set_ylabel('Sales')
axes[1, 1].grid(True, linestyle='--', alpha=0.6)

fig.delaxes(axes[1, 2])

plt.suptitle('Monthly Sales Analysis Dashboard', fontsize=16, y=0.98)
plt.tight_layout()
plt.show()
