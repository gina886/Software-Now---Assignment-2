import csv
import os

station_temps = {} # to stored tempe data for each station

# process all csv files 
folder = 'temperatures'
for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith('.csv'):
            filepath = os.path.join(root, filename)
            station_name = os.path.basename(filepath).split('_')[0].strip()

            with open(filepath, 'r') as f:# read CSV data
                reader = csv.DictReader(f)
                
                 for row in reader:
                    try:
                        if 'MAX' in filename.upper():
                            temp = float(row['Maximum temperature (Degree C)'])
                        else:  # MIN file
                            temp = float(row['Minimum temperature (Degree C)'])
                        if station_name not in station_temps:
                            station_temps[station_name] = []
                            #add temp to station's record
                        station_temps[station_name].append(temp)
                    except (ValueError, KeyError):
                        continue

# find largest temerature range
max_range = -1
range_stations = []
for station, temps in station_temps.items():
    current_range = max(temps) - min(temps)
    if current_range > max_range:# update recording if find larger range
        max_range = current_range
        range_stations = [station]
    elif current_range == max_range:
        range_stations.append(station)
        
# write results to output file
with open("largest_temp_range_station.txt", "w") as f:
    for s in range_stations:
        f.write(f"{s} (Range: {max_range:.2f}°C)\n")

