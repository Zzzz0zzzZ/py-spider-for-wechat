# coding=utf-8
# @Time : 2022/12/20 11:55 AM
# @Author : 王思哲
# @File : getFakId.py
# @Software: PyCharm

import requests


def get_fakid(headers, tok, query):
    '''

    :param headers:请求头
    :param tok: token
    :param query: 查询名称
    :return:
    '''
    url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz'
    data = {
        'action': 'search_biz',
        'scene': 1,  # 页数
        'begin': 0,
        'count': 10,
        'query': query,
        'token': tok,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
    }
    # 发送请求
    r = requests.get(url, headers=headers, params=data)
    # 解析json
    dic = r.json()
    # 获取公众号名称、fakeid
    wpub_list = [
        {
            'wpub_name': item['nickname'],
            'wpub_fakid': item['fakeid']
        }
        for item in dic['list']
    ]

    return wpub_list
