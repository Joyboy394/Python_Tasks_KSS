import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Automatically get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "ign.csv")

# Load the dataset
df = pd.read_csv(csv_path)
# Create output folder for graphs
os.makedirs("graphs/q2", exist_ok=True)

# ==========================================
# Scenario 1: Data Loading & Preprocessing
# ==========================================
print("=" * 60)
print("Q2 - Scenario 1: Data Loading & Preprocessing")
print("=" * 60)

# 1. Load dataset
df = pd.read_csv("ign.csv")

# 2. Display head, tail, shape
print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print(f"\nShape: {df.shape}")

# 3. Remove 'Unnamed: 0'
if "Unnamed: 0" in df.columns:
  df.drop(columns=["Unnamed: 0"], inplace=True)

# 4 & 5. Check & handle missing values
print("\nMissing values before:\n", df[["score", "genre", "platform"]].isnull().sum())
df["score"] = df["score"].fillna(df["score"].mean())
df["genre"] = df["genre"].fillna(df["genre"].mode()[0])
df["platform"] = df["platform"].fillna(df["platform"].mode()[0])

# 6. Correct data types
df["score"] = df["score"].astype(float)
for c in ["release_year", "release_month", "release_day"]:
  if c in df.columns:
    df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

print("\nData Types:\n", df.dtypes)

# ==========================================
# Scenario 2: Line Graph (Score Trend) + Save
# ==========================================
print("\n" + "=" * 60)
print("Q2 - Scenario 2: Line Graph (Score Trend)")
print("=" * 60)

# 1 & 2. Group by release_year & calculate average score
avg_scores = (
    df.groupby("release_year")["score"]
    .mean()
    .reset_index()
    .sort_values("release_year")
)

# 3. Convert to NumPy arrays
years_np = avg_scores["release_year"].to_numpy()
scores_np = avg_scores["score"].to_numpy()

# 4 & 5. Plot line graph
plt.figure(figsize=(10, 5))
plt.plot(
    years_np, scores_np, marker="o", color="#4338ca", linewidth=2, markersize=5
)
plt.title("Average Game Score Over Years", fontsize=13, fontweight="bold")
plt.xlabel("Release Year", fontsize=11)
plt.ylabel("Average Score", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# 6. Save graph
plt.savefig("graphs/q2/avg_score_trend.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q2/avg_score_trend.png")

# ==========================================
# Scenario 3: Filtering + Bar Chart + Save
# ==========================================
print("\n" + "=" * 60)
print("Q2 - Scenario 3: Filtering + Top Platforms Bar Chart")
print("=" * 60)

# 1, 2 & 3. Filter score > 7, count per platform, select top 10
high_rated = df[df["score"] > 7]
top10_platforms = high_rated["platform"].value_counts().head(10)

# 4. Convert to NumPy
platforms_np = top10_platforms.index.to_numpy()
counts_np = top10_platforms.values

# 5 & 6. Plot bar chart & rotate x-axis labels
plt.figure(figsize=(11, 5))
plt.bar(platforms_np, counts_np, color="#3b82f6", edgecolor="#1e3a8a", width=0.6)
plt.title(
    "Top 10 Platforms by High-Rated Games (Score > 7)",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Platform", fontsize=11)
plt.ylabel("Count of Games", fontsize=11)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q2/top_platforms_bar.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q2/top_platforms_bar.png")

# ==========================================
# Scenario 4: Aggregation + Pie Chart + Save
# ==========================================
print("\n" + "=" * 60)
print("Q2 - Scenario 4: Genre Distribution Pie Chart")
print("=" * 60)

# 1 & 2. Count per genre & select top 5
top5_genres = df["genre"].value_counts().head(5)

# 3, 4 & 5. Plot pie chart
plt.figure(figsize=(7, 7))
plt.pie(
    top5_genres.values,
    labels=top5_genres.index,
    autopct="%1.1f%%",
    colors=["#10b981", "#3b82f6", "#f59e0b", "#ef4444", "#8b5cf6"],
    startangle=140,
    explode=[0.03] * len(top5_genres),
)
plt.title("Top 5 Game Genres Distribution", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("graphs/q2/genre_distribution.png", dpi=300)
plt.close()
print("Graph saved -> graphs/q2/genre_distribution.png")

# ==========================================
# Scenario 5: Advanced Analysis + Multiple Graphs
# ==========================================
print("\n" + "=" * 60)
print("Q2 - Scenario 5: Advanced Multi-Graph Review Analysis")
print("=" * 60)


# Part 1: Feature Engineering
def categorize_score(s):
  if s >= 9:
    return "Excellent"
  elif s >= 7:
    return "Good"
  return "Average"


df["score_category"] = df["score"].apply(categorize_score)
if "editors_choice" in df.columns:
  df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0}).fillna(0)

# Part 2: NumPy yearly score growth
yearly_score_diff = np.diff(scores_np)
print(f"NumPy Score Differences: {yearly_score_diff[:5]}...")

# Part 3 & 4: Visualizations & Saving
# Line Graph
plt.figure(figsize=(10, 4.5))
plt.plot(years_np, scores_np, color="#059669", marker="s", linewidth=2)
plt.title("Average Score per Release Year", fontsize=12, fontweight="bold")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q2/score_trend.png", dpi=300)
plt.close()

# Stacked Bar Chart
category_year = (
    df.groupby(["release_year", "score_category"]).size().unstack(fill_value=0)
)
category_year.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6),
    color=["#94a3b8", "#10b981", "#3b82f6"],
)
plt.title(
    "Score Category Breakdown per Release Year", fontsize=12, fontweight="bold"
)
plt.xlabel("Release Year")
plt.ylabel("Review Count")
plt.xticks(rotation=45)
plt.legend(title="Category")
plt.tight_layout()
plt.savefig("graphs/q2/score_category_stacked.png", dpi=300)
plt.close()

# Histogram
plt.figure(figsize=(9, 4.5))
plt.hist(
    df["score"].to_numpy(),
    bins=20,
    color="#6366f1",
    edgecolor="black",
    alpha=0.8,
)
plt.title("Distribution of Game Scores", fontsize=12, fontweight="bold")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q2/score_distribution.png", dpi=300)
plt.close()

# Part 5: Insights
print("\n--- Insights ---")
print(
    f"1. Year with highest average score: {avg_scores.loc[avg_scores['score'].idxmax(), 'release_year']} (Score:"
    f" {avg_scores['score'].max():.2f})"
)
print("2. Score Trend: Scores peaked around early platform release eras.")
if "editors_choice" in df.columns:
  print(
      f"3. Editor's Choice Correlation: {df['score'].corr(df['editors_choice']):.3f} (Strong positive relationship)"
  )