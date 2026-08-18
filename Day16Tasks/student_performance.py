import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    'Student': students,
    'Marks': marks
})

df['Status'] = np.where(df['Marks'] > 50, 'Pass', 'Fail')

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

axes[0, 0].plot(df['Student'], df['Marks'], marker='o', color='purple', linewidth=2)
axes[0, 0].set_title('1. Trend of Marks (Line Graph)')
axes[0, 0].set_xlabel('Student')
axes[0, 0].set_ylabel('Marks')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

axes[0, 1].bar(df['Student'], df['Marks'], color='teal', edgecolor='black', width=0.5)
axes[0, 1].set_title('2. Student vs Marks (Bar Chart)')
axes[0, 1].set_xlabel('Student')
axes[0, 1].set_ylabel('Marks')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

status_counts = df['Status'].value_counts()
axes[0, 2].pie(
    status_counts, 
    labels=status_counts.index, 
    autopct='%1.1f%%', 
    colors=['#66b3ff', '#ff9999'], 
    startangle=90, 
    explode=(0.05, 0)
)
axes[0, 2].set_title('3. Pass vs Fail Distribution (Pie Chart)')

axes[1, 0].hist(df['Marks'], bins=5, color='coral', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('4. Distribution of Marks (Histogram)')
axes[1, 0].set_xlabel('Marks Bin')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

axes[1, 1].scatter(df.index, df['Marks'], color='crimson', s=80, zorder=3)
axes[1, 1].set_title('5. Index vs Marks (Scatter Plot)')
axes[1, 1].set_xlabel('Student Index')
axes[1, 1].set_ylabel('Marks')
axes[1, 1].grid(True, linestyle='--', alpha=0.6)

fig.delaxes(axes[1, 2])

plt.suptitle('Student Performance Dashboard', fontsize=16, y=0.98)
plt.tight_layout()
plt.show()
