import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Automatically get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "kc_house_data.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Create output folder for graphs
os.makedirs("graphs/q4", exist_ok=True)

# ==========================================
# Scenario 1: Data Loading & Basic Cleaning
# ==========================================
print("=" * 60)
print("Q4 - Scenario 1: Data Loading & Basic Cleaning")
print("=" * 60)

# 1. Load dataset
df = pd.read_csv("kc_house_data.csv")

# 2. Display head & columns
print("First 5 Rows:\n", df.head())
print("\nColumns:", df.columns.tolist())

# 3, 4 & 5. Check, fill missing values & convert to numeric
num_cols = ["bedrooms", "bathrooms", "sqft_living", "price"]
for c in num_cols:
  df[c] = pd.to_numeric(df[c], errors="coerce")

df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].mode()[0])
df["bathrooms"] = df["bathrooms"].fillna(df["bathrooms"].mean())
df["sqft_living"] = df["sqft_living"].fillna(df["sqft_living"].mean())
df["price"] = df["price"].fillna(df["price"].mean())

print("\nMissing values after cleaning:\n", df[num_cols].isnull().sum())

# ==========================================
# Scenario 2: Line Graph + Save
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 2: Line Graph (First 10 House Prices)")
print("=" * 60)

# 1, 2 & 3. Select columns, first 10 rows, convert to NumPy
sample_prices = df["price"].head(10).to_numpy()

# 4, 5 & 6. Plot line graph & save
plt.figure(figsize=(9, 4.5))
plt.plot(
    range(10),
    sample_prices,
    marker="o",
    color="#2563eb",
    linewidth=2,
    markersize=6,
)
plt.title("House Prices for First 10 Records", fontsize=12, fontweight="bold")
plt.xlabel("Index (0-9)")
plt.ylabel("Price ($)")
plt.xticks(range(10))
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q4/house_prices_line.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q4/house_prices_line.png")

# ==========================================
# Scenario 3: Filtering + Bar Chart + Save
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 3: Expensive Houses Bar Chart (Price > 1,000,000)")
print("=" * 60)

# 1, 2 & 3. Filter price > 1000000, count by bedrooms, select top
exp_houses = df[df["price"] > 1_000_000]
bed_counts = exp_houses["bedrooms"].value_counts().head(6)

# 4. Convert to NumPy
beds_np = bed_counts.index.astype(str).to_numpy()
counts_np = bed_counts.values

# 5, 6 & 7. Plot bar chart and save
plt.figure(figsize=(9, 4.5))
plt.bar(beds_np, counts_np, color="#7c3aed", width=0.55)
plt.title(
    "Count of Expensive Houses (> $1,000,000) by Bedroom Category",
    fontweight="bold",
)
plt.xlabel("Bedrooms")
plt.ylabel("Count of Houses")
plt.tight_layout()
plt.savefig("graphs/q4/expensive_houses_bar.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q4/expensive_houses_bar.png")

# ==========================================
# Scenario 4: Pie Chart (Bedroom Distribution) + Save
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 4: Bedroom Distribution Pie Chart")
print("=" * 60)

# 1, 2 & 3. Count by bedrooms, select top 5, prepare labels
top5_beds = df["bedrooms"].value_counts().head(5)

# 4, 5 & 6. Plot pie chart and save
plt.figure(figsize=(7, 7))
plt.pie(
    top5_beds.values,
    labels=[f"{int(b)} Beds" for b in top5_beds.index],
    autopct="%1.1f%%",
    colors=["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6"],
    startangle=140,
)
plt.title("Top 5 Bedroom Categories Distribution", fontweight="bold")
plt.tight_layout()
plt.savefig("graphs/q4/bedroom_distribution.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q4/bedroom_distribution.png")

# ==========================================
# Scenario 5: Advanced Analysis + Multiple Graphs
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 5: Advanced House Price Analysis")
print("=" * 60)


# Part 1: Feature Creation
def categorize_price(p):
  if p >= 1_000_000:
    return "Luxury"
  elif p >= 500_000:
    return "Mid Range"
  return "Affordable"


df["Price Category"] = df["price"].apply(categorize_price)

# Part 2: NumPy Usage
prices_np = df["price"].to_numpy()
price_diffs = np.diff(prices_np)

# Part 3 & 4: Visualizations & Saving
# Line Graph
plt.figure(figsize=(10, 4.5))
plt.plot(range(len(prices_np)), prices_np, color="#475569", alpha=0.7)
plt.title("Price Trend for All Houses", fontweight="bold")
plt.xlabel("House Index")
plt.ylabel("Price ($)")
plt.tight_layout()
plt.savefig("graphs/q4/price_trend.png", dpi=300)
plt.close()

# Stacked Bar Chart
top_beds_list = df["bedrooms"].value_counts().head(5).index
filtered_df = df[df["bedrooms"].isin(top_beds_list)]
stacked_price = (
    filtered_df.groupby(["bedrooms", "Price Category"])
    .size()
    .unstack(fill_value=0)
)

stacked_price.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 5),
    color=["#10b981", "#3b82f6", "#f59e0b"],
)
plt.title("Price Category Count per Bedroom Category", fontweight="bold")
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.legend(title="Price Category")
plt.tight_layout()
plt.savefig("graphs/q4/price_category_stacked.png", dpi=300)
plt.close()

# Histogram
plt.figure(figsize=(9, 4.5))
plt.hist(
    prices_np[prices_np < 3_000_000],
    bins=30,
    color="#059669",
    edgecolor="black",
    alpha=0.8,
)
plt.title("Distribution of House Prices (Up to $3M)", fontweight="bold")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q4/price_histogram.png", dpi=300)
plt.close()

# Part 5: Insights
print("\n--- Insights ---")
print(
    "1. Most expensive houses bedroom category: 4 bedrooms (followed by 3 & 5"
    " bedrooms)."
)
print(
    f"2. Most common price category: {df['Price Category'].value_counts().idxmax()} ({df['Price Category'].value_counts().max()} houses)."
)
print(
    "3. Price distribution pattern: Strongly Right-skewed and concentrated in"
    " the lower/affordable tier (< $500k)."
)