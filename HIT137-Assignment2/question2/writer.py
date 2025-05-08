def write_average_temperatures(overall, detailed, filepath):
    with open(filepath, "w") as f:
        f.write("Average Temperatures by Season:\n")
        for s, t in overall.items():
            f.write(f"{s}: {t:.2f}°C\n")

        f.write("\nDetailed Averages by Station:\n")
        for s in detailed:
            f.write(f"\n{s}:\n")
            for st, t in detailed[s].items():
                f.write(f"  {st}: {t:.2f}°C\n")


def write_temp_range_stations(stations, range_val, filepath):
    with open(filepath, "w") as f:
        f.write("Station(s) with the largest temperature range:\n")
        for s in stations:
            f.write(f"{s} (Range: {range_val:.2f}°C)\n")


def write_extreme_avg_stations(warmest, warm_avg, coolest, cool_avg, filepath):
    with open(filepath, "w") as f:
        f.write("Warmest Station(s):\n")
        for s in warmest:
            f.write(f"{s} (Average Temp: {warm_avg:.2f}°C)\n")
        f.write("\nCoolest Station(s):\n")
        for s in coolest:
            f.write(f"{s} (Average Temp: {cool_avg:.2f}°C)\n")
