# 239. Sliding Window Maximum
# Hard

# 2372

# 139

# Add to List

# Share
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example:

# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], and k = 3
# Output: [3, 3, 5, 5, 6, 7]
# Explanation:

# Window position                Max
# --------------- -----
# [1  3 - 1] - 3  5  3  6  7       3
# 1 [3 - 1 - 3] 5  3  6  7       3
# 1  3 [-1 - 3  5] 3  6  7       5
# 1  3 - 1 [-3  5  3] 6  7       5
# 1  3 - 1 - 3 [5  3  6] 7       6
# 1  3 - 1 - 3  5 [3  6  7]      7


def maxSlidingWindow(nums, k):
    import collections
    q = collections.deque([])
    res = []
    for i in range(k):
        num = nums[i]
        while q and num > nums[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, len(nums)):
        res.append(nums[q[0]])

        num = nums[i]

        while q and num > nums[q[-1]]:
            q.pop()
        q.append(i)

    res.append(nums[q[0]])

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))
