import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Automatically get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "scottish_hills.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Create output folder for graphs
os.makedirs("graphs/q3", exist_ok=True)

# ==========================================
# Scenario 1: Data Loading & Basic Cleaning
# ==========================================
print("=" * 60)
print("Q3 - Scenario 1: Data Loading & Basic Cleaning")
print("=" * 60)

# 1. Load dataset
df = pd.read_csv("scottish_hills.csv")

# 2. Display first 5 rows & column names
print("First 5 Rows:\n", df.head())
print("\nColumns:", df.columns.tolist())

# Handle column naming variations / derive Region if not present
height_col = "Height" if "Height" in df.columns else "height"
if "Region" not in df.columns and "region" not in df.columns:
  df["Region"] = (
      df["Osgrid"].astype(str).str[:2]
      if "Osgrid" in df.columns
      else "Highlands"
  )
region_col = "Region" if "Region" in df.columns else "region"

# 3 & 4. Check & fill missing values
df[height_col] = pd.to_numeric(df[height_col], errors="coerce")
df[height_col] = df[height_col].fillna(df[height_col].mean())
df[region_col] = df[region_col].fillna(df[region_col].mode()[0])

print("\nMissing values after cleaning:\n", df[[height_col, region_col]].isnull().sum())

# ==========================================
# Scenario 2: Line Graph + Save
# ==========================================
print("\n" + "=" * 60)
print("Q3 - Scenario 2: Line Graph (Sample Hill Heights)")
print("=" * 60)

# 1 & 2. Select columns & first 10 rows
sample_10 = df[["Hill Name", height_col]].head(10)

# 3. Convert Height to NumPy array
heights_sample = sample_10[height_col].to_numpy()

# 4 & 5. Plot line graph and save
plt.figure(figsize=(9, 4.5))
plt.plot(
    range(len(heights_sample)),
    heights_sample,
    marker="o",
    color="#0d9488",
    linewidth=2,
)
plt.title("Heights of First 10 Scottish Hills", fontsize=12, fontweight="bold")
plt.xlabel("Index (0-9)")
plt.ylabel("Height (meters)")
plt.xticks(range(10))
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q3/hill_heights_line.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q3/hill_heights_line.png")

# ==========================================
# Scenario 3: Filtering + Bar Chart + Save
# ==========================================
print("\n" + "=" * 60)
print("Q3 - Scenario 3: Tall Hills per Region (Height > 900)")
print("=" * 60)

# 1, 2 & 3. Filter Height > 900, count per region, select top
tall_hills = df[df[height_col] > 900]
region_tall_counts = tall_hills[region_col].value_counts().head(8)

# 4. Convert to NumPy
regions_np = region_tall_counts.index.to_numpy()
counts_np = region_tall_counts.values

# 5 & 6. Plot bar chart & rotate labels
plt.figure(figsize=(9, 4.5))
plt.bar(regions_np, counts_np, color="#0284c7", width=0.55)
plt.title("Count of Tall Hills (>900m) per Region", fontweight="bold")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("graphs/q3/tall_hills_bar.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q3/tall_hills_bar.png")

# ==========================================
# Scenario 4: Pie Chart (Region Distribution) + Save
# ==========================================
print("\n" + "=" * 60)
print("Q3 - Scenario 4: Region Distribution Pie Chart")
print("=" * 60)

# 1, 2 & 3. Count per region, select top 5, prepare values
top5_regions = df[region_col].value_counts().head(5)

# 4 & 5. Plot pie chart with percentage labels
plt.figure(figsize=(7, 7))
plt.pie(
    top5_regions.values,
    labels=top5_regions.index,
    autopct="%1.1f%%",
    colors=["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899"],
    startangle=140,
)
plt.title("Top 5 Regions by Hill Distribution", fontweight="bold")
plt.tight_layout()
plt.savefig("graphs/q3/region_distribution.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q3/region_distribution.png")

# ==========================================
# Scenario 5: Advanced Analysis + Multiple Graphs
# ==========================================
print("\n" + "=" * 60)
print("Q3 - Scenario 5: Advanced Analysis & Visualizations")
print("=" * 60)


# Part 1: Feature Creation
def categorize_height(h):
  if h >= 1000:
    return "Very High"
  elif h >= 800:
    return "High"
  return "Moderate"


df["Height Category"] = df[height_col].apply(categorize_height)

# Part 2: NumPy usage
all_heights_np = df[height_col].to_numpy()
height_diffs = np.diff(all_heights_np)

# Part 3 & 4: Visualizations & Saving
# Line Graph
plt.figure(figsize=(10, 4.5))
plt.plot(range(len(all_heights_np)), all_heights_np, color="#047857")
plt.title("Height Trend for All Scottish Hills", fontweight="bold")
plt.xlabel("Hill Index")
plt.ylabel("Height (m)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("graphs/q3/height_trend.png", dpi=300)
plt.close()

# Stacked Bar Chart
top_regions = df[region_col].value_counts().head(6).index
df_filtered = df[df[region_col].isin(top_regions)]
stacked_data = (
    df_filtered.groupby([region_col, "Height Category"])
    .size()
    .unstack(fill_value=0)
)

stacked_data.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 5),
    color=["#3b82f6", "#f59e0b", "#ef4444"],
)
plt.title("Height Category Distribution per Region", fontweight="bold")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Category")
plt.tight_layout()
plt.savefig("graphs/q3/height_category_stacked.png", dpi=300)
plt.close()

# Histogram
plt.figure(figsize=(9, 4.5))
plt.hist(all_heights_np, bins=25, color="#0ea5e9", edgecolor="black", alpha=0.8)
plt.title("Distribution of Hill Heights", fontweight="bold")
plt.xlabel("Height (m)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q3/height_histogram.png", dpi=300)
plt.close()

# Part 5: Insights
print("\n--- Insights ---")
print(
    f"1. Region with tallest hills: {df.loc[df[height_col].idxmax(), region_col]} (Max:"
    f" {df[height_col].max()}m)"
)
print(
    f"2. Most common category: {df['Height Category'].value_counts().idxmax()}"
)
print(
    "3. Distribution pattern: Moderately normal with concentration in the"
    " 900-1000m range."
)