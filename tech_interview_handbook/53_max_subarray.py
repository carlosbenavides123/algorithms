#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#Example:

#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
#Follow up:

#If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

def solve(nums):
    max_sum = 0
    curr_max = 0
    for num in nums:
        curr_max = max(curr_max + num, num)
        max_sum = max(curr_max, max_sum)
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solve(nums))