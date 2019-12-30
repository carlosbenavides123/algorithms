# 560. Subarray Sum Equals K
# Medium

# 2897

# 78

# Add to List

# Share
# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2

nums = [1, 1, 1]
k = 2


def subarraySum(nums, k):
    dic = {0: 1}
    _sum = 0
    res = 0
    for num in nums:
        _sum += num
        res += dic.get(_sum-k, 0)
        dic[_sum] = dic.get(_sum, 0) + 1
    return res


print(subarraySum(nums, k))
