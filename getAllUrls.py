# -*- coding: utf-8 -*-
import random
import requests
import time
import csv
from tqdm import tqdm
import datetime
import os


# cookie注意更新
# headers = {
#     "cookie": "RK=kzslnuy1fj; ptcz=a94363703c487d5ceaef1119fb4e14ab7b2e73d313aa975f6198872bb78dbeeb; pgv_pvid=1429613752; pac_uid=0_012041c10b7f5; ua_id=DAIAARGIrbAfLgOlAAAAABNe61cI4YL5pX-j1h33BYw=; wxuin=60056270789759; ptui_loginuin=1175690167; mm_lang=zh_CN; uuid=54396a53ff3f0282913295afdcefebf8; rand_info=CAESIMzHN99y9Q3fbZekMmzzB/xWwif6Z1d+BPmQkdLH2XVe; slave_bizuin=3940396966; data_bizuin=3940396966; bizuin=3940396966; data_ticket=04csz1WhV8MNkw+OiR68UJaKfq1p+jIVEGy5f1MknGIHHRX5bkUTxcKsPpxY+cgq; slave_sid=OExNU0ZUS2lGSGdzNjcwZE9HUEx2eE5iaVlYcnhfaWZjZ0VKVUVQUnBzOTJQTlR4WHJHczdIUE5kbGI5T3F3bnZrNWpIeEZicXBGcFUyRm1pM0s3Y3JiSVdvWk1UYWFTcmRIbV9rM1ZQbU93S3F1Tnp1UDF6cFJySXNMV2J1WTR2QnFST3Y1Z2JVVkFyY1JK; slave_user=gh_495d307185e5; xid=61e496efd593cf0772f32e0f2f88ba38",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
# }

# fad = 'MzA3OTI0OTk3OQ=='                     # fakeid， 公众号唯一标识  [诺维信中国]
# fad = 'Mzg5ODU5MTA5NA=='                   # [渡你到彼岸]
# tok = '1196926817'                            # token， 注意更新

# path = f'./data/{str(datetime.date.today())}/'


def getAllUrl(page_num, start_page, fad, tok, headers):                             # pages
    url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
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

def write2csv(path, filename, data_list, eType:str):
    # file_name = input("please name the file\n")
    mkdir(path=path)
    with open(path + '/' + filename + '_' + eType + '.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
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

def run_getAllUrls(page_start, page_num, save_path, fad, tok, headers, filename):
    # set args
    # Page_Num = int(input("please input the [Page-Num] you need:\n"))
    # Page_Start = int(input("please input the [Page_Start] you need:\n"))
    # Page_Start = 490
    # begin
    start = time.time()
    title, link, update_time = getAllUrl(page_num=page_num, start_page=page_start, fad=fad, tok=tok, headers=headers)
    # save urls, titles, update_times
    # print("link-->title-->update_time")
    write2csv(save_path, filename, link, eType="url")
    write2csv(save_path, filename, title, eType="title")
    write2csv(save_path, filename, update_time, eType="update-time")
    end = time.time()
    print("time cost:", end - start, "s")

# if __name__ == '__main__':
#     # set args
#     Page_Num = int(input("please input the [Page-Num] you need:\n"))
#     Page_Start = int(input("please input the [Page_Start] you need:\n"))
#     # Page_Start = 490
#     # begin
#     start = time.time()
#     title, link, update_time = getAllUrl(page_num=Page_Num, start_page=Page_Start)
#     # save urls, titles, update_times
#     # print("link-->title-->update_time")
#     write2csv(link, eType="url")
#     write2csv(title, eType="title")
#     write2csv(update_time, eType="update-time")
#     end = time.time()
#     print("time cost:", end-start, "s")

