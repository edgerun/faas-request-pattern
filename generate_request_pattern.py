import argparse
import datetime
import os
import pickle
import sys
from multiprocessing.pool import ThreadPool
import pandas

from utils import checkCSV, load_Topology, get_max_bounds_topology, load_Trips, get_nearest_cell_tower, load_Requests, \
    saveCSV, is_date

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate Request Pattern")
    parser.add_argument('--name', help='naming of the request pattern output files')
    parser.add_argument('--topology', help='path to topology csv')
    parser.add_argument('--trips', help='path to trips csv')
    parser.add_argument('--start', help='start date time')
    parser.add_argument('--end', help='end date time')
    args = parser.parse_args()
    pickup_path = 'output/' + args.name

    if args.topology is None:
        print("Please set --topology !")
        sys.exit()
    else:
        checkCSV(args.topology)

    if args.trips is None:
        print("Please set --trips !")
        sys.exit()
    else:
        checkCSV(args.trips)

    if args.name is None:
        print("Please set --name !")
        sys.exit()

    if args.start is not None:
        if not is_date(args.start):
            print("Please enter a correct start date!")
            sys.exit()

    if args.end is not None:
        if not is_date(args.end):
            print("Please enter a correct end date!")
            sys.exit()
        if args.start > args.end:
            print("The start date has to be smaller than the end date!")
            sys.exit()


    df_topology = load_Topology(args.topology)

    df_trips = load_Trips(args.trips)
    df_trips['pickup_datetime'] = pandas.to_datetime(df_trips['pickup_datetime'])

    if args.start is not None and args.end is not None:
        fromD = datetime.datetime.fromisoformat(args.start)
        toD = datetime.datetime.fromisoformat(args.end)
        mask = (df_trips['pickup_datetime'] >= fromD) & (df_trips['pickup_datetime'] <= toD)
        df_trips = df_trips.loc[mask]

    request_cols = ['timestamp', 'requests', 'cell', 'cloudlet']

    print("generating pickup data...")
    requests = []
    pool = ThreadPool(50)
    results = []
    results_sum = []
    values = df_topology.values
    for v in df_trips.values:
        results.append(pool.apply_async(get_nearest_cell_tower, args=(v[0], v[1], v[3], v[2], values)))
    pool.close()
    pool.join()
    for r in results:
        r = r.get()
        if r:
            results_sum.append(r)
    pickups = pandas.DataFrame(results_sum, columns=request_cols)
    pickups['cell'] = pickups['cell'].astype(str)

    print("fix multiple requests...")
    temp_rows = []
    rows_to_delete = []

    # show plots
    # df_plot = dict(tuple(pickups.groupby('cloudlet')))
    # for i, df in df_plot.items():
        # df = df.groupby(["timestamp"]).requests.sum().reset_index()
        # df["timestamp"] = pandas.to_datetime(df["timestamp"])
        # plt.figure()
        # plt.scatter(df['timestamp'], df['requests'])  # 1s wide bars
        # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        # plt.show()

    # add rows for requests > 1
    for i, row in pickups.iterrows():
        r = row['requests']
        if r > 1:
            rows_to_delete.append(i)
            for x in range(0, r):
                temp_rows.append((row['timestamp'], 1, row['cell'], row['cloudlet']))
    pickups.drop(rows_to_delete, inplace=True)
    new_df = pandas.DataFrame(temp_rows, columns=request_cols)
    pickups = pandas.concat([pickups, new_df], keys=request_cols)
    cloudletDfs = dict(tuple(pickups.groupby('cloudlet')))
    print("calc time delta between requests...")
    if not os.path.exists(pickup_path):
        os.mkdir(pickup_path)
    for i, df in cloudletDfs.items():
        df.sort_values(by=['timestamp'], inplace=True)
        lastTimestamp = 0
        first = True
        for k, row in df.iterrows():
            # set 11s for first request
            if first:
                first = False
                lastTimestamp = float(str(row['timestamp'].timestamp()))
                df.at[k, 'timestamp'] = 11
            else:
                diff = float(str(row['timestamp'].timestamp())) - lastTimestamp
                if diff == 0:
                    diff = 0.1
                lastTimestamp = float(str(row['timestamp'].timestamp()))
                df.at[k, 'timestamp'] = diff
        df.drop(columns=["requests", "cell", "cloudlet"], inplace=True)
        pathCSV = pickup_path + "/" + str(i) + '_pickups.csv'
        pathPkl = pickup_path + "/" + str(i) + '_pickups.pkl'
        df.to_csv(pathCSV, header=False, index=False)

        pklArray = []
        for x in df['timestamp'].values:
            print(x)
            pklArray.append(x)
        with open(pathPkl, 'wb') as f:
            pickle.dump(pklArray, f)
        # output = open(pathPkl, 'wb')
        # output.close()





