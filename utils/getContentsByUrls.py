import csv
import random
import requests
import bs4
import time
from tqdm import tqdm

# 从文件读取URLs，返回字典
def getUrlList(url_storage_path):
    with open(url_storage_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        url_list = [row for row in reader]
    return url_list


def getContentByUrl(url_list):
    # 返回结果
    contents = []
    # 请求头
    headers = {
        "cookie":
            "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; cert=8usVhBJvV_bhiOGzvEr5KNZrBLVPpLvI; sig=h01f5bf100266357f9042120ae1f1e6812f0dd97700fa5cc0af9d3206ec20ce8d58f65c6dfd9ddf258b; master_key=oqWPTPRNLKNRxZ933GO+CKIV6t0+ii+8093Le9A8ayE=; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; uuid=9a488fb0b902debc7c27e896a8cad45a; rand_info=CAESIJrdL2xSqHo7JtTHuM8d4zAMoSNjxacqc6VQsR4g87rR; slave_bizuin=3940396966; data_bizuin=3940396966; bizuin=3940396966; data_ticket=GYSHLkTsYGcdfdQ/Oj2wGnYGGBkKpTBgA59H5y7Zb2Su8NHcYn40uu+pALruIHzO; slave_sid=VnNCREhCQ1diTkoyQ091ejQ0ckoxdDBiTUxLMWxURHFPVDNsWmFhZVY0UjFzemc0UjhZc19hOERZY2tGa2dEcFRmeEJjV2tWRXRoZlFfMjFlUmhkbXRUdF9pdzUxTEVSVzQxbmhaYnVMMnNuSm55b0NsYkJwOHhLSEdOMk9mYk1hSW5DcDFsZTFjVEw5YUkw; slave_user=gh_495d307185e5; xid=1f54bfb9bf5268fecf62675424ba6a66; mm_lang=zh_CN",
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    # 遍历url
    with tqdm(total=len(url_list)) as pbar:
        for url in url_list:
            # 随机休眠，防止被封
            # time.sleep(random.randint(1, 5))
            # 发送请求
            response = requests.get(url[0], headers=headers)
            # print("state_code:", response.status_code)    # 200即正常
            # 解析html
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            # 大多数p标签中包含的是文字，但也有一些直接是 “section > span”， 这些内容没有爬到
            soup_sel = soup.select("p")
            # soup_sel = soup.select(".rich_media_inner")
            content = ""
            for c in soup_sel:
                t = c.get_text().strip('\n')
                if t != '':
                    content += t
            # print(content)
            # print(content[116:-11])
            content = content[116:-11]
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
    start = time.time()
    url_list_storage_path = "./data/20pages_link.csv"

    url_list = getUrlList(url_list_storage_path)
    contents = getContentByUrl(url_list)
    # print(contents)
    saveContentsTocsv(contents)
    end = time.time()
    print("time cost:", end-start, "s")
