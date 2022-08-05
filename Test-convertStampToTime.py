import time

time_stamp = 1604620800    # 时间戳
time_array = time.localtime(time_stamp)     # 时间序列
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
print(otherStyleTime)   # 2020-04-23 16:30:00
