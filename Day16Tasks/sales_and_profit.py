import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    'Product': products,
    'Sales': sales,
    'Profit': profit
})

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

axes[0, 0].plot(df['Product'], df['Sales'], marker='o', color='darkblue', linewidth=2)
axes[0, 0].set_title('1. Sales Trend (Line Graph)', fontsize=12)
axes[0, 0].set_xlabel('Product')
axes[0, 0].set_ylabel('Sales ($)')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

axes[0, 1].bar(df['Product'], df['Sales'], color='forestgreen', edgecolor='black', width=0.5)
axes[0, 1].set_title('2. Product vs Sales (Bar Chart)', fontsize=12)
axes[0, 1].set_xlabel('Product')
axes[0, 1].set_ylabel('Sales ($)')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

axes[0, 2].pie(
    df['Sales'], 
    labels=df['Product'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
)
axes[0, 2].set_title('3. Sales Contribution (Pie Chart)', fontsize=12)

axes[1, 0].hist(df['Profit'], bins=5, color='sandybrown', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('4. Profit Distribution (Histogram)', fontsize=12)
axes[1, 0].set_xlabel('Profit ($)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

axes[1, 1].scatter(df['Sales'], df['Profit'], color='purple', s=100, zorder=3)
for i, txt in enumerate(df['Product']):
    axes[1, 1].annotate(txt, (df['Sales'][i] + 5, df['Profit'][i] - 1), fontsize=10)
axes[1, 1].set_title('5. Sales vs Profit (Scatter Plot)', fontsize=12)
axes[1, 1].set_xlabel('Sales ($)')
axes[1, 1].set_ylabel('Profit ($)')
axes[1, 1].grid(True, linestyle='--', alpha=0.6)

fig.delaxes(axes[1, 2])

plt.suptitle('Product Sales & Profit Analysis Dashboard', fontsize=16, y=0.98)
plt.tight_layout()
plt.show()
