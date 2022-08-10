# -*- coding: utf-8 -*-
import random
import requests
import time
import csv
from tqdm import tqdm
import datetime

# cookie注意更新
headers = {
    "cookie": "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; mm_lang=zh_CN; uuid=cfef0bb197ffadcc39cd19672192d886; rand_info=CAESIGwNspMVbwTqis6Zen9lzi/uA+0WslkGq/2PwEPjSuMv; slave_bizuin=3940396966; data_bizuin=3940396966; bizuin=3940396966; data_ticket=Qx0Ar2KLEjMps6NWmjT6XSa1ywc1l4aQ8R/QrtlPr3XhA3icpTy/+Mdkx+Z7YZ5N; slave_sid=UDdlWUlxV21XWjk2UU5UR3R5Zjh2Q2pleTFDVmJ0OXMwMUtXVXpQRFFtVWdnTmJHdEdQYlhLYlROdF9aYnZ4bUwzc1lPdVc4SHV6U2QxYm0yYlc0SFlyX2xSZGNXSjBtT1RtcE9UcVcwR3dfMGdKMWNuRjRuelMwUnlESFAzR2Z1WVdJdmFNd3hLNFZCdE5U; slave_user=gh_495d307185e5; xid=f0acfc05b17919a15423b39668ab4673",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
fad = 'MzA3OTI0OTk3OQ=='                     # fakeid， 公众号唯一标识  [诺维信中国]
# fad = 'Mzg5ODU5MTA5NA=='                   # [渡你到彼岸]
tok = '618429680'                            # token， 注意更新

path = f'./data/{str(datetime.date.today())}/'


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
            time.sleep(random.randint(1, 2))
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

def write2csv(data_list, eType:str):
    # file_name = input("please name the file\n")
    mkdir(path=path)
    with open(path + eType + '.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list:
            writer.writerow([row])
    print(f"[save {eType} list] {str(datetime.datetime.now())} done")

def mkdir(path):
    '''
    创建指定的文件夹
    :param path: 文件夹路径，字符串格式
    :return: True(新建成功) or False(文件夹已存在，新建失败)
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

if __name__ == '__main__':
    # set args
    Page_Num = int(input("please input the [Page-Num] you need:\n"))
    Page_Start = int(input("please input the [Page_Start] you need:\n"))
    # Page_Start = 490
    # begin
    start = time.time()
    title, link, update_time = getAllUrl(page_num=Page_Num, start_page=Page_Start)
    # save urls, titles, update_times
    # print("link-->title-->update_time")
    write2csv(link, eType="url")
    write2csv(title, eType="title")
    write2csv(update_time, eType="update-time")
    end = time.time()
    print("time cost:", end-start, "s")

