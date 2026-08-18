import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    'Student': names,
    'Marks': marks
})

df_filtered = df[df['Marks'] > 50].reset_index(drop=True)

plt.figure(figsize=(7, 5))
plt.bar(df_filtered['Student'], df_filtered['Marks'], color='mediumseagreen', edgecolor='black', width=0.45)

plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.title('Students Scoring Above 50 Marks', fontsize=14)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
