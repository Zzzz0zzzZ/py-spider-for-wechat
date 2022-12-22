import csv
import random
import threading
import requests
import bs4
import time
import queue
import datetime


contents = []

# 从文件读取URLs，返回字典
def getUrlList(url_storage_path):
    with open(url_storage_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        url_list = [[idx, row] for idx, row in enumerate(reader)]
    return url_list

# 不断向rep队列添加response对象
def do_craw(headers, url_queue:queue.Queue, response_queue:queue.Queue):
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
        contents.append([response[0], content])
        # print("parse")
        time.sleep(random.randint(1, 2))
    # return contents

# 按行存csv， 编码'utf-8-sig'存中文
def saveContentsTocsv(path, filename, contents):
    with open(path + '/' + filename + '_content.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        for row in contents:
            writer.writerow([row])
    print(f"[save content list] {str(datetime.datetime.now())} done")


def run_getContentsByUrls_MultiThread(savepath, filename, headers):
    url_list_storage_path = savepath + '/' + filename + '_url.csv'
    url_list = getUrlList(url_list_storage_path)
    url_queue = queue.Queue()
    response_queue = queue.Queue()

    start = time.time()

    for url in url_list:
        url_queue.put(url)

    thread_list = []
    # craw
    for idx in range(20):
        tc = threading.Thread(target=do_craw, args=(headers, url_queue, response_queue))
        thread_list.append(tc)
        tc.start()
    # parse
    for idx in range(20):
        tp = threading.Thread(target=do_parse, args=(response_queue,))
        thread_list.append(tp)
        tp.start()

    for thread in thread_list:
        thread.join()

    contents.sort(key=lambda x: (x[0]))
    res = []
    for c in contents:
        res.append(c[1])
    end = time.time()
    saveContentsTocsv(savepath, filename, res)
    print(f"time cost:{end - start}s")
