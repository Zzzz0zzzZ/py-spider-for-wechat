import csv
import re

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

if __name__ == "__main__" :
    # keyword list
    keyword_list = ["日", "节", "新年", "快乐", "祝"]
    # Path
    title_path = "./data/20pages_title.csv"
    update_time_path = "./data/20pages_real-time.csv"
    url_path = "./data/20pages_link.csv"
    content_path = "data/20pages_content.csv"
    # load files
    title_list = getTitleList(title_path)
    update_time_list = getTitleList(update_time_path)
    url_list = getTitleList(url_path)
    content_list = getTitleList(content_path)
    # get index
    res_index = regexTitleByKeywords(title_list, keyword_list)

    data_list = []
    for a, b, c, d in zip(update_time_list, title_list, url_list, content_list):
        x = {}
        x['时间'] = a[0]
        x['标题'] = b[0]
        x['地址'] = c[0]
        x['内容'] = d[0]
        data_list.append(x)

    file_name = input("please name the new csv-file\n")
    with open('./filtered_data/' + file_name + '.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['时间', '标题', '地址', '内容'])
        for idx in res_index:
            writer.writerow(
                data_list[idx].values()
            )

    print("done")




