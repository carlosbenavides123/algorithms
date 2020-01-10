# 57. Insert Interval
# Hard

# 1169

# 140

# Add to List

# Share
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


def insert(intervals, newInterval):
    start, end = newInterval[0], newInterval[1]
    i = 0
    res = []
    while i < len(intervals):
        interval_start = intervals[i][0]
        interval_end = intervals[i][1]
        if start <= interval_end:
            if end < interval_start:
                print(end, interval_start, start)
                break
            start = min(start, interval_start)
            end = max(end, interval_end)
        else:
            res.append(intervals[i])
        i += 1
    res.append([start, end])
    for i in range(i, len(intervals)):
        res.append(intervals[i])
    return res


print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
