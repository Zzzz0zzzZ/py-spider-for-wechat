import datetime
import csv

dic_name = str(datetime.date.today())
file_name = "hahaa"

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

mkdir(f'./data/{dic_name}/')
with open(f'./data/{dic_name}/' + file_name + '.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['1'])
