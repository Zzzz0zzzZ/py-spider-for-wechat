import csv
import re
import getAllUrls
import datetime

# path = getAllUrls.path

def getTitleList(titles_storage_path):
    with open(titles_storage_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        titles_list = [row for row in reader]
    return titles_list

def regexTitleByKeywords(sentences_list, keywords_list):
    '''
    :param sentences_list: 待匹配句子列表
    :param keywords_list:  匹配关键词列表
    :return: 匹配成功的句子下标
    '''
    res = []
    for index, sentence in enumerate(sentences_list):
        pattern = re.compile('|'.join(keywords_list))
        result_findall = pattern.findall(sentence[0])   # .match()-匹配开头  .search()-只匹配第一个  .findall()-匹配所有
        if result_findall:                              # .match() / .search() 返回None    .findall() 返回空列表
            res.append(index)
    return res


def run_getTitleByKeywords(keywords_str:str, savepath:str, filename:str):
    public_path = savepath + '/raw/' + filename + '_'
    # Path
    title_path = public_path + "title.csv"
    update_time_path = public_path + "real-time.csv"
    url_path = public_path + "url.csv"
    content_path = public_path + "content.csv"
    # load files
    title_list = getTitleList(title_path)
    update_time_list = getTitleList(update_time_path)
    url_list = getTitleList(url_path)
    content_list = getTitleList(content_path)

    # get index
    FlAG = True
    if keywords_str != '':
        keyword_list = keywords_str.split('；')
        print("kw_list", keyword_list)
        # 正则获取下标
        res_index = regexTitleByKeywords(title_list, keyword_list)
    else:
        FlAG = False

    data_list = []
    for a, b, c, d in zip(update_time_list, title_list, url_list, content_list):
        x = {}
        x['时间'] = a[0]
        x['标题'] = b[0]
        x['地址'] = c[0]
        x['内容'] = d[0]
        data_list.append(x)
    with open( savepath + '/' + filename + '_爬取结果.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['时间', '标题', '地址', '内容'])
        if FlAG:
            for idx in res_index:
                writer.writerow(
                    data_list[idx].values()
                )
        else:
            for i in range(len(data_list)):
                writer.writerow(
                    data_list[i].values()
                )
    print(f"[save filtered data list] {str(datetime.datetime.now())} done")

# if __name__ == "__main__" :
#     # keyword list
#     keyword_list = ["日", "节", "新年", "快乐", "祝"]
#     # Path
#     title_path = path + "title.csv"
#     update_time_path = path + "real-time.csv"
#     url_path = path + "url.csv"
#     content_path = path + "content.csv"
#     # load files
#     title_list = getTitleList(title_path)
#     update_time_list = getTitleList(update_time_path)
#     url_list = getTitleList(url_path)
#     content_list = getTitleList(content_path)
#     # get index
#     res_index = regexTitleByKeywords(title_list, keyword_list)
#
#     data_list = []
#     for a, b, c, d in zip(update_time_list, title_list, url_list, content_list):
#         x = {}
#         x['时间'] = a[0]
#         x['标题'] = b[0]
#         x['地址'] = c[0]
#         x['内容'] = d[0]
#         data_list.append(x)
#     # print(data_list)
#     file_name = input("please name the new csv-file\n")
#     with open('./filtered_data/' + f'{str(datetime.date.today())}_' + file_name + '.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['时间', '标题', '地址', '内容'])
#         for idx in res_index:
#             writer.writerow(
#                 data_list[idx].values()
#             )
#     print(f"[save filtered data list] {str(datetime.datetime.now())} done")




