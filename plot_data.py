import matplotlib.pyplot as plt
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('sensor_data')

# Query data
rows = session.execute("SELECT timestamp, temperature, solar_irradiation FROM environmental_readings")

# Prepare lists
timestamps, temperatures, irradiation = [], [], []

for row in rows:
    timestamps.append(row.timestamp)
    temperatures.append(row.temperature)
    irradiation.append(row.solar_irradiation)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(timestamps, temperatures, label='Temperature (°C)', marker='o')
plt.plot(timestamps, irradiation, label='Solar Irradiation (W/m²)', marker='x')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Sensor Readings Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
