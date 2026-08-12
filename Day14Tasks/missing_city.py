import pandas as pd

cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

# Create a Series using only the requested cities as the index
population = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

print("Population Series:\n", population)

# Identify missing cities
missing = population[population.isna()]
print("\nCities with missing data:", list(missing.index))
