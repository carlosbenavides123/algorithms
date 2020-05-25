#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

#Note:

#The solution set must not contain duplicate triplets.

#Example:

#Given array nums = [-1, 0, 1, 2, -1, -4],

#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]

def solve(nums):
    nums.sort()
    res = set()
    
    for i in range(len(nums) - 2):
        curr = nums[i]
        l = i + 1
        r = len(nums) - 1
        while l < r:
            num_l = nums[l]
            num_r = nums[r]
            curr_sum = curr + num_l + num_r
            if curr_sum == 0:
                res.add((curr, num_l, num_r))
                l += 1
                r -= 1
            elif curr_sum > 0:
                r -= 1
            else:
                l += 1
nums = [-1, 0, 1, 2, -1, -4]
print(solve(nums))