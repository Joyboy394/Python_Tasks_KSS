import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

df = pd.DataFrame({
    'Product': products,
    'Sales': sales
})

plt.figure(figsize=(7, 5))
plt.bar(df['Product'], df['Sales'], color='darkorange', edgecolor='black', width=0.45)

plt.xlabel('Product', fontsize=12)
plt.ylabel('Sales Volume', fontsize=12)
plt.title('Product Sales Overview', fontsize=14)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
