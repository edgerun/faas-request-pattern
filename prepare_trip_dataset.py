import glob
import os
import sys
import argparse

import pandas as pd

from utils import checkCSV, load_Topology, get_max_bounds_topology

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prepare Trips dataset")
    parser.add_argument(
        '--path',
        help='Path to trip csv files'
    )
    parser.add_argument(
        '--topology',
        help='Path to to topology csv file'
    )
    parser.add_argument(
        '--name',
        help='naming of the output files folder'
    )
    args = parser.parse_args()

    if args.name is None:
        print("Please set --name")
        sys.exit()

    if args.topology is None:
        print("Please set --topology")
        sys.exit()
    else:
        checkCSV(args.topology)

    col_list = ['medallion', 'hack_license', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'pickup_datetime',
                'dropoff_datetime', 'passenger_count', 'trip_time_in_secs', 'trip_distance', 'pickup_longitude',
                'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']
    df_topology = load_Topology(args.topology)
    # get [max_lat, min_lat, max_lon, min_lon]
    max_bounds = get_max_bounds_topology(df_topology)
    max_lat = max_bounds[0]
    min_lat = max_bounds[1]
    max_lon = max_bounds[2]
    min_lon = max_bounds[3]

    if args.path is None:
        print("Please set --path")
        sys.exit()
    else:
        for filename in os.listdir(args.path):
            f = os.path.join(args.path, filename)
            checkCSV(f)
            print("load trip dataset...", filename)
            df = pd.read_csv(f, skipinitialspace=True, usecols=col_list, low_memory=False)

            print("drop unnecessary columns...", filename)
            df.drop(['medallion', 'hack_license', 'dropoff_longitude', 'dropoff_latitude', 'dropoff_datetime', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'trip_time_in_secs', 'trip_distance'], axis=1, inplace=True)

            print("get trips in topology bounds...")
            df = df[df['pickup_longitude'].between(min_lon, max_lon)]
            df = df[df['pickup_latitude'].between(min_lat, max_lat)]
            df.sort_values("pickup_datetime", inplace=True)
            p = 'data/trips/' + args.name + "/"
            os.makedirs(p, exist_ok=True)
            df.to_csv(p + filename)
        df = pd.concat(map(pd.read_csv, glob.glob(os.path.join("data/trips/" + args.name + "/", "*.csv"))))
        df.to_csv("data/trips/" + args.name + "/trips.csv")

