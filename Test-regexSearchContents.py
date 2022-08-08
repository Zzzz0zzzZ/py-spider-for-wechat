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
            print(sentence)
    print(res)
    return res

if __name__ == "__main__" :
    keyword_list = ["日", "节"]
    title_list = getTitleList("./data/20pages_title.csv")
    res = regexTitleByKeywords(title_list, keyword_list)
