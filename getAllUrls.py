# -*- coding: utf-8 -*-
import requests
import time
import csv

# cookie注意更新
headers = {
    "cookie": "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; uuid=8f918189cdbb5277042af4cc9972af95; cert=8usVhBJvV_bhiOGzvEr5KNZrBLVPpLvI; sig=h01f5bf100266357f9042120ae1f1e6812f0dd97700fa5cc0af9d3206ec20ce8d58f65c6dfd9ddf258b; data_bizuin=3940396966; data_ticket=/cKAiIbLusvrLMxsPbIqHiMEBtHoNmb8pReRo5lYfrq+u+x1bExHc5Kbhh1jIRaY; master_key=oqWPTPRNLKNRxZ933GO+CKIV6t0+ii+8093Le9A8ayE=; master_user=gh_495d307185e5; master_sid=ZWk4c2ZfaG5PdEV6N1hmeGp0eXhSMFVWVmtBUTJZN0lHY1BrNmozRGZrNG9vcjRTYkxYcWczQWNERzlqb0RrQ0xHbU5QaWRCM1BjdlROdW1jTk1HWVVscWw0SFp6ZVRZZE5aNEF0a3NhWE8wQ2pRNURTb2dReW13alpMN2lCN3lEbTNQcWZHeXpGQ1lzb3BT; master_ticket=22828aaf6915cdba00bb1e491b279738; bizuin=3940396966; slave_user=gh_495d307185e5; slave_sid=elhtbVVEak5uSnZ6TDFMejByR2l1QnZRdmFjOXhGSl9UUk5BWms3UGxVUTFvVDFmX0NIUmswNFZRV3lVaExrbkVqM290UXlDWHFMXzdYckRCR01DcXhibWFaeDQ5b3RfdWtmVGNsdmFxUXFiNUtZcUlWNUFSemhjdk9PMDdMT2FFZnRGb2p4UE9odHlHeEVq",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
fad = 'MzA3OTI0OTk3OQ=='                     # fakeid， 公众号唯一标识
tok = '933321408'                            # token， 注意更新

def getAllUrl(page_num=1):                             # pages
    title = []
    link = []
    for i in range(page_num):
        data = {
            'action': 'list_ex',
            'begin': i*5,       #页数
            'count': '5',
            'fakeid': fad,
            'type': '9',
            'query':'' ,
            'token': tok,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
        }
        r = requests.get(url, headers=headers, params=data)
        # 解析json
        dic = r.json()
        for i in dic['app_msg_list']:     # 遍历dic['app_msg_list']中所有内容
            # 按照键值对的方式选择
            title.append(i['title'])      # 取 key键 为‘title’的 value值
            link.append(i['link'])        # 取 key键 为‘link’的 value值

    return title, link

def write2csv(data_list):
    file_name = input("please name the file\n")
    with open('./data/' + file_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list:
            writer.writerow([row])
    print("done")

if __name__ == '__main__':
    start = time.time()
    title, link = getAllUrl(page_num=5)
    write2csv(link)
    end = time.time()
    print("time cost:", end-start)

