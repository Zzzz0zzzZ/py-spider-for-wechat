# -*- coding: utf-8 -*-
import random
import requests
import time
import csv
from tqdm import tqdm
import datetime
import os


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
    mkdir(save_path + '/raw')
    start = time.time()
    title, link, update_time = getAllUrl(page_num=page_num, start_page=page_start, fad=fad, tok=tok, headers=headers)
    # save urls, titles, update_times
    write2csv(save_path, filename, link, eType="url")
    write2csv(save_path, filename, title, eType="title")
    write2csv(save_path, filename, update_time, eType="update-time")
    end = time.time()
    print("time cost:", end - start, "s")

