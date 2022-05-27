from asyncore import read
import time
from threading import Thread

def writeData():
    k= open("file.csv","w")
    for i in range(100):
        k.write("Hello,"+str(i)+'\n')
        time.sleep(1)
        k.close()
        k=open("file.csv",'a')   
        #print(i)
def readData():
    f= open("file.csv","r")
    for i in range(100):
        time.sleep(1)
        print(f.readlines())
a = Thread(target = writeData)
b = Thread(target = readData)
a.start()
b.start()