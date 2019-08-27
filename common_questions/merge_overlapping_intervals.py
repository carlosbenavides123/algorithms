# This problem was recently asked by Microsoft:

# You are given an array of intervals - that is, an array of tuples (start, end).
# The array may not be sorted, and could contain overlapping intervals.
# Return another array where the overlapping intervals are merged.

# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]

# This input should return [(1, 3), (4, 10), (20, 25)]
# since (5, 8) and (4, 10) can be merged into (4, 10).

# Here's a starting point:


def merge(intervals):
    # Fill this in.
    intervals.sort(key=lambda i: i[0])
    print(intervals)
    res = []
    for start, end in intervals:
        if res and start <= res[-1][1]:
            last_start, last_end = res[-1]
            res[-1] = (last_start, max(last_end, end))
        else:
            res.append((start, end))
    return res


intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
print merge(intervals)
# [(1, 3), (4, 10), (20, 25)]
