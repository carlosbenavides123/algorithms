#Given a collection of intervals, merge all overlapping intervals.

#Example 1:

#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:
#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def solve(intervals):
    if not intervals:
        return []
    res = []
    intervals = sorted(intervals, key=lambda x:(x[0], x[1]))
    end = intervals[0][1]
    res.append(intervals[0])
    for interval in intervals[1:]:
        if end >= interval[0]:
            old_start, old_end = res.pop()
            res.append([old_start, max(old_end, interval[1])])
        else:
            res.append(interval)
        end = max(end, interval[1])
    return res
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solve(intervals))
intervals = [[1,4],[4,5]]
print(solve(intervals))