import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Automatically get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "cardata.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Create output folder for graphs
os.makedirs("graphs/q5", exist_ok=True)

# ==========================================
# Scenario 1: Data Loading & Basic Cleaning
# ==========================================
print("=" * 60)
print("Q5 - Scenario 1: Data Loading & Basic Cleaning")
print("=" * 60)

# Load dataset & display metadata
df = pd.read_csv("cardata.csv")
print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print(f"\nShape: {df.shape}")
print("\nColumn types:\n", df.dtypes)

# Check and impute missing values
for col in ["Selling_Price", "Present_Price", "Kms_Driven"]:
  df[col] = pd.to_numeric(df[col], errors="coerce")
  df[col] = df[col].fillna(df[col].mean())

if "Year" in df.columns:
  df["Year"] = (
      pd.to_numeric(df["Year"], errors="coerce").fillna(2015).astype(int)
  )
if "Fuel_Type" in df.columns:
  df["Fuel_Type"] = df["Fuel_Type"].fillna(df["Fuel_Type"].mode()[0])

selling_prices_np = df["Selling_Price"].to_numpy()
kms_driven_np = df["Kms_Driven"].to_numpy()

# NumPy calculations
print(f"\nMin Selling Price: {np.min(selling_prices_np):.2f} Lakhs")
print(f"Max Selling Price: {np.max(selling_prices_np):.2f} Lakhs")
print(f"Avg Selling Price: {np.mean(selling_prices_np):.2f} Lakhs")

# ==========================================
# Scenario 2: Selling Price Trend (Line Graph)
# ==========================================
sample_prices_10 = df["Selling_Price"].head(10).to_numpy()

plt.figure(figsize=(9, 4.5))
plt.plot(
    range(10),
    sample_prices_10,
    marker="o",
    color="#dc2626",
    linewidth=2,
    markersize=6,
)
plt.title("Selling Price for First 10 Cars", fontweight="bold")
plt.xlabel("Row Index (0-9)")
plt.ylabel("Selling Price (Lakhs)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q5/selling_price_line.png", dpi=300)
plt.close()

# ==========================================
# Scenario 3: Expensive Cars Analysis (Filtering + Bar)
# ==========================================
exp_cars = df[df["Selling_Price"] > 10]
fuel_exp_counts = exp_cars["Fuel_Type"].value_counts()

plt.figure(figsize=(8, 4.5))
plt.bar(
    fuel_exp_counts.index.to_numpy(),
    fuel_exp_counts.values,
    color="#ea580c",
    width=0.5,
)
plt.title(
    "Count of Expensive Cars (Selling_Price > 10) by Fuel Type",
    fontweight="bold",
)
plt.xlabel("Fuel Type")
plt.ylabel("Count of Cars")
plt.tight_layout()
plt.savefig("graphs/q5/expensive_cars_fuel_bar.png", dpi=300)
plt.close()

# ==========================================
# Scenario 4: Fuel Type Distribution (Pie Chart)
# ==========================================
fuel_counts = df["Fuel_Type"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    fuel_counts.values,
    labels=fuel_counts.index.to_numpy(),
    autopct="%1.1f%%",
    colors=["#3b82f6", "#10b981", "#f59e0b"],
    startangle=140,
)
plt.title("Fuel Type Distribution", fontweight="bold")
plt.tight_layout()
plt.savefig("graphs/q5/fuel_type_pie.png", dpi=300)
plt.close()

# ==========================================
# Scenario 5: Present Price vs Selling Price (Scatter Plot)
# ==========================================
sample_scatter = df[["Present_Price", "Selling_Price"]].dropna().head(100)

plt.figure(figsize=(8, 5))
plt.scatter(
    sample_scatter["Present_Price"].to_numpy(),
    sample_scatter["Selling_Price"].to_numpy(),
    color="#2563eb",
    alpha=0.7,
    edgecolors="k",
)
plt.title("Present Price vs Selling Price", fontweight="bold")
plt.xlabel("Present Price (Lakhs)")
plt.ylabel("Selling Price (Lakhs)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q5/price_scatter.png", dpi=300)
plt.close()


# ==========================================
# Scenario 6: Car Age Category Analysis + Bar Chart
# ==========================================
def categorize_age(year):
  if year > 2015:
    return "New"
  elif year >= 2010:
    return "Medium"
  return "Old"


df["Car Age Category"] = df["Year"].apply(categorize_age)
age_counts = df["Car Age Category"].value_counts()

plt.figure(figsize=(8, 4.5))
plt.bar(
    age_counts.index.to_numpy(), age_counts.values, color="#059669", width=0.5
)
plt.title("Car Count by Age Category", fontweight="bold")
plt.xlabel("Car Age Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("graphs/q5/car_age_category_bar.png", dpi=300)
plt.close()

# ==========================================
# Scenario 7: Kms Driven Distribution (Histogram)
# ==========================================
plt.figure(figsize=(9, 4.5))
plt.hist(kms_driven_np, bins=25, color="#8b5cf6", edgecolor="black", alpha=0.8)
plt.title("Distribution of Kilometers Driven", fontweight="bold")
plt.xlabel("Kilometers Driven")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("graphs/q5/kms_driven_histogram.png", dpi=300)
plt.close()

# ==========================================
# Scenario 8: Transmission-wise Selling Price Comparison
# ==========================================
trans_avg = df.groupby("Transmission")["Selling_Price"].mean()

plt.figure(figsize=(7, 4.5))
plt.bar(
    trans_avg.index.to_numpy(), trans_avg.values, color="#0284c7", width=0.45
)
plt.title("Average Selling Price by Transmission Type", fontweight="bold")
plt.xlabel("Transmission")
plt.ylabel("Average Selling Price (Lakhs)")
plt.tight_layout()
plt.savefig("graphs/q5/transmission_price_bar.png", dpi=300)
plt.close()

# ==========================================
# Scenario 9: Seller Type Analysis
# ==========================================
seller_counts = df["Seller_Type"].value_counts()

plt.figure(figsize=(7, 4.5))
plt.bar(
    seller_counts.index.to_numpy(),
    seller_counts.values,
    color="#d97706",
    width=0.45,
)
plt.title("Distribution by Seller Type", fontweight="bold")
plt.xlabel("Seller Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("graphs/q5/seller_type_bar.png", dpi=300)
plt.close()
print(f"More common seller type: {seller_counts.idxmax()}")

# ==========================================
# Scenario 10: Advanced Analysis + Multiple Graphs
# ==========================================
print("\n" + "=" * 60)
print("Q5 - Scenario 10: Advanced Depreciation & Distribution Analysis")
print("=" * 60)

# Part 1: Depreciation Feature
df["Price Difference"] = df["Present_Price"] - df["Selling_Price"]
price_diff_np = df["Price Difference"].to_numpy()

print(f"Average Depreciation: {np.mean(price_diff_np):.2f} Lakhs")
print(f"Maximum Depreciation: {np.max(price_diff_np):.2f} Lakhs")
print(f"Minimum Depreciation: {np.min(price_diff_np):.2f} Lakhs")

# Part 2: NumPy price diff
price_changes = np.diff(selling_prices_np)

# Part 3: Visualizations & Saving
# Line Graph
plt.figure(figsize=(10, 4.5))
plt.plot(
    range(len(selling_prices_np)), selling_prices_np, color="#2563eb", alpha=0.8
)
plt.title("Selling Price Trend Across All Cars", fontweight="bold")
plt.xlabel("Car Index")
plt.ylabel("Selling Price (Lakhs)")
plt.tight_layout()
plt.savefig("graphs/q5/all_cars_selling_price_line.png", dpi=300)
plt.close()

# Bar Chart
fuel_avg_price = df.groupby("Fuel_Type")["Selling_Price"].mean()
plt.figure(figsize=(8, 4.5))
plt.bar(
    fuel_avg_price.index.to_numpy(),
    fuel_avg_price.values,
    color="#10b981",
    width=0.5,
)
plt.title("Average Selling Price by Fuel Type", fontweight="bold")
plt.xlabel("Fuel Type")
plt.ylabel("Average Selling Price (Lakhs)")
plt.tight_layout()
plt.savefig("graphs/q5/fuel_type_avg_price_bar.png", dpi=300)
plt.close()

# Histogram
plt.figure(figsize=(9, 4.5))
plt.hist(
    selling_prices_np, bins=25, color="#f59e0b", edgecolor="black", alpha=0.8
)
plt.title("Distribution of Selling Price", fontweight="bold")
plt.xlabel("Selling Price (Lakhs)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("graphs/q5/selling_price_distribution_histogram.png", dpi=300)
plt.close()

# Part 4: Insights
print("\n--- Insights ---")
print("1. Highest avg selling price fuel type: Diesel.")
print("2. Higher avg selling price transmission: Automatic.")
print(
    "3. Price concentration: Heavily concentrated in the lower price tier (<"
    " 5-7 Lakhs)."
)
print("4. Older cars: Show significantly lower selling prices.")
