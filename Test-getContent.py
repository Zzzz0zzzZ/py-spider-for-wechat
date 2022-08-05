import requests
import urllib.request
import bs4
import csv


# url = 'http://mp.weixin.qq.com/s'
url = "http://mp.weixin.qq.com/s?__biz=MzA3OTI0OTk3OQ==&mid=2650324925&idx=1&sn=148b4accf22da59b7777ba04e9a753c2&chksm=87ba48e9b0cdc1ffbb8ea900bca705e60197a1f19332478d5cd0a28881e42149c100214485b3#rd"
headers = {
    "cookie":
        "ua_id=HvjnK6CPHdz8Zt8LAAAAAOhen6ItkIZVMBtW_LgGBJI=; wxuin=59663835389206; uuid=8f918189cdbb5277042af4cc9972af95; cert=8usVhBJvV_bhiOGzvEr5KNZrBLVPpLvI; sig=h01f5bf100266357f9042120ae1f1e6812f0dd97700fa5cc0af9d3206ec20ce8d58f65c6dfd9ddf258b; data_bizuin=3940396966; data_ticket=/cKAiIbLusvrLMxsPbIqHiMEBtHoNmb8pReRo5lYfrq+u+x1bExHc5Kbhh1jIRaY; master_key=oqWPTPRNLKNRxZ933GO+CKIV6t0+ii+8093Le9A8ayE=; master_user=gh_495d307185e5; master_sid=ZWk4c2ZfaG5PdEV6N1hmeGp0eXhSMFVWVmtBUTJZN0lHY1BrNmozRGZrNG9vcjRTYkxYcWczQWNERzlqb0RrQ0xHbU5QaWRCM1BjdlROdW1jTk1HWVVscWw0SFp6ZVRZZE5aNEF0a3NhWE8wQ2pRNURTb2dReW13alpMN2lCN3lEbTNQcWZHeXpGQ1lzb3BT; master_ticket=22828aaf6915cdba00bb1e491b279738; bizuin=3940396966; slave_user=gh_495d307185e5; slave_sid=elhtbVVEak5uSnZ6TDFMejByR2l1QnZRdmFjOXhGSl9UUk5BWms3UGxVUTFvVDFmX0NIUmswNFZRV3lVaExrbkVqM290UXlDWHFMXzdYckRCR01DcXhibWFaeDQ5b3RfdWtmVGNsdmFxUXFiNUtZcUlWNUFSemhjdk9PMDdMT2FFZnRGb2p4UE9odHlHeEVq; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=",
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

'''
params = {
    "__biz":
        "MzA3OTI0OTk3OQ==",
    "mid":
        "2650325281",
    "idx":
        "1",
    "sn":
        "84407ca761d736cc4f7a962102b67b94",
    "chksm":
        "87ba3675b0cdbf6363dfa4f3576802da970b062fd894ee3edda7e8631a260055e7f728b2f0f5"
}
'''

r = requests.get(url, headers=headers)
print("state_code:", r.status_code)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
contents = soup.select("p")

dat = ""
for content in contents:
    # print(content.get_text())
    t = content.get_text().strip('\n')
    if t != '':
       dat += t

with open('./demoo.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([dat])

# with open("./demo2.txt", "w", encoding='utf-8') as f:
#     writeContent = ""
#     for tt in dat:
#         writeContent += tt
#
#     f.write(writeContent.strip('\n'))
#     print(writeContent[115:])