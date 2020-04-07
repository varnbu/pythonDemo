# try:
#     year = int(input('请输入年份'))
# except ValueError as e:
#     print('请输入数字 %s'%e)

# try:
#     s = 1
# except (ValueError, AttributeError, KeyError):
#     print("出错了")

#  捕获所有的错误
# try:
#     year = int(input('请输入年份'))
# except Exception as e:
#     print('请输入数字 %s'%e)

try:
    raise NameError("名字错误error")
except NameError as e:
    print(e)
finally:
    print("都要执行")



try:
    file = open("name.txt")
except Exception as e:
    print(e)
finally:
    file.close()