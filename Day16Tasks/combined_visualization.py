import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({
    'Product': products,
    'Sales': sales
})

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].plot(df['Product'], df['Sales'], marker='o', color='steelblue', linewidth=2)
axes[0].set_title('Sales Trend (Line Graph)', fontsize=12)
axes[0].set_xlabel('Product')
axes[0].set_ylabel('Sales Volume')
axes[0].grid(True, linestyle='--', alpha=0.6)

axes[1].bar(df['Product'], df['Sales'], color='mediumseagreen', edgecolor='black', width=0.5)
axes[1].set_title('Product Comparison (Bar Chart)', fontsize=12)
axes[1].set_xlabel('Product')
axes[1].set_ylabel('Sales Volume')
axes[1].grid(axis='y', linestyle='--', alpha=0.6)

axes[2].pie(
    df['Sales'], 
    labels=df['Product'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
)
axes[2].set_title('Sales Share (Pie Chart)', fontsize=12)

plt.suptitle('Product Sales Dashboard', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()
