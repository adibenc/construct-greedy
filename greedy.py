#!/bin/python3
import pandas as pd
# load

# greed
data = pd.read_csv("dummydataset_timecost_trade.csv", sep=";")

print(data)

def greedy(data):
    for d in data:
        if data