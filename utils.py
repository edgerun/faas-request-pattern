import csv
import datetime
import os
import sys
import time

from dateutil.parser import parse
import pandas as pd
import mpu

def timestamp_to_delta_time(df):
    i = 0
    delta_times = []
    timestamps = df['timestamp'].values
    for t in timestamps:
        if i == 0:
            delta_times.append(0)
        else:
            delta_times.append(timestamps[i] - timestamps[i-1])
        i = i + 1
    return delta_times

def saveCSV(cols, data, path):
    with open(path, 'w') as f:
        write = csv.writer(f)
        write.writerow(cols)
        write.writerows(data)

def distance(point1, point2):
    return mpu.haversine_distance(point1, point2)

def get_nearest_cell_tower(date, passengers, lat, lon, df):
    minCell = min(df, key=lambda p: distance((lat, lon), (p[3], p[2])))
    return [date, passengers, minCell[1], minCell[5]]

# returns [max_lat, min_lat, max_lon, min_lon]
def get_max_bounds_trips(df):
    max_lat = df["pickup_latitude"].max()
    min_lat = df["pickup_latitude"].min()
    max_lon = df["pickup_longitude"].max()
    min_lon = df["pickup_longitude"].min()
    return [max_lat, min_lat, max_lon, min_lon]

# returns [max_lat, min_lat, max_lon, min_lon]
def get_max_bounds_topology(df):
    max_lat = df["lat"].max()
    min_lat = df["lat"].min()
    max_lon = df["lon"].max()
    min_lon = df["lon"].min()
    return [max_lat, min_lat, max_lon, min_lon]

def load_Topology(path):
    col_list = ['radio', 'cell', 'lon', 'lat', 'distances', 'cloudlet']
    print("load topology dataset...")
    df = pd.read_csv(path,
                     skipinitialspace=True, usecols=col_list)
    return df

def load_Requests(path):
    col_list = ['timestamp', 'requests', 'cell']
    df = pd.read_csv(path,
                     skipinitialspace=True, usecols=col_list)
    return df

def load_Trips(path):
    col_list = ['pickup_datetime', 'passenger_count', 'pickup_longitude', 'pickup_latitude']
    print("load trips dataset...")
    df = pd.read_csv(path,
                     skipinitialspace=True, usecols=col_list)
    return df

def checkCSV(path):
    if os.path.isfile(path):
        if not path.endswith('.csv'):
            print("File must has a .csv extension: ", path)
            sys.exit()
    else:
        print("File does not exist: ", path)
        sys.exit()

def is_date(string, fuzzy=False):
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False