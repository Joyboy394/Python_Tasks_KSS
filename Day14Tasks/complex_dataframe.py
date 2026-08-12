import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# 1. Create Status column
df["Status"] = np.where(df["Marks"] < 50, "Fail", "Pass")

# 2. Filter only passed students
passed = df[df["Status"] == "Pass"]

# 3. Average marks of passed students
avg_passed = passed["Marks"].mean()

print(df)
print("\nPassed students:\n", passed)
print("\nAverage marks of passed students:", avg_passed)