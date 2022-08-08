import re

keyword = ["日", "节"]
sentences = [
    "知识产权日 | 诺维信捍卫知识产权，商标维权战告捷",
    "飒飒都三段式你吃撒",
    "世界卫生日 | 200年人类手术史，一段不可思议的进化之路",
    "世界干净日 | 哈哈哈哈哈哈",
    "哦啊的室内车库菜市场",
    "佛挡杀佛8-2急促SV搭理你",
    "圣诞节",
    "建军节"
]

res = []

for index, sentence in enumerate(sentences):
    pattern = re.compile('|'.join(keyword))
    result_findall = pattern.findall(sentence)
    if result_findall:
        res.append(index)
        print(sentence)
print(res)
