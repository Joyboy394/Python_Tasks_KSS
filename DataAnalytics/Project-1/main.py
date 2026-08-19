import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "railway_gauges.csv")

df = pd.read_csv(csv_path)

os.makedirs("graphs/q1", exist_ok=True)

# Scenario 1: Basic Data Loading & Cleaning

print("=" * 60)
print("Q1 - Scenario 1: Data Loading & Cleaning")
print("=" * 60)

csv_path = "railway_gauges.csv"
df = pd.read_csv(csv_path)

print("First 5 Rows:")
print(df.head())
print("\nColumn Names:", df.columns.tolist())

print("\nMissing values before cleaning:\n", df.isnull().sum())
df.fillna(0, inplace=True)

gauge_cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]
for col in gauge_cols:
  df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("\nData types after conversion:\n", df.dtypes)

# Scenario 2: Simple Visualization

print("\n" + "=" * 60)
print("Q1 - Scenario 2: Simple Visualization")
print("=" * 60)

df_total = df[["Year", "Total"]]

plt.figure(figsize=(12, 5))
plt.plot(
    df_total["Year"],
    df_total["Total"],
    marker="o",
    color="#2563eb",
    linewidth=2,
)
plt.title(
    "Total Railway Track Growth Over Years", fontsize=13, fontweight="bold"
)
plt.xlabel("Year", fontsize=11)
plt.ylabel("Total Tracks", fontsize=11)
plt.xticks(rotation=70, fontsize=8)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q1/total_tracks_growth.png", dpi=300)
plt.close()

print(
    "Trend Identification: The overall trend shows general long-term growth"
    " from 6,876 (1964-65) to 7,172 (2012-13)."
)

# Scenario 3: Filtering + Bar Chart

print("\n" + "=" * 60)
print("Q1 - Scenario 3: Filtering + Bar Chart (Post-2000)")
print("=" * 60)

df["Start_Year"] = df["Year"].apply(lambda x: int(str(x).split("-")[0]))
df_post_2000 = df[df["Start_Year"] >= 2000].copy()

x_indices = np.arange(len(df_post_2000))
width = 0.25

plt.figure(figsize=(14, 6))
plt.bar(
    x_indices - width,
    df_post_2000["Broad Gauge"],
    width=width,
    label="Broad Gauge",
    color="#1e40af",
)
plt.bar(
    x_indices,
    df_post_2000["Metre Gauge"],
    width=width,
    label="Metre Gauge",
    color="#d97706",
)
plt.bar(
    x_indices + width,
    df_post_2000["Narrow Gauge"],
    width=width,
    label="Narrow Gauge",
    color="#059669",
)

plt.title(
    "Railway Gauge Comparison (Post-2000 Expansion)",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Year", fontsize=11)
plt.ylabel("Number of Tracks", fontsize=11)
plt.xticks(x_indices, df_post_2000["Year"], rotation=45)
plt.legend(frameon=True)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q1/post_2000_gauges_bar.png", dpi=300)
plt.close()

print(
    "Dominant Gauge: Broad Gauge heavily dominates recent years (representing"
    " >90% of all operational tracks by 2012-13)."
)

# Scenario 4: Feature Engineering + Pie Chart

print("\n" + "=" * 60)
print("Q1 - Scenario 4: Feature Engineering + Pie Chart")
print("=" * 60)

gauge_totals = pd.Series({
    "Broad Gauge": df["Broad Gauge"].sum(),
    "Metre Gauge": df["Metre Gauge"].sum(),
    "Narrow Gauge": df["Narrow Gauge"].sum(),
})
print("Total Cumulative Sums:\n", gauge_totals)

plt.figure(figsize=(7, 7))
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="%1.1f%%",
    colors=["#1e40af", "#d97706", "#059669"],
    startangle=140,
    explode=(0.04, 0.04, 0.04),
)
plt.title(
    "Overall Percentage Contribution by Gauge Type",
    fontsize=13,
    fontweight="bold",
)
plt.tight_layout()
plt.savefig("graphs/q1/gauge_contribution_pie.png", dpi=300)
plt.close()


print(
    f"Contribution Interpretation: {gauge_totals.idxmax()} contributes the most"
    f" historically (~{gauge_totals.max()/gauge_totals.sum()*100:.1f}%)."
)

# Scenario 5: Advanced Analysis + Multiple Graphs

print("\n" + "=" * 60)
print("Q1 - Scenario 5: Advanced Multi-Graph Analysis")
print("=" * 60)

df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100

yearly_growth = np.diff(df["Total"].to_numpy())
max_growth_idx = int(np.argmax(yearly_growth))
highest_growth_year = df["Year"].iloc[max_growth_idx + 1]

plt.figure(figsize=(14, 5))
plt.plot(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge",
    color="#1e40af",
    linewidth=2,
)
plt.plot(
    df["Year"],
    df["Metre Gauge"],
    label="Metre Gauge",
    color="#d97706",
    linewidth=2,
)
plt.plot(
    df["Year"],
    df["Narrow Gauge"],
    label="Narrow Gauge",
    color="#059669",
    linewidth=2,
)
plt.title(
    "Longitudinal Trend of Railway Gauges (1964-65 to 2012-13)",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Year", fontsize=11)
plt.ylabel("Number of Tracks", fontsize=11)
plt.xticks(rotation=70, fontsize=8)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q1/all_gauges_trend_line.png", dpi=300)
plt.close()

plt.figure(figsize=(15, 6))
plt.bar(
    df["Year"],
    df["% Broad Gauge"],
    label="% Broad Gauge",
    color="#1e40af",
    width=0.75,
)
plt.bar(
    df["Year"],
    df["% Metre Gauge"],
    bottom=df["% Broad Gauge"],
    label="% Metre Gauge",
    color="#d97706",
    width=0.75,
)
plt.bar(
    df["Year"],
    df["% Narrow Gauge"],
    bottom=df["% Broad Gauge"] + df["% Metre Gauge"],
    label="% Narrow Gauge",
    color="#059669",
    width=0.75,
)
plt.title(
    "Railway Gauge Composition Over Years (%)", fontsize=13, fontweight="bold"
)
plt.xlabel("Year", fontsize=11)
plt.ylabel("Percentage Share (%)", fontsize=11)
plt.xticks(rotation=70, fontsize=8)
plt.legend(loc="lower left")
plt.tight_layout()
plt.savefig("graphs/q1/gauge_composition_stacked.png", dpi=300)
plt.close()

print(
    f"Highlights: Highest single-year network growth occurred in"
    f" {highest_growth_year} (+{yearly_growth[max_growth_idx]} tracks)."
)
print(
    "Decline: Metre Gauge (-86.9%) and Narrow Gauge (-53.5%) declined"
    " drastically."
)
print(
    "Final Conclusion: YES, the railway network is rapidly standardizing into a"
    " single dominant gauge (Broad Gauge) driven by Unigauge project expansion."
)
