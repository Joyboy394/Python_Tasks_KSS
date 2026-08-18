import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({
    'Department': departments,
    'Salary': salaries
})

dept_summary = df.groupby('Department')['Salary'].agg(['mean', 'count']).reset_index()

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

axes[0, 0].plot(df.index, df['Salary'], marker='o', color='teal', linewidth=2)
axes[0, 0].set_title('1. Salary Trend (Line Graph)', fontsize=12)
axes[0, 0].set_xlabel('Employee Index')
axes[0, 0].set_ylabel('Salary ($)')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

axes[0, 1].bar(dept_summary['Department'], dept_summary['mean'], color='darkorange', edgecolor='black', width=0.5)
axes[0, 1].set_title('2. Average Salary by Department (Bar Chart)', fontsize=12)
axes[0, 1].set_xlabel('Department')
axes[0, 1].set_ylabel('Average Salary ($)')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

axes[0, 2].pie(
    dept_summary['count'], 
    labels=dept_summary['Department'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#ff9999', '#66b3ff', '#99ff99']
)
axes[0, 2].set_title('3. Department Distribution (Pie Chart)', fontsize=12)

axes[1, 0].hist(df['Salary'], bins=5, color='mediumpurple', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('4. Salary Distribution (Histogram)', fontsize=12)
axes[1, 0].set_xlabel('Salary Bins ($)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

axes[1, 1].scatter(df.index, df['Salary'], c=pd.Categorical(df['Department']).codes, cmap='tab10', s=100, zorder=3)
axes[1, 1].set_title('5. Index vs Salary (Scatter Plot)', fontsize=12)
axes[1, 1].set_xlabel('Employee Index')
axes[1, 1].set_ylabel('Salary ($)')
axes[1, 1].grid(True, linestyle='--', alpha=0.6)

fig.delaxes(axes[1, 2])

plt.suptitle('Employee Salary Insights Dashboard', fontsize=16, y=0.98)
plt.tight_layout()
plt.show()
