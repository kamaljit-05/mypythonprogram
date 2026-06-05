#single task multithread
import threading
class MyThread1(threading.Thread):
    def run(self):
        for i in range(5):
            print("hello")
t1=MyThread1()
t2=MyThread1()
t1.start()
t2.start()
