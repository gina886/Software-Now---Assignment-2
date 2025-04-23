import csv
import os

station_temps = {}

# open the files
folder = 'temperatures'
for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith('.csv'):
            filepath = os.path.join(root, filename)

            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                station_name = os.path.basename(filepath).split('_')[0].strip()

                for row in reader:
                    try:
                        temp = float(row['Maximum temperature (Degree C)']) if 'MAX' in filename else float(row['Minimum temperature (Degree C)'])
                        if station_name not in station_temps:
                            station_temps[station_name] = []
                        station_temps[station_name].append(temp)
                    except:
                        pass
# counting the avg_temps
station_avg = {}
for station, temps in station_temps.items():
    station_avg[station] = sum(temps) / len(temps)

max_avg = max(station_avg.values())
min_avg = min(station_avg.values())

warmest = [s for s, avg in station_avg.items() if avg == max_avg]
coolest = [s for s, avg in station_avg.items() if avg == min_avg]

# input the data to files
with open("warmest_and_coolest_station.txt", "w") as f:
    f.write("Warmest Station(s):\n")
    for s in warmest:
        f.write(f"{s} (Avg: {max_avg:.2f}°C)\n")
    f.write("\nCoolest Station(s):\n")
    for s in coolest:
        f.write(f"{s} (Avg: {min_avg:.2f}°C)\n")
