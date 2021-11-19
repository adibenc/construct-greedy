#!/bin/python3
import pandas as pd
# load

# greed
df = pd.read_csv("dummydataset_timecost_trade.csv", sep=";")

print(df)

def greedy(data):
    for d in data:
        if True:
            print("feasible")

greedy(df)