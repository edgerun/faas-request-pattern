import argparse
import sys
import datetime
import time
from datetime import timedelta

import numpy as np
import pandas
from matplotlib import pyplot as plt

from utils import load_Trips, checkCSV, getNearestKeyToValue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get edge cases of dataset")
    parser.add_argument('--trips', help='path to trips csv')
    parser.add_argument('--name', help='name of trip scenario')
    args = parser.parse_args()
    if args.trips is None:
        print("Please set --trips !")
        sys.exit()
    else:
        checkCSV(args.trips)

    if args.name is None:
        print("Please set --name !")
        sys.exit()

    p = 'data/trips/' + args.name

    startTime = time.time()
    df_trips = load_Trips(args.trips)
    df_trips['pickup_datetime'] = pandas.to_datetime(df_trips['pickup_datetime'])
    firstDate = min(df_trips['pickup_datetime'])
    date = firstDate
    lastDate = max(df_trips['pickup_datetime'])
    df_interval = {}
    interval_sum = {}
    i = 0
    while date <= lastDate:
        start = date
        end = date + timedelta(minutes=10)
        date = date + timedelta(minutes=5)
        df_temp = df_trips.loc[((df_trips['pickup_datetime'] >= start) & (df_trips['pickup_datetime'] <= end))]
        sumPickups = sum(df_temp['passenger_count'])
        if sumPickups > 0:
            interval_sum[i] = sumPickups
            df_interval[i] = df_temp
            i = i + 1

    p5 = np.percentile(list(interval_sum.values()), 5)
    avg = sum(list(interval_sum.values())) / float(len(interval_sum))
    p95 = np.percentile(list(interval_sum.values()), 95)
    print("5th percentile: ", p5)
    print("Average: ", avg)
    print("95th percentile: ", p95)
    minKey = getNearestKeyToValue(interval_sum, p5)
    maxKey = getNearestKeyToValue(interval_sum, p95)
    avgKey = getNearestKeyToValue(interval_sum, avg)
    minDf = df_interval[minKey]
    maxDf = df_interval[maxKey]
    avgDf = df_interval[avgKey]
    minDf.to_csv(p + '/minInterval.csv', index=False)
    maxDf.to_csv(p + '/maxInterval.csv', index=False)
    avgDf.to_csv(p + '/avgInterval.csv', index=False)

    plotMinDf = minDf.set_index('pickup_datetime')
    plotMaxDf = maxDf.set_index('pickup_datetime')
    plotAvgDf = avgDf.set_index('pickup_datetime')
    plotMinDf = plotMinDf.resample('1s')['passenger_count'].sum()
    plotMaxDf = plotMaxDf.resample('1s')['passenger_count'].sum()
    plotAvgDf = plotAvgDf.resample('1s')['passenger_count'].sum()

    plotMinDf.plot(x='pickup_datetime', kind='line')
    plt.ylabel('pickups')
    plt.xlabel('time')
    plt.title("min. interval")
    plt.savefig(p + '/minInterval.pdf')
    plt.cla()
    plotAvgDf.plot(x='pickup_datetime', kind='line')
    plt.ylabel('pickups')
    plt.xlabel('time')
    plt.title("avg. interval")
    plt.savefig(p + '/avgInterval.pdf')
    plt.cla()
    plotMaxDf.plot(x='pickup_datetime', kind='line')
    plt.ylabel('pickups')
    plt.xlabel('time')
    plt.title("max. interval")
    plt.savefig(p + '/maxInterval.pdf')
    plt.cla()
    print("time needed (in minutes): " + str((time.time() - startTime) / 60))
