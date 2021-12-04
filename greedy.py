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



#sourcecode
function optimasi(){
    
    dur #jumlah hari yang diperlukan untuk pengerjaan
    cost #biaya yang diperlukan
    costcrash #biayapengahancuran 
    expdaycrash #lamanya waktu crash
    dailyreward #reward
    timeleft = 4*5*6  = 120 #waktu kerja selama 6 bulan
    task = #jumlah task

    #time
    #reward = 0
    #task = 0
    if(dur > 0 and timeleft > 0){
        timeleft = timeleft - dur;
        if(timeleft > 0 and expdaycrash > 0){
            timeleft = timeleft - expdaycrash;
            if(timeleft > 0){
                task = task + 1; #initiate task
            }
        }
    }

    #costreward
    if(cost != 0){
        totalcost = cost;
        if(costcrash != 0){
             totalcost = totalcost + costcrash
        }
        reward = dailyreward - totalcost;
    }

    print(task,reward,)
}
