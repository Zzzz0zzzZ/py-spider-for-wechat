# -*- coding: utf-8 -*-
import random
import requests
import time
import csv
from tqdm import tqdm

# cookie注意更新
headers = {
    "cookie": "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; rand_info=CAESIJrdL2xSqHo7JtTHuM8d4zAMoSNjxacqc6VQsR4g87rR; slave_bizuin=3940396966; data_bizuin=3940396966; bizuin=3940396966; data_ticket=GYSHLkTsYGcdfdQ/Oj2wGnYGGBkKpTBgA59H5y7Zb2Su8NHcYn40uu+pALruIHzO; slave_sid=VnNCREhCQ1diTkoyQ091ejQ0ckoxdDBiTUxLMWxURHFPVDNsWmFhZVY0UjFzemc0UjhZc19hOERZY2tGa2dEcFRmeEJjV2tWRXRoZlFfMjFlUmhkbXRUdF9pdzUxTEVSVzQxbmhaYnVMMnNuSm55b0NsYkJwOHhLSEdOMk9mYk1hSW5DcDFsZTFjVEw5YUkw; slave_user=gh_495d307185e5; xid=1f54bfb9bf5268fecf62675424ba6a66; mm_lang=zh_CN",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
fad = 'MzA3OTI0OTk3OQ=='                     # fakeid， 公众号唯一标识
tok = '1330118282'                            # token， 注意更新


def getAllUrl(page_num=1, start_page=0):                             # pages
    title = []
    link = []
    update_time = []
    with tqdm(total=page_num) as pbar:
        for i in range(page_num):
            data = {
                'action': 'list_ex',
                'begin': start_page + i*5,       #页数
                'count': '5',
                'fakeid': fad,
                'type': '9',
                'query':'' ,
                'token': tok,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
            }
            time.sleep(random.randint(1, 8))
            r = requests.get(url, headers=headers, params=data)
            # 解析json
            dic = r.json()
            for i in dic['app_msg_list']:     # 遍历dic['app_msg_list']中所有内容
                # 按照键值对的方式选择
                title.append(i['title'])      # get title value
                link.append(i['link'])        # get link value
                update_time.append(i['update_time'])    # get update-time value
            pbar.update(1)

    return title, link, update_time

def write2csv(data_list):
    file_name = input("please name the file\n")
    with open('./data/' + file_name + '.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list:
            writer.writerow([row])
    print("done")


if __name__ == '__main__':
    Page_Num = int(input("please input the [Page-Num] you need:\n"))
    Page_Start = 290
    start = time.time()
    title, link, update_time = getAllUrl(page_num=Page_Num, start_page=Page_Start)
    # save urls, titles, update_times
    print("link-->title-->update_time")
    write2csv(link)
    write2csv(title)
    write2csv(update_time)
    end = time.time()
    print("time cost:", end-start, "s")

