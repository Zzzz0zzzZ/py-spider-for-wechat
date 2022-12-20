# coding=utf-8
# @Time : 2022/12/20 11:55 AM
# @Author : 王思哲
# @File : getFakId.py
# @Software: PyCharm

import requests

# cookie注意更新
headers = {
    "cookie": "RK=kzslnuy1fj; ptcz=a94363703c487d5ceaef1119fb4e14ab7b2e73d313aa975f6198872bb78dbeeb; pgv_pvid=1429613752; pac_uid=0_012041c10b7f5; ua_id=DAIAARGIrbAfLgOlAAAAABNe61cI4YL5pX-j1h33BYw=; wxuin=60056270789759; ptui_loginuin=1175690167; mm_lang=zh_CN; uuid=54396a53ff3f0282913295afdcefebf8; rand_info=CAESIMzHN99y9Q3fbZekMmzzB/xWwif6Z1d+BPmQkdLH2XVe; slave_bizuin=3940396966; data_bizuin=3940396966; bizuin=3940396966; data_ticket=04csz1WhV8MNkw+OiR68UJaKfq1p+jIVEGy5f1MknGIHHRX5bkUTxcKsPpxY+cgq; slave_sid=OExNU0ZUS2lGSGdzNjcwZE9HUEx2eE5iaVlYcnhfaWZjZ0VKVUVQUnBzOTJQTlR4WHJHczdIUE5kbGI5T3F3bnZrNWpIeEZicXBGcFUyRm1pM0s3Y3JiSVdvWk1UYWFTcmRIbV9rM1ZQbU93S3F1Tnp1UDF6cFJySXNMV2J1WTR2QnFST3Y1Z2JVVkFyY1JK; slave_user=gh_495d307185e5; xid=61e496efd593cf0772f32e0f2f88ba38",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
# token， 注意更新
tok = '1196926817'


def getFakId(headers, tok, query):
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

    return dic

if __name__ == '__main__':
    getFakId(headers=headers, tok=tok, query='诺味')