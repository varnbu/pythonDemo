#  普通使用 会自动处理异常
# with open('name.txt') as f:
#     print(f.name)


class TestWith:
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit')
        else:
            print('has error %s' % exc_tb)


#  使用 width 简化异常的编写 异常余上面的类的结合使用
with TestWith():
    print('test is run')
    raise NameError('testError')
