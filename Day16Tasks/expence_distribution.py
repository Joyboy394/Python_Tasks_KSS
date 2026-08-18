import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

df = pd.DataFrame({
    'Category': labels,
    'Expense': expenses
})

plt.figure(figsize=(6, 6))
plt.pie(
    df['Expense'], 
    labels=df['Category'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#ff9999', '#66b3ff', '#99ff99']
)

plt.title('Monthly Expense Distribution', fontsize=14)
plt.tight_layout()
plt.show()

