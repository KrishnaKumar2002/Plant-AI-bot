from threading import Thread
import time
def func1():
    for i in range(100):
        time.sleep(1)
        print('1',i)

def func2():
    for i in range(100):
        time.sleep(1)
        print("2",i)


a = Thread(target = func1)
b = Thread(target = func2)
a.start()
b.start()