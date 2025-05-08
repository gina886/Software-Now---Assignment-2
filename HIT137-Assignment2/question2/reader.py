import csv
import os
from constants import months


def read_temperature_data(data_dir, start_year=1986, end_year=2005):
    data = []
    for year in range(start_year, end_year + 1):
        filepath = os.path.join(data_dir, f"stations_group_{year}.csv")
        if not os.path.exists(filepath):
            print(f"Warning: File not found - {filepath}")
            continue

        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                monthly_temps = [float(row[m]) for m in months]
                data.append(
                    {
                        "station": row["STATION_NAME"],
                        "year": year,
                        "lat": float(row["LAT"]),
                        "lon": float(row["LON"]),
                        "temps": monthly_temps,
                    }
                )
    return data
