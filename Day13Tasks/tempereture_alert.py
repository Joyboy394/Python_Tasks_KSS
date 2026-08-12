import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

hot_day_indices = np.where(temps > 30)[0]

hot_day_temps = temps[hot_day_indices]

print("--- Temperature Alert System ---")
print(f"All Recorded Temps:           {temps}")
print(f"Indices with Temps > 30°C:     {hot_day_indices}")
print(f"Temperatures on those days:    {hot_day_temps}")

print("\nDetailed Breakdown:")
for idx in hot_day_indices:
    print(f"Day {idx}: {temps[idx]}°C")
