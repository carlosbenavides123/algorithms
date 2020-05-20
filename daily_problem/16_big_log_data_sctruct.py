# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or
# equal to N.
# You should be as efficient with time and space as possible


class LogStruct:
    def __init__(self, n):
        self.index = 1
        self.n = n
        self.hmap = {}

    def record(self, order_id):
        if len(self.hmap) > self.n:
            del self.hmap[self.index - self.n]
        self.hmap[self.index] = order_id
        self.index += 1

    def get_last(self, i):
        return self.hmap[self.index - i]


class LogStruct:
    def __init__(self, n):
        self.index = 0
        self.n = n
        self.arr = []

    def record(self, order_id):
        if len(self.arr) == self.n:
            self.arr[self.index] = order_id
        else:
            self.arr.append(order_id)
        self.index = (self.index + 1) % self.n

    def get_last(self, i):
        return self.arr[self.index - i]
