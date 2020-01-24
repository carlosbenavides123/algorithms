# leetcode medium
# given a list of nums and a sorted interval, insert the interval while maintaining order

# IP [ [1, 2], [3, 5], [6, 7], [8, 10], [12, 16] ], [4, 8]
# OP [ [1, 2], [3, 10], [12, 16] ]

def insert_interval(arr, insert):
    start, end = insert[0], insert[1]
    res = []
    i = 0
    while i < len(arr):
        curr = arr[i]
        if start <= curr[1]:
            if end < curr[0]:
                break
            start = min(start, curr[0])
            end = max(end, curr[1])
        else:
            res.append(curr)
        i += 1
    res.append([start, end])
    for start, end in arr[i:]:
        res.append([start, end])
    return res

print(insert_interval([ [1, 2], [3, 5], [6, 7], [8, 10], [12, 16] ], [4, 8]))