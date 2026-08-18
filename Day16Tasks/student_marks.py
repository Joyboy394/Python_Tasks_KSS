import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({
    'Student': names,
    'Marks': marks
})

plt.figure(figsize=(7, 5))
plt.bar(df['Student'], df['Marks'], color='teal', edgecolor='black', width=0.5)

plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.title('Student Marks Distribution', fontsize=14)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
