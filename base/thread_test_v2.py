import threading
from threading import current_thread


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'end')


c1 = MyThread()
c1.start()
c1.join()
print(current_thread().getName(), 'end')
