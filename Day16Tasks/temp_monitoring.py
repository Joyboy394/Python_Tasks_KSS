import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({
    'Day': days,
    'Temperature': temps
})

df['Category'] = np.where(df['Temperature'] > 30, 'High (>30°C)', 'Low/Moderate (<=30°C)')

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

axes[0, 0].plot(df['Day'], df['Temperature'], marker='o', color='crimson', linewidth=2, label='Temp (°C)')
axes[0, 0].axhline(30, color='gray', linestyle='--', alpha=0.7, label='30°C Threshold')
axes[0, 0].set_title('1. Daily Temperature Trend (Line Graph)', fontsize=12)
axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Temperature (°C)')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)
axes[0, 0].legend()

colors_bar = ['darkorange' if t > 30 else 'skyblue' for t in df['Temperature']]
axes[0, 1].bar(df['Day'], df['Temperature'], color=colors_bar, edgecolor='black', width=0.5)
axes[0, 1].set_title('2. Day-Wise Temperature (Bar Chart)', fontsize=12)
axes[0, 1].set_xlabel('Day')
axes[0, 1].set_ylabel('Temperature (°C)')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

cat_counts = df['Category'].value_counts()
axes[0, 2].pie(
    cat_counts, 
    labels=cat_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#ff7f0e', '#1f77b4'],
    explode=(0.05, 0)
)
axes[0, 2].set_title('3. High (>30°C) vs Low/Moderate Proportion', fontsize=12)

axes[1, 0].hist(df['Temperature'], bins=5, color='mediumseagreen', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('4. Temperature Frequency (Histogram)', fontsize=12)
axes[1, 0].set_xlabel('Temperature Range (°C)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

axes[1, 1].scatter(df.index, df['Temperature'], color='darkmagenta', s=100, zorder=3)
axes[1, 1].set_title('5. Day Index vs Temperature (Scatter Plot)', fontsize=12)
axes[1, 1].set_xlabel('Day Index (0=Mon, 6=Sun)')
axes[1, 1].set_ylabel('Temperature (°C)')
axes[1, 1].grid(True, linestyle='--', alpha=0.6)

fig.delaxes(axes[1, 2])

plt.suptitle('Temperature Monitoring System Dashboard', fontsize=16, y=0.98)
plt.tight_layout()
plt.show()
