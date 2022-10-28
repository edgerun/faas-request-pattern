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
    args = parser.parse_args()
    if args.trips is None:
        print("Please set --trips !")
        sys.exit()
    else:
        checkCSV(args.trips)
    df_trips = load_Trips(args.trips)
    df_trips['pickup_datetime'] = pandas.to_datetime(df_trips['pickup_datetime'])
    firstDate = min(df_trips['pickup_datetime'])
    date = firstDate
    lastDate = max(df_trips['pickup_datetime'])
    df_interval = {}
    interval_sum = {}
    i = 0
    startTime = time.time()
    while date <= lastDate:
        start = date
        end = date + timedelta(minutes=10)
        date = date + timedelta(minutes=5)
        mask = (df_trips['pickup_datetime'] >= start) & (df_trips['pickup_datetime'] <= end)
        df_temp = df_trips.loc[mask]
        sumPickups = sum(df_temp['passenger_count'])
        interval_sum[i] = sumPickups
        df_interval[i] = df_temp
        i = i + 1
    print("--- %s seconds ---" % (time.time() - startTime))

    p5 = np.percentile(list(interval_sum.values()), 5)
    avg = sum(interval_sum.values()) / float(len(interval_sum))
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
    minDf.to_csv('data/trips/minInterval.csv', index=False)
    maxDf.to_csv('data/trips/maxInterval.csv', index=False)
    avgDf.to_csv('data/trips/avgInterval.csv', index=False)

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
    plt.savefig('minInterval.png')
    plt.cla()
    plotAvgDf.plot(x='pickup_datetime', kind='line')
    plt.ylabel('pickups')
    plt.xlabel('time')
    plt.title("avg. interval")
    plt.savefig('avgInterval.png')
    plt.cla()
    plotMaxDf.plot(x='pickup_datetime', kind='line')
    plt.ylabel('pickups')
    plt.xlabel('time')
    plt.title("max. interval")
    plt.savefig('maxInterval.png')
    plt.cla()
