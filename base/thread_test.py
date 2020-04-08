import threading
import time
from threading import current_thread


def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s  %s' % (arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')


for i in range(1, 6, 1):
    #  同步的方式
    # t1 = myThread(i, i + 1)
    #  线程的方式运行
    t2 = threading.Thread(target=myThread, args=(i, i + 1))
    t2.start()

print(current_thread().getName(), 'end')
