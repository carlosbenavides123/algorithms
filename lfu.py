# This problem was asked by Google.

# Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value.
# If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item.
# If there is a tie, then the least recently used key should be removed.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

# {0 -> [key]}
# {key -> (val, freq)}

# 

import collections

class LFUCache(object):
    def __init__(self, n):
        self.cache_size = n
        self.min_freq = 0
        self.freq_to_key = collections.defaultdict(collections.deque)
        self.key_to_val = {}

    """
    return int, -1 is error
    """
    def get(self, key):
        if key not in self.key_to_val:
            return -1
        val, freq = self.key_to_val[key]
        self.freq_to_key[freq].remove(key)
        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        self.key_to_val[key] = (val, freq + 1)
        self.freq_to_key[freq + 1].append(key)
        return val

    """
    return void
    """
    def put(self, key, val):
        if self.cache_size == 0: return
        
        if key not in self.key_to_val:
            # eviction
            if len(self.key_to_val) >= self.cache_size:
                to_evict = self.freq_to_key[self.min_freq].popleft()
                del self.key_to_val[to_evict]
                if not self.freq_to_key[self.min_freq]:
                    del self.freq_to_key[self.min_freq]
            self.min_freq = 0
            self.freq_to_key[0].append(key)
            self.key_to_val[key] = (val, 0)
        else:
            _, freq = self.key_to_val[key]
            self.freq_to_key[freq].remove(key)
            if not self.freq_to_key[freq]:
                del self.freq_to_key[freq]
                if freq == self.min_freq:
                    self.min_freq += 1
            self.key_to_val[key] = (val, freq + 1)
            self.freq_to_key[freq + 1].append(key)




