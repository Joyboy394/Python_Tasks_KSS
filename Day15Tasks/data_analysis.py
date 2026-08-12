import numpy as np
import pandas as pd

# 1. Generate marks using NumPy
np.random.seed(42)  # for reproducible results
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
marks = np.random.randint(30, 100, size=len(names))

print("Generated marks:", marks)

# 2. Convert into Pandas DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# 3. Use conditions to filter passing students (pass mark = 40)
df["Status"] = np.where(df["Marks"] >= 40, "Pass", "Fail")
passed = df[df["Status"] == "Pass"]

# 4. Calculate mean using NumPy
overall_mean = np.mean(df["Marks"])
passed_mean = np.mean(passed["Marks"])

print("\nFull DataFrame:\n", df)

# 5. Use loop to print results
print("\n--- Passing Students ---")
for index, row in passed.iterrows():
    print(f"{row['Name']}: {row['Marks']} marks")

print(f"\nOverall average marks: {overall_mean:.2f}")
print(f"Average marks of passed students: {passed_mean:.2f}")
