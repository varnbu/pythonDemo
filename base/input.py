# text = input()
# print('input->', text)
# if int(text) != 3:
#     print('请输入 3')
# else:
#     print('输入了：', text)
#


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(4, 1)

str1 = 'able'
print('长度：', len(str1))
#  字符串切片
print(str1[2:5])

a = range(10)
for i in a:
    print(a[i])
