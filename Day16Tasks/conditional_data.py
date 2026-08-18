import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

status = np.where(scores > 50, 'Pass', 'Fail')

df = pd.DataFrame({'Score': scores, 'Status': status})
status_counts = df['Status'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    status_counts, 
    labels=status_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#66b3ff', '#ff9999'],
    explode=(0.05, 0)
)

plt.title('Pass vs Fail Distribution', fontsize=14)
plt.tight_layout()
plt.show()
