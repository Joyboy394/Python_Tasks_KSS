import pandas as pd
import matplotlib.pyplot as plt

import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "railway_gauges.csv")

df = pd.read_csv(csv_path)

print("--- Top 5 Rows ---")
print(df.head())

print("\n--- Last 5 Rows ---")
print(df.tail())

max_total_row = df.iloc[[df["Total"].idxmax()]]
print("\n--- Row with Maximum Total ---")
print(max_total_row)

df_gauges = df.drop("Total", axis=1)

ax = df_gauges.plot(x="Year", kind="bar", figsize=(15, 6), width=0.8)

plt.title("Gauges - Number of railway tracks installed per year")
plt.xlabel("Year")
plt.ylabel("Total")
plt.xticks(rotation=70)
plt.legend(["Broad Gauge", "Metre Gauge", "Narrow Gauge"])
plt.tight_layout()

plt.savefig("railway_gauges.png")
plt.show()
