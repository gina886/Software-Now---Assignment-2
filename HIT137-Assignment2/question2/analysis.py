from collections import defaultdict
from constants import months, seasons


def process_data(data):
    station_stats = defaultdict(
        lambda: {"temps": [], "max": -float("inf"), "min": float("inf")}
    )
    seasonal_temps = defaultdict(lambda: defaultdict(list))

    for record in data:
        station = record["station"]
        for i, temp in enumerate(record["temps"]):
            month = months[i]
            station_stats[station]["temps"].append(temp)
            station_stats[station]["max"] = max(station_stats[station]["max"], temp)
            station_stats[station]["min"] = min(station_stats[station]["min"], temp)

            for season, season_months in seasons.items():
                if month in season_months:
                    seasonal_temps[season][station].append(temp)

    return station_stats, seasonal_temps


def calculate_seasonal_averages(seasonal_temps):
    detailed = defaultdict(dict)
    overall = {}

    for season, station_data in seasonal_temps.items():
        all_temps = []
        for station, temps in station_data.items():
            avg = sum(temps) / len(temps)
            detailed[season][station] = avg
            all_temps.extend(temps)
        overall[season] = sum(all_temps) / len(all_temps) if all_temps else 0

    return overall, detailed


def find_temperature_range_extremes(station_stats):
    max_range = -1
    stations = []
    for station, stats in station_stats.items():
        r = stats["max"] - stats["min"]
        if r > max_range:
            max_range = r
            stations = [station]
        elif r == max_range:
            stations.append(station)
    return stations, max_range


def find_extreme_stations_by_average(station_stats):
    avg_map = {s: sum(v["temps"]) / len(v["temps"]) for s, v in station_stats.items()}
    max_temp = max(avg_map.values())
    min_temp = min(avg_map.values())
    warmest = [s for s, t in avg_map.items() if t == max_temp]
    coolest = [s for s, t in avg_map.items() if t == min_temp]
    return warmest, max_temp, coolest, min_temp
