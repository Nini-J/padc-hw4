-- Create keyspace
CREATE KEYSPACE IF NOT EXISTS sensor_data 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

-- Use the keyspace
USE sensor_data;

-- Create table
CREATE TABLE IF NOT EXISTS environmental_readings (
    id UUID PRIMARY KEY,
    timestamp timestamp,
    location text,
    temperature float,
    humidity float,
    solar_irradiation float,
    temp_diff_prev float,
    humidity_diff_prev float,
    solar_irradiation_diff_prev float,
    data_source text
);
