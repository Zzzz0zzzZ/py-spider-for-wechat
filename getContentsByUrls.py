import csv
import random
import requests
import bs4
import time
from tqdm import tqdm

# 从文件读取URLs，返回字典
def getUrlList(url_storage_path):
    with open(url_storage_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        url_list = [row for row in reader]
    return url_list


def getContentByUrl(url_list):
    # 返回结果
    contents = []
    # 请求头
    headers = {
        "cookie":
            "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; uuid=8f918189cdbb5277042af4cc9972af95; cert=8usVhBJvV_bhiOGzvEr5KNZrBLVPpLvI; sig=h01f5bf100266357f9042120ae1f1e6812f0dd97700fa5cc0af9d3206ec20ce8d58f65c6dfd9ddf258b; data_bizuin=3940396966; data_ticket=/cKAiIbLusvrLMxsPbIqHiMEBtHoNmb8pReRo5lYfrq+u+x1bExHc5Kbhh1jIRaY; master_key=oqWPTPRNLKNRxZ933GO+CKIV6t0+ii+8093Le9A8ayE=; master_user=gh_495d307185e5; master_sid=ZWk4c2ZfaG5PdEV6N1hmeGp0eXhSMFVWVmtBUTJZN0lHY1BrNmozRGZrNG9vcjRTYkxYcWczQWNERzlqb0RrQ0xHbU5QaWRCM1BjdlROdW1jTk1HWVVscWw0SFp6ZVRZZE5aNEF0a3NhWE8wQ2pRNURTb2dReW13alpMN2lCN3lEbTNQcWZHeXpGQ1lzb3BT; master_ticket=22828aaf6915cdba00bb1e491b279738; bizuin=3940396966; slave_user=gh_495d307185e5; slave_sid=elhtbVVEak5uSnZ6TDFMejByR2l1QnZRdmFjOXhGSl9UUk5BWms3UGxVUTFvVDFmX0NIUmswNFZRV3lVaExrbkVqM290UXlDWHFMXzdYckRCR01DcXhibWFaeDQ5b3RfdWtmVGNsdmFxUXFiNUtZcUlWNUFSemhjdk9PMDdMT2FFZnRGb2p4UE9odHlHeEVq; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=",
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    # 遍历url
    with tqdm(total=len(url_list)) as pbar:
        for url in url_list:
            # 随机休眠，防止被封
            time.sleep(random.randint(1, 5))
            # 发送请求
            response = requests.get(url[0], headers=headers)
            # print("state_code:", response.status_code)    # 200即正常
            # 解析html
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            # 大多数p标签中包含的是文字，但也有一些直接是 “section > span”， 这些内容没有爬到
            soup_sel = soup.select("p")
            content = ""
            for c in soup_sel:
                t = c.get_text().strip('\n')
                if t != '':
                    content += t
            contents.append(content)
            pbar.update(1)
        return contents

# 按行存csv， 编码'utf-8-sig'存中文
def saveContentsTocsv(contents):
    file_name = input("please name the new csv-file\n")
    with open('./data/' + file_name + '.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        for row in contents:
            writer.writerow([row])
    print("done")



if __name__ == "__main__":
    url_list_storage_path = "./data/WeChat_urls.csv"

    url_list = getUrlList(url_list_storage_path)
    contents = getContentByUrl(url_list)
    # print(contents)
    saveContentsTocsv(contents)