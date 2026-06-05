import threading
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("hello")
t=MyThread()
t.start()
for i in range(5):
    print("bye")
