#different task for mult thread
import threading
class MyThread1(threading.Thread):
    def run(self):
        for i in range(5):
            print("hello")
class MyThread2(threading.Thread):
    def run(self):
        for i in range(5):
            print("bye")
t1=MyThread1()
t2=MyThread2()
t1.start()
t2.start()
