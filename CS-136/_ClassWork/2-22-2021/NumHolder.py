#
#River Sheppard
#NumHolder
#

import random
import threading

class NumHolder:
    def __init__(self,c):
        self.list = c

    def increment(self):
        l.acquire()
        for i in range(100):
            self.list[i] += 1
        l.release()

    def decrement(self):
        l.acquire()
        for i in range(100):
            self.list[i] -= 1
        l.release()

    def run(self):
        for i in range(10000):
            c = random.randint(0,1)
            if c == 1:
                self.decrement()
            elif c == 0:
                self.increment()

if __name__ == "__main__":
    l = threading.Lock()
    c = [random.randint(1,9) for i in range(100)]

    v = NumHolder(c)

    a = threading.Thread(target=v.run())
    b = threading.Thread(target=v.run())

    print(v.list)

    a.start()
    b.start()

    print(v.list)
