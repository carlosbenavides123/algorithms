# 209. Minimum Size Subarray Sum
# Medium

# 1540

# 87

# Add to List

# Share
# Given an array of n positive integers and a positive integer s find the minimal length of a contiguous subarray of which the sum  >= s. If there isnt one return 0 instead.

# Example:

# Input: s = 7, nums = [2, 3, 1, 2, 4, 3]
# Output: 2
# Explanation: the subarray[4, 3] has the minimal length under the problem constraint.


def min_size_sub_sum(s, nums):
    left = right = _sum = 0
    res = len(nums) - 1
    for i in range(len(nums)):
        right = i
        _sum += nums[right]
        while _sum >= s:
            res = min(res, right - left + 1)
            _sum -= nums[left]
            left += 1
    return res if res != len(nums) - 1 else 0


print(min_size_sub_sum(7, [2, 3, 1, 2, 4, 3]))
