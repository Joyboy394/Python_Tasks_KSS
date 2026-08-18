import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

df = pd.DataFrame({
    'Month': months,
    'Sales': sales
})

plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='b', linestyle='-', linewidth=2)

plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Monthly Sales Trend', fontsize=14)
plt.grid(True)
plt.show()
