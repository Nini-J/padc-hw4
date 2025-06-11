from cassandra.cluster import Cluster
from cassandra.query import PreparedStatement
import uuid
import random
from datetime import datetime, timedelta

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('sensor_data')

# Prepare insert statement
stmt = session.prepare("""
    INSERT INTO environmental_readings (
        id, timestamp, location, temperature, humidity, solar_irradiation,
        temp_diff_prev, humidity_diff_prev, solar_irradiation_diff_prev, data_source
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""")

# Generate and insert 10 simulated sensor records
base_temp = 22.0
base_humidity = 50.0
base_irradiation = 150.0

for i in range(10):
    timestamp = datetime.now() - timedelta(minutes=10 * (10 - i))
    temperature = base_temp + random.uniform(-2, 2)
    humidity = base_humidity + random.uniform(-5, 5)
    solar_irradiation = base_irradiation + random.uniform(-20, 20)

    session.execute(stmt, (
        uuid.uuid4(), timestamp, 'Tbilisi',
        temperature, humidity, solar_irradiation,
        round(temperature - base_temp, 2),
        round(humidity - base_humidity, 2),
        round(solar_irradiation - base_irradiation, 2),
        'sensor_01'
    ))

print("✅ Sample sensor data inserted.")
