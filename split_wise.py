transactions = [
    [60, 30, 30],
    [25, 25, 10],
    [30, 10, 20],
    [10, 45, 5]
]

def split_bills(transactions):
    _sum = sum([sum(transaction) for transaction in transactions])
    avg = _sum // len(transactions[0])
    group = [0] * len(transactions[0])
    for i in range(len(group)):
        for j in range(len(transactions)):
            group[i] += transactions[j][i]
    group = [paid - avg for paid in group]
    l = 0
    r = len(group) - 1
    while l < r:
        person_to_receive = group[l]
        person_to_pay = group[r]
        amount = min(person_to_receive, -person_to_pay)
        group[l] -= amount
        group[r] += amount
        if group[l] == 0:
            l += 1
        if group[r] == 0:
            r -= 1
    print(group)
print(split_bills(transactions))

def minTransfers(self, transactions):
    """
    :type transactions: List[List[int]]
    :rtype: int
    """
    transaction_map = collections.defaultdict(int)
    payments = []
    for person_a, person_b, amount in transactions:
        transaction_map[person_a] -= amount
        transaction_map[person_b] += amount
    pay = list(transaction_map.values())
    return self.dfs(pay, 0)

def dfs(self, pay, idx):
    while idx < len(pay) and pay[idx] == 0:
        idx += 1
    if idx == len(pay): return 0
    curr_val = pay[idx]
    res = float("inf")
    for i in range(idx+1, len(pay)):
        other_val = pay[i]
        if curr_val * other_val > 0: continue
        pay[i] += curr_val
        res = min(res, 1 + self.dfs(pay, idx + 1))
        pay[i] -= curr_val
    return res



from collections import defaultdict
from collections import deque

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.val_map = {}
        self.freq_map = defaultdict(deque)
        self.min_freq = 0

    def get(self, key):
        if key not in self.val_map:
            return None

        val, freq = self.val_map[key]
        self.freq_map[freq].remove(key)
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Update our dicts as usual.
        self.val_map[key] = (val, freq + 1)
        self.freq_map[freq + 1].append(key)
        return val

    def set(self, key, val):
        if self.capacity == 0:
            return

        if key not in self.val_map:
            if len(self.val_map) >= self.capacity:
                to_evict = self.freq_map[self.min_freq].popleft()
                if not self.freq_map[self.min_freq]:
                    del self.freq_map[self.min_freq]
                del self.val_map[to_evict]

            # Add our key to val_map and freq_map
            self.val_map[key] = (val, 1)
            self.freq_map[1].append(key)
            self.min_freq = 1
        else:
            _, freq = self.val_map[key]
            self.freq_map[freq].remove(key)
            if not self.freq_map[freq]:
                if freq == self.min_freq:
                    self.min_freq += 1
                del self.freq_map[freq]
            self.val_map[key] = (val, freq + 1)
            self.freq_map[freq + 1].append(key)
