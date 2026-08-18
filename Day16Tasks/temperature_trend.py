import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

temp_series = pd.Series(temps, name="Temperature")

plt.figure(figsize=(7, 4.5))
plt.plot(temp_series, marker='o', color='crimson', linestyle='-', linewidth=2)

plt.title('Daily Temperature Trend', fontsize=14)
plt.xlabel('Day Index', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
