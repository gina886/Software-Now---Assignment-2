from reader import read_temperature_data
from analysis import (
    process_data,
    calculate_seasonal_averages,
    find_temperature_range_extremes,
    find_extreme_stations_by_average,
)
from writer import (
    write_average_temperatures,
    write_temp_range_stations,
    write_extreme_avg_stations,
)
import os

DATA_DIR = DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "temperature_data"
)
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = read_temperature_data(DATA_DIR)
station_stats, seasonal_temps = process_data(data)

# Calculation of seasonal temparature
overall_avg, detailed_avg = calculate_seasonal_averages(seasonal_temps)
write_average_temperatures(
    overall_avg, detailed_avg, os.path.join(OUTPUT_DIR, "average_temp.txt")
)

# Finding extreme temperature range
range_stations, temp_range = find_temperature_range_extremes(station_stats)
write_temp_range_stations(
    range_stations,
    temp_range,
    os.path.join(OUTPUT_DIR, "largest_temp_range_station.txt"),
)

# Finding average extreme of the stations
warmest, warm_avg, coolest, cool_avg = find_extreme_stations_by_average(station_stats)
write_extreme_avg_stations(
    warmest,
    warm_avg,
    coolest,
    cool_avg,
    os.path.join(OUTPUT_DIR, "warmest_and_coolest_station.txt"),
)

print("✅ Analysis complete. Results saved in 'output' folder.")
