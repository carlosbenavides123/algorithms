# Given an array nums of n integers, 
# are there elements a, b, c in nums such that 
# a + b + c = 0? Find all unique triplets in the 
# array which gives the sum of zero.

nums = input()

def solve(nums):
    res = set()
    nums = sorted(nums)
    index = 0
    while index < len(nums):
        curr = nums[index]
        l = index + 1
        r = len(nums) - 1
        while l < r:
            left_val = nums[l]
            right_val = nums[r]
            
            _sum = curr + left_val + right_val
            if _sum == 0:
                res.add((curr, left_val, right_val))
                l += 1
                r -= 1
            elif _sum > 0:
                r -= 1
            else:
                l += 1
        index += 1
    return map(list, res)

print(solve(nums))