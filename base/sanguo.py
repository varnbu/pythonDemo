import re


def find_item(hero):
    f = open("sanguo_utf8.txt", encoding="utf8")
    data = f.read().replace('\n', '')
    names = re.findall(hero, data)
    return len(names)


name_dict = {}
with open("san_name.txt", encoding='utf8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print('三国中 人物大名出现的次数')
print(name_sorted)
