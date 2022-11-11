import argparse
import json
import os

import pandas as pd

from utils import load_Trips, checkCSV

if __name__ == '__main__':

    p = "output/"
    cloudlets = {}
    for folder in os.listdir(p):
        j = 1
        for file in os.listdir(p + folder):
            f = os.path.join(p + folder, file)
            checkCSV(f)
            df = pd.read_csv(f)
            if folder in cloudlets.keys():
                cloudlets[folder][j] = len(df)
            else:
                cloudlets[folder] = {}
                cloudlets[folder][j] = len(df)
            j = j + 1
    cloudlets = dict(sorted(cloudlets.items()))
    with open("stats.json", "w") as write_file:
        json.dump(cloudlets, write_file, indent=4)