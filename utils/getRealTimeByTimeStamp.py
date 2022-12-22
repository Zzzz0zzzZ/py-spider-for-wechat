import time
import csv
import datetime


def getRealTimeByTimeStamp(time_stamp):
    time_array = time.localtime(time_stamp)  # 时间序列
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return otherStyleTime

def getTSListAndConvert(ts_storage_path):
    with open(ts_storage_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        ts_list = []
        for row in reader:
            ts_list.append(getRealTimeByTimeStamp(int(row[0])))
    return ts_list

def Write2Csv(data_list, savepath, filename):
    with open(savepath + '/' + filename + '_real-time.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list:
            writer.writerow([row])
    print(f"[save real-time list] {str(datetime.datetime.now())} done")

def run_getRealTimeByTimeStamp(savepath, filename):
    ts_list = getTSListAndConvert(savepath + '/' + filename + "_update-time.csv")
    Write2Csv(ts_list, savepath, filename)
