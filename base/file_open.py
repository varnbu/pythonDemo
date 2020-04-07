# file1 = open('name.txt', "w", encoding='utf8')
# file1.write(u"小星星", )
# file1.close()

# file2 = open('name.txt', encoding="utf8")
# temp = file2.read()
# print(temp)
# file2.close()
#
# file3 = open("name.txt", 'a', encoding="utf8")
# file3.write("小周周")
# file3.close()
#

# file4 = open('name.txt', encoding='utf8')
# for line in file4.readlines():
#     print(line)
#     print('---------------')

file6 = open("name.txt",encoding='utf8')
#  指针位置
print(file6.tell())
#  读取所有内容 再打印指针
file6.read(1)
print(file6.tell())
file6.read()
print(file6.tell())
#  seek 函数两个参数，第一个是偏移量 第二个参数 0表示文件开头偏移 1表示当前位置移动 2表示文件结尾
file6.seek(1,2)