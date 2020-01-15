# 621. Task Scheduler
# Medium

# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.


# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


def leastInterval(tasks, n):
    import collections
    import heapq
    n += 1
    count = collections.Counter(tasks)
    heap = [-v for v in count.values()]
    heapq.heapify(heap)
    res = 0
    while heap:
        arr = []
        cnt = 0
        for _ in range(n):
            if heap:
                item = heapq.heappop(heap)
                cnt += 1
                if item < -1:
                    arr.append(item + 1)
        for item in arr:
            heapq.heappush(heap, item)
        res += heap and n or cnt  # == if heap then n else cnt
    return res


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))
