import numpy as np

sensor1 = np.array([10, 20, 30])
sensor2 = np.array([40, 50, 60])

print(f"Sensor 1 readings: {sensor1}")
print(f"Sensor 2 readings: {sensor2}")

combined_readings = np.concatenate((sensor1, sensor2))
print(f"\nCombined readings: {combined_readings}")
