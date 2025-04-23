import csv
import os
from datetime import datetime

# Seasonal division by month
SEASONS = {
    'Autumn': [3, 4, 5],
    'Winter': [6, 7, 8],
    'Spring': [9, 10, 11],
    'Summer': [12, 1, 2]
}

def get_season(month):
    for season, months in SEASONS.items():
        if month in months:
            return season # return the season according to the months
    return None

# stored the data of temperature accoding to the seasonal
season_temp = {'Summer': [], 'Autumn': [], 'Winter': [], 'Spring': []}

# open the file
folder = 'temperatures'
for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith('.csv'):
            filepath = os.path.join(root, filename)
            
            #reading the CSV file
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                station_name = os.path.basename(filepath).split('_')[0].strip()

                for row in reader:
                    try:
                        year = int(row['Year'])
                        month = int(row['Month'])
                        day = int(row['Day'])
                        date_obj = datetime(year, month, day)

                        # get the data of temperature
                        if 'MAX' in filepath.upper():
                            temp = float(row['Maximum temperature (Degree C)'])
                        elif 'MIN' in filepath.upper():
                            temp = float(row['Minimum temperature (Degree C)'])
                        else:
                            continue  

                        # Classified by season
                        season = get_season(month)
                        if season:
                            season_temp[season].append(temp)

                    except(ValueError, KeyError):
                        continue
                    
# Calculate and output the average temperature of each season
with open("average_temp.txt", "w") as f:
    for season, temps in season_temp.items():
        if temps:
            avg = sum(temps) / len(temps)
            f.write(f"{season}: {avg:.2f}°C\n")
