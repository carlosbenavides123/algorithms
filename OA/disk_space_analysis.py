# Given this analysis procedure, write an algorithm to find the maximum available disk space among all the minima that are found during the analysis.

# Input:
# The input to the function/method consists of 3 arguments:
# numComputer, an integer representing the number of computers;
# hardDiskSpace, a list of integers representing the hard disk space of the computers;
# segmentLength, an integer representing the length of the contiguous segment of computers to
# be consider in each iterations.

# Output:
# Return an integer representing the maximum available disk space among all the minima that are found during the analysis.

# Input:
# numComputer = 3
# hardDiskSpace = [8,2,4]
# segmentLength = 2

# Output:
# 2

# Explanation:
# In this array of computers, the subarrays of size 2 are [8,2] and [2,4].
# Thus, the initial analysis returns 2 and 2 because those are the minima for the segmenets.
# Finally the maximum of these values is 2.
# Therefore, the answer is 2.

def disk_space_analysis(nums, segment_length):
    import collections
    q = collections.deque()
    res = min(nums[:segment_length])
    for i in range(len(nums)):
        while q and q[0] < i - segment_length - 1:
            q.popleft()
        while q and nums[q[-1]] > nums[i]:
            q.pop()
        q.append(i)
        if i >= segment_length - 1:
            res = max(res, nums[q[0]])
    return res