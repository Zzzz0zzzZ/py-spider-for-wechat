import time
import csv
import getAllUrls
import datetime

# path = getAllUrls.path

def getRealTimeByTimeStamp(time_stamp):
    time_array = time.localtime(time_stamp)  # 时间序列
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return otherStyleTime

def getTSListAndConvert(ts_storage_path):
    with open(ts_storage_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        ts_list = []
        for row in reader:
            # print(row[0])
            ts_list.append(getRealTimeByTimeStamp(int(row[0])))
    return ts_list

def Write2Csv(data_list, savepath, filename):
    # file_name = input("please name the file\n")
    with open(savepath + '/' + filename + '_real-time.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list:
            writer.writerow([row])
    print(f"[save real-time list] {str(datetime.datetime.now())} done")


def run_getRealTimeByTimeStamp(savepath, filename):
    ts_list = getTSListAndConvert(savepath + '/' + filename + "_update-time.csv")
    Write2Csv(ts_list, savepath, filename)


# if __name__ == "__main__":
#     start = time.time()
#     time_stamp_list_storage_path = path + "update-time.csv"
#     ts_list = getTSListAndConvert(time_stamp_list_storage_path)
#     Write2Csv(ts_list)
#     end = time.time()
#     print("time cost:", end - start, "s")

