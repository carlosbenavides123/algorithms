# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import threading
from time import time

from time import sleep
class Scheduler():
    def __init__(self):
        self.funcs = []
        t = threading.Thread(target=self.polling)
        t.start()
    def polling(self):
        while True:
            time_now = time() * 1000
            for (f, func_time) in self.funcs:
                if func_time > time_now:
                    f()
            self.funcs = [(f, func_time) for (f, func_time) in self.funcs if func_time > time_now]
            sleep(1)
            
    def hello(self):
        print("hello world")
    
    def solve(self, func, num):
        print(func)
        self.funcs.append((func, time() * 1000 + num))

    def bye(self):
        print("bye world")

sched = Scheduler()

sched.solve(sched.bye, 4000)
sched.solve(sched.hello, 2000)
