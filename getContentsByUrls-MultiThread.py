import csv
import random
import threading

import requests
import bs4
import time
import queue
from tqdm import tqdm
import getAllUrls
import datetime
path = getAllUrls.path

headers = {
        "cookie":
            "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; cert=8usVhBJvV_bhiOGzvEr5KNZrBLVPpLvI; sig=h01f5bf100266357f9042120ae1f1e6812f0dd97700fa5cc0af9d3206ec20ce8d58f65c6dfd9ddf258b; master_key=oqWPTPRNLKNRxZ933GO+CKIV6t0+ii+8093Le9A8ayE=; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; uuid=9a488fb0b902debc7c27e896a8cad45a; rand_info=CAESIJrdL2xSqHo7JtTHuM8d4zAMoSNjxacqc6VQsR4g87rR; slave_bizuin=3940396966; data_bizuin=3940396966; bizuin=3940396966; data_ticket=GYSHLkTsYGcdfdQ/Oj2wGnYGGBkKpTBgA59H5y7Zb2Su8NHcYn40uu+pALruIHzO; slave_sid=VnNCREhCQ1diTkoyQ091ejQ0ckoxdDBiTUxLMWxURHFPVDNsWmFhZVY0UjFzemc0UjhZc19hOERZY2tGa2dEcFRmeEJjV2tWRXRoZlFfMjFlUmhkbXRUdF9pdzUxTEVSVzQxbmhaYnVMMnNuSm55b0NsYkJwOHhLSEdOMk9mYk1hSW5DcDFsZTFjVEw5YUkw; slave_user=gh_495d307185e5; xid=1f54bfb9bf5268fecf62675424ba6a66; mm_lang=zh_CN",
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
contents = []
# 从文件读取URLs，返回字典
def getUrlList(url_storage_path):
    with open(url_storage_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        url_list = [[idx, row] for idx, row in enumerate(reader)]
    return url_list

# 不断向rep队列添加response对象
def do_craw(url_queue:queue.Queue, response_queue:queue.Queue):
    while url_queue.empty() != True:
        url = url_queue.get()
        response = requests.get(url[1][0], headers=headers)
        response_queue.put([url[0], response])
        # print("craw")
        time.sleep(random.randint(1, 2))

# 不断解析对象，将结果添加到contents列表中
def do_parse(response_queue:queue.Queue):
    time.sleep(2)
    while response_queue.empty() != True:
        response = response_queue.get()
        # 解析html
        soup = bs4.BeautifulSoup(response[1].text, 'html.parser')
        # 大多数p标签中包含的是文字，但也有一些直接是 “section > span”， 这些内容没有爬到
        soup_sel = soup.select("p")
        content = ""
        for c in soup_sel:
            t = c.get_text().strip('\n')
            if t != '':
                content += t
        # 删除固定前缀和后缀
        content = content[116:-11]
        contents.append([response[0], content])
        # print("parse")
        time.sleep(random.randint(1, 2))
    # return contents

# 按行存csv， 编码'utf-8-sig'存中文
def saveContentsTocsv(contents):
    # file_name = input("please name the new csv-file\n")
    with open(path + 'content.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        for row in contents:
            writer.writerow([row])
    print(f"[save content list] {str(datetime.datetime.now())} done")


if __name__ == "__main__":
    url_list_storage_path = path + 'url.csv'
    url_list = getUrlList(url_list_storage_path)
    url_queue = queue.Queue()
    response_queue = queue.Queue()

    start = time.time()

    for url in url_list:
        url_queue.put(url)

    thread_list = []
    # craw
    for idx in range(20):
        tc = threading.Thread(target=do_craw, args=(url_queue, response_queue))
        thread_list.append(tc)
        tc.start()
    # parse
    for idx in range(20):
        tp = threading.Thread(target=do_parse, args=(response_queue, ))
        thread_list.append(tp)
        tp.start()

    for thread in thread_list:
        thread.join()

    # print(contents)
    # saveContentsTocsv(contents)
    # print(len(contents))
    contents.sort(key=lambda x: (x[0]))
    res = []
    for c in contents:
        res.append(c[1])
    # for c in contents:
    #     print(c)
    end = time.time()
    saveContentsTocsv(res)
    print(f"time cost:{end-start}s")
