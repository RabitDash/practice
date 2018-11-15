import pandas as pd
import time
import os

edge_data_iter = pd.read_csv("Gowalla_edges.txt",
                            sep='\t',
                            header=None,
                            iterator=True)

checkin_data_iter = pd.read_csv("Gowalla_totalCheckins.txt",
                            sep='\t',
                            header=None,
                            usecols=[0,1,4],
                            iterator=True)

# utc2stamp  将UTC时间转化为数值型的时间戳
def utc2stamp(utc_time):
    stamp_list = []
    for x in utc_time:
        tm = time.strptime(x, '%Y-%m-%dT%H:%M:%SZ')
        timeStamp = int(time.mktime(tm))
        stamp_list.append(timeStamp)
    return stamp_list 

def process_checkin(pditer):
    result = pd.DataFrame()
    num = 0.0
    if os.path.exists("totalCheckins.csv"):
        return
    try:
        while True:
            checkin = pditer.read(10000)
            num += 10000.0
            progress = num / 6442892.0
            print("Processed {}".format(progress * 100.0))
            
            checkin[1] = utc2stamp(checkin[1])
            checkin.to_csv("totalCheckins.csv",mode='a+',sep='\t',header=None, index=None)
#             result = result.append(checkin)
#             print(result)

    except StopIteration:
        print("Finished")
        
def main():
    process_checkin(checkin_data_iter)

main()